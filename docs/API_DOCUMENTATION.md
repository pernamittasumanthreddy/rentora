# Rentora - Complete REST API Documentation

Base API URL: `http://localhost:8080/api`  
Swagger UI Interactive Console: `http://localhost:8080/swagger-ui.html`  
OpenAPI JSON Schema: `http://localhost:8080/v3/api-docs`  

---

## 1. Authentication Service (`/api/auth`)

### `POST /api/auth/register`
Register a new customer or equipment vendor.

**Request Payload:**
```json
{
  "name": "Rahul Sharma",
  "email": "customer@rentora.in",
  "password": "password123",
  "role": "ROLE_CUSTOMER",
  "phone": "+91 98450 11223",
  "city": "Bengaluru",
  "businessName": null
}
```

**Response `201 Created`:**
```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "tokenType": "Bearer",
  "userId": 1,
  "name": "Rahul Sharma",
  "email": "customer@rentora.in",
  "role": "ROLE_CUSTOMER",
  "businessName": null
}
```

### `POST /api/auth/login`
Authenticate with email and password to receive a JWT Bearer token.

**Request Payload:**
```json
{
  "email": "customer@rentora.in",
  "password": "password123"
}
```

**Response `200 OK`:**
```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "tokenType": "Bearer",
  "userId": 1,
  "name": "Rahul Sharma",
  "email": "customer@rentora.in",
  "role": "ROLE_CUSTOMER"
}
```

---

## 2. Product Catalog Service (`/api/products`)

### `GET /api/products`
Fetch all available equipment or filter with search queries.
- Query Parameters:
  - `search`: Filter by model or keywords (e.g. `Sony`, `Drone`)
  - `categoryId`: Filter by department ID (e.g. `1`)

**Response `200 OK`:**
```json
[
  {
    "id": 1,
    "vendorId": 101,
    "vendorName": "Apex Cine Rentals",
    "vendorRating": 4.9,
    "categoryId": 1,
    "categoryName": "Cameras & Cinematic Gear",
    "name": "Sony FX3 Cinema Line Full-Frame Camera",
    "description": "Compact cinema camera with 12.1MP full-frame sensor...",
    "pricePerDay": 2800.00,
    "deposit": 8500.00,
    "availability": true,
    "stockCount": 3,
    "imageUrl": "https://images.unsplash.com/photo-1516035069371-29a1b244cc32...",
    "rating": 4.9,
    "reviewCount": 42
  }
]
```

### `POST /api/products` *(Requires `ROLE_VENDOR` or `ROLE_ADMIN`)*
Add a new hardware unit to the marketplace.

---

## 3. Rental Lifecycle Service (`/api/rentals`)

### `POST /api/rentals` *(Requires Bearer Token)*
Create and checkout a new rental booking with Escrow deposit.

**Request Payload:**
```json
{
  "customerId": 1,
  "productId": 1,
  "startDate": "2026-09-08",
  "endDate": "2026-09-11",
  "totalAmount": 18412.00,
  "deposit": 8500.00,
  "deliveryAddress": "Flat 402, Green Glen Layout, Bellandur, Bengaluru 560103"
}
```

**Response `201 Created`:**
```json
{
  "id": 1001,
  "customerId": 1,
  "customerName": "Rahul Sharma",
  "productId": 1,
  "productName": "Sony FX3 Cinema Line Full-Frame Camera",
  "startDate": "2026-09-08",
  "endDate": "2026-09-11",
  "status": "PENDING",
  "totalAmount": 18412.00,
  "deposit": 8500.00,
  "trackingNumber": "TRK-2026-892144"
}
```

### `PUT /api/rentals/{id}/status`
Update lifecycle state (`APPROVED`, `ACTIVE`, `RETURNED`, `COMPLETED`, `CANCELLED`).

---

## 4. Return & Inspection Service (`/api/returns`)

### `POST /api/returns`
Initiate return pickup for an active hardware rental.

### `PUT /api/returns/{id}/settle` *(Requires `ROLE_VENDOR` or `ROLE_ADMIN`)*
Record 5-point technical inspection results, assess damage fee (₹0 if pristine), and release remaining escrow deposit.

**Request Payload:**
```json
{
  "damageFee": 0,
  "damageReport": "Hardware returned in pristine condition. All 3 batteries and case verified."
}
```

---

## 5. Reports & Analytics Service (`/api/reports`)

### `GET /api/reports/analytics` *(Requires `ROLE_ADMIN`)*
Platform KPIs and financial overview.

**Response `200 OK`:**
```json
{
  "totalGMV": 5288600.00,
  "activeRentals": 14,
  "completedRentals": 268,
  "totalUsers": 54,
  "totalVendors": 16,
  "totalProducts": 33
}
```
