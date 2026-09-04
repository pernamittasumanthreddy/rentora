import React, { useState } from 'react';
import { useNotification } from '../../contexts/NotificationContext';
import { Sliders, Save, Shield, Percent, AlertCircle } from 'lucide-react';

export default function AdminSettings() {
  const { addToast } = useNotification();

  const [commissionRate, setCommissionRate] = useState(10);
  const [defaultDepositPercent, setDefaultDepositPercent] = useState(30);
  const [gstRate, setGstRate] = useState(18);
  const [allowInstantBooking, setAllowInstantBooking] = useState(true);
  const [maintenanceMode, setMaintenanceMode] = useState(false);

  const handleSave = (e) => {
    e.preventDefault();
    addToast('Platform business rules updated successfully!', 'success');
  };

  return (
    <div className="max-w-2xl space-y-6">
      <div>
        <h1 className="text-2xl font-bold font-display text-gray-900">
          Platform Business Rules &amp; Settings
        </h1>
        <p className="text-xs text-gray-500 mt-1">
          Adjust runtime financial commission rates, tax rates, and security deposit thresholds
        </p>
      </div>

      <div className="card p-8 bg-white border border-gray-100 rounded-3xl shadow-sm space-y-6">
        <form onSubmit={handleSave} className="space-y-5 text-xs">
          <div>
            <label className="font-semibold text-gray-700 block mb-1">
              Vendor Platform Commission (%)
            </label>
            <div className="relative">
              <input
                type="number"
                min="0"
                max="30"
                value={commissionRate}
                onChange={(e) => setCommissionRate(Number(e.target.value))}
                className="input-field pl-9 text-xs"
              />
              <Percent className="w-4 h-4 text-gray-400 absolute left-3 top-3" />
            </div>
            <span className="text-[10px] text-gray-400 mt-1 block">
              Currently deducting 10% from vendor rental earnings.
            </span>
          </div>

          <div>
            <label className="font-semibold text-gray-700 block mb-1">
              Default Recommended Escrow Deposit (% of replacement value)
            </label>
            <div className="relative">
              <input
                type="number"
                min="10"
                max="100"
                value={defaultDepositPercent}
                onChange={(e) => setDefaultDepositPercent(Number(e.target.value))}
                className="input-field pl-9 text-xs"
              />
              <Shield className="w-4 h-4 text-gray-400 absolute left-3 top-3" />
            </div>
          </div>

          <div>
            <label className="font-semibold text-gray-700 block mb-1">
              GST Commercial Rate (%)
            </label>
            <div className="relative">
              <input
                type="number"
                disabled
                value={gstRate}
                className="input-field pl-9 text-xs bg-sand-50 text-gray-400 cursor-not-allowed"
              />
              <Percent className="w-4 h-4 text-gray-400 absolute left-3 top-3" />
            </div>
            <span className="text-[10px] text-gray-400 mt-1 block">
              18% GST (9% CGST + 9% SGST) applied per Indian Commercial Goods &amp; Services Tax regulation.
            </span>
          </div>

          <div className="pt-2 border-t border-gray-100 space-y-3">
            <label className="flex items-center space-x-3 cursor-pointer">
              <input
                type="checkbox"
                checked={allowInstantBooking}
                onChange={(e) => setAllowInstantBooking(e.target.checked)}
                className="rounded text-forest-900 focus:ring-forest-900 w-4 h-4"
              />
              <div>
                <span className="font-bold text-gray-900 block">Instant Automated Escrow Approval</span>
                <span className="text-[11px] text-gray-400">
                  Allow immediate confirmation upon deposit clearance without manual dispatch lock.
                </span>
              </div>
            </label>
          </div>

          <div className="pt-4">
            <button
              type="submit"
              className="btn-primary py-2.5 px-6 rounded-xl font-bold flex items-center space-x-2 shadow-sm"
            >
              <Save className="w-4 h-4" />
              <span>Save System Rules</span>
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
