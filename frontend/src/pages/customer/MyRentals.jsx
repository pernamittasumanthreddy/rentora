import React, { useState } from 'react';
import { useAuth } from '../../contexts/AuthContext';
import { storageService } from '../../services/mockStorage';
import { useNotification } from '../../contexts/NotificationContext';
import { formatCurrency, formatDate } from '../../utils/formatters';
import {
  ShoppingBag,
  RotateCcw,
  CheckCircle2,
  Clock,
  Truck,
  ShieldCheck,
  AlertCircle,
  FileText,
} from 'lucide-react';

export default function MyRentals() {
  const { user } = useAuth();
  const { addToast } = useNotification();
  const [activeTab, setActiveTab] = useState('ALL');
  const [rentals, setRentals] = useState(
    storageService.getRentals().filter((r) => r.customerId === user?.id || r.customerId === 1)
  );
  const [returningRental, setReturningRental] = useState(null);
  const [returnNotes, setReturnNotes] = useState('');

  const filteredRentals = rentals.filter((r) => {
    if (activeTab === 'ALL') return true;
    return r.status === activeTab;
  });

  const handleInitiateReturn = (e) => {
    e.preventDefault();
    if (!returningRental) return;

    storageService.createReturn({
      rentalId: returningRental.id,
      productId: returningRental.productId,
      productName: returningRental.productName,
      customerName: returningRental.customerName,
      vendorName: returningRental.vendorName,
      condition: 'PENDING_INSPECTION',
      damageReport: returnNotes || 'Customer declared item returned in good condition.',
      damageFee: 0,
      depositRefunded: 0,
    });

    addToast('Return initiated! Pickup courier has been dispatched.', 'success');
    setReturningRental(null);
    setReturnNotes('');
    setRentals(storageService.getRentals().filter((r) => r.customerId === user?.id || r.customerId === 1));
  };

  const getStatusBadge = (status) => {
    switch (status) {
      case 'ACTIVE':
        return <span className="badge-active">ACTIVE IN USE</span>;
      case 'PENDING':
        return <span className="badge-pending">PENDING DISPATCH</span>;
      case 'RETURNED':
        return <span className="bg-purple-100 text-purple-800 text-xs font-semibold px-2.5 py-0.5 rounded-full">INSPECTION PENDING</span>;
      case 'COMPLETED':
        return <span className="badge-completed">RETURNED &amp; REFUNDED</span>;
      default:
        return <span className="badge-cancelled">{status}</span>;
    }
  };

  return (
    <div className="space-y-6">
      {/* Page Header */}
      <div>
        <h1 className="text-2xl font-bold font-display text-gray-900">
          My Equipment Rentals
        </h1>
        <p className="text-xs text-gray-500 mt-1">
          Track fulfillment status, active shoot windows, and escrow deposit refunds
        </p>
      </div>

      {/* Filter Tabs */}
      <div className="flex space-x-2 border-b border-gray-200 pb-3 overflow-x-auto text-xs font-semibold">
        {['ALL', 'ACTIVE', 'PENDING', 'COMPLETED'].map((tab) => (
          <button
            key={tab}
            onClick={() => setActiveTab(tab)}
            className={`px-4 py-2 rounded-xl transition-all ${
              activeTab === tab
                ? 'bg-forest-900 text-white shadow-sm'
                : 'bg-white text-gray-600 hover:bg-sand-100'
            }`}
          >
            {tab}
          </button>
        ))}
      </div>

      {/* Rentals List */}
      <div className="space-y-4">
        {filteredRentals.length > 0 ? (
          filteredRentals.map((rental) => (
            <div
              key={rental.id}
              className="card p-6 bg-white border border-gray-100 rounded-3xl space-y-4 shadow-sm"
            >
              <div className="flex flex-col sm:flex-row sm:items-center justify-between pb-4 border-b border-gray-100 gap-2">
                <div>
                  <div className="flex items-center space-x-2">
                    <span className="text-xs font-bold text-gray-500">Order #{rental.id}</span>
                    <span>•</span>
                    <span className="text-xs text-gray-400">Placed on {formatDate(rental.createdAt)}</span>
                  </div>
                  <h3 className="text-base font-bold text-gray-900 mt-1">{rental.productName}</h3>
                </div>
                <div>{getStatusBadge(rental.status)}</div>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-4 gap-4 text-xs">
                <div>
                  <span className="text-gray-400 block uppercase font-semibold text-[10px]">
                    Rental Window
                  </span>
                  <p className="font-semibold text-gray-800 mt-0.5">
                    {formatDate(rental.startDate)} – {formatDate(rental.endDate)}
                  </p>
                  <p className="text-gray-500 mt-0.5">{rental.rentalDays} Total Days</p>
                </div>

                <div>
                  <span className="text-gray-400 block uppercase font-semibold text-[10px]">
                    Vendor &amp; City
                  </span>
                  <p className="font-semibold text-gray-800 mt-0.5">{rental.vendorName}</p>
                  <p className="text-gray-500 mt-0.5">Tracking: {rental.trackingNumber}</p>
                </div>

                <div>
                  <span className="text-gray-400 block uppercase font-semibold text-[10px]">
                    Financial Summary
                  </span>
                  <p className="font-semibold text-gray-800 mt-0.5">
                    Total Paid: {formatCurrency(rental.totalAmount)}
                  </p>
                  <p className="text-emerald-700 font-medium mt-0.5">
                    Escrow Deposit: {formatCurrency(rental.deposit)}
                  </p>
                </div>

                <div className="flex items-center justify-start md:justify-end">
                  {rental.status === 'ACTIVE' && (
                    <button
                      onClick={() => setReturningRental(rental)}
                      className="btn-primary text-xs py-2 px-4 flex items-center space-x-1.5"
                    >
                      <RotateCcw className="w-3.5 h-3.5" />
                      <span>Initiate Return</span>
                    </button>
                  )}
                  {rental.status === 'COMPLETED' && (
                    <div className="text-right">
                      <span className="inline-flex items-center text-xs font-semibold text-emerald-800 bg-emerald-50 px-2.5 py-1 rounded-lg">
                        <CheckCircle2 className="w-3.5 h-3.5 mr-1 text-emerald-600" />
                        Deposit 100% Refunded
                      </span>
                    </div>
                  )}
                </div>
              </div>
            </div>
          ))
        ) : (
          <div className="card p-12 text-center bg-white rounded-2xl border border-gray-100">
            <ShoppingBag className="w-10 h-10 text-gray-300 mx-auto mb-3" />
            <p className="text-sm font-semibold text-gray-700">No rentals found in this section</p>
          </div>
        )}
      </div>

      {/* Return Modal */}
      {returningRental && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/50 backdrop-blur-sm">
          <div className="card p-6 max-w-md w-full bg-white rounded-3xl shadow-2xl space-y-4 animate-in fade-in zoom-in-95">
            <h3 className="text-lg font-bold text-gray-900">
              Initiate Equipment Return
            </h3>
            <p className="text-xs text-gray-500">
              You are returning <strong>{returningRental.productName}</strong> to {returningRental.vendorName}.
            </p>

            <form onSubmit={handleInitiateReturn} className="space-y-3">
              <div>
                <label className="text-xs font-semibold text-gray-700 block mb-1">
                  Pickup Delivery Address
                </label>
                <input
                  type="text"
                  readOnly
                  value={returningRental.deliveryAddress}
                  className="input-field bg-sand-100 text-xs text-gray-600"
                />
              </div>

              <div>
                <label className="text-xs font-semibold text-gray-700 block mb-1">
                  Item Condition &amp; Return Notes
                </label>
                <textarea
                  rows="3"
                  placeholder="e.g. Returned with all 3 batteries, charger, and hard case. Clean condition."
                  value={returnNotes}
                  onChange={(e) => setReturnNotes(e.target.value)}
                  className="input-field text-xs resize-none"
                />
              </div>

              <div className="bg-emerald-50 p-3 rounded-xl text-[11px] text-emerald-900">
                Escrow Deposit of <strong>{formatCurrency(returningRental.deposit)}</strong> will be automatically credited to your account upon vendor 5-point inspection.
              </div>

              <div className="flex justify-end space-x-2 pt-2">
                <button
                  type="button"
                  onClick={() => setReturningRental(null)}
                  className="btn-outline text-xs py-2 px-4"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  className="btn-primary text-xs py-2 px-4"
                >
                  Confirm &amp; Schedule Courier
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
}
