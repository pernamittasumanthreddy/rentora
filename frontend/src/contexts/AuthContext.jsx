import React, { createContext, useContext, useState, useEffect } from 'react';
import { api } from '../services/apiClient';
import { storageService, initializeStorage } from '../services/mockStorage';

const AuthContext = createContext(null);

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [token, setToken] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    initializeStorage();
    const savedToken = localStorage.getItem('rentora_token');
    const savedUser = localStorage.getItem('rentora_user');

    if (savedToken && savedUser) {
      try {
        setToken(savedToken);
        setUser(JSON.parse(savedUser));
      } catch {
        localStorage.removeItem('rentora_token');
        localStorage.removeItem('rentora_user');
      }
    } else {
      // Default to demo customer for first-time instant preview
      const defaultUser = {
        id: 1,
        name: 'Rahul Sharma',
        email: 'customer@rentora.in',
        role: 'ROLE_CUSTOMER',
        phone: '+91 98450 11223',
        status: 'ACTIVE',
        avatar: 'https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?auto=format&fit=crop&w=200&q=80',
        city: 'Bengaluru',
      };
      const defaultToken = 'mock-jwt-customer-initial';
      setUser(defaultUser);
      setToken(defaultToken);
      localStorage.setItem('rentora_user', JSON.stringify(defaultUser));
      localStorage.setItem('rentora_token', defaultToken);
    }
    setLoading(false);
  }, []);

  const login = async (email, password) => {
    const data = await api.login({ email, password });
    setUser(data.user);
    setToken(data.token);
    localStorage.setItem('rentora_user', JSON.stringify(data.user));
    localStorage.setItem('rentora_token', data.token);
    return data.user;
  };

  const register = async (userData) => {
    const data = await api.register(userData);
    setUser(data.user);
    setToken(data.token);
    localStorage.setItem('rentora_user', JSON.stringify(data.user));
    localStorage.setItem('rentora_token', data.token);
    return data.user;
  };

  const logout = () => {
    setUser(null);
    setToken(null);
    localStorage.removeItem('rentora_user');
    localStorage.removeItem('rentora_token');
  };

  // Quick helper to effortlessly switch between Customer, Vendor, and Admin roles
  const switchDemoRole = (role) => {
    const users = storageService.getUsers();
    let target = users.find((u) => u.role === role);
    if (!target) {
      if (role === 'ROLE_VENDOR') {
        target = {
          id: 2,
          name: 'Vikram Verma',
          email: 'vendor@rentora.in',
          role: 'ROLE_VENDOR',
          phone: '+91 98201 44521',
          status: 'ACTIVE',
          businessName: 'Apex Cine Rentals',
          city: 'Bengaluru',
        };
      } else if (role === 'ROLE_ADMIN') {
        target = {
          id: 3,
          name: 'Platform Administrator',
          email: 'admin@rentora.in',
          role: 'ROLE_ADMIN',
          phone: '+91 98111 00000',
          status: 'ACTIVE',
          city: 'Bengaluru',
        };
      } else {
        target = {
          id: 1,
          name: 'Rahul Sharma',
          email: 'customer@rentora.in',
          role: 'ROLE_CUSTOMER',
          phone: '+91 98450 11223',
          status: 'ACTIVE',
          city: 'Bengaluru',
        };
      }
    }
    const mockToken = `mock-jwt-token-${target.role.toLowerCase()}-${Date.now()}`;
    setUser(target);
    setToken(mockToken);
    localStorage.setItem('rentora_user', JSON.stringify(target));
    localStorage.setItem('rentora_token', mockToken);
  };

  return (
    <AuthContext.Provider
      value={{
        user,
        token,
        loading,
        login,
        register,
        logout,
        switchDemoRole,
        isAuthenticated: !!user,
        isCustomer: user?.role === 'ROLE_CUSTOMER',
        isVendor: user?.role === 'ROLE_VENDOR',
        isAdmin: user?.role === 'ROLE_ADMIN',
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
