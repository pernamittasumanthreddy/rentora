import React from 'react';
import { Outlet, NavLink, Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';
import {
  LayoutDashboard,
  ShoppingBag,
  Heart,
  CreditCard,
  Star,
  Settings,
  Compass,
  LogOut,
  ArrowLeft,
  Sparkles,
} from 'lucide-react';

export default function CustomerLayout() {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  const navItems = [
    { label: 'Overview', to: '/customer/dashboard', icon: LayoutDashboard, end: true },
    { label: 'Explore Gear', to: '/products', icon: Compass },
    { label: 'My Rentals', to: '/customer/rentals', icon: ShoppingBag },
    { label: 'Saved Wishlist', to: '/customer/wishlist', icon: Heart },
    { label: 'Payments & Deposits', to: '/customer/payments', icon: CreditCard },
    { label: 'My Reviews', to: '/customer/reviews', icon: Star },
    { label: 'Account Settings', to: '/customer/settings', icon: Settings },
  ];

  return (
    <div className="min-h-screen flex flex-col bg-sand-100">
      <div className="flex flex-1">
        {/* Sidebar */}
        <aside className="w-64 bg-white border-r border-gray-200 hidden md:flex flex-col justify-between p-4">
          <div>
            {/* Brand */}
            <div className="flex items-center justify-between px-2 pb-6 border-b border-gray-100 mb-6">
              <Link to="/" className="flex items-center space-x-2.5">
                <div className="w-9 h-9 rounded-xl bg-forest-900 flex items-center justify-center text-white">
                  <Sparkles className="w-5 h-5 text-gold-400" />
                </div>
                <div>
                  <span className="text-lg font-bold font-display text-forest-900 leading-tight">
                    RENTORA
                  </span>
                  <span className="block text-[9px] uppercase font-bold tracking-wider text-emerald-700">
                    Customer Portal
                  </span>
                </div>
              </Link>
            </div>

            {/* Navigation links */}
            <nav className="space-y-1">
              {navItems.map((item) => (
                <NavLink
                  key={item.to}
                  to={item.to}
                  end={item.end}
                  className={({ isActive }) =>
                    `flex items-center space-x-3 px-3.5 py-2.5 rounded-xl text-sm font-medium transition-all ${
                      isActive
                        ? 'bg-forest-900 text-white shadow-sm'
                        : 'text-gray-600 hover:text-forest-900 hover:bg-sand-100'
                    }`
                  }
                >
                  <item.icon className="w-4 h-4" />
                  <span>{item.label}</span>
                </NavLink>
              ))}
            </nav>
          </div>

          {/* User profile card & Logout */}
          <div className="pt-4 border-t border-gray-100">
            <div className="flex items-center space-x-3 px-2 py-2 mb-2">
              <img
                src={user?.avatar || 'https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?auto=format&fit=crop&w=100&q=80'}
                alt={user?.name}
                className="w-9 h-9 rounded-full object-cover border border-emerald-600"
              />
              <div className="overflow-hidden">
                <p className="text-sm font-semibold text-gray-800 truncate">{user?.name}</p>
                <p className="text-xs text-gray-400 truncate">{user?.email}</p>
              </div>
            </div>

            <button
              onClick={() => {
                logout();
                navigate('/');
              }}
              className="w-full flex items-center justify-center space-x-2 px-3 py-2 rounded-xl text-xs font-medium text-rose-600 hover:bg-rose-50 transition-colors"
            >
              <LogOut className="w-3.5 h-3.5" />
              <span>Sign Out</span>
            </button>
          </div>
        </aside>

        {/* Content Area */}
        <div className="flex-1 flex flex-col min-w-0">
          {/* Top action strip */}
          <header className="bg-white border-b border-gray-200 px-6 py-4 flex items-center justify-between">
            <div className="flex items-center space-x-4">
              <Link
                to="/"
                className="inline-flex items-center space-x-1.5 text-xs font-medium text-gray-500 hover:text-forest-900 bg-sand-50 hover:bg-sand-100 px-3 py-1.5 rounded-lg transition-colors"
              >
                <ArrowLeft className="w-3.5 h-3.5" />
                <span>Return to Marketplace</span>
              </Link>
              <h2 className="text-lg font-bold text-gray-900">
                Welcome, {user?.name || 'Customer'}
              </h2>
            </div>

            <div className="flex items-center space-x-3">
              <Link to="/products" className="btn-primary text-xs py-2 px-4">
                + Rent New Gear
              </Link>
            </div>
          </header>

          <main className="flex-1 p-6 md:p-8 overflow-y-auto">
            <Outlet />
          </main>
        </div>
      </div>
    </div>
  );
}
