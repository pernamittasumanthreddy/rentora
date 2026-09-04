/**
 * RENTORA - API Client with Spring Boot JWT Bearer Interceptors & Mock Fallback
 */

import axios from 'axios';
import { storageService } from './mockStorage';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8080/api';

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 5000,
});

// Request interceptor for JWT
apiClient.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('rentora_token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// Unified Service APIs with automatic fallback
export const api = {
  // Auth
  login: async (credentials) => {
    try {
      const response = await apiClient.post('/auth/login', credentials);
      return response.data;
    } catch {
      // Fallback for local demo
      const users = storageService.getUsers();
      const user = users.find((u) => u.email.toLowerCase() === credentials.email.toLowerCase());
      if (user) {
        const token = `mock-jwt-token-${user.id}-${Date.now()}`;
        return {
          token,
          user: {
            id: user.id,
            name: user.name,
            email: user.email,
            role: user.role,
            phone: user.phone,
            avatar: user.avatar,
            city: user.city,
            businessName: user.businessName,
          },
        };
      }
      throw new Error('Invalid email or password');
    }
  },

  register: async (userData) => {
    try {
      const response = await apiClient.post('/auth/register', userData);
      return response.data;
    } catch {
      const users = storageService.getUsers();
      const newUser = {
        id: Date.now(),
        name: userData.name,
        email: userData.email,
        role: userData.role || 'ROLE_CUSTOMER',
        phone: userData.phone || '',
        status: 'ACTIVE',
        city: userData.city || 'Bengaluru',
        createdAt: new Date().toISOString().split('T')[0],
      };
      users.push(newUser);
      localStorage.setItem('rentora_users', JSON.stringify(users));
      const token = `mock-jwt-token-${newUser.id}-${Date.now()}`;
      return { token, user: newUser };
    }
  },

  // Products
  getProducts: async () => {
    try {
      const res = await apiClient.get('/products');
      return res.data;
    } catch {
      return storageService.getProducts();
    }
  },

  getProductById: async (id) => {
    try {
      const res = await apiClient.get(`/products/${id}`);
      return res.data;
    } catch {
      return storageService.getProductById(id);
    }
  },

  createProduct: async (productData) => {
    try {
      const res = await apiClient.post('/products', productData);
      return res.data;
    } catch {
      return storageService.addProduct(productData);
    }
  },

  updateProduct: async (id, productData) => {
    try {
      const res = await apiClient.put(`/products/${id}`, productData);
      return res.data;
    } catch {
      return storageService.updateProduct(id, productData);
    }
  },

  deleteProduct: async (id) => {
    try {
      const res = await apiClient.delete(`/products/${id}`);
      return res.data;
    } catch {
      return storageService.deleteProduct(id);
    }
  },

  // Categories
  getCategories: async () => {
    try {
      const res = await apiClient.get('/categories');
      return res.data;
    } catch {
      return storageService.getCategories();
    }
  },

  // Rentals
  getRentals: async () => {
    try {
      const res = await apiClient.get('/rentals');
      return res.data;
    } catch {
      return storageService.getRentals();
    }
  },

  createRental: async (rentalData) => {
    try {
      const res = await apiClient.post('/rentals', rentalData);
      return res.data;
    } catch {
      return storageService.createRental(rentalData);
    }
  },

  updateRentalStatus: async (id, status) => {
    try {
      const res = await apiClient.put(`/rentals/${id}/status`, { status });
      return res.data;
    } catch {
      return storageService.updateRentalStatus(id, status);
    }
  },

  // Returns
  getReturns: async () => {
    try {
      const res = await apiClient.get('/returns');
      return res.data;
    } catch {
      return storageService.getReturns();
    }
  },

  createReturn: async (returnData) => {
    try {
      const res = await apiClient.post('/returns', returnData);
      return res.data;
    } catch {
      return storageService.createReturn(returnData);
    }
  },

  settleReturn: async (returnId, settlementData) => {
    try {
      const res = await apiClient.put(`/returns/${returnId}/settle`, settlementData);
      return res.data;
    } catch {
      return storageService.settleReturn(
        returnId,
        settlementData.damageFee,
        settlementData.condition,
        settlementData.damageReport
      );
    }
  },

  // Payments
  getPayments: async () => {
    try {
      const res = await apiClient.get('/payments');
      return res.data;
    } catch {
      return storageService.getPayments();
    }
  },

  // Reviews
  getReviews: async () => {
    try {
      const res = await apiClient.get('/reviews');
      return res.data;
    } catch {
      return storageService.getReviews();
    }
  },

  createReview: async (reviewData) => {
    try {
      const res = await apiClient.post('/reviews', reviewData);
      return res.data;
    } catch {
      return storageService.addReview(reviewData);
    }
  },

  // Users & Vendors
  getUsers: async () => {
    try {
      const res = await apiClient.get('/users');
      return res.data;
    } catch {
      return storageService.getUsers();
    }
  },

  getVendors: async () => {
    try {
      const res = await apiClient.get('/vendors');
      return res.data;
    } catch {
      return storageService.getVendors();
    }
  },
};

export default apiClient;
