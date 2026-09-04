package com.rentora.dto;

import com.rentora.entity.ReturnStatus;
import lombok.*;
import java.math.BigDecimal;
import java.time.LocalDate;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class ReturnDto {

    private Long id;
    private Long rentalId;
    private String productName;
    private String customerName;
    private String vendorName;
    private ReturnStatus status;
    private String damageReport;
    private BigDecimal damageFee;
    private BigDecimal depositRefunded;
    private LocalDate returnDate;
}
