import React, { useState } from 'react';
import { useAuth } from '../../contexts/AuthContext';
import { storageService } from '../../services/mockStorage';
import { Star, MessageSquare } from 'lucide-react';

export default function CustomerReviews() {
  const { user } = useAuth();
  const [reviews] = useState(
    storageService.getReviews().filter((r) => r.customerId === user?.id || r.customerId === 1)
  );

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold font-display text-gray-900">
          My Ratings &amp; Feedback
        </h1>
        <p className="text-xs text-gray-500 mt-1">
          Reviews shared on products and verified vendor rental experiences
        </p>
      </div>

      {reviews.length > 0 ? (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
          {reviews.map((rev) => (
            <div key={rev.id} className="card p-6 bg-white border border-gray-100 rounded-2xl shadow-sm space-y-3">
              <div className="flex items-center justify-between">
                <div className="flex text-gold-500">
                  {Array.from({ length: rev.rating }).map((_, i) => (
                    <Star key={i} className="w-4 h-4 fill-current" />
                  ))}
                </div>
                <span className="text-[11px] text-gray-400">{rev.date}</span>
              </div>
              <p className="text-xs text-gray-700 leading-relaxed font-medium">"{rev.comment}"</p>
              <div className="pt-2 border-t border-gray-100 flex items-center justify-between text-[11px] text-gray-500">
                <span>Verified Renter Feedback</span>
                <span className="text-emerald-700 font-semibold">Published on Marketplace</span>
              </div>
            </div>
          ))}
        </div>
      ) : (
        <div className="card p-12 text-center bg-white rounded-2xl border border-gray-100">
          <MessageSquare className="w-10 h-10 text-gray-300 mx-auto mb-3" />
          <p className="text-sm font-semibold text-gray-700">No reviews submitted yet</p>
          <p className="text-xs text-gray-400 mt-1">Once you complete an equipment rental, you can rate the hardware condition and vendor.</p>
        </div>
      )}
    </div>
  );
}
