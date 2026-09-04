import React from 'react';
import { Outlet, NavLink, Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';
import {
  ShieldAlert,
  Users,
  Building2,
  PackageCheck,
  FolderTree,
  FileSpreadsheet,
  Scale,
  BarChart3,
  Sliders,
  LogOut,
  ArrowLeft,
  Sparkles,
} from 'lucide-react';

export default function AdminLayout() {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  const navItems = [
    { label: 'Overview', to: '/admin/dashboard', icon: ShieldAlert, end: true },
    { label: 'User Directory', to: '/admin/users', icon: Users },
    { label: 'Vendor Governance', to: '/admin/vendors', icon: Building2 },
    { label: 'Product Moderation', to: '/admin/products', icon: PackageCheck },
    { label: 'Category Hierarchy', to: '/admin/categories', icon: FolderTree },
    { label: 'Rental Orders Audit', to: '/admin/rentals', icon: FileSpreadsheet },
    { label: 'Disputes & Returns', to: '/admin/returns', icon: Scale },
    { label: 'Reports & Analytics', to: '/admin/reports', icon: BarChart3 },
    { label: 'Platform Settings', to: '/admin/settings', icon: Sliders },
  ];

  return (
    <div className="min-h-screen flex flex-col bg-sand-100">
      <div className="flex flex-1">
        {/* Admin Sidebar */}
        <aside className="w-64 bg-forest-950 text-sand-100 border-r border-forest-900 hidden md:flex flex-col justify-between p-4">
          <div>
            <div className="px-2 pb-6 border-b border-forest-900 mb-6">
              <Link to="/" className="flex items-center space-x-2.5">
                <div className="w-9 h-9 rounded-xl bg-forest-900 flex items-center justify-center text-white border border-gold-500/40">
                  <Sparkles className="w-5 h-5 text-gold-400" />
                </div>
                <div>
                  <span className="text-lg font-bold font-display text-white leading-tight">
                    RENTORA
                  </span>
                  <span className="block text-[9px] uppercase font-bold tracking-wider text-rose-400">
                    Admin Command
                  </span>
                </div>
              </Link>
            </div>

            <nav className="space-y-1">
              {navItems.map((item) => (
                <NavLink
                  key={item.to}
                  to={item.to}
                  end={item.end}
                  className={({ isActive }) =>
                    `flex items-center space-x-3 px-3.5 py-2.5 rounded-xl text-sm font-medium transition-all ${
                      isActive
                        ? 'bg-gold-600 text-white font-semibold shadow-sm'
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
                Operations Command Center
              </h2>
            </div>

            <div className="flex items-center space-x-2">
              <span className="inline-flex items-center px-2.5 py-1 rounded-full text-xs font-semibold bg-emerald-100 text-emerald-800">
                ● Live System Healthy
              </span>
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
