import React from 'react';
import { Sparkles, Shield, HeartHandshake, Leaf, Target, Eye, Users } from 'lucide-react';
import { Link } from 'react-router-dom';

export default function AboutUs() {
  const team = [
    {
      name: 'Aditya Kashyap',
      role: 'Co-Founder & Chief Executive',
      bio: 'Ex-Logistics architect with 12 years experience building supply chain software across South Asia.',
      image: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=400&q=80',
    },
    {
      name: 'Dr. Meera Nambisan',
      role: 'Co-Founder & VP Operations',
      bio: 'Former electronics asset lifecycle manager and sustainability researcher focusing on circular hardware reuse.',
      image: 'https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=400&q=80',
    },
    {
      name: 'Siddharth Roy',
      role: 'Head of Hardware Trust & Safety',
      bio: 'Senior cinema equipment engineer who oversaw cinematic gear maintenance for premier Bollywood studios.',
      image: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=400&q=80',
    },
  ];

  return (
    <div className="space-y-16 pb-20">
      {/* Hero */}
      <section className="bg-forest-950 text-white py-16 sm:py-24">
        <div className="max-w-4xl mx-auto px-4 text-center">
          <div className="inline-flex items-center space-x-2 px-3.5 py-1.5 rounded-full bg-emerald-900/60 border border-emerald-500/30 text-emerald-300 text-xs font-semibold mb-6">
            <Sparkles className="w-3.5 h-3.5 text-gold-400" />
            <span>Our Purpose &amp; Ethos</span>
          </div>
          <h1 className="text-3xl sm:text-5xl font-extrabold font-display tracking-tight">
            Democratizing Access to World-Class Tools and Hardware
          </h1>
          <p className="mt-6 text-gray-300 text-base sm:text-lg leading-relaxed max-w-2xl mx-auto">
            Rentora is founded on a simple conviction: you don’t need to buy a ₹3,00,000 cinema camera or heavy machinery to produce extraordinary work. You just need access when inspiration strikes.
          </p>
        </div>
      </section>

      {/* Mission & Vision Cards */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          <div className="card p-8 bg-white border border-gray-100 rounded-3xl">
            <div className="w-12 h-12 rounded-2xl bg-forest-50 text-forest-900 flex items-center justify-center mb-6">
              <Target className="w-6 h-6" />
            </div>
            <h2 className="text-2xl font-bold font-display text-gray-900 mb-3">Our Mission</h2>
            <p className="text-gray-600 text-sm leading-relaxed">
              To eliminate the capital barriers of production for creators, engineers, builders, and entrepreneurs by establishing a verified, peer-to-peer and vendor-backed asset sharing ecosystem. We enable high-utilization hardware distribution with absolute trust, escrow protection, and rapid turnaround.
            </p>
          </div>

          <div className="card p-8 bg-white border border-gray-100 rounded-3xl">
            <div className="w-12 h-12 rounded-2xl bg-emerald-50 text-emerald-700 flex items-center justify-center mb-6">
              <Eye className="w-6 h-6" />
            </div>
            <h2 className="text-2xl font-bold font-display text-gray-900 mb-3">Our Vision</h2>
            <p className="text-gray-600 text-sm leading-relaxed">
              A regenerative circular economy where hardware is manufactured for longevity, shared transparently, and utilized to its utmost capacity before responsible recycling. We envision an India where every creator has the tools of a premier studio within 60 minutes of their doorstep.
            </p>
          </div>
        </div>
      </section>

      {/* Sustainability Impact Numbers */}
      <section className="bg-sand-200/60 py-16 border-y border-gray-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center max-w-2xl mx-auto mb-12">
            <span className="text-xs font-bold uppercase tracking-wider text-emerald-700">
              Measurable Environmental Impact
            </span>
            <h2 className="text-3xl font-bold font-display text-gray-900 mt-1">
              Sharing is the Purest Form of Sustainability
            </h2>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-3 gap-8 text-center">
            <div className="bg-white p-8 rounded-2xl shadow-sm border border-gray-100">
              <Leaf className="w-8 h-8 text-emerald-600 mx-auto mb-3" />
              <p className="text-3xl font-black font-display text-forest-900">42.8 Metric Tons</p>
              <p className="text-xs text-gray-500 mt-1 uppercase font-semibold">e-Waste Prevented Through Sharing</p>
            </div>
            <div className="bg-white p-8 rounded-2xl shadow-sm border border-gray-100">
              <Shield className="w-8 h-8 text-gold-600 mx-auto mb-3" />
              <p className="text-3xl font-black font-display text-forest-900">8.4x Higher</p>
              <p className="text-xs text-gray-500 mt-1 uppercase font-semibold">Average Unit Lifetime Utilization</p>
            </div>
            <div className="bg-white p-8 rounded-2xl shadow-sm border border-gray-100">
              <HeartHandshake className="w-8 h-8 text-emerald-600 mx-auto mb-3" />
              <p className="text-3xl font-black font-display text-forest-900">₹6.4 Crores</p>
              <p className="text-xs text-gray-500 mt-1 uppercase font-semibold">Capital Saved by Independent Creators</p>
            </div>
          </div>
        </div>
      </section>

      {/* Team */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center max-w-xl mx-auto mb-12">
          <span className="text-xs font-bold uppercase tracking-wider text-forest-900">
            Passionate Leadership
          </span>
          <h2 className="text-3xl font-bold font-display text-gray-900 mt-1">
            Meet the Rentora Team
          </h2>
          <p className="text-xs text-gray-500 mt-2">
            Engineers, gearheads, and logistics specialists obsessed with frictionless equipment sharing.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {team.map((member, i) => (
            <div key={i} className="card p-6 text-center flex flex-col items-center">
              <img
                src={member.image}
                alt={member.name}
                className="w-24 h-24 rounded-full object-cover border-2 border-emerald-600 mb-4"
              />
              <h3 className="font-bold text-gray-900 text-lg">{member.name}</h3>
              <p className="text-xs font-semibold text-emerald-700 uppercase tracking-wider mt-0.5">
                {member.role}
              </p>
              <p className="text-xs text-gray-500 mt-3 leading-relaxed">
                {member.bio}
              </p>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
}
