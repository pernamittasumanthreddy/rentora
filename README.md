# RENTORA – Smart Product Rental & Sharing Platform
> **"Rent • Share • Save • Sustain"**

![Rentora Platform](https://images.unsplash.com/photo-1516035069371-29a1b244cc32?auto=format&fit=crop&w=1200&q=80)

Rentora is a production-grade, full-stack rental marketplace connecting content creators, engineers, and professionals with commercial hardware vendors across India. The platform supports seamless discovery, live calendar booking, 100% escrow security deposit protection, 5-point technical damage inspections, and multi-tenant role dashboards.

---

## 🚀 Live Preview Links

The React + Vite frontend is **currently running locally**:

👉 **[http://127.0.0.1:3000/](http://127.0.0.1:3000/)**

| Portal / Module | URL | Description |
| :--- | :--- | :--- |
| **Marketplace Home** | [http://127.0.0.1:3000/](http://127.0.0.1:3000/) | Hero search, curated departments, how it works, testimonials |
| **Equipment Catalog** | [http://127.0.0.1:3000/products](http://127.0.0.1:3000/products) | Faceted filters (category, price slider, city, rating sort) |
| **Customer Portal** | [http://127.0.0.1:3000/customer/dashboard](http://127.0.0.1:3000/customer/dashboard) | Active rentals, held escrow deposits, wishlist, orders |
| **Vendor Operations** | [http://127.0.0.1:3000/vendor/dashboard](http://127.0.0.1:3000/vendor/dashboard) | Fleet management, rental requests, returns & 5-point checks |
| **Admin Command Center** | [http://127.0.0.1:3000/admin/dashboard](http://127.0.0.1:3000/admin/dashboard) | Platform governance, dispute mediation, user & vendor KYC |
| **Reports & Analytics** | [http://127.0.0.1:3000/admin/reports](http://127.0.0.1:3000/admin/reports) | Recharts interactive GMV, category share, and CSV export |

---

## 🔑 Demo Login Accounts

Rentora comes pre-configured with 1-click role switching on the top floating banner, or you can log in with:

| Role | Email | Password | Pre-loaded Data |
| :--- | :--- | :--- | :--- |
| **Customer** | `customer@rentora.in` | `password123` | Active rentals (Sony FX3), saved wishlist items, escrow ledger |
| **Vendor** | `vendor@rentora.in` | `password123` | Apex Cine Rentals, listed equipment fleet, pending requests |
| **Admin** | `admin@rentora.in` | `password123` | Full operations access, dispute resolution, analytics charts |

---

## 🛠 Technology Stack

### Frontend
- **Framework**: React 18 + Vite
- **Styling**: Tailwind CSS (Custom luxury color tokens: Forest Green `#14532D`, Emerald `#10B981`, Accent Gold `#D97706`, Sand `#F8F7F4`)
- **Routing**: React Router DOM v6 (Nested role layouts & protected routes)
- **Visual Charts**: Recharts (Monthly GMV bar charts, category donut charts, order volume area charts)
- **Icons**: Lucide React
- **HTTP Client**: Axios with JWT Bearer Interceptors & Mock Storage Bridge

### Backend
- **Framework**: Spring Boot 3.3.x
- **Security**: Spring Security 6 + JWT (JJWT 0.12.x) stateless filter chain
- **Persistence**: Spring Data JPA + Hibernate ORM
- **Database**: MySQL 8.0+ (with H2 dev profile fallback)
- **API Documentation**: SpringDoc OpenAPI 3.0 & Swagger UI
- **Build Tool**: Apache Maven

---

## 📁 Repository Structure

```
rentora/
├── frontend/                          # React + Vite + Tailwind Frontend
│   ├── src/
│   │   ├── components/                # UI components (Navbar, Footer, ProductCard, StatCard)
│   │   ├── contexts/                  # AuthContext, CartContext, NotificationContext
│   │   ├── data/                      # Initial seed products, categories, reviews, and vendors
│   │   ├── layouts/                   # PublicLayout, CustomerLayout, VendorLayout, AdminLayout
│   │   ├── pages/
│   │   │   ├── public/                # Home, AboutUs, ProductListing, ProductDetails, Login, Register
│   │   │   ├── customer/              # Dashboard, MyRentals, Wishlist, Payments, Reviews, Settings, Checkout
│   │   │   ├── vendor/                # Dashboard, Products, AddEditProduct, Inventory, Requests, Returns, Earnings
│   │   │   └── admin/                 # Dashboard, Users, Vendors, Products, Categories, Rentals, Returns, Reports, Settings
│   │   ├── routes/                    # AppRoutes & ProtectedRoute
│   │   ├── services/                  # apiClient & mockStorage bridge
│   │   ├── utils/                     # Currency (₹ INR), date, and GST calculations
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── index.css
│   ├── package.json
│   ├── vite.config.js
│   └── tailwind.config.js
│
├── backend/                           # Spring Boot 3 Enterprise API
│   ├── pom.xml                        # Maven configuration
│   ├── src/main/java/com/rentora/
│   │   ├── RentoraApplication.java    # Spring Boot entry point
│   │   ├── config/                    # SecurityConfig, CorsConfig, OpenApiConfig
│   │   ├── controller/                # Auth, User, Product, Category, Rental, Return, Review, Payment, Report
│   │   ├── dto/                       # Request/Response DTOs
│   │   ├── entity/                    # User, Vendor, Category, Product, Rental, ReturnRecord, Payment, Review
│   │   ├── exception/                 # GlobalExceptionHandler & custom exceptions
│   │   ├── repository/                # Spring Data JPA repositories
│   │   ├── security/                  # JwtTokenProvider, JwtAuthenticationFilter, UserPrincipal
│   │   └── service/                   # Business logic services
│   └── src/main/resources/
│       ├── application.yml            # MySQL production datasource
│       └── application-dev.yml        # In-memory H2 dev profile
│
├── database/                          # MySQL 8.0 Assets
│   ├── schema.sql                     # Complete DDL with foreign keys and indexes
│   ├── seed.sql                       # Seed data for immediate database population
│   └── er_diagram.md                  # Mermaid ER diagram and table dictionary
│
├── docs/                              # Production Documentation
│   ├── API_DOCUMENTATION.md           # Full OpenAPI specifications
│   └── DEPLOYMENT_GUIDE.md            # Vercel/Netlify + Render/Railway cloud deployment
└── README.md
```

---

## 💻 Local Setup & Execution

### 1. Frontend
```bash
cd frontend
npm install
npm run dev
```
Runs at `http://127.0.0.1:3000/`.

### 2. Backend (Spring Boot 3)
```bash
cd backend
mvn clean spring-boot:run
```
Swagger UI will be live at `http://localhost:8080/swagger-ui.html`.

### 3. Database (MySQL)
Import the provided schema and seed data:
```bash
mysql -u root -p < database/schema.sql
mysql -u root -p < database/seed.sql
```

---

## 📄 License & Commercial Rights
Designed and built for **Rentora Technologies Private Limited**. All rights reserved.
