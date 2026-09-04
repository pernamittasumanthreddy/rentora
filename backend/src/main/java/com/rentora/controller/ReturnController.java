package com.rentora.controller;

import com.rentora.dto.ReturnDto;
import com.rentora.service.ReturnService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.math.BigDecimal;
import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api/returns")
@RequiredArgsConstructor
@Tag(name = "Return & Inspection", description = "Equipment return initiation, 5-point inspection, and deposit settlement")
public class ReturnController {

    private final ReturnService returnService;

    @GetMapping
    @Operation(summary = "Get all equipment return records")
    public ResponseEntity<List<ReturnDto>> getAllReturns() {
        return ResponseEntity.ok(returnService.getAllReturns());
    }

    @GetMapping("/{id}")
    @Operation(summary = "Get return record by ID")
    public ResponseEntity<ReturnDto> getReturnById(@PathVariable Long id) {
        return ResponseEntity.ok(returnService.getReturnById(id));
    }

    @PostMapping
    @Operation(summary = "Initiate return for an active rental")
    public ResponseEntity<ReturnDto> initiateReturn(@RequestBody Map<String, Object> request) {
        Long rentalId = Long.valueOf(request.get("rentalId").toString());
        String notes = request.get("damageReport") != null ? request.get("damageReport").toString() : "Good condition";
        return new ResponseEntity<>(returnService.initiateReturn(rentalId, notes), HttpStatus.CREATED);
    }

    @PutMapping("/{id}/settle")
    @Operation(summary = "Settle inspection report, assess damages, and release deposit")
    public ResponseEntity<ReturnDto> settleReturn(
            @PathVariable Long id,
            @RequestBody Map<String, Object> settlement) {

        BigDecimal fee = settlement.get("damageFee") != null ?
                new BigDecimal(settlement.get("damageFee").toString()) : BigDecimal.ZERO;
        String remarks = settlement.get("damageReport") != null ?
                settlement.get("damageReport").toString() : null;

        return ResponseEntity.ok(returnService.settleReturn(id, fee, remarks));
    }
}
