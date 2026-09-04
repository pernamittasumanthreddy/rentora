import React from 'react';
import { Navigate, Outlet } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';

export default function ProtectedRoute({ allowedRoles }) {
  const { user, loading } = useAuth();

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-sand-100">
        <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-forest-900"></div>
      </div>
    );
  }

  if (!user) {
    return <Navigate to="/login" replace />;
  }

  // Admin has universal portal viewing privileges for testing
  if (allowedRoles && !allowedRoles.includes(user.role) && user.role !== 'ROLE_ADMIN') {
    return <Navigate to="/" replace />;
  }

  return <Outlet />;
}
