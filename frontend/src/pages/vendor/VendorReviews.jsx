import React from 'react';
import { storageService } from '../../services/mockStorage';
import { Star, ShieldCheck } from 'lucide-react';

export default function VendorReviews() {
  const reviews = storageService.getReviews();

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold font-display text-gray-900">
          Client Reviews &amp; Vendor Trust Rating
        </h1>
        <p className="text-xs text-gray-500 mt-1">
          Feedback left by directors, creators, and professionals who rented your fleet
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
        {reviews.map((rev) => (
          <div key={rev.id} className="card p-6 bg-white border border-gray-100 rounded-2xl shadow-sm space-y-3">
            <div className="flex items-center justify-between">
              <div className="flex items-center space-x-3">
                <img
                  src={rev.customerAvatar}
                  alt=""
                  className="w-9 h-9 rounded-full object-cover"
                />
                <div>
                  <h4 className="font-bold text-gray-900 text-xs">{rev.customerName}</h4>
                  <span className="text-[10px] text-gray-400">{rev.date}</span>
                </div>
              </div>

              <div className="flex text-gold-500">
                {Array.from({ length: rev.rating }).map((_, i) => (
                  <Star key={i} className="w-3.5 h-3.5 fill-current" />
                ))}
              </div>
            </div>

            <p className="text-xs text-gray-700 leading-relaxed font-medium">
              "{rev.comment}"
            </p>

            <div className="pt-2 border-t border-gray-100 flex items-center justify-between text-[11px] text-emerald-800">
              <span className="flex items-center space-x-1">
                <ShieldCheck className="w-3.5 h-3.5 text-emerald-600" />
                <span>Verified Equipment Booking</span>
              </span>
              <span className="font-semibold">Rating: {rev.rating}.0 / 5.0</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
