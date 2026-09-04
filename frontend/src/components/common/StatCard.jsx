import React from 'react';

export default function StatCard({ title, value, change, isPositive, icon: Icon, color = 'emerald' }) {
  const colorMap = {
    emerald: {
      bg: 'bg-emerald-50',
      border: 'border-emerald-200',
      icon: 'text-emerald-700',
      badge: 'bg-emerald-100 text-emerald-800',
    },
    forest: {
      bg: 'bg-forest-50',
      border: 'border-forest-200',
      icon: 'text-forest-900',
      badge: 'bg-forest-100 text-forest-900',
    },
    gold: {
      bg: 'bg-gold-50',
      border: 'border-gold-200',
      icon: 'text-gold-700',
      badge: 'bg-gold-100 text-gold-800',
    },
    rose: {
      bg: 'bg-rose-50',
      border: 'border-rose-200',
      icon: 'text-rose-700',
      badge: 'bg-rose-100 text-rose-800',
    },
  };

  const scheme = colorMap[color] || colorMap.emerald;

  return (
    <div className="card p-6 flex flex-col justify-between">
      <div className="flex items-center justify-between">
        <span className="text-xs font-semibold uppercase tracking-wider text-gray-500">
          {title}
        </span>
        {Icon && (
          <div className={`w-10 h-10 rounded-xl ${scheme.bg} flex items-center justify-center ${scheme.icon}`}>
            <Icon className="w-5 h-5" />
          </div>
        )}
      </div>

      <div className="mt-4">
        <h3 className="text-2xl font-bold font-display text-gray-900 tracking-tight">
          {value}
        </h3>
        {change && (
          <div className="mt-2 flex items-center space-x-1 text-xs">
            <span
              className={`font-semibold px-2 py-0.5 rounded-full ${
                isPositive ? 'bg-emerald-100 text-emerald-800' : 'bg-rose-100 text-rose-800'
              }`}
            >
              {isPositive ? '↑' : '↓'} {change}
            </span>
            <span className="text-gray-400">vs last month</span>
          </div>
        )}
      </div>
    </div>
  );
}
