import React from 'react';
import { Link } from 'react-router-dom';
import { storageService } from '../../services/mockStorage';
import { formatCurrency } from '../../utils/formatters';
import StatCard from '../../components/common/StatCard';
import {
  Users,
  Building2,
  PackageCheck,
  IndianRupee,
  ShieldCheck,
  TrendingUp,
  ArrowRight,
  Sparkles,
} from 'lucide-react';

export default function AdminDashboard() {
  const users = storageService.getUsers();
  const vendors = storageService.getVendors();
  const products = storageService.getProducts();
  const rentals = storageService.getRentals();

  const totalGMV = rentals.reduce((sum, r) => sum + (r.totalAmount || 0), 0);
  const activeRentals = rentals.filter((r) => r.status === 'ACTIVE');

  return (
    <div className="space-y-8">
      {/* Header Banner */}
      <div className="bg-gradient-to-r from-forest-950 via-forest-900 to-forest-950 rounded-3xl p-6 sm:p-8 text-white shadow-card flex flex-col md:flex-row items-center justify-between gap-6 border border-gold-600/30">
        <div>
          <div className="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-gold-950/80 border border-gold-500/40 text-gold-300 text-xs font-semibold mb-3">
            <Sparkles className="w-3.5 h-3.5" />
            <span>Platform Operations Console</span>
          </div>
          <h1 className="text-2xl sm:text-3xl font-extrabold font-display tracking-tight">
            Rentora Central Governance
          </h1>
          <p className="text-xs sm:text-sm text-sand-200 mt-2 max-w-xl leading-relaxed">
            Monitor nationwide rental volume, manage verified commercial vendors, mediate returns, and oversee regulatory compliance.
          </p>
        </div>

        <Link
          to="/admin/reports"
          className="btn-accent py-3 px-6 rounded-xl text-xs font-bold shrink-0 shadow-md flex items-center space-x-2"
        >
          <TrendingUp className="w-4 h-4" />
          <span>Financial Reports &amp; KPIs</span>
        </Link>
      </div>

      {/* KPI Stats */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
        <StatCard
          title="Total Platform GMV"
          value={formatCurrency(totalGMV)}
          change="24%"
          isPositive={true}
          icon={IndianRupee}
          color="emerald"
        />
        <StatCard
          title="Active Live Rentals"
          value={activeRentals.length}
          icon={PackageCheck}
          color="forest"
        />
        <StatCard
          title="Registered Users"
          value={users.length}
          icon={Users}
          color="gold"
        />
        <StatCard
          title="Verified Vendors"
          value={vendors.length}
          icon={Building2}
          color="rose"
        />
      </div>

      {/* Operations Quick Grid */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="card p-6 bg-white border border-gray-100 rounded-3xl shadow-sm space-y-3">
          <div className="flex items-center justify-between">
            <h3 className="font-bold text-gray-900 text-sm">User &amp; Vendor Governance</h3>
            <span className="badge-active text-[10px]">{users.length} Active</span>
          </div>
          <p className="text-xs text-gray-500">
            Moderate registered customer accounts, verify business GSTIN, and adjust trust scores.
          </p>
          <Link
            to="/admin/users"
            className="text-xs font-semibold text-forest-900 hover:text-emerald-700 flex items-center space-x-1 pt-2"
          >
            <span>Open User Directory</span>
            <ArrowRight className="w-3.5 h-3.5" />
          </Link>
        </div>

        <div className="card p-6 bg-white border border-gray-100 rounded-3xl shadow-sm space-y-3">
          <div className="flex items-center justify-between">
            <h3 className="font-bold text-gray-900 text-sm">Catalog &amp; Categories</h3>
            <span className="badge-active text-[10px]">{products.length} Units</span>
          </div>
          <p className="text-xs text-gray-500">
            Audit newly listed cinema hardware, drones, and manage department taxonomy.
          </p>
          <Link
            to="/admin/products"
            className="text-xs font-semibold text-forest-900 hover:text-emerald-700 flex items-center space-x-1 pt-2"
          >
            <span>Moderate Products</span>
            <ArrowRight className="w-3.5 h-3.5" />
          </Link>
        </div>

        <div className="card p-6 bg-white border border-gray-100 rounded-3xl shadow-sm space-y-3">
          <div className="flex items-center justify-between">
            <h3 className="font-bold text-gray-900 text-sm">Returns &amp; Escrow Mediation</h3>
            <span className="badge-pending text-[10px]">100% Escrow Intact</span>
          </div>
          <p className="text-xs text-gray-500">
            Arbitrate damage disputes, review 5-point inspection logs, and monitor auto-refunds.
          </p>
          <Link
            to="/admin/returns"
            className="text-xs font-semibold text-forest-900 hover:text-emerald-700 flex items-center space-x-1 pt-2"
          >
            <span>Disputes Console</span>
            <ArrowRight className="w-3.5 h-3.5" />
          </Link>
        </div>
      </div>
    </div>
  );
}
