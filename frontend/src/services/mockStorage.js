/**
 * RENTORA - Mock State & Local Storage Bridge
 * Synchronizes local mutations for seamless browser testing with Spring Boot DTO parity.
 */

import {
  INITIAL_CATEGORIES,
  INITIAL_PRODUCTS,
  INITIAL_USERS,
  INITIAL_VENDORS,
  INITIAL_RENTALS,
  INITIAL_RETURNS,
  INITIAL_PAYMENTS,
  INITIAL_REVIEWS,
  INITIAL_NOTIFICATIONS,
} from '../data/mockData';

const STORAGE_KEYS = {
  PRODUCTS: 'rentora_products',
  CATEGORIES: 'rentora_categories',
  USERS: 'rentora_users',
  VENDORS: 'rentora_vendors',
  RENTALS: 'rentora_rentals',
  RETURNS: 'rentora_returns',
  PAYMENTS: 'rentora_payments',
  REVIEWS: 'rentora_reviews',
  NOTIFICATIONS: 'rentora_notifications',
  WISHLIST: 'rentora_wishlist',
};

const getStored = (key, fallback) => {
  try {
    const item = localStorage.getItem(key);
    return item ? JSON.parse(item) : fallback;
  } catch {
    return fallback;
  }
};

const setStored = (key, data) => {
  try {
    localStorage.setItem(key, JSON.stringify(data));
  } catch (err) {
    console.error(`Failed saving ${key} to localStorage:`, err);
  }
};

// Initial sync if empty or missing new items
export const initializeStorage = () => {
  // Sync products
  const storedProducts = getStored(STORAGE_KEYS.PRODUCTS, null);
  if (!storedProducts) {
    setStored(STORAGE_KEYS.PRODUCTS, INITIAL_PRODUCTS);
  } else {
    const existingIds = new Set(storedProducts.map((p) => p.id));
    const missing = INITIAL_PRODUCTS.filter((p) => !existingIds.has(p.id));
    if (missing.length > 0) {
      setStored(STORAGE_KEYS.PRODUCTS, [...storedProducts, ...missing]);
    }
  }

  // Sync categories
  const storedCats = getStored(STORAGE_KEYS.CATEGORIES, null);
  if (!storedCats) {
    setStored(STORAGE_KEYS.CATEGORIES, INITIAL_CATEGORIES);
  } else {
    const existingCatIds = new Set(storedCats.map((c) => c.id));
    const missingCats = INITIAL_CATEGORIES.filter((c) => !existingCatIds.has(c.id));
    if (missingCats.length > 0) {
      setStored(STORAGE_KEYS.CATEGORIES, [...storedCats, ...missingCats]);
    }
  }

  // Sync reviews
  const storedReviews = getStored(STORAGE_KEYS.REVIEWS, null);
  if (!storedReviews) {
    setStored(STORAGE_KEYS.REVIEWS, INITIAL_REVIEWS);
  } else {
    const existingRevIds = new Set(storedReviews.map((r) => r.id));
    const missingRevs = INITIAL_REVIEWS.filter((r) => !existingRevIds.has(r.id));
    if (missingRevs.length > 0) {
      setStored(STORAGE_KEYS.REVIEWS, [...storedReviews, ...missingRevs]);
    }
  }

  // Sync vendors
  const storedVendors = getStored(STORAGE_KEYS.VENDORS, null);
  if (!storedVendors) {
    setStored(STORAGE_KEYS.VENDORS, INITIAL_VENDORS);
  } else {
    const existingVendorIds = new Set(storedVendors.map((v) => v.id));
    const missingVendors = INITIAL_VENDORS.filter((v) => !existingVendorIds.has(v.id));
    if (missingVendors.length > 0) {
      setStored(STORAGE_KEYS.VENDORS, [...storedVendors, ...missingVendors]);
    }
  }

  if (!localStorage.getItem(STORAGE_KEYS.USERS)) {
    setStored(STORAGE_KEYS.USERS, INITIAL_USERS);
  }
  if (!localStorage.getItem(STORAGE_KEYS.RENTALS)) {
    setStored(STORAGE_KEYS.RENTALS, INITIAL_RENTALS);
  }
  if (!localStorage.getItem(STORAGE_KEYS.RETURNS)) {
    setStored(STORAGE_KEYS.RETURNS, INITIAL_RETURNS);
  }
  if (!localStorage.getItem(STORAGE_KEYS.PAYMENTS)) {
    setStored(STORAGE_KEYS.PAYMENTS, INITIAL_PAYMENTS);
  }
  if (!localStorage.getItem(STORAGE_KEYS.NOTIFICATIONS)) {
    setStored(STORAGE_KEYS.NOTIFICATIONS, INITIAL_NOTIFICATIONS);
  }
  if (!localStorage.getItem(STORAGE_KEYS.WISHLIST)) {
    setStored(STORAGE_KEYS.WISHLIST, [1, 2, 9, 11]);
  }
};

