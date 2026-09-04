import React, { useState } from 'react';
import { Camera, AlertCircle, CheckCircle2, ShieldCheck, Tag, Trash2, Plus } from 'lucide-react';

export default function InteractiveDamageAnnotationCanvas({ rentalId = 1001, onAssessmentComplete }) {
  const [annotations, setAnnotations] = useState([
    { id: 1, x: 38, y: 52, part: 'Front Bumper Diffuser', note: 'Minor surface stone-chip', severity: 'MILD', fee: 0 }
  ]);

  const [selectedPart, setSelectedPart] = useState('Front Bumper');
  const [noteText, setNoteText] = useState('');
  const [damageFee, setDamageFee] = useState(0);

  const handleCanvasClick = (e) => {
    const rect = e.currentTarget.getBoundingClientRect();
    const x = Math.round(((e.clientX - rect.left) / rect.width) * 100);
    const y = Math.round(((e.clientY - rect.top) / rect.height) * 100);

    const newMarker = {
      id: Date.now(),
      x,
      y,
      part: selectedPart,
      note: noteText || 'Inspected checkpoint',
      severity: damageFee > 0 ? 'NEEDS_REPAIR' : 'MILD',
      fee: Number(damageFee) || 0
    };

    setAnnotations([...annotations, newMarker]);
    setNoteText('');
    setDamageFee(0);
  };

  const removeMarker = (id) => {
    setAnnotations(annotations.filter(a => a.id !== id));
  };

  const totalDamageFee = annotations.reduce((sum, a) => sum + a.fee, 0);

  return (
    <div className="bg-white rounded-3xl border border-gray-200/80 shadow-card p-6 space-y-6">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-gray-100">
        <div>
          <span className="text-xs font-bold uppercase tracking-wider text-emerald-700 flex items-center space-x-1.5">
            <ShieldCheck className="w-3.5 h-3.5" />
            <span>Digital 5-Point Check</span>
          </span>
          <h3 className="text-xl font-bold font-display text-gray-900 mt-0.5">
            Vehicle &amp; Gear Damage Annotation Canvas
          </h3>
        </div>

        <div className="flex items-center space-x-3">
          <span className="text-xs font-bold text-gray-500">Total Deduction:</span>
          <span className="text-base font-extrabold text-forest-900">₹{totalDamageFee.toLocaleString('en-IN')}</span>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Interactive Coordinate Canvas */}
        <div className="lg:col-span-2 space-y-3">
          <p className="text-xs text-gray-500">
            Click anywhere on the schematic canvas to pin an inspection observation tag:
          </p>

          <div
            onClick={handleCanvasClick}
            className="w-full h-80 rounded-2xl bg-gradient-to-b from-gray-100 to-gray-200 border-2 border-dashed border-gray-300 relative overflow-hidden cursor-crosshair flex items-center justify-center group"
          >
            {/* Blueprint Wireframe Grid */}
            <div className="absolute inset-0 opacity-15 bg-[radial-gradient(#000_1px,transparent_1px)] [background-size:20px_20px]"></div>

            <div className="text-center pointer-events-none opacity-40">
              <Camera className="w-12 h-12 mx-auto mb-2 text-gray-600" />
              <p className="text-xs font-bold uppercase tracking-widest text-gray-700">Vehicle / Rig 360° Schematic</p>
            </div>

            {/* Render Pinned Damage Annotations */}
            {annotations.map(a => (
              <div
                key={a.id}
                style={{ left: `${a.x}%`, top: `${a.y}%` }}
                className="absolute -translate-x-1/2 -translate-y-1/2 group/marker z-10"
              >
                <span className={`w-6 h-6 rounded-full flex items-center justify-center text-white text-[10px] font-bold shadow-md cursor-pointer ${
                  a.fee > 0 ? 'bg-red-500 animate-bounce' : 'bg-emerald-600'
                }`}>
                  !
                </span>
                <div className="hidden group-hover/marker:block absolute bottom-8 left-1/2 -translate-x-1/2 bg-gray-900 text-white text-[11px] p-2 rounded-xl whitespace-nowrap z-20 shadow-lg">
                  <p className="font-bold">{a.part}</p>
                  <p className="text-gray-300">{a.note}</p>
                  {a.fee > 0 && <p className="text-red-400 font-bold">Penalty: ₹{a.fee}</p>}
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Observation Tagging Form */}
        <div className="bg-sand-100/60 p-5 rounded-2xl border border-gray-200/80 space-y-4">
          <h4 className="text-xs font-bold uppercase tracking-wider text-gray-700">
            Observation Details
          </h4>

          <div>
            <label className="text-xs font-semibold text-gray-700 block mb-1">Inspected Part</label>
            <select
              value={selectedPart}
              onChange={(e) => setSelectedPart(e.target.value)}
              className="w-full text-xs p-2.5 rounded-xl border border-gray-200 bg-white font-medium focus:outline-none"
            >
              <option value="Front Bumper">Front Bumper &amp; Grill</option>
              <option value="Windshield">Windshield &amp; Wipers</option>
              <option value="Alloy Wheels">Alloy Wheels &amp; Tyres</option>
              <option value="Side Doors">Side Doors &amp; Paint</option>
              <option value="Rear Diffuser">Rear Diffuser &amp; Boot</option>
              <option value="Interior Cabin">Interior Seats &amp; Infotainment</option>
            </select>
          </div>

          <div>
            <label className="text-xs font-semibold text-gray-700 block mb-1">Notes / Description</label>
            <input
              type="text"
              placeholder="e.g. Scratch on clear-coat..."
              value={noteText}
              onChange={(e) => setNoteText(e.target.value)}
              className="w-full text-xs p-2.5 rounded-xl border border-gray-200 bg-white focus:outline-none"
            />
          </div>

          <div>
            <label className="text-xs font-semibold text-gray-700 block mb-1">Assessed Penalty Fee (₹)</label>
            <input
              type="number"
              min="0"
              step="100"
              placeholder="0 for normal wear"
              value={damageFee}
              onChange={(e) => setDamageFee(e.target.value)}
              className="w-full text-xs p-2.5 rounded-xl border border-gray-200 bg-white focus:outline-none font-bold"
            />
          </div>

          {/* List of Marked Annotations */}
          <div className="pt-2 border-t border-gray-200 space-y-2">
            <span className="text-[11px] font-bold text-gray-500 uppercase">Logged Points ({annotations.length})</span>
            <div className="max-h-36 overflow-y-auto space-y-1.5">
              {annotations.map(a => (
                <div key={a.id} className="flex items-center justify-between p-2 rounded-lg bg-white text-xs border border-gray-100">
                  <div>
                    <span className="font-bold text-gray-800">{a.part}</span>
                    <p className="text-[10px] text-gray-500">{a.note}</p>
                  </div>
                  <button onClick={() => removeMarker(a.id)} className="text-red-500 hover:text-red-700 p-1">
                    <Trash2 className="w-3.5 h-3.5" />
                  </button>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
