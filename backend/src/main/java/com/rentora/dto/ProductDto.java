package com.rentora.dto;

import jakarta.validation.constraints.DecimalMin;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import lombok.*;
import java.math.BigDecimal;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class ProductDto {

    private Long id;
    private Long vendorId;
    private String vendorName;
    private Double vendorRating;

    @NotNull(message = "Category ID is required")
    private Long categoryId;
    private String categoryName;

    @NotBlank(message = "Product name is required")
    private String name;

    private String description;

    @NotNull(message = "Price per day is required")
    @DecimalMin(value = "0.0", inclusive = false, message = "Price per day must be greater than 0")
    private BigDecimal pricePerDay;

    @NotNull(message = "Deposit is required")
    @DecimalMin(value = "0.0", inclusive = false, message = "Deposit must be greater than 0")
    private BigDecimal deposit;

    @Builder.Default
    private Boolean availability = true;

    @Builder.Default
    private Integer stockCount = 1;

    private String imageUrl;
    private Double rating;
    private Integer reviewCount;
}
