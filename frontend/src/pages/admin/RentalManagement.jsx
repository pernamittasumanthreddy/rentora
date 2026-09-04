import React, { useState } from 'react';
import { storageService } from '../../services/mockStorage';
import { formatCurrency, formatDate } from '../../utils/formatters';
import { FileSpreadsheet, Search, CheckCircle2, Clock } from 'lucide-react';

export default function RentalManagement() {
  const [rentals] = useState(storageService.getRentals());
  const [statusFilter, setStatusFilter] = useState('ALL');

  const filtered = rentals.filter((r) => {
    if (statusFilter === 'ALL') return true;
    return r.status === statusFilter;
  });

  return (
    <div className="space-y-6">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h1 className="text-2xl font-bold font-display text-gray-900">
            Platform Rental Orders Audit
          </h1>
          <p className="text-xs text-gray-500 mt-1">
            Complete transaction trail of active, completed, and pending equipment bookings
          </p>
        </div>

        <select
          value={statusFilter}
          onChange={(e) => setStatusFilter(e.target.value)}
          className="px-3 py-2 rounded-xl bg-white border border-gray-200 text-xs font-semibold text-gray-700 cursor-pointer"
        >
          <option value="ALL">All Order States</option>
          <option value="ACTIVE">Active in Client Custody</option>
          <option value="PENDING">Pending Dispatch</option>
          <option value="COMPLETED">Completed &amp; Settled</option>
        </select>
      </div>

      <div className="card p-6 bg-white border border-gray-100 rounded-3xl shadow-sm overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead>
              <tr className="border-b border-gray-100 text-gray-400 uppercase font-semibold text-[10px]">
                <th className="pb-3 px-3">Order ID</th>
                <th className="pb-3 px-3">Equipment</th>
                <th className="pb-3 px-3">Renter</th>
                <th className="pb-3 px-3">Vendor</th>
                <th className="pb-3 px-3">Rental Dates</th>
                <th className="pb-3 px-3">Total Billed</th>
                <th className="pb-3 px-3">Escrow Deposit</th>
                <th className="pb-3 px-3 text-right">Lifecycle Status</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-100">
              {filtered.map((r) => (
                <tr key={r.id} className="hover:bg-sand-50/60 transition-colors">
                  <td className="py-4 px-3 font-bold text-gray-900">#{r.id}</td>
                  <td className="py-4 px-3 font-semibold text-gray-800 line-clamp-1 max-w-[180px]">
                    {r.productName}
                  </td>
                  <td className="py-4 px-3 text-gray-700">{r.customerName}</td>
                  <td className="py-4 px-3 text-gray-600">{r.vendorName}</td>
                  <td className="py-4 px-3 text-gray-500">
                    {formatDate(r.startDate)} – {formatDate(r.endDate)}
                  </td>
                  <td className="py-4 px-3 font-bold text-gray-900">{formatCurrency(r.totalAmount)}</td>
                  <td className="py-4 px-3 font-semibold text-emerald-700">{formatCurrency(r.deposit)}</td>
                  <td className="py-4 px-3 text-right">
                    {r.status === 'ACTIVE' ? (
                      <span className="badge-active text-[10px]">ACTIVE</span>
                    ) : r.status === 'PENDING' ? (
                      <span className="badge-pending text-[10px]">PENDING</span>
                    ) : (
                      <span className="badge-completed text-[10px]">COMPLETED</span>
                    )}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
