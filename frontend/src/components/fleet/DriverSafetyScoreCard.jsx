import React from 'react';
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
