import React, { useState } from 'react';
import { storageService } from '../../services/mockStorage';
import { formatCurrency, formatDate } from '../../utils/formatters';
import { Scale, CheckCircle2, AlertTriangle, ShieldCheck } from 'lucide-react';

export default function ReturnManagement() {
  const [returns] = useState(storageService.getReturns());

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold font-display text-gray-900">
          Returns &amp; Dispute Mediation Console
        </h1>
        <p className="text-xs text-gray-500 mt-1">
          Arbitrate hardware damage assessments, escrow deductions, and ensure fair vendor-client settlement
        </p>
      </div>

      <div className="card p-6 bg-white border border-gray-100 rounded-3xl shadow-sm overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead>
              <tr className="border-b border-gray-100 text-gray-400 uppercase font-semibold text-[10px]">
                <th className="pb-3 px-3">Case ID</th>
                <th className="pb-3 px-3">Equipment Rented</th>
                <th className="pb-3 px-3">Client</th>
                <th className="pb-3 px-3">Vendor</th>
                <th className="pb-3 px-3">Inspection Condition</th>
                <th className="pb-3 px-3">Damage Penalty</th>
                <th className="pb-3 px-3">Deposit Refunded</th>
                <th className="pb-3 px-3 text-right">Arbitration Status</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-100">
              {returns.map((ret) => (
                <tr key={ret.id} className="hover:bg-sand-50/60 transition-colors">
                  <td className="py-4 px-3 font-bold text-gray-900">#RET-{ret.id}</td>
                  <td className="py-4 px-3 font-semibold text-gray-800">{ret.productName}</td>
                  <td className="py-4 px-3 text-gray-700">{ret.customerName}</td>
                  <td className="py-4 px-3 text-gray-600">{ret.vendorName}</td>
                  <td className="py-4 px-3">
                    <span className="text-gray-700 block font-medium">{ret.condition || 'PRISTINE'}</span>
                    <span className="text-[10px] text-gray-400 line-clamp-1">{ret.damageReport}</span>
                  </td>
                  <td className="py-4 px-3 font-semibold text-rose-600">
                    {formatCurrency(ret.damageFee || 0)}
                  </td>
                  <td className="py-4 px-3 font-bold text-emerald-700">
                    {formatCurrency(ret.depositRefunded || 0)}
                  </td>
                  <td className="py-4 px-3 text-right">
                    <span className="badge-active text-[10px]">
                      SETTLED BY ESCROW
                    </span>
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
