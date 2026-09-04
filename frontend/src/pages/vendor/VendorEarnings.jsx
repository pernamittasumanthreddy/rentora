import React from 'react';
import { storageService } from '../../services/mockStorage';
import { formatCurrency } from '../../utils/formatters';
import StatCard from '../../components/common/StatCard';
import { IndianRupee, ArrowUpRight, FileSpreadsheet, CheckCircle2 } from 'lucide-react';

export default function VendorEarnings() {
  const rentals = storageService.getRentals().filter((r) => r.vendorId === 101);

  const grossEarnings = rentals.reduce((sum, r) => sum + (r.rentalFee || 0), 0);
  const platformFee = Math.round(grossEarnings * 0.10); // 10% platform commission
  const netEarnings = grossEarnings - platformFee;

  return (
    <div className="space-y-8">
      <div>
        <h1 className="text-2xl font-bold font-display text-gray-900">
          Vendor Earnings &amp; Financial Payouts
        </h1>
        <p className="text-xs text-gray-500 mt-1">
          Review net hardware payouts, 10% platform commissions, and direct bank settlement cycles
        </p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-3 gap-5">
        <StatCard
          title="Gross Equipment Billings"
          value={formatCurrency(grossEarnings)}
          icon={IndianRupee}
          color="emerald"
        />
        <StatCard
          title="Platform Commission (10%)"
          value={formatCurrency(platformFee)}
          icon={ArrowUpRight}
          color="gold"
        />
        <StatCard
          title="Net Vendor Earnings"
          value={formatCurrency(netEarnings)}
          icon={CheckCircle2}
          color="forest"
        />
      </div>

      {/* Payout records */}
      <div className="card p-6 bg-white border border-gray-100 rounded-3xl shadow-sm overflow-hidden space-y-4">
        <h3 className="text-sm font-bold text-gray-900">Rental Item Billing Ledger</h3>
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead>
              <tr className="border-b border-gray-100 text-gray-400 uppercase font-semibold text-[10px]">
                <th className="pb-3 px-3">Order ID</th>
                <th className="pb-3 px-3">Renter</th>
                <th className="pb-3 px-3">Gross Rental</th>
                <th className="pb-3 px-3">Commission (10%)</th>
                <th className="pb-3 px-3">Net Payout</th>
                <th className="pb-3 px-3">Settlement</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-100">
              {rentals.map((r) => {
                const comm = Math.round((r.rentalFee || 0) * 0.1);
                const net = (r.rentalFee || 0) - comm;
                return (
                  <tr key={r.id} className="hover:bg-sand-50/60 transition-colors">
                    <td className="py-4 px-3 font-bold text-gray-900">#{r.id}</td>
                    <td className="py-4 px-3 text-gray-700">{r.customerName}</td>
                    <td className="py-4 px-3 font-semibold text-gray-900">{formatCurrency(r.rentalFee)}</td>
                    <td className="py-4 px-3 text-rose-600 font-medium">-{formatCurrency(comm)}</td>
                    <td className="py-4 px-3 font-bold text-emerald-700">{formatCurrency(net)}</td>
                    <td className="py-4 px-3">
                      <span className="badge-active text-[10px]">SETTLED</span>
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
