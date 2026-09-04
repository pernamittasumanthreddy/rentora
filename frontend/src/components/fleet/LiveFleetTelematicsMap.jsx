import React, { useState, useEffect } from 'react';
import { Navigation, MapPin, Gauge, Battery, ShieldAlert, CheckCircle, RefreshCw, Car, Bike } from 'lucide-react';
import { motion } from 'framer-motion';

export default function LiveFleetTelematicsMap({ selectedVehicleVin }) {
  const [vehicles, setVehicles] = useState([
    {
      vin: 'VIN-THAR-4X4-8821',
      model: 'Mahindra Thar 4x4 Hard-Top',
      type: 'CAR',
      driver: 'Arjun Namboodiri',
      lat: 12.9716,
      lon: 77.5946,
      speedKmh: 64,
      fuelPct: 82,
      batteryV: 13.8,
      status: 'ON_TRIP',
      zone: 'Bengaluru Metro Permitted'
    },
    {
      vin: 'VIN-BMW-330I-1049',
      model: 'BMW 330i M-Sport',
      type: 'CAR',
      driver: 'Kavita Menon',
      lat: 19.0760,
      lon: 72.8777,
      speedKmh: 48,
      fuelPct: 94,
      batteryV: 14.1,
      status: 'ON_TRIP',
      zone: 'Mumbai Coastal Corridor'
    },
    {
      vin: 'VIN-HIMALAYAN-450-993',
      model: 'Royal Enfield Himalayan 450',
      type: 'BIKE',
      driver: 'Rahul Sharma',
      lat: 11.4102,
      lon: 76.6950,
      speedKmh: 58,
      fuelPct: 76,
      batteryV: 13.5,
      status: 'ON_TRIP',
      zone: 'Nilgiris Adventure Loop'
    },
    {
      vin: 'VIN-NINJA-ZX6R-441',
      model: 'Kawasaki Ninja ZX-6R',
      type: 'BIKE',
      driver: 'Devansh Kulkarni',
      lat: 13.0827,
      lon: 80.2707,
      speedKmh: 0,
      fuelPct: 65,
      batteryV: 13.2,
      status: 'PARKED_SAFE',
      zone: 'Irungattukottai Track Paddock'
    }
  ]);

  const [activeVin, setActiveVin] = useState(selectedVehicleVin || 'VIN-THAR-4X4-8821');
  const activeVehicle = vehicles.find(v => v.vin === activeVin) || vehicles[0];

  return (
    <div className="bg-white rounded-3xl border border-gray-200/80 shadow-card p-6 space-y-6">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-gray-100">
        <div>
          <span className="text-xs font-bold uppercase tracking-wider text-emerald-700 flex items-center space-x-1.5">
            <Navigation className="w-3.5 h-3.5" />
            <span>IoT CAN-Bus Telemetry</span>
          </span>
          <h3 className="text-xl font-bold font-display text-gray-900 mt-0.5">
            Live Fleet Radar &amp; Geofence Watchdog
          </h3>
        </div>

        <div className="flex items-center space-x-2">
          <span className="inline-flex items-center space-x-1.5 px-3 py-1 rounded-full bg-emerald-50 text-emerald-800 text-xs font-semibold">
            <span className="w-2 h-2 rounded-full bg-emerald-500 animate-ping"></span>
            <span>4 Vehicles Streaming</span>
          </span>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Vehicle Selection List */}
        <div className="space-y-2.5">
          <label className="text-xs font-bold text-gray-600 uppercase tracking-wider block">
            Active Monitored Fleet
          </label>
          {vehicles.map(v => (
            <button
              key={v.vin}
              onClick={() => setActiveVin(v.vin)}
              className={`w-full p-4 rounded-2xl text-left border transition-all flex items-center justify-between ${
                activeVin === v.vin
                  ? 'border-forest-900 bg-forest-50/50 shadow-sm ring-1 ring-forest-900/10'
                  : 'border-gray-100 hover:border-gray-200 bg-white'
              }`}
            >
              <div className="flex items-center space-x-3">
                <div className="w-10 h-10 rounded-xl bg-forest-900 text-white flex items-center justify-center shrink-0">
                  {v.type === 'CAR' ? <Car className="w-5 h-5" /> : <Bike className="w-5 h-5" />}
                </div>
                <div>
                  <h4 className="text-xs font-bold text-gray-900">{v.model}</h4>
                  <p className="text-[11px] text-gray-500">Renter: {v.driver}</p>
                </div>
              </div>
              <div className="text-right">
                <span className="text-xs font-extrabold text-forest-900">{v.speedKmh} km/h</span>
                <p className="text-[10px] text-emerald-600 font-semibold">{v.status}</p>
              </div>
            </button>
          ))}
        </div>

        {/* Live Gauges & Telemetry Detail */}
        <div className="lg:col-span-2 bg-sand-100/60 p-6 rounded-2xl border border-gray-200/80 space-y-6">
          <div className="flex items-center justify-between">
            <div>
              <h4 className="text-sm font-bold text-gray-900">{activeVehicle.model}</h4>
              <p className="text-xs text-gray-500 font-mono mt-0.5">VIN: {activeVehicle.vin}</p>
            </div>
            <div className="flex items-center space-x-1.5 px-3 py-1 rounded-full bg-white border border-gray-200 text-xs font-semibold text-gray-700">
              <MapPin className="w-3.5 h-3.5 text-emerald-600" />
              <span>{activeVehicle.zone}</span>
            </div>
          </div>

          <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
            <div className="bg-white p-4 rounded-xl border border-gray-100 shadow-sm text-center">
              <Gauge className="w-5 h-5 text-emerald-600 mx-auto mb-1" />
              <p className="text-2xl font-black font-display text-gray-900">{activeVehicle.speedKmh}</p>
              <p className="text-[10px] font-semibold text-gray-400 uppercase">Current Speed</p>
            </div>

            <div className="bg-white p-4 rounded-xl border border-gray-100 shadow-sm text-center">
              <span className="text-emerald-600 font-bold text-lg block mb-1">⛽</span>
              <p className="text-2xl font-black font-display text-gray-900">{activeVehicle.fuelPct}%</p>
              <p className="text-[10px] font-semibold text-gray-400 uppercase">Fuel Level</p>
            </div>

            <div className="bg-white p-4 rounded-xl border border-gray-100 shadow-sm text-center">
              <Battery className="w-5 h-5 text-emerald-600 mx-auto mb-1" />
              <p className="text-2xl font-black font-display text-gray-900">{activeVehicle.batteryV} V</p>
              <p className="text-[10px] font-semibold text-gray-400 uppercase">Aux Battery</p>
            </div>

            <div className="bg-white p-4 rounded-xl border border-gray-100 shadow-sm text-center">
              <CheckCircle className="w-5 h-5 text-gold-500 mx-auto mb-1" />
              <p className="text-2xl font-black font-display text-gray-900">0</p>
              <p className="text-[10px] font-semibold text-gray-400 uppercase">Active Faults</p>
            </div>
          </div>

          {/* Simulated Map Coordinates Radar Box */}
          <div className="h-44 rounded-xl bg-forest-950 text-white flex flex-col items-center justify-center relative overflow-hidden p-4 text-center">
            <div className="absolute inset-0 opacity-20 bg-[radial-gradient(#10B981_1px,transparent_1px)] [background-size:16px_16px]"></div>
            <Navigation className="w-8 h-8 text-emerald-400 animate-pulse mb-2 z-10" />
            <p className="text-xs font-semibold z-10 text-emerald-300">Live Satellite GPS Fix Locked</p>
            <p className="text-[11px] font-mono text-gray-400 z-10 mt-1">
              Latitude: {activeVehicle.lat.toFixed(4)}° N • Longitude: {activeVehicle.lon.toFixed(4)}° E
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}
