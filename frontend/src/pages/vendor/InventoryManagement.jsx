import React, { useState } from 'react';
import { storageService } from '../../services/mockStorage';
import { useNotification } from '../../contexts/NotificationContext';
import { Boxes, CheckCircle2, Wrench, AlertTriangle, ShieldCheck } from 'lucide-react';

export default function InventoryManagement() {
  const { addToast } = useNotification();
  const products = storageService.getProducts().filter((p) => p.vendorId === 101);

  // Simulated physical serial inventory fleet
  const [fleetUnits, setFleetUnits] = useState([
    { id: 'SN-FX3-001', model: 'Sony FX3 Cinema Line Full-Frame Camera', status: 'RENTED', condition: 'A+ Mint', barcode: 'BC-FX3-8821' },
    { id: 'SN-FX3-002', model: 'Sony FX3 Cinema Line Full-Frame Camera', status: 'AVAILABLE', condition: 'A+ Mint', barcode: 'BC-FX3-8822' },
    { id: 'SN-FX3-003', model: 'Sony FX3 Cinema Line Full-Frame Camera', status: 'MAINTENANCE', condition: 'Sensor Cleaning', barcode: 'BC-FX3-8823' },
    { id: 'SN-RS3-011', model: 'DJI RS 3 Pro 3-Axis Gimbal Stabilizer', status: 'AVAILABLE', condition: 'Calibrated', barcode: 'BC-RS3-1092' },
    { id: 'SN-RS3-012', model: 'DJI RS 3 Pro 3-Axis Gimbal Stabilizer', status: 'RENTED', condition: 'Excellent', barcode: 'BC-RS3-1093' },
    { id: 'SN-M3P-001', model: 'DJI Mavic 3 Pro Cine Combo Drone', status: 'AVAILABLE', condition: 'Propellers Inspected', barcode: 'BC-M3P-4401' },
  ]);

  const handleToggleMaintenance = (unitId) => {
    setFleetUnits((prev) =>
      prev.map((unit) => {
        if (unit.id === unitId) {
          const nextStatus = unit.status === 'MAINTENANCE' ? 'AVAILABLE' : 'MAINTENANCE';
          return { ...unit, status: nextStatus };
        }
        return unit;
      })
    );
    addToast('Fleet unit service status updated!', 'success');
  };

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold font-display text-gray-900">
          Physical Fleet Inventory &amp; Serial Units
        </h1>
        <p className="text-xs text-gray-500 mt-1">
          Barcoded hardware tracking, sensor maintenance logs, and readiness inspection
        </p>
      </div>

      <div className="card p-6 bg-white border border-gray-100 rounded-3xl shadow-sm overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead>
              <tr className="border-b border-gray-100 text-gray-400 uppercase font-semibold text-[10px]">
                <th className="pb-3 px-3">Serial ID</th>
                <th className="pb-3 px-3">Barcode Tracking</th>
                <th className="pb-3 px-3">Hardware Model</th>
                <th className="pb-3 px-3">Health / Condition</th>
                <th className="pb-3 px-3">Status</th>
                <th className="pb-3 px-3 text-right">Service Action</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-100">
              {fleetUnits.map((u) => (
                <tr key={u.id} className="hover:bg-sand-50/60 transition-colors">
                  <td className="py-4 px-3 font-bold text-gray-900">{u.id}</td>
                  <td className="py-4 px-3 text-gray-500 font-mono">{u.barcode}</td>
                  <td className="py-4 px-3 text-gray-800 font-medium">{u.model}</td>
                  <td className="py-4 px-3 text-gray-600">{u.condition}</td>
                  <td className="py-4 px-3">
                    {u.status === 'AVAILABLE' ? (
                      <span className="badge-active text-[10px]">READY FOR HIRE</span>
                    ) : u.status === 'RENTED' ? (
                      <span className="badge-pending text-[10px]">IN CLIENT SHOOT</span>
                    ) : (
                      <span className="badge-cancelled text-[10px]">IN SERVICING</span>
                    )}
                  </td>
                  <td className="py-4 px-3 text-right">
                    {u.status !== 'RENTED' && (
                      <button
                        onClick={() => handleToggleMaintenance(u.id)}
                        className="text-xs font-semibold text-forest-900 hover:text-emerald-700"
                      >
                        {u.status === 'MAINTENANCE' ? 'Mark Ready' : 'Log Maintenance'}
                      </button>
                    )}
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
