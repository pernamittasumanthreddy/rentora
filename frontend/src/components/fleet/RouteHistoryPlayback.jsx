import React, { useState } from 'react';
import { Play, Pause, RotateCcw, MapPin, Gauge, Navigation } from 'lucide-react';

export default function RouteHistoryPlayback() {
  const [isPlaying, setIsPlaying] = useState(false);
  const [currentStep, setCurrentStep] = useState(0);

  const routePoints = [
        { step: 1, time: '08:05 AM', lat: 12.9050, lon: 77.5040, speed: 41, status: 'CRUISING' },
        { step: 2, time: '08:10 AM', lat: 12.9100, lon: 77.5080, speed: 42, status: 'CRUISING' },
        { step: 3, time: '08:15 AM', lat: 12.9150, lon: 77.5120, speed: 43, status: 'CRUISING' },
        { step: 4, time: '08:20 AM', lat: 12.9200, lon: 77.5160, speed: 44, status: 'CRUISING' },
        { step: 5, time: '08:25 AM', lat: 12.9250, lon: 77.5200, speed: 45, status: 'CRUISING' },
        { step: 6, time: '08:30 AM', lat: 12.9300, lon: 77.5240, speed: 46, status: 'CHECKPOINT' },
        { step: 7, time: '08:35 AM', lat: 12.9350, lon: 77.5280, speed: 47, status: 'CRUISING' },
        { step: 8, time: '08:40 AM', lat: 12.9400, lon: 77.5320, speed: 48, status: 'CRUISING' },
        { step: 9, time: '08:45 AM', lat: 12.9450, lon: 77.5360, speed: 49, status: 'CRUISING' },
        { step: 10, time: '09:50 AM', lat: 12.9500, lon: 77.5400, speed: 50, status: 'CRUISING' },
        { step: 11, time: '09:55 AM', lat: 12.9550, lon: 77.5440, speed: 51, status: 'CRUISING' },
        { step: 12, time: '09:00 AM', lat: 12.9600, lon: 77.5480, speed: 52, status: 'CHECKPOINT' },
        { step: 13, time: '09:05 AM', lat: 12.9650, lon: 77.5520, speed: 53, status: 'CRUISING' },
        { step: 14, time: '09:10 AM', lat: 12.9700, lon: 77.5560, speed: 54, status: 'CRUISING' },
        { step: 15, time: '09:15 AM', lat: 12.9750, lon: 77.5600, speed: 55, status: 'CRUISING' },
        { step: 16, time: '09:20 AM', lat: 12.9800, lon: 77.5640, speed: 56, status: 'CRUISING' },
        { step: 17, time: '09:25 AM', lat: 12.9850, lon: 77.5680, speed: 57, status: 'CRUISING' },
        { step: 18, time: '09:30 AM', lat: 12.9900, lon: 77.5720, speed: 58, status: 'CHECKPOINT' },
        { step: 19, time: '09:35 AM', lat: 12.9950, lon: 77.5760, speed: 59, status: 'CRUISING' },
        { step: 20, time: '10:40 AM', lat: 13.0000, lon: 77.5800, speed: 60, status: 'CRUISING' },
        { step: 21, time: '10:45 AM', lat: 13.0050, lon: 77.5840, speed: 61, status: 'CRUISING' },
        { step: 22, time: '10:50 AM', lat: 13.0100, lon: 77.5880, speed: 62, status: 'CRUISING' },
        { step: 23, time: '10:55 AM', lat: 13.0150, lon: 77.5920, speed: 63, status: 'CRUISING' },
        { step: 24, time: '10:00 AM', lat: 13.0200, lon: 77.5960, speed: 64, status: 'CHECKPOINT' },
        { step: 25, time: '10:05 AM', lat: 13.0250, lon: 77.6000, speed: 65, status: 'CRUISING' },
        { step: 26, time: '10:10 AM', lat: 13.0300, lon: 77.6040, speed: 66, status: 'CRUISING' },
        { step: 27, time: '10:15 AM', lat: 13.0350, lon: 77.6080, speed: 67, status: 'CRUISING' },
        { step: 28, time: '10:20 AM', lat: 13.0400, lon: 77.6120, speed: 68, status: 'CRUISING' },
        { step: 29, time: '10:25 AM', lat: 13.0450, lon: 77.6160, speed: 69, status: 'CRUISING' },
        { step: 30, time: '11:30 AM', lat: 13.0500, lon: 77.6200, speed: 70, status: 'CHECKPOINT' },
        { step: 31, time: '11:35 AM', lat: 13.0550, lon: 77.6240, speed: 71, status: 'CRUISING' },
        { step: 32, time: '11:40 AM', lat: 13.0600, lon: 77.6280, speed: 72, status: 'CRUISING' },
        { step: 33, time: '11:45 AM', lat: 13.0650, lon: 77.6320, speed: 73, status: 'CRUISING' },
        { step: 34, time: '11:50 AM', lat: 13.0700, lon: 77.6360, speed: 74, status: 'CRUISING' },
        { step: 35, time: '11:55 AM', lat: 13.0750, lon: 77.6400, speed: 40, status: 'CRUISING' },
        { step: 36, time: '11:00 AM', lat: 13.0800, lon: 77.6440, speed: 41, status: 'CHECKPOINT' },
        { step: 37, time: '11:05 AM', lat: 13.0850, lon: 77.6480, speed: 42, status: 'CRUISING' },
        { step: 38, time: '11:10 AM', lat: 13.0900, lon: 77.6520, speed: 43, status: 'CRUISING' },
        { step: 39, time: '11:15 AM', lat: 13.0950, lon: 77.6560, speed: 44, status: 'CRUISING' },
        { step: 40, time: '12:20 AM', lat: 13.1000, lon: 77.6600, speed: 45, status: 'CRUISING' },
        { step: 41, time: '12:25 AM', lat: 13.1050, lon: 77.6640, speed: 46, status: 'CRUISING' },
        { step: 42, time: '12:30 AM', lat: 13.1100, lon: 77.6680, speed: 47, status: 'CHECKPOINT' },
        { step: 43, time: '12:35 AM', lat: 13.1150, lon: 77.6720, speed: 48, status: 'CRUISING' },
        { step: 44, time: '12:40 AM', lat: 13.1200, lon: 77.6760, speed: 49, status: 'CRUISING' },
        { step: 45, time: '12:45 AM', lat: 13.1250, lon: 77.6800, speed: 50, status: 'CRUISING' },
        { step: 46, time: '12:50 AM', lat: 13.1300, lon: 77.6840, speed: 51, status: 'CRUISING' },
        { step: 47, time: '12:55 AM', lat: 13.1350, lon: 77.6880, speed: 52, status: 'CRUISING' },
        { step: 48, time: '12:00 AM', lat: 13.1400, lon: 77.6920, speed: 53, status: 'CHECKPOINT' },
        { step: 49, time: '12:05 AM', lat: 13.1450, lon: 77.6960, speed: 54, status: 'CRUISING' },
        { step: 50, time: '13:10 AM', lat: 13.1500, lon: 77.7000, speed: 55, status: 'CRUISING' },
        { step: 51, time: '13:15 AM', lat: 13.1550, lon: 77.7040, speed: 56, status: 'CRUISING' },
        { step: 52, time: '13:20 AM', lat: 13.1600, lon: 77.7080, speed: 57, status: 'CRUISING' },
        { step: 53, time: '13:25 AM', lat: 13.1650, lon: 77.7120, speed: 58, status: 'CRUISING' },
        { step: 54, time: '13:30 AM', lat: 13.1700, lon: 77.7160, speed: 59, status: 'CHECKPOINT' },
        { step: 55, time: '13:35 AM', lat: 13.1750, lon: 77.7200, speed: 60, status: 'CRUISING' },
        { step: 56, time: '13:40 AM', lat: 13.1800, lon: 77.7240, speed: 61, status: 'CRUISING' },
        { step: 57, time: '13:45 AM', lat: 13.1850, lon: 77.7280, speed: 62, status: 'CRUISING' },
        { step: 58, time: '13:50 AM', lat: 13.1900, lon: 77.7320, speed: 63, status: 'CRUISING' },
        { step: 59, time: '13:55 AM', lat: 13.1950, lon: 77.7360, speed: 64, status: 'CRUISING' },
        { step: 60, time: '14:00 AM', lat: 13.2000, lon: 77.7400, speed: 65, status: 'CHECKPOINT' },
  ];

  return (
    <div className="bg-white rounded-3xl border border-gray-200/80 shadow-card p-6 space-y-6">
      <div className="flex items-center justify-between pb-4 border-b border-gray-100">
        <div>
          <span className="text-xs font-bold uppercase tracking-wider text-emerald-700">Trip Telemetry Audit</span>
          <h3 className="text-xl font-bold font-display text-gray-900 mt-0.5">Route Timeline &amp; Speed Playback</h3>
        </div>
        <div className="flex items-center space-x-2">
          <button onClick={() => setIsPlaying(!isPlaying)} className="btn-primary py-2 px-4 rounded-xl text-xs font-bold flex items-center space-x-1.5">
            {isPlaying ? <Pause className="w-4 h-4" /> : <Play className="w-4 h-4" />}
            <span>{isPlaying ? 'Pause' : 'Play Simulation'}</span>
          </button>
        </div>
      </div>
      <div className="p-4 rounded-2xl bg-sand-100/60 border border-gray-200 text-xs">
        <p className="font-semibold text-gray-800">Total Route Checkpoints: {routePoints.length}</p>
        <p className="text-gray-500 mt-1">Simulated GPS breadcrumb coordinates tracked by Rentora IoT transponder.</p>
      </div>
    </div>
  );
}
