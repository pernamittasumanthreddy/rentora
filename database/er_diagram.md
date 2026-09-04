# Rentora - Database Entity Relationship (ER) Diagram & Data Dictionary

```mermaid
erDiagram
    USERS ||--o| VENDORS : "owns hub"
    USERS ||--o{ RENTALS : "places order"
    USERS ||--o{ REVIEWS : "writes review"
    VENDORS ||--o{ PRODUCTS : "lists hardware"
    CATEGORIES ||--o{ PRODUCTS : "categorizes"
    PRODUCTS ||--o{ RENTALS : "is rented in"
    PRODUCTS ||--o{ REVIEWS : "receives feedback"
    RENTALS ||--o| RETURNS : "initiates return"
    RENTALS ||--o{ PAYMENTS : "records ledger"

    USERS {
        bigint id PK
        string name
        string email UK
        string password
        enum role "CUSTOMER, VENDOR, ADMIN"
        string phone
        string status
        string city
        string address
        timestamp created_at
    }

    VENDORS {
        bigint id PK
        bigint user_id FK
        string business_name
        string address
        string city
        double rating
        int trust_score
    }

    CATEGORIES {
        bigint id PK
        string name UK
        string slug UK
        text description
    }

    PRODUCTS {
        bigint id PK
        bigint vendor_id FK
        bigint category_id FK
        string name
        text description
        decimal price_per_day
        decimal deposit
        boolean availability
        int stock_count
        string image_url
        double rating
        int review_count
    }

    RENTALS {
        bigint id PK
        bigint customer_id FK
        bigint product_id FK
        date start_date
        date end_date
        enum status "PENDING, APPROVED, ACTIVE, RETURNED, COMPLETED, CANCELLED"
        decimal total_amount
        decimal deposit
        text delivery_address
        string tracking_number
        timestamp created_at
    }

    RETURNS {
        bigint id PK
        bigint rental_id FK, UK
        enum status "PENDING, INSPECTED, SETTLED"
        text damage_report
        decimal damage_fee
        decimal deposit_refunded
        date return_date
    }

    PAYMENTS {
        bigint id PK
        bigint rental_id FK
        decimal amount
        enum payment_status "PENDING, PAID, HELD_IN_ESCROW, REFUNDED"
        string payment_method
        string transaction_ref UK
        timestamp payment_date
    }

    REVIEWS {
        bigint id PK
        bigint customer_id FK
        bigint product_id FK
        int rating "1-5"
        text comment
        timestamp created_at
    }
```

---

## Table Descriptions

| Table Name | Primary Purpose | Foreign Keys | Key Constraints |
| :--- | :--- | :--- | :--- |
| **`users`** | Core accounts for Customers, Vendors, and Admins | None | `email UNIQUE` |
| **`vendors`** | Commercial business profiles & Trust Scores | `user_id -> users(id)` | `user_id UNIQUE` |
| **`categories`** | Equipment departments & classification | None | `name UNIQUE, slug UNIQUE` |
| **`products`** | Hardware catalog items with daily rate & deposit | `vendor_id`, `category_id` | Indexed price, category, vendor |
| **`rentals`** | Booking contracts with dates, tracking, & total amount | `customer_id`, `product_id` | Indexed status, dates |
| **`returns`** | Multi-point technical inspection & deposit deductions | `rental_id -> rentals(id)` | `rental_id UNIQUE` (1:1) |
| **`payments`** | Financial transaction log & Escrow states | `rental_id -> rentals(id)` | `transaction_ref UNIQUE` |
| **`reviews`** | Verified customer feedback and 1-5 star ratings | `customer_id`, `product_id` | Rating check `1 <= rating <= 5` |
