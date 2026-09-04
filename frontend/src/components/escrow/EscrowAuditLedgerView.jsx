import React from 'react';
import { ShieldCheck, Hash, Lock, CheckCircle2, ArrowDownRight, ArrowUpRight, Clock } from 'lucide-react';

export default function EscrowAuditLedgerView({ rentalId = 1001 }) {
  const auditEntries = [
    { id: 104821, ref: 'ESCROW-LOCK-1001', type: 'HOLD_DEPOSIT', debit: '₹10,000.00', credit: '—', account: '1010 Escrow Holding', hash: '8f4c1e...92a1', time: 'Aug 28, 2026 10:15 AM' },
    { id: 104822, ref: 'BANK-CLEAR-1001', type: 'NODAL_INFLOW', debit: '—', credit: '₹10,000.00', account: '1020 Nodal Bank Account', hash: 'e3b0c4...118a', time: 'Aug 28, 2026 10:15 AM' },
    { id: 105190, ref: 'ESCROW-REFUND-1001', type: 'AUTO_REFUND', debit: '₹10,000.00', credit: '—', account: '1010 Escrow Holding', hash: 'd4735e...3bc9', time: 'Aug 30, 2026 02:40 PM' },
    { id: 105191, ref: 'BANK-OUTFLOW-1001', type: 'CUSTOMER_CREDIT', debit: '—', credit: '₹10,000.00', account: '1020 Nodal Bank Account', hash: 'fa2201...88cc', time: 'Aug 30, 2026 02:40 PM' }
  ];

  return (
    <div className="bg-white rounded-3xl border border-gray-200/80 shadow-card p-6 space-y-6">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-gray-100">
        <div>
          <span className="text-xs font-bold uppercase tracking-wider text-emerald-700 flex items-center space-x-1.5">
            <Lock className="w-3.5 h-3.5" />
            <span>Immutable Double-Entry Ledger</span>
          </span>
          <h3 className="text-xl font-bold font-display text-gray-900 mt-0.5">
            Cryptographic Escrow Audit Journal
          </h3>
        </div>

        <div className="flex items-center space-x-2">
          <span className="px-3 py-1 rounded-full bg-emerald-50 text-emerald-800 text-xs font-bold flex items-center space-x-1 border border-emerald-200/60">
            <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600" />
            <span>SHA-256 Hash Chain Verified</span>
          </span>
        </div>
      </div>

      <div className="overflow-x-auto">
        <table className="w-full text-left text-xs">
          <thead>
            <tr className="border-b border-gray-200 bg-sand-50/50 text-gray-500 uppercase tracking-wider">
              <th className="py-3 px-4">Entry #</th>
              <th className="py-3 px-4">Ref Code</th>
              <th className="py-3 px-4">Target Account</th>
              <th className="py-3 px-4">Debit (INR)</th>
              <th className="py-3 px-4">Credit (INR)</th>
              <th className="py-3 px-4">Block Hash</th>
              <th className="py-3 px-4">Timestamp</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-gray-100">
            {auditEntries.map(entry => (
              <tr key={entry.id} className="hover:bg-sand-50/50 transition-colors">
                <td className="py-3 px-4 font-mono font-bold text-gray-900">{entry.id}</td>
                <td className="py-3 px-4 font-semibold text-emerald-800">{entry.ref}</td>
                <td className="py-3 px-4 text-gray-700">{entry.account}</td>
                <td className="py-3 px-4 font-bold text-forest-900">{entry.debit}</td>
                <td className="py-3 px-4 font-bold text-forest-900">{entry.credit}</td>
                <td className="py-3 px-4 font-mono text-gray-400 text-[11px]">{entry.hash}</td>
                <td className="py-3 px-4 text-gray-500 text-[11px]">{entry.time}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
