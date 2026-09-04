import React from 'react';
import { DollarSign, TrendingUp, BarChart3, PieChart, ShieldCheck, ArrowUpRight } from 'lucide-react';

export default function EnterpriseRevenueAnalytics() {
  const kpis = [
    { title: 'Gross Merchandise Value (GMV)', val: '₹3,42,80,000', change: '+24.6% MoM', positive: true },
    { title: 'Escrow Deposits Currently Held', val: '₹48,50,000', change: '100% RBI Escrow Backed', positive: true },
    { title: 'Net Platform Commission (10%)', val: '₹34,28,000', change: '+18.2% vs Target', positive: true },
    { title: 'Average Deposit Refund SLA', val: '2.4 Hours', change: '99.8% Dispute Free', positive: true }
  ];

  return (
    <div className="bg-white rounded-3xl border border-gray-200/80 shadow-card p-6 space-y-6">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-gray-100">
        <div>
          <span className="text-xs font-bold uppercase tracking-wider text-emerald-700 flex items-center space-x-1.5">
            <TrendingUp className="w-3.5 h-3.5" />
            <span>Executive Business Intelligence</span>
          </span>
          <h3 className="text-xl font-bold font-display text-gray-900 mt-0.5">
            Platform GMV, Escrow Velocity &amp; Yield Analytics
          </h3>
        </div>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        {kpis.map((kpi, i) => (
          <div key={i} className="p-5 rounded-2xl bg-sand-50/60 border border-gray-100 space-y-1">
            <p className="text-xs font-semibold text-gray-500">{kpi.title}</p>
            <p className="text-2xl font-black font-display text-gray-900">{kpi.val}</p>
            <p className="text-[11px] font-bold text-emerald-700 flex items-center space-x-1">
              <ArrowUpRight className="w-3 h-3" />
              <span>{kpi.change}</span>
            </p>
          </div>
        ))}
      </div>
    </div>
  );
}
