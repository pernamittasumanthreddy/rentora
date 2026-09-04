import React, { useState } from 'react';
import { storageService } from '../../services/mockStorage';
import { useNotification } from '../../contexts/NotificationContext';
import { formatCurrency, formatDate } from '../../utils/formatters';
import { Clock, Check, X, ShieldCheck, MapPin } from 'lucide-react';

export default function RentalRequests() {
  const { addToast } = useNotification();
  const [rentals, setRentals] = useState(
    storageService.getRentals().filter((r) => r.vendorId === 101)
  );

  const handleApprove = (id) => {
    storageService.updateRentalStatus(id, 'ACTIVE');
    setRentals(storageService.getRentals().filter((r) => r.vendorId === 101));
    addToast('Rental request approved and dispatched for fulfillment!', 'success');
  };

  const handleReject = (id) => {
    storageService.updateRentalStatus(id, 'CANCELLED');
    setRentals(storageService.getRentals().filter((r) => r.vendorId === 101));
    addToast('Rental request declined and customer notified.', 'warning');
  };

  const pendingRequests = rentals.filter((r) => r.status === 'PENDING');
  const otherRentals = rentals.filter((r) => r.status !== 'PENDING');

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold font-display text-gray-900">
          Rental Requests &amp; Approvals
        </h1>
        <p className="text-xs text-gray-500 mt-1">
          Review client identities, rental durations, and approve dispatch schedules
        </p>
      </div>

      {/* Pending Queue */}
      <div className="space-y-4">
        <h2 className="text-sm font-bold text-gray-900 uppercase tracking-wider text-gold-700 flex items-center space-x-2">
          <Clock className="w-4 h-4" />
          <span>Pending Approvals ({pendingRequests.length})</span>
        </h2>

        {pendingRequests.length > 0 ? (
          pendingRequests.map((req) => (
            <div
              key={req.id}
              className="card p-6 bg-white border border-gray-100 rounded-3xl space-y-4 shadow-sm"
            >
              <div className="flex flex-col sm:flex-row sm:items-center justify-between pb-4 border-b border-gray-100 gap-2">
                <div>
                  <span className="text-[10px] font-bold text-gray-400">Order #{req.id}</span>
                  <h3 className="text-base font-bold text-gray-900">{req.productName}</h3>
                </div>
                <span className="badge-pending text-xs">PENDING APPROVAL</span>
              </div>

              <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 text-xs">
                <div>
                  <span className="text-gray-400 block uppercase font-semibold text-[10px]">
                    Client / Renter
                  </span>
                  <p className="font-bold text-gray-800 mt-0.5">{req.customerName}</p>
                  <p className="text-gray-500">{req.customerEmail}</p>
                </div>

                <div>
                  <span className="text-gray-400 block uppercase font-semibold text-[10px]">
                    Requested Rental Dates
                  </span>
                  <p className="font-bold text-gray-800 mt-0.5">
                    {formatDate(req.startDate)} to {formatDate(req.endDate)}
                  </p>
                  <p className="text-gray-500">{req.rentalDays} Total Days</p>
                </div>

                <div>
                  <span className="text-gray-400 block uppercase font-semibold text-[10px]">
                    Gross Financial Value
                  </span>
                  <p className="font-bold text-emerald-700 text-sm mt-0.5">
                    {formatCurrency(req.totalAmount)}
                  </p>
                  <p className="text-gray-500">Deposit: {formatCurrency(req.deposit)} (In Escrow)</p>
                </div>
              </div>

              <div className="bg-sand-50 p-3 rounded-xl flex items-center space-x-2 text-xs text-gray-600">
                <MapPin className="w-4 h-4 text-gray-400 shrink-0" />
                <span>Delivery: {req.deliveryAddress}</span>
              </div>

              <div className="flex justify-end space-x-3 pt-2">
                <button
                  onClick={() => handleReject(req.id)}
                  className="btn-outline text-xs py-2 px-4 text-rose-600 hover:bg-rose-50 border-rose-200"
                >
                  <X className="w-3.5 h-3.5 mr-1 inline" />
                  <span>Decline</span>
                </button>
                <button
                  onClick={() => handleApprove(req.id)}
                  className="btn-primary text-xs py-2 px-5 font-bold"
                >
                  <Check className="w-3.5 h-3.5 mr-1 inline" />
                  <span>Approve &amp; Dispatch</span>
                </button>
              </div>
            </div>
          ))
        ) : (
          <div className="card p-8 text-center bg-white rounded-2xl border border-gray-100">
            <p className="text-xs text-gray-400 italic">No rental requests awaiting approval.</p>
          </div>
        )}
      </div>
    </div>
  );
}
