package com.rentora.controller;

import com.rentora.dto.PaymentDto;
import com.rentora.service.PaymentService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import jakarta.validation.Valid;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/payments")
@RequiredArgsConstructor
@Tag(name = "Payments & Escrow", description = "Simulated payment processing and escrow transaction ledger")
public class PaymentController {

    private final PaymentService paymentService;

    @GetMapping
    @Operation(summary = "Get all payments or filter by rental ID")
    public ResponseEntity<List<PaymentDto>> getAllPayments(@RequestParam(required = false) Long rentalId) {
        if (rentalId != null) {
            return ResponseEntity.ok(paymentService.getPaymentsByRental(rentalId));
        }
        return ResponseEntity.ok(paymentService.getAllPayments());
    }

    @PostMapping
    @Operation(summary = "Process simulated payment transaction")
    public ResponseEntity<PaymentDto> processPayment(@Valid @RequestBody PaymentDto paymentDto) {
        return new ResponseEntity<>(paymentService.processPayment(paymentDto), HttpStatus.CREATED);
    }
}
