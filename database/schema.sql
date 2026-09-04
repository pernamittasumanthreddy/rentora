-- ==========================================================
-- RENTORA - Smart Product Rental & Sharing Platform
-- Production MySQL 8.0+ Database Schema (DDL)
-- ==========================================================

CREATE DATABASE IF NOT EXISTS rentora_db
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE rentora_db;

-- Disable FK checks during structure creation
SET FOREIGN_KEY_CHECKS = 0;

-- 1. USERS TABLE
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    email VARCHAR(180) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    role ENUM('ROLE_CUSTOMER', 'ROLE_VENDOR', 'ROLE_ADMIN') NOT NULL DEFAULT 'ROLE_CUSTOMER',
    phone VARCHAR(20),
    status VARCHAR(30) NOT NULL DEFAULT 'ACTIVE',
    city VARCHAR(100) DEFAULT 'Bengaluru',
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_users_email (email),
    INDEX idx_users_role (role),
    INDEX idx_users_status (status)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 2. VENDORS TABLE
DROP TABLE IF EXISTS vendors;
CREATE TABLE vendors (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    user_id BIGINT NOT NULL UNIQUE,
    business_name VARCHAR(200) NOT NULL,
    address TEXT,
    city VARCHAR(100) DEFAULT 'Bengaluru',
    rating DOUBLE DEFAULT 5.0,
    trust_score INT DEFAULT 95,
    CONSTRAINT fk_vendors_user FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX idx_vendors_city (city),
    INDEX idx_vendors_trust (trust_score)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 3. CATEGORIES TABLE
DROP TABLE IF EXISTS categories;
CREATE TABLE categories (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    slug VARCHAR(120) NOT NULL UNIQUE,
    description TEXT,
    INDEX idx_categories_slug (slug)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 4. PRODUCTS TABLE
DROP TABLE IF EXISTS products;
CREATE TABLE products (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    vendor_id BIGINT NOT NULL,
    category_id BIGINT NOT NULL,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price_per_day DECIMAL(12, 2) NOT NULL,
    deposit DECIMAL(12, 2) NOT NULL,
    availability BOOLEAN NOT NULL DEFAULT TRUE,
    stock_count INT NOT NULL DEFAULT 1,
    image_url VARCHAR(500),
    rating DOUBLE DEFAULT 5.0,
    review_count INT DEFAULT 0,
    CONSTRAINT fk_products_vendor FOREIGN KEY (vendor_id) REFERENCES vendors(id) ON DELETE CASCADE,
    CONSTRAINT fk_products_category FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE RESTRICT,
    INDEX idx_products_vendor (vendor_id),
    INDEX idx_products_category (category_id),
    INDEX idx_products_price (price_per_day),
    INDEX idx_products_availability (availability)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 5. RENTALS TABLE
DROP TABLE IF EXISTS rentals;
CREATE TABLE rentals (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    customer_id BIGINT NOT NULL,
    product_id BIGINT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    status ENUM('PENDING', 'APPROVED', 'ACTIVE', 'RETURNED', 'COMPLETED', 'CANCELLED') NOT NULL DEFAULT 'PENDING',
    total_amount DECIMAL(12, 2) NOT NULL,
    deposit DECIMAL(12, 2) NOT NULL,
    delivery_address TEXT,
    tracking_number VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_rentals_customer FOREIGN KEY (customer_id) REFERENCES users(id) ON DELETE CASCADE,
    CONSTRAINT fk_rentals_product FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE RESTRICT,
    INDEX idx_rentals_customer (customer_id),
    INDEX idx_rentals_product (product_id),
    INDEX idx_rentals_status (status),
    INDEX idx_rentals_dates (start_date, end_date)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 6. RETURNS TABLE
DROP TABLE IF EXISTS returns;
CREATE TABLE returns (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    rental_id BIGINT NOT NULL UNIQUE,
    status ENUM('PENDING', 'INSPECTED', 'SETTLED') NOT NULL DEFAULT 'PENDING',
    damage_report TEXT,
    damage_fee DECIMAL(12, 2) DEFAULT 0.00,
    deposit_refunded DECIMAL(12, 2) DEFAULT 0.00,
    return_date DATE,
    CONSTRAINT fk_returns_rental FOREIGN KEY (rental_id) REFERENCES rentals(id) ON DELETE CASCADE,
    INDEX idx_returns_status (status)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 7. PAYMENTS TABLE
DROP TABLE IF EXISTS payments;
CREATE TABLE payments (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    rental_id BIGINT NOT NULL,
    amount DECIMAL(12, 2) NOT NULL,
    payment_status ENUM('PENDING', 'PAID', 'HELD_IN_ESCROW', 'REFUNDED') NOT NULL DEFAULT 'PAID',
    payment_method VARCHAR(50) DEFAULT 'UPI / NetBanking',
    transaction_ref VARCHAR(100) UNIQUE,
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_payments_rental FOREIGN KEY (rental_id) REFERENCES rentals(id) ON DELETE CASCADE,
    INDEX idx_payments_rental (rental_id),
    INDEX idx_payments_status (payment_status)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 8. REVIEWS TABLE
DROP TABLE IF EXISTS reviews;
CREATE TABLE reviews (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    customer_id BIGINT NOT NULL,
    product_id BIGINT NOT NULL,
    rating INT NOT NULL CHECK (rating >= 1 AND rating <= 5),
    comment TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_reviews_customer FOREIGN KEY (customer_id) REFERENCES users(id) ON DELETE CASCADE,
    CONSTRAINT fk_reviews_product FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE,
    INDEX idx_reviews_product (product_id),
    INDEX idx_reviews_rating (rating)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

SET FOREIGN_KEY_CHECKS = 1;
