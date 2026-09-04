#!/usr/bin/env python3
"""
Rentora Part 3: React / JSX Enterprise Modules Generator
Generates comprehensive React components for live telematics route playback,
driver safety scoring, escrow audit ledger view, and enterprise revenue analytics.
"""

import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend", "src")

def write_jsx(component_dir, file_name, content):
    target_dir = os.path.join(FRONTEND_DIR, "components", component_dir)
    os.makedirs(target_dir, exist_ok=True)
    file_path = os.path.join(target_dir, file_name)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    lines = len(content.splitlines())
    print(f"  + frontend/src/components/{component_dir}/{file_name} ({lines} lines)")

def generate_react_components():
    # 1. DriverSafetyScoreCard.jsx
    write_jsx("fleet", "DriverSafetyScoreCard.jsx", """import React from 'react';
import { ShieldCheck, Award, AlertTriangle, Zap, CheckCircle2, TrendingUp, Info } from 'lucide-react';
import { motion } from 'framer-motion';

export default function DriverSafetyScoreCard({ score = 94, driverName = 'Arjun Namboodiri', rentalId = 1001 }) {
  const isExcellent = score >= 90;
  const isGood = score >= 75 && score < 90;

  const incidents = [
    { id: 1, type: 'Smooth Braking', status: 'PASS', scoreImpact: '+12 pts', desc: 'No harsh decelerations recorded over 240 km' },
    { id: 2, type: 'Speed Regulation', status: 'PASS', scoreImpact: '+15 pts', desc: 'Maintained 90 km/h cruising on expressway' },
    { id: 3, type: 'Night Driving', status: 'NOTICE', scoreImpact: '-2 pts', desc: 'Driven 1.5 hrs past midnight with headlights on' },
    { id: 4, type: 'Cornering G-Force', status: 'PASS', scoreImpact: '+10 pts', desc: 'Lateral acceleration within comfortable 0.25G bounds' }
  ];

  return (
    <div className="bg-white rounded-3xl border border-gray-200/80 shadow-card p-6 space-y-6">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-gray-100">
        <div>
          <span className="text-xs font-bold uppercase tracking-wider text-emerald-700 flex items-center space-x-1.5">
            <Award className="w-3.5 h-3.5" />
            <span>Telematics Trust Rating</span>
          </span>
          <h3 className="text-xl font-bold font-display text-gray-900 mt-0.5">
            Driver Behavioral Scorecard
          </h3>
        </div>

        <div className="flex items-center space-x-2">
          <span className="text-xs text-gray-400">Renter:</span>
          <span className="text-xs font-bold text-gray-800">{driverName}</span>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {/* Large Score Dial Badge */}
        <div className="bg-gradient-to-b from-forest-950 via-forest-900 to-forest-950 rounded-2xl p-6 text-white text-center flex flex-col items-center justify-center relative overflow-hidden">
          <div className="w-28 h-28 rounded-full border-4 border-emerald-400 flex flex-col items-center justify-center bg-forest-900/80 shadow-lg shadow-emerald-950/50">
            <span className="text-4xl font-black font-display text-emerald-300">{score}</span>
            <span className="text-[10px] font-bold uppercase tracking-wider text-gray-300">Out of 100</span>
          </div>

          <p className="text-sm font-bold text-white mt-4">
            {isExcellent ? 'Gold Tier Renter' : isGood ? 'Silver Tier Renter' : 'Standard Renter'}
          </p>
          <p className="text-[11px] text-gray-300 mt-1">
            Qualifies for 20% discount on future security deposits
          </p>
        </div>

        {/* Detailed Breakdown */}
        <div className="md:col-span-2 space-y-3">
          <h4 className="text-xs font-bold uppercase tracking-wider text-gray-700">
            Telemetry Evaluation Log
          </h4>
          <div className="space-y-2">
            {incidents.map(inc => (
              <div key={inc.id} className="p-3.5 rounded-xl border border-gray-100 bg-sand-50 flex items-center justify-between">
                <div className="flex items-center space-x-3">
                  {inc.status === 'PASS' ? (
                    <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0" />
                  ) : (
                    <Info className="w-4 h-4 text-gold-500 shrink-0" />
                  )}
                  <div>
                    <h5 className="text-xs font-bold text-gray-900">{inc.type}</h5>
                    <p className="text-[11px] text-gray-500">{inc.desc}</p>
                  </div>
                </div>
                <span className="text-xs font-bold text-emerald-700">{inc.scoreImpact}</span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
""")

    # 2. EscrowAuditLedgerView.jsx
    write_jsx("escrow", "EscrowAuditLedgerView.jsx", """import React from 'react';
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
""")

    # 3. EnterpriseRevenueAnalytics.jsx
    write_jsx("analytics", "EnterpriseRevenueAnalytics.jsx", """import React from 'react';
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
""")

if __name__ == "__main__":
    print("=" * 70)
    print("Building React Enterprise Modules (Part 3)...")
    print("=" * 70)
    generate_react_components()
    print("Done generating React components.")
