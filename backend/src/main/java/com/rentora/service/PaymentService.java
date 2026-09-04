package com.rentora.service;

import com.rentora.dto.PaymentDto;
import com.rentora.entity.Payment;
import com.rentora.entity.Rental;
import com.rentora.exception.ResourceNotFoundException;
import com.rentora.repository.PaymentRepository;
import com.rentora.repository.RentalRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDateTime;
import java.util.List;
import java.util.UUID;
import java.util.stream.Collectors;

@Service
@RequiredArgsConstructor
public class PaymentService {

    private final PaymentRepository paymentRepository;
    private final RentalRepository rentalRepository;

    public List<PaymentDto> getAllPayments() {
        return paymentRepository.findAll().stream()
                .map(this::mapToDto)
                .collect(Collectors.toList());
    }

    public List<PaymentDto> getPaymentsByRental(Long rentalId) {
        return paymentRepository.findByRentalId(rentalId).stream()
                .map(this::mapToDto)
                .collect(Collectors.toList());
    }

    @Transactional
    public PaymentDto processPayment(PaymentDto dto) {
        Rental rental = rentalRepository.findById(dto.getRentalId())
                .orElseThrow(() -> new ResourceNotFoundException("Rental", "id", dto.getRentalId()));

        Payment payment = Payment.builder()
                .rental(rental)
                .amount(dto.getAmount())
                .paymentStatus(dto.getPaymentStatus())
                .paymentMethod(dto.getPaymentMethod() != null ? dto.getPaymentMethod() : "UPI")
                .transactionRef("TXN-" + UUID.randomUUID().toString().substring(0, 8).toUpperCase())
                .paymentDate(LocalDateTime.now())
                .build();

        return mapToDto(paymentRepository.save(payment));
    }

    private PaymentDto mapToDto(Payment p) {
        return PaymentDto.builder()
                .id(p.getId())
                .rentalId(p.getRental().getId())
                .amount(p.getAmount())
                .depositAmount(p.getRental().getDeposit())
                .paymentStatus(p.getPaymentStatus())
                .paymentMethod(p.getPaymentMethod())
                .transactionRef(p.getTransactionRef())
                .paymentDate(p.getPaymentDate())
                .build();
    }
}
