package com.rentora.controller;

import com.rentora.dto.ReviewDto;
import com.rentora.service.ReviewService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import jakarta.validation.Valid;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/reviews")
@RequiredArgsConstructor
@Tag(name = "Reviews & Ratings", description = "Verified customer hardware and vendor ratings")
public class ReviewController {

    private final ReviewService reviewService;

    @GetMapping
    @Operation(summary = "Get all customer reviews")
    public ResponseEntity<List<ReviewDto>> getAllReviews(@RequestParam(required = false) Long productId) {
        if (productId != null) {
            return ResponseEntity.ok(reviewService.getReviewsByProduct(productId));
        }
        return ResponseEntity.ok(reviewService.getAllReviews());
    }

    @PostMapping
    @Operation(summary = "Submit verified customer review for hardware")
    public ResponseEntity<ReviewDto> addReview(@Valid @RequestBody ReviewDto reviewDto) {
        return new ResponseEntity<>(reviewService.addReview(reviewDto), HttpStatus.CREATED);
    }

    @DeleteMapping("/{id}")
    @Operation(summary = "Delete review by ID")
    public ResponseEntity<Void> deleteReview(@PathVariable Long id) {
        reviewService.deleteReview(id);
        return ResponseEntity.noContent().build();
    }
}
