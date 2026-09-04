# ==============================================================================
# Rentora Multi-Stage Production Dockerfile
# Stage 1: Build React Frontend
# Stage 2: Build Spring Boot Backend
# Stage 3: Unified Production Runtime Container
# ==============================================================================

FROM node:20-alpine AS frontend-builder
WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm ci
COPY frontend/ ./
RUN npm run build

FROM maven:3.9-eclipse-temurin-17-alpine AS backend-builder
WORKDIR /app/backend
COPY backend/pom.xml ./
RUN mvn dependency:go-offline -B
COPY backend/src ./src
RUN mvn clean package -DskipTests -B

FROM eclipse-temurin:17-jre-alpine AS runtime
LABEL maintainer="Rentora DevOps Team <devops@rentora.in>"
LABEL version="1.0.0"
LABEL description="Rentora Smart Rental & Sharing Platform Unified Container"

RUN apk add --no-cache bash curl python3 py3-pip nginx supervisor

WORKDIR /app

# Copy built frontend assets to Nginx html directory
COPY --from=frontend-builder /app/frontend/dist /usr/share/nginx/html

# Copy built Spring Boot executable jar
COPY --from=backend-builder /app/backend/target/*.jar /app/rentora-backend.jar

# Copy database migrations and seed scripts
COPY database/ /app/database/
COPY services/ /app/services/

# Expose ports: 80 (Frontend / Reverse Proxy), 8080 (Spring Boot API), 8000 (Python Engine)
EXPOSE 80 8080 8000

ENV SPRING_PROFILES_ACTIVE=prod
ENV SERVER_PORT=8080

HEALTHCHECK --interval=30s --timeout=5s --start-period=40s --retries=3 \
  CMD curl -f http://localhost:8080/actuator/health || exit 1

ENTRYPOINT ["java", "-Djava.security.egd=file:/dev/./urandom", "-jar", "/app/rentora-backend.jar"]
