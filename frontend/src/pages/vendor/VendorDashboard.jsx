import React from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../../contexts/AuthContext';
import { storageService } from '../../services/mockStorage';
import { formatCurrency, formatDate } from '../../utils/formatters';
import StatCard from '../../components/common/StatCard';
import {
  IndianRupee,
  Layers,
  Clock,
  RotateCcw,
  PlusCircle,
  ShieldCheck,
  ArrowRight,
  Sparkles,
} from 'lucide-react';

export default function VendorDashboard() {
  const { user } = useAuth();
  const products = storageService.getProducts().filter((p) => p.vendorId === 101);
  const rentals = storageService.getRentals().filter((r) => r.vendorId === 101);
  const pendingRequests = rentals.filter((r) => r.status === 'PENDING');
  const activeRentals = rentals.filter((r) => r.status === 'ACTIVE');
  const returns = storageService.getReturns().filter((ret) => ret.status === 'PENDING');

  const totalGrossEarnings = rentals
    .filter((r) => r.status === 'COMPLETED' || r.status === 'ACTIVE')
    .reduce((sum, r) => sum + (r.rentalFee || 0), 0);

  return (
    <div className="space-y-8">
      {/* Welcome Banner */}
      <div className="bg-gradient-to-r from-forest-950 via-forest-900 to-forest-950 rounded-3xl p-6 sm:p-8 text-white shadow-card flex flex-col md:flex-row items-center justify-between gap-6 border border-emerald-800/40">
        <div>
          <div className="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-emerald-950/80 border border-emerald-500/40 text-emerald-300 text-xs font-semibold mb-3">
            <Sparkles className="w-3.5 h-3.5 text-gold-400" />
            <span>Verified Commercial Fleet Partner</span>
          </div>
          <h1 className="text-2xl sm:text-3xl font-extrabold font-display tracking-tight">
            {user?.businessName || 'Apex Cine Rentals'}
          </h1>
          <p className="text-xs sm:text-sm text-sand-200 mt-2 max-w-xl leading-relaxed">
            Manage your hardware fleet, dispatch units, inspect returns, and track monthly payouts across your equipment.
          </p>
        </div>

        <Link
          to="/vendor/products/new"
          className="btn-accent py-3 px-6 rounded-xl text-xs font-bold shrink-0 shadow-md flex items-center space-x-2"
        >
          <PlusCircle className="w-4 h-4" />
          <span>Add New Equipment</span>
        </Link>
      </div>

      {/* KPI Stats */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
        <StatCard
          title="Gross Rental Revenue"
          value={formatCurrency(totalGrossEarnings)}
          change="18%"
          isPositive={true}
          icon={IndianRupee}
          color="emerald"
        />
        <StatCard
          title="Active Live Rentals"
          value={activeRentals.length}
          icon={Layers}
          color="forest"
        />
        <StatCard
          title="Pending Requests"
          value={pendingRequests.length}
          icon={Clock}
          color="gold"
        />
        <StatCard
          title="Returns To Inspect"
          value={returns.length}
          icon={RotateCcw}
          color="rose"
        />
      </div>

      {/* Quick Action Tables */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        {/* Pending Requests Queue */}
        <div className="card p-6 bg-white border border-gray-100 rounded-3xl shadow-sm space-y-4">
          <div className="flex items-center justify-between">
            <h2 className="text-base font-bold font-display text-gray-900 flex items-center space-x-2">
              <Clock className="w-4 h-4 text-gold-600" />
              <span>Rental Requests Requiring Action</span>
            </h2>
            <Link to="/vendor/requests" className="text-xs font-semibold text-forest-900 hover:underline">
              View All
            </Link>
          </div>

          {pendingRequests.length > 0 ? (
            <div className="space-y-3">
              {pendingRequests.map((req) => (
                <div
                  key={req.id}
                  className="p-4 rounded-2xl bg-sand-50 border border-gray-100 flex items-center justify-between text-xs"
                >
                  <div>
                    <p className="font-bold text-gray-900">{req.productName}</p>
                    <p className="text-gray-500 mt-0.5">
                      Renter: <strong>{req.customerName}</strong> ({req.rentalDays} Days)
                    </p>
                    <p className="text-emerald-700 font-semibold mt-1">
                      Gross: {formatCurrency(req.totalAmount)}
                    </p>
                  </div>
                  <Link
                    to="/vendor/requests"
                    className="btn-primary text-xs py-1.5 px-3 rounded-lg"
                  >
                    Review
                  </Link>
                </div>
              ))}
            </div>
          ) : (
            <p className="text-xs text-gray-400 py-6 text-center italic">
              No pending rental requests at this time.
            </p>
          )}
        </div>

        {/* Fleet Products Snapshot */}
        <div className="card p-6 bg-white border border-gray-100 rounded-3xl shadow-sm space-y-4">
          <div className="flex items-center justify-between">
            <h2 className="text-base font-bold font-display text-gray-900 flex items-center space-x-2">
              <Layers className="w-4 h-4 text-emerald-600" />
              <span>Your Listed Gear ({products.length})</span>
            </h2>
            <Link to="/vendor/products" className="text-xs font-semibold text-forest-900 hover:underline">
              Manage Catalog
            </Link>
          </div>

          <div className="space-y-3">
            {products.slice(0, 3).map((prod) => (
              <div
                key={prod.id}
                className="p-3 rounded-2xl bg-sand-50 border border-gray-100 flex items-center justify-between text-xs"
              >
                <div className="flex items-center space-x-3">
                  <img
                    src={prod.imageUrl}
                    alt=""
                    className="w-12 h-12 rounded-xl object-cover border border-gray-100"
                  />
                  <div>
                    <p className="font-bold text-gray-900 truncate max-w-[200px]">{prod.name}</p>
                    <p className="text-gray-500">{formatCurrency(prod.pricePerDay)}/day • Stock: {prod.stockCount}</p>
                  </div>
                </div>
                <span className="badge-active text-[10px]">ACTIVE</span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
