import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../../contexts/AuthContext';
import { storageService } from '../../services/mockStorage';
import { formatCurrency, formatDate } from '../../utils/formatters';
import StatCard from '../../components/common/StatCard';
import {
  ShoppingBag,
  Shield,
  CreditCard,
  Heart,
  Truck,
  RotateCcw,
  ArrowRight,
  Sparkles,
} from 'lucide-react';

export default function CustomerDashboard() {
  const { user } = useAuth();
  const rentals = storageService.getRentals().filter((r) => r.customerId === user?.id || r.customerId === 1);
  const activeRentals = rentals.filter((r) => r.status === 'ACTIVE');
  const wishlist = storageService.getWishlist();

  const totalDepositInEscrow = activeRentals.reduce((sum, r) => sum + (r.deposit || 0), 0);
  const totalCompletedRentals = rentals.filter((r) => r.status === 'COMPLETED').length;

  return (
    <div className="space-y-8">
      {/* Welcome Banner */}
      <div className="bg-gradient-to-r from-forest-900 to-forest-800 rounded-3xl p-6 sm:p-8 text-white shadow-card flex flex-col md:flex-row items-center justify-between gap-6">
        <div>
          <div className="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-emerald-950/60 border border-emerald-500/30 text-emerald-300 text-xs font-semibold mb-3">
            <Sparkles className="w-3.5 h-3.5 text-gold-400" />
            <span>Verified Customer Account</span>
          </div>
          <h1 className="text-2xl sm:text-3xl font-extrabold font-display tracking-tight">
            Welcome back, {user?.name || 'Rahul'}!
          </h1>
          <p className="text-xs sm:text-sm text-sand-200 mt-2 max-w-xl leading-relaxed">
            You currently have <strong className="text-emerald-300 font-bold">{activeRentals.length} active rentals</strong> in your possession. Your security deposits are safely protected in Escrow.
          </p>
        </div>

        <Link
          to="/products"
          className="btn-accent py-3 px-6 rounded-xl text-xs font-bold shrink-0 shadow-md flex items-center space-x-2"
        >
          <span>Rent More Equipment</span>
          <ArrowRight className="w-4 h-4" />
        </Link>
      </div>

      {/* KPI Stats */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
        <StatCard
          title="Active Rentals"
          value={activeRentals.length}
          icon={ShoppingBag}
          color="emerald"
        />
        <StatCard
          title="Escrow Deposit Locked"
          value={formatCurrency(totalDepositInEscrow)}
          icon={Shield}
          color="gold"
        />
        <StatCard
          title="Saved in Wishlist"
          value={wishlist.length}
          icon={Heart}
          color="rose"
        />
        <StatCard
          title="Completed Bookings"
          value={totalCompletedRentals}
          icon={CreditCard}
          color="forest"
        />
      </div>

      {/* Active Rental Equipment Strip */}
      <div className="space-y-4">
        <div className="flex items-center justify-between">
          <h2 className="text-lg font-bold font-display text-gray-900 flex items-center space-x-2">
            <span>Currently Active Gear</span>
            <span className="text-xs font-semibold bg-emerald-100 text-emerald-800 px-2 py-0.5 rounded-full">
              {activeRentals.length}
            </span>
          </h2>
          <Link
            to="/customer/rentals"
            className="text-xs font-semibold text-forest-900 hover:text-emerald-700 flex items-center space-x-1"
          >
            <span>View All Rentals</span>
            <ArrowRight className="w-3.5 h-3.5" />
          </Link>
        </div>

        {activeRentals.length > 0 ? (
          <div className="grid grid-cols-1 gap-4">
            {activeRentals.map((rental) => (
              <div
                key={rental.id}
                className="card p-5 bg-white border border-gray-100 rounded-2xl flex flex-col md:flex-row items-center justify-between gap-4 shadow-sm"
              >
                <div className="flex items-center space-x-4 w-full md:w-auto">
                  <img
                    src={rental.productImage}
                    alt={rental.productName}
                    className="w-16 h-16 rounded-xl object-cover border border-gray-100 shrink-0"
                  />
                  <div>
                    <span className="badge-active text-[10px] mb-1">
                      ACTIVE RENTAL
                    </span>
                    <h3 className="font-bold text-gray-900 text-sm">{rental.productName}</h3>
                    <p className="text-xs text-gray-500 mt-0.5">
                      Vendor: <strong>{rental.vendorName}</strong> • {rental.rentalDays} Days Duration
                    </p>
                  </div>
                </div>

                <div className="flex items-center justify-between w-full md:w-auto gap-8 text-xs border-t md:border-t-0 pt-3 md:pt-0">
                  <div>
                    <span className="text-gray-400 block text-[10px] uppercase font-semibold">
                      Return Date
                    </span>
                    <span className="font-bold text-gray-900">{formatDate(rental.endDate)}</span>
                  </div>

                  <div>
                    <span className="text-gray-400 block text-[10px] uppercase font-semibold">
                      Held Deposit
                    </span>
                    <span className="font-bold text-emerald-700">{formatCurrency(rental.deposit)}</span>
                  </div>

                  <Link
                    to="/customer/rentals"
                    className="btn-outline text-xs py-2 px-3.5 flex items-center space-x-1.5"
                  >
                    <RotateCcw className="w-3.5 h-3.5 text-forest-900" />
                    <span>Return Info</span>
                  </Link>
                </div>
              </div>
            ))}
          </div>
        ) : (
          <div className="card p-8 text-center bg-white rounded-2xl border border-gray-100">
            <ShoppingBag className="w-10 h-10 text-gray-300 mx-auto mb-3" />
            <p className="text-sm font-semibold text-gray-700">No gear currently rented</p>
            <p className="text-xs text-gray-400 mt-1">Browse our catalog to pick up cinema cameras or gear.</p>
            <Link to="/products" className="btn-primary text-xs py-2 px-4 mt-4 inline-block">
              Browse Catalog
            </Link>
          </div>
        )}
      </div>
    </div>
  );
}
