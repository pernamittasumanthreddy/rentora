import React, { useState } from 'react';
import { Link, useNavigate, useLocation } from 'react-router-dom';
import { useAuth } from '../../contexts/AuthContext';
import { useCart } from '../../contexts/CartContext';
import {
  Search,
  ShoppingBag,
  Heart,
  User,
  LogOut,
  LayoutDashboard,
  Menu,
  X,
  ChevronDown,
  Sparkles,
} from 'lucide-react';

export default function Navbar() {
  const { user, logout, isCustomer, isVendor, isAdmin } = useAuth();
  const { cartItem } = useCart();
  const navigate = useNavigate();
  const location = useLocation();
  const [searchTerm, setSearchTerm] = useState('');
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [userDropdownOpen, setUserDropdownOpen] = useState(false);

  const handleSearch = (e) => {
    e.preventDefault();
    if (searchTerm.trim()) {
      navigate(`/products?search=${encodeURIComponent(searchTerm.trim())}`);
    }
  };

  const dashboardUrl = isAdmin
    ? '/admin/dashboard'
    : isVendor
    ? '/vendor/dashboard'
    : '/customer/dashboard';

  return (
    <header className="sticky top-0 z-30 bg-white/95 backdrop-blur-md border-b border-gray-100 shadow-sm transition-all">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-20">
          {/* Brand Logo */}
          <Link to="/" className="flex items-center space-x-3 group">
            <div className="w-11 h-11 rounded-xl bg-gradient-to-br from-forest-900 to-forest-800 flex items-center justify-center text-white shadow-md shadow-forest-900/10 group-hover:scale-105 transition-transform duration-200">
              <Sparkles className="w-6 h-6 text-gold-400" />
            </div>
            <div>
              <span className="text-2xl font-bold font-display tracking-tight text-forest-900 flex items-center">
                RENTORA
                <span className="w-2 h-2 rounded-full bg-emerald-500 ml-1"></span>
              </span>
              <span className="block text-[10px] uppercase font-semibold tracking-wider text-gray-500 -mt-1">
                Rent • Share • Save
              </span>
            </div>
          </Link>

          {/* Search Bar - Desktop */}
          <form
            onSubmit={handleSearch}
            className="hidden md:flex flex-1 max-w-md mx-8 relative"
          >
            <div className="relative w-full">
              <input
                type="text"
                placeholder="Search cinema cameras, drones, tools, consoles..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                className="w-full pl-11 pr-4 py-2.5 rounded-full bg-sand-100 border border-gray-200 text-sm focus:outline-none focus:ring-2 focus:ring-emerald-500/20 focus:border-emerald-600 transition-all placeholder:text-gray-400"
              />
              <Search className="w-4 h-4 text-gray-400 absolute left-4 top-3.5" />
            </div>
          </form>

          {/* Nav Links - Desktop */}
          <nav className="hidden lg:flex items-center space-x-7 text-sm font-medium text-gray-600">
            <Link
              to="/products"
              className={`hover:text-forest-900 transition-colors ${
                location.pathname === '/products' ? 'text-forest-900 font-semibold' : ''
              }`}
            >
              Explore Catalog
            </Link>
            <Link
              to="/about"
              className={`hover:text-forest-900 transition-colors ${
                location.pathname === '/about' ? 'text-forest-900 font-semibold' : ''
              }`}
            >
              About Platform
            </Link>
            <Link
              to="/products?category=cameras-gear"
              className="hover:text-forest-900 transition-colors"
            >
              Cinema Gear
            </Link>
          </nav>

          {/* Right Action Icons */}
          <div className="flex items-center space-x-3">
            {/* Wishlist Link (Customer) */}
            <Link
              to="/customer/wishlist"
              className="p-2.5 text-gray-500 hover:text-forest-900 hover:bg-sand-100 rounded-full transition-colors relative"
              title="Saved Wishlist"
            >
              <Heart className="w-5 h-5" />
              <span className="absolute top-1 right-1 w-2 h-2 bg-gold-500 rounded-full"></span>
            </Link>

            {/* Cart / Active Booking */}
            <Link
              to={cartItem ? '/checkout' : '/products'}
              className="p-2.5 text-gray-500 hover:text-forest-900 hover:bg-sand-100 rounded-full transition-colors relative"
              title="Current Booking"
            >
              <ShoppingBag className="w-5 h-5" />
              {cartItem && (
                <span className="absolute top-1.5 right-1.5 w-2 h-2 bg-emerald-500 rounded-full ring-2 ring-white animate-pulse"></span>
              )}
            </Link>

            {/* User Account / Dropdown */}
            {user ? (
              <div className="relative">
                <button
                  onClick={() => setUserDropdownOpen(!userDropdownOpen)}
                  className="flex items-center space-x-2 pl-2 pr-3 py-1.5 rounded-full border border-gray-200 hover:border-gray-300 hover:bg-sand-50 transition-all"
                >
                  <img
                    src={user.avatar || 'https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?auto=format&fit=crop&w=100&q=80'}
                    alt={user.name}
                    className="w-7 h-7 rounded-full object-cover border border-emerald-600"
                  />
                  <span className="text-xs font-semibold text-gray-800 max-w-[100px] truncate hidden sm:inline">
                    {user.name}
                  </span>
                  <ChevronDown className="w-3.5 h-3.5 text-gray-400" />
                </button>

                {userDropdownOpen && (
                  <div
                    className="absolute right-0 mt-2 w-56 bg-white rounded-2xl shadow-xl border border-gray-100 py-2 z-50 animate-in fade-in zoom-in-95 duration-100"
                    onMouseLeave={() => setUserDropdownOpen(false)}
                  >
                    <div className="px-4 py-2 border-b border-gray-100">
                      <p className="text-xs text-gray-400">Signed in as</p>
                      <p className="text-sm font-semibold text-gray-800 truncate">{user.email}</p>
                      <span className="inline-block mt-1 px-2 py-0.5 rounded-md text-[10px] font-bold bg-emerald-50 text-emerald-800 uppercase tracking-wide">
                        {user.role.replace('ROLE_', '')}
                      </span>
                    </div>

                    <Link
                      to={dashboardUrl}
                      onClick={() => setUserDropdownOpen(false)}
                      className="flex items-center space-x-2 px-4 py-2.5 text-sm text-gray-700 hover:bg-sand-50 hover:text-forest-900 transition-colors"
                    >
                      <LayoutDashboard className="w-4 h-4 text-emerald-600" />
                      <span>Control Dashboard</span>
                    </Link>

                    {isCustomer && (
                      <Link
                        to="/customer/rentals"
                        onClick={() => setUserDropdownOpen(false)}
                        className="flex items-center space-x-2 px-4 py-2.5 text-sm text-gray-700 hover:bg-sand-50 hover:text-forest-900 transition-colors"
                      >
                        <ShoppingBag className="w-4 h-4 text-gray-400" />
                        <span>My Rentals</span>
                      </Link>
                    )}

                    <button
                      onClick={() => {
                        setUserDropdownOpen(false);
                        logout();
                      }}
                      className="w-full flex items-center space-x-2 px-4 py-2.5 text-sm text-rose-600 hover:bg-rose-50 transition-colors text-left"
                    >
                      <LogOut className="w-4 h-4" />
                      <span>Sign Out</span>
                    </button>
                  </div>
                )}
              </div>
            ) : (
              <div className="flex items-center space-x-2">
                <Link
                  to="/login"
                  className="px-4 py-2 text-sm font-medium text-forest-900 hover:text-emerald-700 transition-colors"
                >
                  Sign In
                </Link>
                <Link
                  to="/register"
                  className="btn-primary text-xs py-2 px-4"
                >
                  Get Started
                </Link>
              </div>
            )}

            {/* Mobile menu toggle button */}
            <button
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              className="lg:hidden p-2 text-gray-500 hover:text-gray-900 rounded-lg"
            >
              {mobileMenuOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
            </button>
          </div>
        </div>
      </div>

      {/* Mobile Drawer */}
      {mobileMenuOpen && (
        <div className="lg:hidden border-t border-gray-100 bg-white px-4 pt-3 pb-6 space-y-3">
          <form onSubmit={handleSearch} className="relative mb-4">
            <input
              type="text"
              placeholder="Search cameras, tools, consoles..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="w-full pl-10 pr-4 py-2 rounded-xl bg-sand-100 border border-gray-200 text-sm"
            />
            <Search className="w-4 h-4 text-gray-400 absolute left-3 top-3" />
          </form>

          <Link
            to="/products"
            onClick={() => setMobileMenuOpen(false)}
            className="block px-3 py-2 rounded-lg text-sm font-medium text-gray-700 hover:bg-sand-100"
          >
            Explore Catalog
          </Link>
          <Link
            to="/about"
            onClick={() => setMobileMenuOpen(false)}
            className="block px-3 py-2 rounded-lg text-sm font-medium text-gray-700 hover:bg-sand-100"
          >
            About Us
          </Link>
          <Link
            to={dashboardUrl}
            onClick={() => setMobileMenuOpen(false)}
            className="block px-3 py-2 rounded-lg text-sm font-medium text-emerald-800 bg-emerald-50"
          >
            Go to {user ? user.role.replace('ROLE_', '') : 'Portal'} Dashboard
          </Link>
        </div>
      )}
    </header>
  );
}
