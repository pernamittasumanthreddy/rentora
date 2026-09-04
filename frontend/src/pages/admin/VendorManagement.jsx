import React, { useState } from 'react';
import { storageService } from '../../services/mockStorage';
import { useNotification } from '../../contexts/NotificationContext';
import { Building2, CheckCircle2, Star, ShieldCheck } from 'lucide-react';

export default function VendorManagement() {
  const { addToast } = useNotification();
  const [vendors, setVendors] = useState(storageService.getVendors());

  const handleUpdateScore = (id, newScore) => {
    storageService.updateVendorTrustScore(id, Number(newScore));
    setVendors(storageService.getVendors());
    addToast('Vendor Trust Score updated!', 'success');
  };

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold font-display text-gray-900">
          Commercial Vendor Governance
        </h1>
        <p className="text-xs text-gray-500 mt-1">
          Audit partner hub reliability, adjust platform Trust Scores, and verify enterprise credentials
        </p>
      </div>

      <div className="card p-6 bg-white border border-gray-100 rounded-3xl shadow-sm overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead>
              <tr className="border-b border-gray-100 text-gray-400 uppercase font-semibold text-[10px]">
                <th className="pb-3 px-3">Business / Partner Hub</th>
                <th className="pb-3 px-3">Owner Contact</th>
                <th className="pb-3 px-3">City &amp; Location</th>
                <th className="pb-3 px-3">Marketplace Rating</th>
                <th className="pb-3 px-3">Trust Score (0-100)</th>
                <th className="pb-3 px-3">Total Orders</th>
                <th className="pb-3 px-3 text-right">Verification</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-100">
              {vendors.map((v) => (
                <tr key={v.id} className="hover:bg-sand-50/60 transition-colors">
                  <td className="py-4 px-3 font-bold text-gray-900">
                    <div className="flex items-center space-x-2">
                      <Building2 className="w-4 h-4 text-emerald-700" />
                      <span>{v.businessName}</span>
                    </div>
                  </td>
                  <td className="py-4 px-3 text-gray-700">
                    <span className="font-semibold block">{v.ownerName}</span>
                    <span className="text-gray-400 text-[10px]">{v.email}</span>
                  </td>
                  <td className="py-4 px-3 text-gray-600">{v.city}</td>
                  <td className="py-4 px-3">
                    <span className="font-bold text-gray-900 flex items-center space-x-1">
                      <Star className="w-3.5 h-3.5 fill-gold-500 text-gold-500" />
                      <span>{v.rating}</span>
                      <span className="text-gray-400 font-normal">({v.reviewCount})</span>
                    </span>
                  </td>
                  <td className="py-4 px-3">
                    <div className="flex items-center space-x-2">
                      <input
                        type="number"
                        min="0"
                        max="100"
                        value={v.trustScore}
                        onChange={(e) => handleUpdateScore(v.id, e.target.value)}
                        className="w-16 px-2 py-1 rounded-lg border border-gray-200 text-xs font-bold text-forest-900"
                      />
                      <span className="text-gray-400 text-[10px]">/ 100</span>
                    </div>
                  </td>
                  <td className="py-4 px-3 font-medium text-gray-700">{v.totalRentals} Rentals</td>
                  <td className="py-4 px-3 text-right">
                    <span className="inline-flex items-center px-2 py-0.5 rounded-full text-[10px] font-bold bg-emerald-100 text-emerald-800">
                      <CheckCircle2 className="w-3 h-3 mr-1" />
                      VERIFIED
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
