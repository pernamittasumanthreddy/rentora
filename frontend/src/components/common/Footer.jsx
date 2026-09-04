import React from 'react';
import { Link } from 'react-router-dom';
import { Sparkles, ShieldCheck, RefreshCw, Truck, HeartHandshake } from 'lucide-react';

export default function Footer() {
  return (
    <footer className="bg-forest-950 text-sand-200 border-t border-forest-900 pt-16 pb-12">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Value Highlights Strip */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6 pb-12 border-b border-forest-900">
          <div className="flex items-start space-x-3.5">
            <div className="w-10 h-10 rounded-xl bg-forest-900 flex items-center justify-center text-emerald-400 shrink-0">
              <ShieldCheck className="w-5 h-5" />
            </div>
            <div>
              <h4 className="text-sm font-semibold text-white">Verified Equipment</h4>
              <p className="text-xs text-gray-400 mt-1">Multi-point tested units from trusted commercial vendors.</p>
            </div>
          </div>

          <div className="flex items-start space-x-3.5">
            <div className="w-10 h-10 rounded-xl bg-forest-900 flex items-center justify-center text-gold-400 shrink-0">
              <RefreshCw className="w-5 h-5" />
            </div>
            <div>
              <h4 className="text-sm font-semibold text-white">Escrow Protection</h4>
              <p className="text-xs text-gray-400 mt-1">100% refundable security deposits held in audited escrow.</p>
            </div>
          </div>

          <div className="flex items-start space-x-3.5">
            <div className="w-10 h-10 rounded-xl bg-forest-900 flex items-center justify-center text-emerald-400 shrink-0">
              <Truck className="w-5 h-5" />
            </div>
            <div>
              <h4 className="text-sm font-semibold text-white">Doorstep Delivery</h4>
              <p className="text-xs text-gray-400 mt-1">Scheduled dispatch with secure OTP handover and tracking.</p>
            </div>
          </div>

          <div className="flex items-start space-x-3.5">
            <div className="w-10 h-10 rounded-xl bg-forest-900 flex items-center justify-center text-gold-400 shrink-0">
              <HeartHandshake className="w-5 h-5" />
            </div>
            <div>
              <h4 className="text-sm font-semibold text-white">Circular Economy</h4>
              <p className="text-xs text-gray-400 mt-1">Reduce electronic waste through high-utilization product sharing.</p>
            </div>
          </div>
        </div>

        {/* 4 Column Main Footer */}
        <div className="grid grid-cols-1 md:grid-cols-5 gap-10 py-12">
          {/* Col 1: Brand Info */}
          <div className="md:col-span-2 space-y-4">
            <div className="flex items-center space-x-3">
              <div className="w-10 h-10 rounded-xl bg-forest-900 flex items-center justify-center text-white">
                <Sparkles className="w-5 h-5 text-gold-400" />
              </div>
              <span className="text-2xl font-bold font-display text-white tracking-tight">
                RENTORA
              </span>
            </div>
            <p className="text-sm text-gray-300 max-w-sm leading-relaxed">
              India's premier smart product rental and sharing platform. Empowering creators, professionals, and enthusiasts with flexible on-demand access to cinema cameras, drones, audio rigs, and gear.
            </p>
            <p className="text-xs text-gray-400">
              CIN: U72900KA2024PTC188201 • Registered GST: 29AABCU9603R1ZM
            </p>
          </div>

          {/* Col 2: Marketplace */}
          <div>
            <h5 className="text-xs uppercase font-bold tracking-wider text-emerald-400 mb-4">
              Explore Gear
            </h5>
            <ul className="space-y-2.5 text-sm text-gray-300">
              <li>
                <Link to="/products?category=cameras-gear" className="hover:text-white transition-colors">
                  Cameras &amp; Cinema Line
                </Link>
              </li>
              <li>
                <Link to="/products?category=drones-aerial" className="hover:text-white transition-colors">
                  Drones &amp; Aerial Video
                </Link>
              </li>
              <li>
                <Link to="/products?category=pro-audio" className="hover:text-white transition-colors">
                  Pro Audio &amp; Microphones
                </Link>
              </li>
              <li>
                <Link to="/products?category=gaming-vr" className="hover:text-white transition-colors">
                  Gaming Consoles &amp; VR
                </Link>
              </li>
              <li>
                <Link to="/products?category=power-tools" className="hover:text-white transition-colors">
                  Power Tools &amp; DIY
                </Link>
              </li>
            </ul>
          </div>

          {/* Col 3: Company */}
          <div>
            <h5 className="text-xs uppercase font-bold tracking-wider text-emerald-400 mb-4">
              Platform
            </h5>
            <ul className="space-y-2.5 text-sm text-gray-300">
              <li>
                <Link to="/about" className="hover:text-white transition-colors">
                  About Our Mission
                </Link>
              </li>
              <li>
                <Link to="/register" className="hover:text-white transition-colors">
                  Become a Partner Vendor
                </Link>
              </li>
              <li>
                <Link to="/customer/dashboard" className="hover:text-white transition-colors">
                  Customer Portal
                </Link>
              </li>
              <li>
                <Link to="/vendor/dashboard" className="hover:text-white transition-colors">
                  Vendor Hub
                </Link>
              </li>
              <li>
                <Link to="/admin/dashboard" className="hover:text-white transition-colors">
                  Admin Console
                </Link>
              </li>
            </ul>
          </div>

          {/* Col 4: Trust & Support */}
          <div>
            <h5 className="text-xs uppercase font-bold tracking-wider text-gold-400 mb-4">
              Trust &amp; Legal
            </h5>
            <ul className="space-y-2.5 text-sm text-gray-300">
              <li>
                <span className="hover:text-white cursor-pointer transition-colors">
                  Escrow Deposit Protection
                </span>
              </li>
              <li>
                <span className="hover:text-white cursor-pointer transition-colors">
                  Damage &amp; Inspection Matrix
                </span>
              </li>
              <li>
                <span className="hover:text-white cursor-pointer transition-colors">
                  Rental Agreement Terms
                </span>
              </li>
              <li>
                <span className="hover:text-white cursor-pointer transition-colors">
                  Privacy Policy &amp; Security
                </span>
              </li>
              <li>
                <span className="text-xs text-gray-400 block mt-2">
                  Support: help@rentora.in
                </span>
              </li>
            </ul>
          </div>
        </div>

        {/* Bottom bar */}
        <div className="pt-8 border-t border-forest-900 flex flex-col sm:flex-row items-center justify-between text-xs text-gray-400 gap-4">
          <p>© {new Date().getFullYear()} Rentora Technologies Private Limited. All rights reserved.</p>
          <div className="flex items-center space-x-6">
            <span>Built with React 18 &amp; Spring Boot 3</span>
            <span className="text-emerald-400 font-medium">Bengaluru • Mumbai • Chennai</span>
          </div>
        </div>
      </div>
    </footer>
  );
}
