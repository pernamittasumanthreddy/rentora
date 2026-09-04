package com.rentora.entity;

import jakarta.persistence.*;
import lombok.*;
import java.math.BigDecimal;
import java.time.LocalDate;

@Entity
@Table(name = "returns")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class ReturnRecord {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @OneToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "rental_id", nullable = false)
    private Rental rental;

    @Enumerated(EnumType.STRING)
    @Column(nullable = false)
    @Builder.Default
    private ReturnStatus status = ReturnStatus.PENDING;

    @Column(name = "damage_report", columnDefinition = "TEXT")
    private String damageReport;

    @Column(name = "damage_fee")
    @Builder.Default
    private BigDecimal damageFee = BigDecimal.ZERO;

    @Column(name = "deposit_refunded")
    @Builder.Default
    private BigDecimal depositRefunded = BigDecimal.ZERO;

    @Column(name = "return_date")
    private LocalDate returnDate;
}
