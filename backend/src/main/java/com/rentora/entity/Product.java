package com.rentora.entity;

import jakarta.persistence.*;
import lombok.*;
import java.math.BigDecimal;

@Entity
@Table(name = "products")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Product {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "vendor_id", nullable = false)
    private Vendor vendor;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "category_id", nullable = false)
    private Category category;

    @Column(nullable = false)
    private String name;

    @Column(columnDefinition = "TEXT")
    private String description;

    @Column(name = "price_per_day", nullable = false)
    private BigDecimal pricePerDay;

    @Column(nullable = false)
    private BigDecimal deposit;

    @Builder.Default
    private Boolean availability = true;

    @Builder.Default
    @Column(name = "stock_count")
    private Integer stockCount = 1;

    @Column(name = "image_url")
    private String imageUrl;

    @Builder.Default
    private Double rating = 5.0;

    @Builder.Default
    @Column(name = "review_count")
    private Integer reviewCount = 0;
}
