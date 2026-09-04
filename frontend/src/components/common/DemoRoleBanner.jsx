import React from 'react';
import { useAuth } from '../../contexts/AuthContext';
import { Shield, Store, User, ArrowRight } from 'lucide-react';
import { Link } from 'react-router-dom';

export default function DemoRoleBanner() {
  const { user, switchDemoRole, isCustomer, isVendor, isAdmin } = useAuth();

  return (
    <div className="bg-forest-950 text-emerald-100 text-xs py-1.5 px-4 border-b border-emerald-900/50 flex flex-wrap items-center justify-between gap-2 z-40">
      <div className="flex items-center space-x-2">
        <span className="font-semibold text-gold-400 tracking-wide uppercase text-[10px] bg-gold-950/80 px-2 py-0.5 rounded border border-gold-800/60">
          Demo Mode
        </span>
        <span className="text-gray-300">
          Active Role: <strong className="text-white">{user ? user.role.replace('ROLE_', '') : 'GUEST'}</strong> ({user?.name || 'Visitor'})
        </span>
      </div>

      <div className="flex items-center space-x-3">
        <span className="text-gray-400 hidden sm:inline">Switch Role:</span>
        <button
          onClick={() => switchDemoRole('ROLE_CUSTOMER')}
          className={`flex items-center space-x-1 px-2 py-1 rounded transition-colors ${
            isCustomer ? 'bg-emerald-600 text-white font-medium' : 'hover:bg-forest-900 text-emerald-200'
          }`}
        >
          <User className="w-3 h-3" />
          <span>Customer</span>
        </button>

        <button
          onClick={() => switchDemoRole('ROLE_VENDOR')}
          className={`flex items-center space-x-1 px-2 py-1 rounded transition-colors ${
            isVendor ? 'bg-emerald-600 text-white font-medium' : 'hover:bg-forest-900 text-emerald-200'
          }`}
        >
          <Store className="w-3 h-3" />
          <span>Vendor</span>
        </button>

        <button
          onClick={() => switchDemoRole('ROLE_ADMIN')}
          className={`flex items-center space-x-1 px-2 py-1 rounded transition-colors ${
            isAdmin ? 'bg-emerald-600 text-white font-medium' : 'hover:bg-forest-900 text-emerald-200'
          }`}
        >
          <Shield className="w-3 h-3" />
          <span>Admin</span>
        </button>

        {user && (
          <Link
            to={
              isAdmin
                ? '/admin/dashboard'
                : isVendor
                ? '/vendor/dashboard'
                : '/customer/dashboard'
            }
            className="flex items-center space-x-1 ml-2 text-gold-400 hover:text-gold-300 font-medium underline underline-offset-2"
          >
            <span>Go to Portal</span>
            <ArrowRight className="w-3 h-3" />
          </Link>
        )}
      </div>
    </div>
  );
}
