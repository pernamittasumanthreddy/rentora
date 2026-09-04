import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../../contexts/AuthContext';
import { useNotification } from '../../contexts/NotificationContext';
import { Sparkles, Lock, Mail, ArrowRight, User, Store, Shield } from 'lucide-react';

export default function Login() {
  const { login, switchDemoRole } = useAuth();
  const { addToast } = useNotification();
  const navigate = useNavigate();

  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const user = await login(email, password);
      addToast(`Welcome back, ${user.name}!`, 'success');
      if (user.role === 'ROLE_ADMIN') {
        navigate('/admin/dashboard');
      } else if (user.role === 'ROLE_VENDOR') {
        navigate('/vendor/dashboard');
      } else {
        navigate('/customer/dashboard');
      }
    } catch (err) {
      addToast(err.message || 'Failed to authenticate', 'error');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-[80vh] flex items-center justify-center px-4 py-12">
      <div className="card p-8 sm:p-10 max-w-md w-full bg-white rounded-3xl border border-gray-100 shadow-xl space-y-6">
        <div className="text-center">
          <div className="w-12 h-12 rounded-2xl bg-forest-900 text-white flex items-center justify-center mx-auto mb-4">
            <Sparkles className="w-6 h-6 text-gold-400" />
          </div>
          <h1 className="text-2xl font-bold font-display text-gray-900">Sign in to Rentora</h1>
          <p className="text-xs text-gray-500 mt-1">
            Access your rentals, vendor fleet, or administrative controls
          </p>
        </div>

        {/* Regular Login Form */}
        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="text-xs font-semibold text-gray-700 block mb-1">
              Email Address
            </label>
            <div className="relative">
              <input
                type="email"
                required
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="input-field pl-9 text-xs"
                placeholder="name@rentora.in"
              />
              <Mail className="w-4 h-4 text-gray-400 absolute left-3 top-3" />
            </div>
          </div>

          <div>
            <div className="flex items-center justify-between mb-1">
              <label className="text-xs font-semibold text-gray-700">Password</label>
              <Link to="/forgot-password" className="text-[11px] text-emerald-700 hover:underline">
                Forgot password?
              </Link>
            </div>
            <div className="relative">
              <input
                type="password"
                required
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="input-field pl-9 text-xs"
                placeholder="••••••••"
              />
              <Lock className="w-4 h-4 text-gray-400 absolute left-3 top-3" />
            </div>
          </div>

          <button
            type="submit"
            disabled={loading}
            className="w-full btn-primary py-3 rounded-xl font-bold flex items-center justify-center space-x-2 text-xs shadow-md mt-2"
          >
            <span>{loading ? 'Authenticating...' : 'Sign In'}</span>
            <ArrowRight className="w-4 h-4" />
          </button>
        </form>

        <p className="text-center text-xs text-gray-500">
          Don’t have an account?{' '}
          <Link to="/register" className="font-semibold text-forest-900 hover:underline">
            Register now
          </Link>
        </p>
      </div>
    </div>
  );
}
