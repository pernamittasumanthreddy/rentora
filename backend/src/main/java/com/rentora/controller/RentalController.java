package com.rentora.controller;

import com.rentora.dto.RentalDto;
import com.rentora.entity.RentalStatus;
import com.rentora.service.RentalService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import jakarta.validation.Valid;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api/rentals")
@RequiredArgsConstructor
@Tag(name = "Rental Lifecycle", description = "Booking, active shoot tracking, and status transitions")
public class RentalController {

    private final RentalService rentalService;

    @GetMapping
    @Operation(summary = "Get rentals filtered by customer or vendor ID")
    public ResponseEntity<List<RentalDto>> getRentals(
            @RequestParam(required = false) Long customerId,
            @RequestParam(required = false) Long vendorId) {

        if (customerId != null) {
            return ResponseEntity.ok(rentalService.getRentalsByCustomer(customerId));
        }
        if (vendorId != null) {
            return ResponseEntity.ok(rentalService.getRentalsByVendor(vendorId));
        }
        return ResponseEntity.ok(rentalService.getAllRentals());
    }

    @GetMapping("/{id}")
    @Operation(summary = "Get rental details by ID")
    public ResponseEntity<RentalDto> getRentalById(@PathVariable Long id) {
        return ResponseEntity.ok(rentalService.getRentalById(id));
    }

    @PostMapping
    @Operation(summary = "Create and checkout new rental booking with Escrow deposit")
    public ResponseEntity<RentalDto> createRental(@Valid @RequestBody RentalDto rentalDto) {
        return new ResponseEntity<>(rentalService.createRental(rentalDto), HttpStatus.CREATED);
    }

    @PutMapping("/{id}/status")
    @Operation(summary = "Update rental status (APPROVED, ACTIVE, RETURNED, COMPLETED, CANCELLED)")
    public ResponseEntity<RentalDto> updateRentalStatus(
            @PathVariable Long id,
            @RequestBody Map<String, String> statusUpdate) {

        RentalStatus status = RentalStatus.valueOf(statusUpdate.get("status"));
        return ResponseEntity.ok(rentalService.updateRentalStatus(id, status));
    }
}
