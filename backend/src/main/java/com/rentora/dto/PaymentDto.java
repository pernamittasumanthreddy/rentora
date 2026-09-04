package com.rentora.dto;

import com.rentora.entity.PaymentStatus;
import lombok.*;
import java.math.BigDecimal;
import java.time.LocalDateTime;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class PaymentDto {

    private Long id;
    private Long rentalId;
    private BigDecimal amount;
    private BigDecimal depositAmount;
    private PaymentStatus paymentStatus;
    private String paymentMethod;
    private String transactionRef;
    private LocalDateTime paymentDate;
}
