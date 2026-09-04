import React from 'react';
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  PieChart,
  Pie,
  Cell,
  AreaChart,
  Area,
  Legend,
} from 'recharts';
import { formatCurrency } from '../../utils/formatters';
import { Download, TrendingUp, BarChart3, PieChart as PieIcon } from 'lucide-react';

const MONTHLY_REVENUE_DATA = [
  { month: 'Apr', gross: 420000, commission: 42000, rentals: 84 },
  { month: 'May', gross: 560000, commission: 56000, rentals: 112 },
  { month: 'Jun', gross: 710000, commission: 71000, rentals: 145 },
  { month: 'Jul', gross: 890000, commission: 89000, rentals: 178 },
  { month: 'Aug', gross: 1150000, commission: 115000, rentals: 220 },
  { month: 'Sep', gross: 1380000, commission: 138000, rentals: 265 },
];

const CATEGORY_SHARE_DATA = [
  { name: 'Cameras & Cinematic Gear', value: 45, color: '#14532D' },
  { name: 'Drones & Aerial Video', value: 25, color: '#10B981' },
  { name: 'Pro Audio & Sound', value: 12, color: '#D97706' },
  { name: 'Gaming & Virtual Reality', value: 10, color: '#059669' },
  { name: 'Power Tools & Outdoor', value: 8, color: '#047857' },
];

export default function AnalyticsReports() {
  const handleExportCSV = () => {
    const csvRows = [
      ['Month', 'Gross Billings (INR)', 'Platform Commission (INR)', 'Completed Rentals'],
      ...MONTHLY_REVENUE_DATA.map((row) => [row.month, row.gross, row.commission, row.rentals]),
    ];

    const csvContent =
      'data:text/csv;charset=utf-8,' + csvRows.map((e) => e.join(',')).join('\n');
    const encodedUri = encodeURI(csvContent);
    const link = document.createElement('a');
    link.setAttribute('href', encodedUri);
    link.setAttribute('download', `rentora_financial_report_${new Date().toISOString().split('T')[0]}.csv`);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  return (
    <div className="space-y-8">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h1 className="text-2xl font-bold font-display text-gray-900">
            Platform Analytics &amp; Revenue Reports
          </h1>
          <p className="text-xs text-gray-500 mt-1">
            Real-time visual reports of gross merchandise value, commission fees, and category velocity
          </p>
        </div>

        <button
          onClick={handleExportCSV}
          className="btn-primary py-2.5 px-5 text-xs font-bold flex items-center space-x-2 shadow-sm"
        >
          <Download className="w-4 h-4" />
          <span>Export Audit CSV</span>
        </button>
      </div>

      {/* Chart 1: Monthly GMV & Commission */}
      <div className="card p-6 sm:p-8 bg-white border border-gray-100 rounded-3xl shadow-sm space-y-6">
        <div className="flex items-center justify-between">
          <div>
            <h3 className="text-base font-bold font-display text-gray-900 flex items-center space-x-2">
              <TrendingUp className="w-5 h-5 text-emerald-600" />
              <span>Gross Equipment Revenue &amp; Platform Commission</span>
            </h3>
            <p className="text-xs text-gray-500 mt-0.5">
              Tracking consistent month-on-month GMV expansion across nationwide vendor hubs
            </p>
          </div>
          <span className="text-xs font-bold text-forest-900 bg-sand-100 px-3 py-1.5 rounded-xl">
            Total H1 GMV: ₹51.1 Lakhs
          </span>
        </div>

        <div className="h-72 w-full">
          <ResponsiveContainer width="100%" height="100%">
            <BarChart data={MONTHLY_REVENUE_DATA} margin={{ top: 10, right: 10, left: -20, bottom: 0 }}>
              <XAxis dataKey="month" stroke="#94a3b8" fontSize={12} tickLine={false} />
              <YAxis stroke="#94a3b8" fontSize={12} tickLine={false} tickFormatter={(val) => `₹${val / 1000}k`} />
              <Tooltip
                formatter={(value) => [formatCurrency(value), '']}
                contentStyle={{ backgroundColor: '#fff', borderRadius: '12px', border: '1px solid #e2e8f0', fontSize: '12px' }}
              />
              <Legend wrapperStyle={{ fontSize: '12px', paddingTop: '10px' }} />
              <Bar dataKey="gross" name="Gross Rental GMV" fill="#14532D" radius={[6, 6, 0, 0]} />
              <Bar dataKey="commission" name="Platform Take (10%)" fill="#10B981" radius={[6, 6, 0, 0]} />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>

      {/* Chart 2 & 3: Category Velocity & Growth Trends */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        {/* Category Share Donut */}
        <div className="card p-6 sm:p-8 bg-white border border-gray-100 rounded-3xl shadow-sm space-y-4">
          <div>
            <h3 className="text-base font-bold font-display text-gray-900 flex items-center space-x-2">
              <PieIcon className="w-5 h-5 text-gold-600" />
              <span>Category Revenue Share</span>
            </h3>
            <p className="text-xs text-gray-500 mt-0.5">
              Proportion of GMV generated by equipment departments
            </p>
          </div>

          <div className="h-64 w-full flex items-center justify-center">
            <ResponsiveContainer width="100%" height="100%">
              <PieChart>
                <Pie
                  data={CATEGORY_SHARE_DATA}
                  cx="50%"
                  cy="50%"
                  innerRadius={60}
                  outerRadius={90}
                  paddingAngle={5}
                  dataKey="value"
                >
                  {CATEGORY_SHARE_DATA.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={entry.color} />
                  ))}
                </Pie>
                <Tooltip
                  formatter={(value) => [`${value}% Share`, 'Volume']}
                  contentStyle={{ backgroundColor: '#fff', borderRadius: '12px', border: '1px solid #e2e8f0', fontSize: '12px' }}
                />
                <Legend wrapperStyle={{ fontSize: '11px' }} />
              </PieChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* Rental Volume Growth Area Chart */}
        <div className="card p-6 sm:p-8 bg-white border border-gray-100 rounded-3xl shadow-sm space-y-4">
          <div>
            <h3 className="text-base font-bold font-display text-gray-900 flex items-center space-x-2">
              <BarChart3 className="w-5 h-5 text-forest-900" />
              <span>Completed Rental Orders Volume</span>
            </h3>
            <p className="text-xs text-gray-500 mt-0.5">
              Total successful fulfillment orders completed per month
            </p>
          </div>

          <div className="h-64 w-full">
            <ResponsiveContainer width="100%" height="100%">
              <AreaChart data={MONTHLY_REVENUE_DATA} margin={{ top: 10, right: 10, left: -20, bottom: 0 }}>
                <defs>
                  <linearGradient id="colorRentals" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="5%" stopColor="#10B981" stopOpacity={0.4} />
                    <stop offset="95%" stopColor="#10B981" stopOpacity={0} />
                  </linearGradient>
                </defs>
                <XAxis dataKey="month" stroke="#94a3b8" fontSize={12} tickLine={false} />
                <YAxis stroke="#94a3b8" fontSize={12} tickLine={false} />
                <Tooltip
                  contentStyle={{ backgroundColor: '#fff', borderRadius: '12px', border: '1px solid #e2e8f0', fontSize: '12px' }}
                />
                <Area type="monotone" dataKey="rentals" stroke="#10B981" strokeWidth={3} fillOpacity={1} fill="url(#colorRentals)" />
              </AreaChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>
    </div>
  );
}
