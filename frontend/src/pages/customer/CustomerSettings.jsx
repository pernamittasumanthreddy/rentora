import React, { useState } from 'react';
import { useAuth } from '../../contexts/AuthContext';
import { useNotification } from '../../contexts/NotificationContext';
import { User, Mail, Phone, MapPin, Save, ShieldCheck } from 'lucide-react';

export default function CustomerSettings() {
  const { user } = useAuth();
  const { addToast } = useNotification();

  const [name, setName] = useState(user?.name || 'Rahul Sharma');
  const [email] = useState(user?.email || 'customer@rentora.in');
  const [phone, setPhone] = useState(user?.phone || '+91 98450 11223');
  const [city, setCity] = useState(user?.city || 'Bengaluru');
  const [address, setAddress] = useState(
    user?.address || 'Flat 402, Green Glen Layout, Bellandur, Bengaluru 560103'
  );

  const handleSave = (e) => {
    e.preventDefault();
    addToast('Profile and delivery address updated successfully!', 'success');
  };

  return (
    <div className="max-w-2xl space-y-6">
      <div>
        <h1 className="text-2xl font-bold font-display text-gray-900">
          Account Settings
        </h1>
        <p className="text-xs text-gray-500 mt-1">
          Manage identity verification details and default hardware dispatch addresses
        </p>
      </div>

      <div className="card p-8 bg-white border border-gray-100 rounded-3xl shadow-sm space-y-6">
        <div className="flex items-center space-x-4 pb-6 border-b border-gray-100">
          <img
            src={user?.avatar || 'https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?auto=format&fit=crop&w=150&q=80'}
            alt=""
            className="w-16 h-16 rounded-full object-cover border-2 border-emerald-600"
          />
          <div>
            <h3 className="font-bold text-gray-900 text-base">{name}</h3>
            <span className="inline-flex items-center text-xs font-semibold text-emerald-800 bg-emerald-50 px-2 py-0.5 rounded-full mt-1">
              <ShieldCheck className="w-3.5 h-3.5 mr-1 text-emerald-600" />
              KYC Identity Verified
            </span>
          </div>
        </div>

        <form onSubmit={handleSave} className="space-y-4 text-xs">
          <div>
            <label className="font-semibold text-gray-700 block mb-1">Full Legal Name</label>
            <div className="relative">
              <input
                type="text"
                value={name}
                onChange={(e) => setName(e.target.value)}
                className="input-field pl-9 text-xs"
              />
              <User className="w-4 h-4 text-gray-400 absolute left-3 top-3" />
            </div>
          </div>

          <div>
            <label className="font-semibold text-gray-700 block mb-1">Email Address</label>
            <div className="relative">
              <input
                type="email"
                disabled
                value={email}
                className="input-field pl-9 text-xs bg-sand-50 text-gray-400 cursor-not-allowed"
              />
              <Mail className="w-4 h-4 text-gray-400 absolute left-3 top-3" />
            </div>
          </div>

          <div className="grid grid-cols-2 gap-4">
            <div>
              <label className="font-semibold text-gray-700 block mb-1">Phone Number</label>
              <div className="relative">
                <input
                  type="text"
                  value={phone}
                  onChange={(e) => setPhone(e.target.value)}
                  className="input-field pl-9 text-xs"
                />
                <Phone className="w-4 h-4 text-gray-400 absolute left-3 top-3" />
              </div>
            </div>

            <div>
              <label className="font-semibold text-gray-700 block mb-1">City</label>
              <div className="relative">
                <input
                  type="text"
                  value={city}
                  onChange={(e) => setCity(e.target.value)}
                  className="input-field pl-9 text-xs"
                />
                <MapPin className="w-4 h-4 text-gray-400 absolute left-3 top-3" />
              </div>
            </div>
          </div>

          <div>
            <label className="font-semibold text-gray-700 block mb-1">
              Default Equipment Delivery Address
            </label>
            <textarea
              rows="3"
              value={address}
              onChange={(e) => setAddress(e.target.value)}
              className="input-field text-xs resize-none"
            />
          </div>

          <div className="pt-4">
            <button
              type="submit"
              className="btn-primary py-2.5 px-6 rounded-xl font-bold flex items-center space-x-2 shadow-sm"
            >
              <Save className="w-4 h-4" />
              <span>Save Preferences</span>
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
