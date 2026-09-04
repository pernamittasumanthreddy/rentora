import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { Sparkles, Mail, KeyRound, ArrowRight, CheckCircle2 } from 'lucide-react';

export default function ForgotPassword() {
  const [email, setEmail] = useState('');
  const [submitted, setSubmitted] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (email) setSubmitted(true);
  };

  return (
    <div className="min-h-[75vh] flex items-center justify-center px-4 py-12">
      <div className="card p-8 sm:p-10 max-w-md w-full bg-white rounded-3xl border border-gray-100 shadow-xl space-y-6">
        <div className="text-center">
          <div className="w-12 h-12 rounded-2xl bg-forest-900 text-white flex items-center justify-center mx-auto mb-4">
            <KeyRound className="w-6 h-6 text-gold-400" />
          </div>
          <h1 className="text-2xl font-bold font-display text-gray-900">Reset Password</h1>
          <p className="text-xs text-gray-500 mt-1">
            Enter your registered email address to receive password recovery instructions
          </p>
        </div>

        {submitted ? (
          <div className="bg-emerald-50 border border-emerald-200 rounded-2xl p-6 text-center space-y-3">
            <CheckCircle2 className="w-10 h-10 text-emerald-600 mx-auto" />
            <h3 className="text-sm font-bold text-emerald-950">Reset Instructions Sent!</h3>
            <p className="text-xs text-emerald-800 leading-relaxed">
              We have dispatched a simulated 6-digit recovery OTP and password reset link to <strong>{email}</strong>.
            </p>
            <Link to="/login" className="btn-primary text-xs py-2 px-4 inline-block mt-3">
              Return to Login
            </Link>
          </div>
        ) : (
          <form onSubmit={handleSubmit} className="space-y-4">
            <div>
              <label className="text-xs font-semibold text-gray-700 block mb-1">
                Account Email
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

            <button
              type="submit"
              className="w-full btn-primary py-3 rounded-xl font-bold flex items-center justify-center space-x-2 text-xs shadow-md"
            >
              <span>Send Recovery Email</span>
              <ArrowRight className="w-4 h-4" />
            </button>
          </form>
        )}

        <p className="text-center text-xs text-gray-500">
          Remember your credentials?{' '}
          <Link to="/login" className="font-semibold text-forest-900 hover:underline">
            Back to Sign In
          </Link>
        </p>
      </div>
    </div>
  );
}