// Product Service
export const storageService = {
  // Products
  getProducts: () => getStored(STORAGE_KEYS.PRODUCTS, INITIAL_PRODUCTS),
  getProductById: (id) => {
    const products = getStored(STORAGE_KEYS.PRODUCTS, INITIAL_PRODUCTS);
    return products.find((p) => p.id === Number(id));
  },
  addProduct: (productData) => {
    const products = getStored(STORAGE_KEYS.PRODUCTS, INITIAL_PRODUCTS);
    const newProduct = {
      ...productData,
      id: Date.now(),
      rating: 5.0,
      reviewCount: 0,
      availability: true,
      gallery: productData.imageUrl ? [productData.imageUrl] : [],
    };
    products.unshift(newProduct);
    setStored(STORAGE_KEYS.PRODUCTS, products);
    return newProduct;
  },
  updateProduct: (id, updatedData) => {
    const products = getStored(STORAGE_KEYS.PRODUCTS, INITIAL_PRODUCTS);
    const index = products.findIndex((p) => p.id === Number(id));
    if (index !== -1) {
      products[index] = { ...products[index], ...updatedData };
      setStored(STORAGE_KEYS.PRODUCTS, products);
      return products[index];
    }
    return null;
  },
  deleteProduct: (id) => {
    const products = getStored(STORAGE_KEYS.PRODUCTS, INITIAL_PRODUCTS);
    const filtered = products.filter((p) => p.id !== Number(id));
    setStored(STORAGE_KEYS.PRODUCTS, filtered);
    return true;
  },

  // Categories
  getCategories: () => getStored(STORAGE_KEYS.CATEGORIES, INITIAL_CATEGORIES),
  addCategory: (cat) => {
    const cats = getStored(STORAGE_KEYS.CATEGORIES, INITIAL_CATEGORIES);
    const newCat = { ...cat, id: Date.now(), itemCount: 0, slug: cat.name.toLowerCase().replace(/\s+/g, '-') };
    cats.push(newCat);
    setStored(STORAGE_KEYS.CATEGORIES, cats);
    return newCat;
  },
  deleteCategory: (id) => {
    const cats = getStored(STORAGE_KEYS.CATEGORIES, INITIAL_CATEGORIES);
    const filtered = cats.filter((c) => c.id !== Number(id));
    setStored(STORAGE_KEYS.CATEGORIES, filtered);
    return true;
  },

  // Rentals
  getRentals: () => getStored(STORAGE_KEYS.RENTALS, INITIAL_RENTALS),
  getRentalById: (id) => {
    const rentals = getStored(STORAGE_KEYS.RENTALS, INITIAL_RENTALS);
    return rentals.find((r) => r.id === Number(id));
  },
  createRental: (rentalData) => {
    const rentals = getStored(STORAGE_KEYS.RENTALS, INITIAL_RENTALS);
    const newRental = {
      ...rentalData,
      id: Date.now(),
      status: 'PENDING',
      createdAt: new Date().toISOString().split('T')[0],
      trackingNumber: `TRK-${new Date().getFullYear()}-${Math.floor(100000 + Math.random() * 900000)}`,
    };
    rentals.unshift(newRental);
    setStored(STORAGE_KEYS.RENTALS, rentals);

    // Also create corresponding payment record
    const payments = getStored(STORAGE_KEYS.PAYMENTS, INITIAL_PAYMENTS);
    payments.unshift({
      id: `TXN-${Math.floor(1000 + Math.random() * 9000)}`,
      rentalId: newRental.id,
      amount: newRental.totalAmount,
      depositAmount: newRental.deposit,
      paymentStatus: 'PAID',
      paymentMethod: rentalData.paymentMethod || 'UPI / NetBanking',
      transactionRef: `UPI-RENT-${Math.floor(100000 + Math.random() * 900000)}`,
      paymentDate: new Date().toLocaleString(),
    });
    setStored(STORAGE_KEYS.PAYMENTS, payments);

    return newRental;
  },
  updateRentalStatus: (id, status) => {
    const rentals = getStored(STORAGE_KEYS.RENTALS, INITIAL_RENTALS);
    const index = rentals.findIndex((r) => r.id === Number(id));
    if (index !== -1) {
      rentals[index].status = status;
      setStored(STORAGE_KEYS.RENTALS, rentals);
      return rentals[index];
    }
    return null;
  },

  // Returns
  getReturns: () => getStored(STORAGE_KEYS.RETURNS, INITIAL_RETURNS),
  createReturn: (returnData) => {
    const returns = getStored(STORAGE_KEYS.RETURNS, INITIAL_RETURNS);
    const newReturn = {
      ...returnData,
      id: Date.now(),
      status: 'PENDING',
      returnDate: new Date().toISOString().split('T')[0],
    };
    returns.unshift(newReturn);
    setStored(STORAGE_KEYS.RETURNS, returns);

    // Update rental status
    storageService.updateRentalStatus(returnData.rentalId, 'RETURNED');
    return newReturn;
  },
  settleReturn: (returnId, damageFee, condition, damageReport) => {
    const returns = getStored(STORAGE_KEYS.RETURNS, INITIAL_RETURNS);
    const index = returns.findIndex((r) => r.id === Number(returnId));
    if (index !== -1) {
      const ret = returns[index];
      const rental = storageService.getRentalById(ret.rentalId);
      const refundAmount = Math.max(0, (rental ? rental.deposit : 0) - damageFee);

      returns[index] = {
        ...ret,
        status: 'SETTLED',
        damageFee,
        condition,
        damageReport,
        depositRefunded: refundAmount,
      };
      setStored(STORAGE_KEYS.RETURNS, returns);
      if (rental) {
        storageService.updateRentalStatus(rental.id, 'COMPLETED');
      }
      return returns[index];
    }
    return null;
  },

  // Users
  getUsers: () => getStored(STORAGE_KEYS.USERS, INITIAL_USERS),
  updateUserStatus: (id, status) => {
    const users = getStored(STORAGE_KEYS.USERS, INITIAL_USERS);
    const idx = users.findIndex((u) => u.id === Number(id));
    if (idx !== -1) {
      users[idx].status = status;
      setStored(STORAGE_KEYS.USERS, users);
      return users[idx];
    }
    return null;
  },

  // Vendors
  getVendors: () => getStored(STORAGE_KEYS.VENDORS, INITIAL_VENDORS),
  updateVendorTrustScore: (id, score) => {
    const vendors = getStored(STORAGE_KEYS.VENDORS, INITIAL_VENDORS);
    const idx = vendors.findIndex((v) => v.id === Number(id));
    if (idx !== -1) {
      vendors[idx].trustScore = score;
      setStored(STORAGE_KEYS.VENDORS, vendors);
      return vendors[idx];
    }
    return null;
  },

  // Payments
  getPayments: () => getStored(STORAGE_KEYS.PAYMENTS, INITIAL_PAYMENTS),

  // Reviews
  getReviews: () => getStored(STORAGE_KEYS.REVIEWS, INITIAL_REVIEWS),
  addReview: (reviewData) => {
    const reviews = getStored(STORAGE_KEYS.REVIEWS, INITIAL_REVIEWS);
    const newRev = {
      ...reviewData,
      id: Date.now(),
      date: new Date().toISOString().split('T')[0],
    };
    reviews.unshift(newRev);
    setStored(STORAGE_KEYS.REVIEWS, reviews);
    return newRev;
  },

  // Wishlist
  getWishlist: () => getStored(STORAGE_KEYS.WISHLIST, [1, 2]),
  toggleWishlist: (productId) => {
    const list = getStored(STORAGE_KEYS.WISHLIST, [1, 2]);
    const id = Number(productId);
    const exists = list.includes(id);
    const updated = exists ? list.filter((i) => i !== id) : [...list, id];
    setStored(STORAGE_KEYS.WISHLIST, updated);
    return updated;
  },
};
