import React from 'react';
import { Routes, Route, Navigate } from 'react-router-dom';

// Layouts
import PublicLayout from '../layouts/PublicLayout';
import CustomerLayout from '../layouts/CustomerLayout';
import VendorLayout from '../layouts/VendorLayout';
import AdminLayout from '../layouts/AdminLayout';
import ProtectedRoute from './ProtectedRoute';

// Public Pages
import Home from '../pages/public/Home';
import AboutUs from '../pages/public/AboutUs';
import ProductListing from '../pages/public/ProductListing';
import ProductDetails from '../pages/public/ProductDetails';
import Login from '../pages/public/Login';
import Register from '../pages/public/Register';
import ForgotPassword from '../pages/public/ForgotPassword';

// Customer Pages
import CustomerDashboard from '../pages/customer/CustomerDashboard';
import MyRentals from '../pages/customer/MyRentals';
import Wishlist from '../pages/customer/Wishlist';
import PaymentsHistory from '../pages/customer/PaymentsHistory';
import CustomerReviews from '../pages/customer/CustomerReviews';
import CustomerSettings from '../pages/customer/CustomerSettings';
import BookingCheckout from '../pages/customer/BookingCheckout';

// Vendor Pages
import VendorDashboard from '../pages/vendor/VendorDashboard';
import ProductManagement from '../pages/vendor/ProductManagement';
import AddEditProduct from '../pages/vendor/AddEditProduct';
import InventoryManagement from '../pages/vendor/InventoryManagement';
import RentalRequests from '../pages/vendor/RentalRequests';
import VendorReturns from '../pages/vendor/VendorReturns';
import VendorEarnings from '../pages/vendor/VendorEarnings';
import VendorReviews from '../pages/vendor/VendorReviews';

// Admin Pages
import AdminDashboard from '../pages/admin/AdminDashboard';
import UserManagement from '../pages/admin/UserManagement';
import VendorManagement from '../pages/admin/VendorManagement';
import ProductCatalogManagement from '../pages/admin/ProductCatalogManagement';
import CategoryManagement from '../pages/admin/CategoryManagement';
import RentalManagement from '../pages/admin/RentalManagement';
import ReturnManagement from '../pages/admin/ReturnManagement';
import AnalyticsReports from '../pages/admin/AnalyticsReports';
import AdminSettings from '../pages/admin/AdminSettings';

export default function AppRoutes() {
  return (
    <Routes>
      {/* Public Pages */}
      <Route element={<PublicLayout />}>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<AboutUs />} />
        <Route path="/products" element={<ProductListing />} />
        <Route path="/products/:id" element={<ProductDetails />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/forgot-password" element={<ForgotPassword />} />
        <Route path="/checkout" element={<BookingCheckout />} />
      </Route>

      {/* Customer Portal */}
      <Route element={<ProtectedRoute allowedRoles={['ROLE_CUSTOMER', 'ROLE_ADMIN']} />}>
        <Route element={<CustomerLayout />}>
          <Route path="/customer/dashboard" element={<CustomerDashboard />} />
          <Route path="/customer/rentals" element={<MyRentals />} />
          <Route path="/customer/wishlist" element={<Wishlist />} />
          <Route path="/customer/payments" element={<PaymentsHistory />} />
          <Route path="/customer/reviews" element={<CustomerReviews />} />
          <Route path="/customer/settings" element={<CustomerSettings />} />
        </Route>
      </Route>

      {/* Vendor Portal */}
      <Route element={<ProtectedRoute allowedRoles={['ROLE_VENDOR', 'ROLE_ADMIN']} />}>
        <Route element={<VendorLayout />}>
          <Route path="/vendor/dashboard" element={<VendorDashboard />} />
          <Route path="/vendor/products" element={<ProductManagement />} />
          <Route path="/vendor/products/new" element={<AddEditProduct />} />
          <Route path="/vendor/inventory" element={<InventoryManagement />} />
          <Route path="/vendor/requests" element={<RentalRequests />} />
          <Route path="/vendor/returns" element={<VendorReturns />} />
          <Route path="/vendor/earnings" element={<VendorEarnings />} />
          <Route path="/vendor/reviews" element={<VendorReviews />} />
        </Route>
      </Route>

      {/* Admin Portal */}
      <Route element={<ProtectedRoute allowedRoles={['ROLE_ADMIN']} />}>
        <Route element={<AdminLayout />}>
          <Route path="/admin/dashboard" element={<AdminDashboard />} />
          <Route path="/admin/users" element={<UserManagement />} />
          <Route path="/admin/vendors" element={<VendorManagement />} />
          <Route path="/admin/products" element={<ProductCatalogManagement />} />
          <Route path="/admin/categories" element={<CategoryManagement />} />
          <Route path="/admin/rentals" element={<RentalManagement />} />
          <Route path="/admin/returns" element={<ReturnManagement />} />
          <Route path="/admin/reports" element={<AnalyticsReports />} />
          <Route path="/admin/settings" element={<AdminSettings />} />
        </Route>
      </Route>

      {/* Wildcard Fallback */}
      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  );
}
