import React, { useState } from 'react';
import { storageService } from '../../services/mockStorage';
import { useNotification } from '../../contexts/NotificationContext';
import { formatCurrency, formatDate } from '../../utils/formatters';
import { RotateCcw, ShieldCheck, CheckSquare, AlertCircle, FileCheck, CheckCircle2 } from 'lucide-react';

export default function VendorReturns() {
  const { addToast } = useNotification();
  const [returns, setReturns] = useState(storageService.getReturns());
  const [inspectingReturn, setInspectingReturn] = useState(null);

  // 5-point checklist state
  const [checklist, setChecklist] = useState({
    optics: true,
    electronics: true,
    casing: true,
    accessories: true,
    operational: true,
  });
  const [damageFee, setDamageFee] = useState(0);
  const [inspectionNotes, setInspectionNotes] = useState('Hardware returned in pristine factory condition.');

  const handleOpenInspection = (ret) => {
    setInspectingReturn(ret);
    setChecklist({
      optics: true,
      electronics: true,
      casing: true,
      accessories: true,
      operational: true,
    });
    setDamageFee(0);
    setInspectionNotes('Hardware returned in pristine factory condition.');
  };

  const handleSettleReturn = (e) => {
    e.preventDefault();
    if (!inspectingReturn) return;

    const condition = damageFee > 0 ? 'MINOR_DAMAGE' : 'PRISTINE';
    storageService.settleReturn(inspectingReturn.id, Number(damageFee), condition, inspectionNotes);

    addToast('Return inspection completed! Security deposit settled & released.', 'success');
    setInspectingReturn(null);
    setReturns(storageService.getReturns());
  };

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold font-display text-gray-900">
          Returns &amp; Hardware Inspection
        </h1>
        <p className="text-xs text-gray-500 mt-1">
          Perform multi-point checks, assess damage reports, and release customer escrow deposits
        </p>
      </div>

      <div className="card p-6 bg-white border border-gray-100 rounded-3xl shadow-sm overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead>
              <tr className="border-b border-gray-100 text-gray-400 uppercase font-semibold text-[10px]">
                <th className="pb-3 px-3">Return ID</th>
                <th className="pb-3 px-3">Equipment</th>
                <th className="pb-3 px-3">Renter Name</th>
                <th className="pb-3 px-3">Return Date</th>
                <th className="pb-3 px-3">Condition Status</th>
                <th className="pb-3 px-3">Damage Fee</th>
                <th className="pb-3 px-3">Deposit Refunded</th>
                <th className="pb-3 px-3 text-right">Action</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-100">
              {returns.map((ret) => (
                <tr key={ret.id} className="hover:bg-sand-50/60 transition-colors">
                  <td className="py-4 px-3 font-bold text-gray-900">#{ret.id}</td>
                  <td className="py-4 px-3 font-semibold text-gray-800">{ret.productName}</td>
                  <td className="py-4 px-3 text-gray-600">{ret.customerName}</td>
                  <td className="py-4 px-3 text-gray-500">{formatDate(ret.returnDate)}</td>
                  <td className="py-4 px-3">
                    {ret.status === 'SETTLED' ? (
                      <span className="badge-completed text-[10px]">SETTLED &amp; CLOSED</span>
                    ) : (
                      <span className="badge-pending text-[10px]">INSPECTION PENDING</span>
                    )}
                  </td>
                  <td className="py-4 px-3 font-semibold text-rose-600">
                    {formatCurrency(ret.damageFee || 0)}
                  </td>
                  <td className="py-4 px-3 font-bold text-emerald-700">
                    {formatCurrency(ret.depositRefunded || 0)}
                  </td>
                  <td className="py-4 px-3 text-right">
                    {ret.status !== 'SETTLED' ? (
                      <button
                        onClick={() => handleOpenInspection(ret)}
                        className="btn-primary text-xs py-1.5 px-3 rounded-lg"
                      >
                        Inspect Unit
                      </button>
                    ) : (
                      <span className="text-gray-400 text-xs">Completed</span>
                    )}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>

      {/* 5-Point Inspection Modal */}
      {inspectingReturn && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/50 backdrop-blur-sm">
          <div className="card p-6 sm:p-8 max-w-lg w-full bg-white rounded-3xl shadow-2xl space-y-5 animate-in fade-in zoom-in-95 max-h-[90vh] overflow-y-auto">
            <div>
              <span className="text-[10px] font-bold uppercase tracking-wider text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded">
                Quality Assurance Check
              </span>
              <h3 className="text-lg font-bold font-display text-gray-900 mt-2">
                5-Point Technical Return Inspection
              </h3>
              <p className="text-xs text-gray-500">
                Unit: <strong>{inspectingReturn.productName}</strong> (Returned by {inspectingReturn.customerName})
              </p>
            </div>

            <form onSubmit={handleSettleReturn} className="space-y-4 text-xs">
              {/* 5 Points */}
              <div className="space-y-2.5 bg-sand-50 p-4 rounded-2xl border border-gray-200">
                <span className="font-bold text-gray-800 block text-xs mb-1">
                  Checklist Inspection Protocol:
                </span>

                <label className="flex items-center space-x-2.5 cursor-pointer">
                  <input
                    type="checkbox"
                    checked={checklist.optics}
                    onChange={(e) => setChecklist({ ...checklist, optics: e.target.checked })}
                    className="rounded text-forest-900 focus:ring-forest-900 w-4 h-4"
                  />
                  <span className="text-gray-700">1. Optical glass, sensor, and gimbal axis intact</span>
                </label>

                <label className="flex items-center space-x-2.5 cursor-pointer">
                  <input
                    type="checkbox"
                    checked={checklist.electronics}
                    onChange={(e) => setChecklist({ ...checklist, electronics: e.target.checked })}
                    className="rounded text-forest-900 focus:ring-forest-900 w-4 h-4"
                  />
                  <span className="text-gray-700">2. Electronic ports, battery pins, and display panel clear</span>
                </label>

                <label className="flex items-center space-x-2.5 cursor-pointer">
                  <input
                    type="checkbox"
                    checked={checklist.casing}
                    onChange={(e) => setChecklist({ ...checklist, casing: e.target.checked })}
                    className="rounded text-forest-900 focus:ring-forest-900 w-4 h-4"
                  />
                  <span className="text-gray-700">3. Physical housing and carbon-fiber arms undamaged</span>
                </label>

                <label className="flex items-center space-x-2.5 cursor-pointer">
                  <input
                    type="checkbox"
                    checked={checklist.accessories}
                    onChange={(e) => setChecklist({ ...checklist, accessories: e.target.checked })}
                    className="rounded text-forest-900 focus:ring-forest-900 w-4 h-4"
                  />
                  <span className="text-gray-700">4. Inclusions (chargers, cables, SD card, case) verified</span>
                </label>

                <label className="flex items-center space-x-2.5 cursor-pointer">
                  <input
                    type="checkbox"
                    checked={checklist.operational}
                    onChange={(e) => setChecklist({ ...checklist, operational: e.target.checked })}
                    className="rounded text-forest-900 focus:ring-forest-900 w-4 h-4"
                  />
                  <span className="text-gray-700">5. 60-second live test video/flight run passed</span>
                </label>
              </div>

              <div>
                <label className="font-semibold text-gray-700 block mb-1">
                  Damage Deduction Fee (₹)
                </label>
                <input
                  type="number"
                  min="0"
                  value={damageFee}
                  onChange={(e) => setDamageFee(e.target.value)}
                  className="input-field text-xs"
                  placeholder="Enter 0 if no damage found"
                />
                <span className="text-[10px] text-gray-400 mt-1 block">
                  Remaining escrow deposit is instantly refunded to client.
                </span>
              </div>

              <div>
                <label className="font-semibold text-gray-700 block mb-1">
                  Inspection Assessment Remarks
                </label>
                <textarea
                  rows="2"
                  value={inspectionNotes}
                  onChange={(e) => setInspectionNotes(e.target.value)}
                  className="input-field text-xs resize-none"
                />
              </div>

              <div className="flex justify-end space-x-3 pt-3">
                <button
                  type="button"
                  onClick={() => setInspectingReturn(null)}
                  className="btn-outline text-xs py-2 px-4"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  className="btn-primary text-xs py-2 px-5 font-bold flex items-center space-x-1.5"
                >
                  <CheckCircle2 className="w-4 h-4" />
                  <span>Release Escrow &amp; Close</span>
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
}
