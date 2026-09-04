package com.rentora.repository;

import com.rentora.entity.Rental;
import com.rentora.entity.RentalStatus;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface RentalRepository extends JpaRepository<Rental, Long> {
    List<Rental> findByCustomerId(Long customerId);
    List<Rental> findByProductVendorId(Long vendorId);
    List<Rental> findByStatus(RentalStatus status);
}
