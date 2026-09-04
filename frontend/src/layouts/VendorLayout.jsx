import React from 'react';
import { Outlet, NavLink, Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';
import {
  LayoutDashboard,
  Layers,
  PlusCircle,
  Clock,
  RotateCcw,
  IndianRupee,
  Star,
  CheckCircle2,
  Boxes,
  LogOut,
  ArrowLeft,
  Sparkles,
} from 'lucide-react';

export default function VendorLayout() {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  const navItems = [
    { label: 'Overview', to: '/vendor/dashboard', icon: LayoutDashboard, end: true },
    { label: 'Listed Products', to: '/vendor/products', icon: Layers, end: true },
    { label: 'Add New Product', to: '/vendor/products/new', icon: PlusCircle },
    { label: 'Fleet Inventory', to: '/vendor/inventory', icon: Boxes },
    { label: 'Rental Requests', to: '/vendor/requests', icon: Clock },
    { label: 'Returns & Inspection', to: '/vendor/returns', icon: RotateCcw },
    { label: 'Earnings & Payouts', to: '/vendor/earnings', icon: IndianRupee },
    { label: 'Customer Reviews', to: '/vendor/reviews', icon: Star },
  ];

  return (
    <div className="min-h-screen flex flex-col bg-sand-100">
      <div className="flex flex-1">
        {/* Vendor Sidebar */}
        <aside className="w-64 bg-forest-950 text-sand-100 border-r border-forest-900 hidden md:flex flex-col justify-between p-4">
          <div>
            {/* Brand */}
            <div className="px-2 pb-6 border-b border-forest-900 mb-6">
              <Link to="/" className="flex items-center space-x-2.5">
                <div className="w-9 h-9 rounded-xl bg-forest-900 flex items-center justify-center text-white border border-emerald-600/40">
                  <Sparkles className="w-5 h-5 text-gold-400" />
                </div>
                <div>
                  <span className="text-lg font-bold font-display text-white leading-tight">
                    RENTORA
                  </span>
                  <span className="block text-[9px] uppercase font-bold tracking-wider text-gold-400">
                    Vendor Partner Hub
                  </span>
                </div>
              </Link>
            </div>

            {/* Vendor Business Strip */}
            <div className="bg-forest-900/80 rounded-xl p-3 mb-6 border border-emerald-800/50">
              <div className="flex items-center justify-between mb-1">
                <span className="text-[10px] uppercase font-bold text-gray-300">Hub Account</span>
                <span className="inline-flex items-center text-[10px] font-semibold text-emerald-300 bg-emerald-950/60 px-1.5 py-0.5 rounded border border-emerald-700/60">
                  <CheckCircle2 className="w-2.5 h-2.5 mr-1" />
                  Verified
                </span>
              </div>
              <p className="text-xs font-bold text-white truncate">
                {user?.businessName || 'Apex Cine Rentals'}
              </p>
              <div className="flex items-center justify-between text-[11px] text-gray-300 mt-2 pt-2 border-t border-forest-800">
                <span>Trust Score</span>
                <strong className="text-gold-400">98 / 100</strong>
              </div>
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
                        ? 'bg-emerald-600 text-white font-semibold shadow-sm'
                        : 'text-sand-300 hover:text-white hover:bg-forest-900'
                    }`
                  }
                >
                  <item.icon className="w-4 h-4" />
                  <span>{item.label}</span>
                </NavLink>
              ))}
            </nav>
          </div>

          {/* User profile & Logout */}
          <div className="pt-4 border-t border-forest-900">
            <button
              onClick={() => {
                logout();
                navigate('/');
              }}
              className="w-full flex items-center justify-center space-x-2 px-3 py-2 rounded-xl text-xs font-medium text-rose-400 hover:bg-forest-900 transition-colors"
            >
              <LogOut className="w-3.5 h-3.5" />
              <span>Sign Out</span>
            </button>
          </div>
        </aside>

        {/* Content Area */}
        <div className="flex-1 flex flex-col min-w-0">
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
                Vendor Operations Console
              </h2>
            </div>

            <div className="flex items-center space-x-3">
              <Link to="/vendor/products/new" className="btn-accent text-xs py-2 px-4">
                + Add Product
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
