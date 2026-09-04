import React, { useState } from 'react';
import { storageService } from '../../services/mockStorage';
import { formatCurrency } from '../../utils/formatters';
import { CreditCard, CheckCircle2, RefreshCw, Shield, FileDown } from 'lucide-react';

export default function PaymentsHistory() {
  const [payments] = useState(storageService.getPayments());

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold font-display text-gray-900">
          Payments &amp; Escrow Ledger
        </h1>
        <p className="text-xs text-gray-500 mt-1">
          Detailed itemized audit receipts, GST breakdowns, and security deposit refund records
        </p>
      </div>

      <div className="card p-6 bg-white border border-gray-100 rounded-3xl shadow-sm overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead>
              <tr className="border-b border-gray-100 text-gray-400 uppercase font-semibold text-[10px]">
                <th className="pb-3 px-3">Transaction Ref</th>
                <th className="pb-3 px-3">Linked Order</th>
                <th className="pb-3 px-3">Date &amp; Time</th>
                <th className="pb-3 px-3">Payment Method</th>
                <th className="pb-3 px-3">Total Paid</th>
                <th className="pb-3 px-3">Escrow Deposit</th>
                <th className="pb-3 px-3">Status</th>
                <th className="pb-3 px-3 text-right">Invoice</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-100">
              {payments.map((p) => (
                <tr key={p.id} className="hover:bg-sand-50/60 transition-colors">
                  <td className="py-4 px-3 font-bold text-gray-900">{p.id}</td>
                  <td className="py-4 px-3 text-gray-600 font-medium">#{p.rentalId}</td>
                  <td className="py-4 px-3 text-gray-500">{p.paymentDate}</td>
                  <td className="py-4 px-3 text-gray-700">{p.paymentMethod}</td>
                  <td className="py-4 px-3 font-bold text-gray-900">{formatCurrency(p.amount)}</td>
                  <td className="py-4 px-3 font-semibold text-emerald-700">
                    {formatCurrency(p.depositAmount)}
                  </td>
                  <td className="py-4 px-3">
                    {p.paymentStatus === 'PAID' ? (
                      <span className="inline-flex items-center px-2 py-0.5 rounded-full text-[10px] font-semibold bg-emerald-100 text-emerald-800">
                        <CheckCircle2 className="w-2.5 h-2.5 mr-1" />
                        COMPLETED
                      </span>
                    ) : p.paymentStatus === 'HELD_IN_ESCROW' ? (
                      <span className="inline-flex items-center px-2 py-0.5 rounded-full text-[10px] font-semibold bg-amber-100 text-amber-800">
                        <Shield className="w-2.5 h-2.5 mr-1" />
                        IN ESCROW
                      </span>
                    ) : (
                      <span className="inline-flex items-center px-2 py-0.5 rounded-full text-[10px] font-semibold bg-blue-100 text-blue-800">
                        <RefreshCw className="w-2.5 h-2.5 mr-1" />
                        REFUNDED
                      </span>
                    )}
                  </td>
                  <td className="py-4 px-3 text-right">
                    <button
                      onClick={() => alert(`Simulated GST Invoice download for ${p.id} initiated.`)}
                      className="text-forest-900 hover:text-emerald-700 font-semibold inline-flex items-center space-x-1"
                      title="Download GST Commercial Receipt"
                    >
                      <FileDown className="w-3.5 h-3.5" />
                      <span>PDF</span>
                    </button>
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
