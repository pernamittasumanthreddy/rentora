package com.rentora.service;

import com.rentora.entity.Rental;
import com.rentora.entity.RentalStatus;
import com.rentora.repository.*;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.math.BigDecimal;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Service
@RequiredArgsConstructor
public class ReportService {

    private final RentalRepository rentalRepository;
    private final ProductRepository productRepository;
    private final UserRepository userRepository;
    private final VendorRepository vendorRepository;

    public Map<String, Object> getAnalyticsSummary() {
        List<Rental> rentals = rentalRepository.findAll();

        BigDecimal totalGMV = rentals.stream()
                .map(Rental::getTotalAmount)
                .reduce(BigDecimal.ZERO, BigDecimal::add);

        long activeRentalsCount = rentals.stream()
                .filter(r -> r.getStatus() == RentalStatus.ACTIVE)
                .count();

        long completedCount = rentals.stream()
                .filter(r -> r.getStatus() == RentalStatus.COMPLETED)
                .count();

        Map<String, Object> summary = new HashMap<>();
        summary.put("totalGMV", totalGMV);
        summary.put("activeRentals", activeRentalsCount);
        summary.put("completedRentals", completedCount);
        summary.put("totalUsers", userRepository.count());
        summary.put("totalVendors", vendorRepository.count());
        summary.put("totalProducts", productRepository.count());

        return summary;
    }
}
