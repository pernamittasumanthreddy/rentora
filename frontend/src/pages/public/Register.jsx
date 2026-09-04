import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../../contexts/AuthContext';
import { useNotification } from '../../contexts/NotificationContext';
import { Sparkles, Lock, Mail, User, Phone, MapPin, Store, ArrowRight } from 'lucide-react';

export default function Register() {
  const { register } = useAuth();
  const { addToast } = useNotification();
  const navigate = useNavigate();

  const [role, setRole] = useState('ROLE_CUSTOMER');
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [phone, setPhone] = useState('');
  const [city, setCity] = useState('Bengaluru');
  const [password, setPassword] = useState('');
  const [businessName, setBusinessName] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const user = await register({
        name,
        email,
        phone,
        city,
        password,
        role,
        businessName: role === 'ROLE_VENDOR' ? businessName : undefined,
      });
      addToast(`Account created successfully! Welcome to Rentora.`, 'success');
      if (user.role === 'ROLE_VENDOR') {
        navigate('/vendor/dashboard');
      } else {
        navigate('/customer/dashboard');
      }
    } catch (err) {
      addToast(err.message || 'Registration failed', 'error');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-[85vh] flex items-center justify-center px-4 py-12">
      <div className="card p-8 sm:p-10 max-w-lg w-full bg-white rounded-3xl border border-gray-100 shadow-xl space-y-6">
        <div className="text-center">
          <div className="w-12 h-12 rounded-2xl bg-forest-900 text-white flex items-center justify-center mx-auto mb-4">
            <Sparkles className="w-6 h-6 text-gold-400" />
          </div>
          <h1 className="text-2xl font-bold font-display text-gray-900">Create Rentora Account</h1>
          <p className="text-xs text-gray-500 mt-1">
            Join India's premier verified product rental community
          </p>
        </div>

        {/* Role Selector */}
        <div>
          <label className="text-xs font-semibold text-gray-700 block mb-2">
            I want to join as:
          </label>
          <div className="grid grid-cols-2 gap-3">
            <button
              type="button"
              onClick={() => setRole('ROLE_CUSTOMER')}
              className={`p-3 rounded-2xl border text-center transition-all flex flex-col items-center justify-center ${
                role === 'ROLE_CUSTOMER'
                  ? 'border-forest-900 bg-forest-50/50 text-forest-900 ring-2 ring-forest-900/20'
                  : 'border-gray-200 text-gray-600 hover:bg-sand-50'
              }`}
            >
              <User className="w-5 h-5 mb-1 text-emerald-600" />
              <span className="text-xs font-bold block">Customer / Creator</span>
              <span className="text-[10px] text-gray-400">Rent &amp; use hardware</span>
            </button>

            <button
              type="button"
              onClick={() => setRole('ROLE_VENDOR')}
              className={`p-3 rounded-2xl border text-center transition-all flex flex-col items-center justify-center ${
                role === 'ROLE_VENDOR'
                  ? 'border-forest-900 bg-forest-50/50 text-forest-900 ring-2 ring-forest-900/20'
                  : 'border-gray-200 text-gray-600 hover:bg-sand-50'
              }`}
            >
              <Store className="w-5 h-5 mb-1 text-gold-600" />
              <span className="text-xs font-bold block">Partner Vendor</span>
              <span className="text-[10px] text-gray-400">List gear &amp; earn</span>
            </button>
          </div>
        </div>

        <form onSubmit={handleSubmit} className="space-y-3.5">
          <div>
            <label className="text-xs font-semibold text-gray-700 block mb-1">
              Full Legal Name
            </label>
            <div className="relative">
              <input
                type="text"
                required
                value={name}
                onChange={(e) => setName(e.target.value)}
                className="input-field pl-9 text-xs"
                placeholder="e.g. Rahul Sharma"
              />
              <User className="w-4 h-4 text-gray-400 absolute left-3 top-3" />
            </div>
          </div>

          {role === 'ROLE_VENDOR' && (
            <div>
              <label className="text-xs font-semibold text-gray-700 block mb-1">
                Business / Studio Name
              </label>
              <div className="relative">
                <input
                  type="text"
                  required
                  value={businessName}
                  onChange={(e) => setBusinessName(e.target.value)}
                  className="input-field pl-9 text-xs"
                  placeholder="e.g. Apex Cine Rentals"
                />
                <Store className="w-4 h-4 text-gray-400 absolute left-3 top-3" />
              </div>
            </div>
          )}

          <div>
            <label className="text-xs font-semibold text-gray-700 block mb-1">
              Work / Personal Email
            </label>
            <div className="relative">
              <input
                type="email"
                required
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="input-field pl-9 text-xs"
                placeholder="name@example.com"
              />
              <Mail className="w-4 h-4 text-gray-400 absolute left-3 top-3" />
            </div>
          </div>

          <div className="grid grid-cols-2 gap-3">
            <div>
              <label className="text-xs font-semibold text-gray-700 block mb-1">
                Phone Number
              </label>
              <div className="relative">
                <input
                  type="tel"
                  required
                  value={phone}
                  onChange={(e) => setPhone(e.target.value)}
                  className="input-field pl-9 text-xs"
                  placeholder="+91 98450 11223"
                />
                <Phone className="w-4 h-4 text-gray-400 absolute left-3 top-3" />
              </div>
            </div>

            <div>
              <label className="text-xs font-semibold text-gray-700 block mb-1">
                Operating City
              </label>
              <div className="relative">
                <select
                  value={city}
                  onChange={(e) => setCity(e.target.value)}
                  className="input-field pl-9 text-xs cursor-pointer"
                >
                  <option value="Bengaluru">Bengaluru</option>
                  <option value="Mumbai">Mumbai</option>
                  <option value="Chennai">Chennai</option>
                  <option value="Delhi NCR">Delhi NCR</option>
                  <option value="Hyderabad">Hyderabad</option>
                </select>
                <MapPin className="w-4 h-4 text-gray-400 absolute left-3 top-3" />
              </div>
            </div>
          </div>

          <div>
            <label className="text-xs font-semibold text-gray-700 block mb-1">
              Create Password
            </label>
            <div className="relative">
              <input
                type="password"
                required
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="input-field pl-9 text-xs"
                placeholder="At least 8 characters"
              />
              <Lock className="w-4 h-4 text-gray-400 absolute left-3 top-3" />
            </div>
          </div>

          <button
            type="submit"
            disabled={loading}
            className="w-full btn-primary py-3 rounded-xl font-bold flex items-center justify-center space-x-2 text-xs shadow-md mt-4"
          >
            <span>{loading ? 'Creating Account...' : 'Complete Registration'}</span>
            <ArrowRight className="w-4 h-4" />
          </button>
        </form>

        <p className="text-center text-xs text-gray-500">
          Already have an account?{' '}
          <Link to="/login" className="font-semibold text-forest-900 hover:underline">
            Sign in
          </Link>
        </p>
      </div>
    </div>
  );
}
