package com.rentora.repository;

import com.rentora.entity.ReturnRecord;
import com.rentora.entity.ReturnStatus;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Repository
public interface ReturnRepository extends JpaRepository<ReturnRecord, Long> {
    Optional<ReturnRecord> findByRentalId(Long rentalId);
    List<ReturnStatus> findByStatus(ReturnStatus status);
}
