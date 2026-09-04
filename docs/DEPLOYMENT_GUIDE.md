# Rentora - Production Cloud Deployment Guide

This guide details steps to deploy **Rentora** to production cloud environments:
- **Frontend**: Vercel or Netlify (Vite SPA)
- **Backend**: Render, Railway, or Docker Container (Spring Boot 3)
- **Database**: Managed MySQL 8.0 (Railway, Aiven, or AWS RDS)

---

## 1. Database Deployment (MySQL 8.0)

1. Provision a managed MySQL instance on **Railway**, **Aiven**, or **AWS RDS**.
2. Connect using MySQL Workbench, DBeaver, or command line:
   ```bash
   mysql -h <DB_HOST> -u <DB_USER> -p -P <DB_PORT> < database/schema.sql
   mysql -h <DB_HOST> -u <DB_USER> -p -P <DB_PORT> < database/seed.sql
   ```
3. Note your JDBC connection string:
   ```
   jdbc:mysql://<DB_HOST>:<DB_PORT>/rentora_db?useSSL=true&serverTimezone=UTC
   ```

---

## 2. Backend Deployment (Spring Boot 3)

### Option A: Railway / Render (Using Dockerfile)

Create a `backend/Dockerfile`:
```dockerfile
FROM eclipse-temurin:17-jdk-jammy AS build
WORKDIR /app
COPY pom.xml .
COPY src ./src
RUN ./mvnw clean package -DskipTests

FROM eclipse-temurin:17-jre-jammy
WORKDIR /app
COPY --from=build /app/target/*.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
```

### Environment Variables for Backend:
| Variable | Value | Description |
| :--- | :--- | :--- |
| `DB_URL` | `jdbc:mysql://.../rentora_db` | Cloud MySQL connection string |
| `DB_USERNAME` | `root` | Database user |
| `DB_PASSWORD` | `your_db_password` | Database password |
| `APP_JWT_SECRET` | `your-secure-256-bit-secret` | 32+ character hex or base64 key |

---

## 3. Frontend Deployment (Vercel / Netlify)

1. Push your repository to GitHub or GitLab.
2. Link the repository in **Vercel** or **Netlify**.
3. Set **Root Directory** to `frontend`.
4. Build Settings:
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`
5. Configure Environment Variables:
   - `VITE_API_URL`: `https://your-backend-service.onrender.com/api`
6. Add SPA rewrite rule in `frontend/vercel.json` or `frontend/public/_redirects`:
   ```
   /*    /index.html   200
   ```

---

## 4. Local Quick Start

### Running the Frontend:
```powershell
cd c:\Users\BABI\Desktop\rentora\frontend
npm install
npm run dev
```
Open **[http://127.0.0.1:3000/](http://127.0.0.1:3000/)** in your browser.

### Running the Backend:
```powershell
cd c:\Users\BABI\Desktop\rentora\backend
mvn clean spring-boot:run
```
Swagger UI will be live at: **`http://localhost:8080/swagger-ui.html`**
