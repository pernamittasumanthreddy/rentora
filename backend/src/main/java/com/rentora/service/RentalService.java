package com.rentora.service;

import com.rentora.dto.RentalDto;
import com.rentora.entity.*;
import com.rentora.exception.ResourceNotFoundException;
import com.rentora.repository.*;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDateTime;
import java.util.List;
import java.util.UUID;
import java.util.stream.Collectors;

@Service
@RequiredArgsConstructor
public class RentalService {

    private final RentalRepository rentalRepository;
    private final UserRepository userRepository;
    private final ProductRepository productRepository;
    private final PaymentRepository paymentRepository;

    public List<RentalDto> getAllRentals() {
        return rentalRepository.findAll().stream()
                .map(this::mapToDto)
                .collect(Collectors.toList());
    }

    public RentalDto getRentalById(Long id) {
        Rental rental = rentalRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Rental", "id", id));
        return mapToDto(rental);
    }

    public List<RentalDto> getRentalsByCustomer(Long customerId) {
        return rentalRepository.findByCustomerId(customerId).stream()
                .map(this::mapToDto)
                .collect(Collectors.toList());
    }

    public List<RentalDto> getRentalsByVendor(Long vendorId) {
        return rentalRepository.findByProductVendorId(vendorId).stream()
                .map(this::mapToDto)
                .collect(Collectors.toList());
    }

    @Transactional
    public RentalDto createRental(RentalDto dto) {
        User customer = userRepository.findById(dto.getCustomerId())
                .orElseThrow(() -> new ResourceNotFoundException("User", "id", dto.getCustomerId()));

        Product product = productRepository.findById(dto.getProductId())
                .orElseThrow(() -> new ResourceNotFoundException("Product", "id", dto.getProductId()));

        String tracking = "TRK-" + LocalDateTime.now().getYear() + "-" + UUID.randomUUID().toString().substring(0, 6).toUpperCase();

        Rental rental = Rental.builder()
                .customer(customer)
                .product(product)
                .startDate(dto.getStartDate())
                .endDate(dto.getEndDate())
                .status(RentalStatus.PENDING)
                .totalAmount(dto.getTotalAmount())
                .deposit(dto.getDeposit() != null ? dto.getDeposit() : product.getDeposit())
                .deliveryAddress(dto.getDeliveryAddress())
                .trackingNumber(tracking)
                .build();

        Rental saved = rentalRepository.save(rental);

        // Record Initial Payment In Escrow
        Payment payment = Payment.builder()
                .rental(saved)
                .amount(saved.getTotalAmount())
                .paymentStatus(PaymentStatus.PAID)
                .paymentMethod("UPI / NetBanking")
                .transactionRef("TXN-" + UUID.randomUUID().toString().substring(0, 8).toUpperCase())
                .build();
        paymentRepository.save(payment);

        return mapToDto(saved);
    }

    @Transactional
    public RentalDto updateRentalStatus(Long id, RentalStatus status) {
        Rental rental = rentalRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Rental", "id", id));

        rental.setStatus(status);
        return mapToDto(rentalRepository.save(rental));
    }

    private RentalDto mapToDto(Rental r) {
        return RentalDto.builder()
                .id(r.getId())
                .customerId(r.getCustomer().getId())
                .customerName(r.getCustomer().getName())
                .customerEmail(r.getCustomer().getEmail())
                .productId(r.getProduct().getId())
                .productName(r.getProduct().getName())
                .productImage(r.getProduct().getImageUrl())
                .vendorId(r.getProduct().getVendor().getId())
                .vendorName(r.getProduct().getVendor().getBusinessName())
                .startDate(r.getStartDate())
                .endDate(r.getEndDate())
                .status(r.getStatus())
                .totalAmount(r.getTotalAmount())
                .deposit(r.getDeposit())
                .deliveryAddress(r.getDeliveryAddress())
                .trackingNumber(r.getTrackingNumber())
                .createdAt(r.getCreatedAt())
                .build();
    }
}
