package com.rentora.service;

import com.rentora.dto.ProductDto;
import com.rentora.entity.Category;
import com.rentora.entity.Product;
import com.rentora.entity.Vendor;
import com.rentora.exception.ResourceNotFoundException;
import com.rentora.repository.CategoryRepository;
import com.rentora.repository.ProductRepository;
import com.rentora.repository.VendorRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.stream.Collectors;

@Service
@RequiredArgsConstructor
public class ProductService {

    private final ProductRepository productRepository;
    private final VendorRepository vendorRepository;
    private final CategoryRepository categoryRepository;

    public List<ProductDto> getAllProducts() {
        return productRepository.findAll().stream()
                .map(this::mapToDto)
                .collect(Collectors.toList());
    }

    public ProductDto getProductById(Long id) {
        Product product = productRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Product", "id", id));
        return mapToDto(product);
    }

    public List<ProductDto> getProductsByCategory(Long categoryId) {
        return productRepository.findByCategoryId(categoryId).stream()
                .map(this::mapToDto)
                .collect(Collectors.toList());
    }

    public List<ProductDto> searchProducts(String query) {
        return productRepository.findByNameContainingIgnoreCase(query).stream()
                .map(this::mapToDto)
                .collect(Collectors.toList());
    }

    @Transactional
    public ProductDto createProduct(ProductDto dto) {
        Vendor vendor = vendorRepository.findById(dto.getVendorId())
                .orElseThrow(() -> new ResourceNotFoundException("Vendor", "id", dto.getVendorId()));

        Category category = categoryRepository.findById(dto.getCategoryId())
                .orElseThrow(() -> new ResourceNotFoundException("Category", "id", dto.getCategoryId()));

        Product product = Product.builder()
                .vendor(vendor)
                .category(category)
                .name(dto.getName())
                .description(dto.getDescription())
                .pricePerDay(dto.getPricePerDay())
                .deposit(dto.getDeposit())
                .availability(dto.getAvailability() != null ? dto.getAvailability() : true)
                .stockCount(dto.getStockCount() != null ? dto.getStockCount() : 1)
                .imageUrl(dto.getImageUrl())
                .rating(5.0)
                .reviewCount(0)
                .build();

        return mapToDto(productRepository.save(product));
    }

    @Transactional
    public ProductDto updateProduct(Long id, ProductDto dto) {
        Product product = productRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Product", "id", id));

        if (dto.getName() != null) product.setName(dto.getName());
        if (dto.getDescription() != null) product.setDescription(dto.getDescription());
        if (dto.getPricePerDay() != null) product.setPricePerDay(dto.getPricePerDay());
        if (dto.getDeposit() != null) product.setDeposit(dto.getDeposit());
        if (dto.getAvailability() != null) product.setAvailability(dto.getAvailability());
        if (dto.getStockCount() != null) product.setStockCount(dto.getStockCount());
        if (dto.getImageUrl() != null) product.setImageUrl(dto.getImageUrl());

        if (dto.getCategoryId() != null) {
            Category category = categoryRepository.findById(dto.getCategoryId())
                    .orElseThrow(() -> new ResourceNotFoundException("Category", "id", dto.getCategoryId()));
            product.setCategory(category);
        }

        return mapToDto(productRepository.save(product));
    }

    @Transactional
    public void deleteProduct(Long id) {
        Product product = productRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Product", "id", id));
        productRepository.delete(product);
    }

    private ProductDto mapToDto(Product p) {
        return ProductDto.builder()
                .id(p.getId())
                .vendorId(p.getVendor().getId())
                .vendorName(p.getVendor().getBusinessName())
                .vendorRating(p.getVendor().getRating())
                .categoryId(p.getCategory().getId())
                .categoryName(p.getCategory().getName())
                .name(p.getName())
                .description(p.getDescription())
                .pricePerDay(p.getPricePerDay())
                .deposit(p.getDeposit())
                .availability(p.getAvailability())
                .stockCount(p.getStockCount())
                .imageUrl(p.getImageUrl())
                .rating(p.getRating())
                .reviewCount(p.getReviewCount())
                .build();
    }
}
