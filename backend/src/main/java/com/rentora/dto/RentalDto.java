package com.rentora.dto;

import com.rentora.entity.RentalStatus;
import jakarta.validation.constraints.NotNull;
import lombok.*;
import java.math.BigDecimal;
import java.time.LocalDate;
import java.time.LocalDateTime;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class RentalDto {

    private Long id;
    private Long customerId;
    private String customerName;
    private String customerEmail;

    @NotNull(message = "Product ID is required")
    private Long productId;
    private String productName;
    private String productImage;

    private Long vendorId;
    private String vendorName;

    @NotNull(message = "Start date is required")
    private LocalDate startDate;

    @NotNull(message = "End date is required")
    private LocalDate endDate;

    private RentalStatus status;
    private BigDecimal totalAmount;
    private BigDecimal deposit;
    private String deliveryAddress;
    private String trackingNumber;
    private LocalDateTime createdAt;
}
