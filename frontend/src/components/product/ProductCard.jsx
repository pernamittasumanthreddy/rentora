import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { Star, ShieldCheck, Heart, ArrowRight } from 'lucide-react';
import { formatCurrency } from '../../utils/formatters';
import { storageService } from '../../services/mockStorage';
import { useCart } from '../../contexts/CartContext';

export default function ProductCard({ product, isWishlisted, onWishlistToggle }) {
  const navigate = useNavigate();
  const { saveCart } = useCart();

  const handleInstantRent = (e) => {
    e.preventDefault();
    e.stopPropagation();
    saveCart(product);
    navigate('/checkout');
  };

  return (
    <div className="card-hover group flex flex-col overflow-hidden bg-white border border-gray-100 rounded-2xl relative">
      {/* Wishlist Button */}
      <button
        onClick={(e) => {
          e.preventDefault();
          e.stopPropagation();
          onWishlistToggle && onWishlistToggle(product.id);
        }}
        className={`absolute top-3 right-3 z-10 w-8 h-8 rounded-full flex items-center justify-center backdrop-blur-md transition-all ${
          isWishlisted
            ? 'bg-rose-50 text-rose-600 shadow-sm'
            : 'bg-white/80 text-gray-400 hover:text-rose-500 hover:bg-white'
        }`}
        title="Add to Wishlist"
      >
        <Heart className={`w-4 h-4 ${isWishlisted ? 'fill-current' : ''}`} />
      </button>

      {/* Image Thumbnail with Overlay */}
      <Link to={`/products/${product.id}`} className="relative aspect-[4/3] overflow-hidden bg-sand-100">
        <img
          src={product.imageUrl}
          alt={product.name}
          className="w-full h-full object-cover object-center group-hover:scale-105 transition-transform duration-500 ease-out"
          loading="lazy"
        />
        {/* Category Pill */}
        <div className="absolute bottom-3 left-3">
          <span className="px-2.5 py-1 rounded-md text-[11px] font-semibold bg-forest-950/80 text-sand-100 backdrop-blur-sm shadow-sm">
            {product.categoryName}
          </span>
        </div>
      </Link>

      {/* Content */}
      <div className="p-5 flex-1 flex flex-col justify-between">
        <div>
          {/* Vendor & Rating */}
          <div className="flex items-center justify-between text-xs text-gray-500 mb-2">
            <span className="flex items-center space-x-1 truncate max-w-[170px]" title={product.vendorName}>
              <ShieldCheck className="w-3.5 h-3.5 text-emerald-600 shrink-0" />
              <span className="truncate">{product.vendorName}</span>
            </span>
            <span className="flex items-center space-x-1 font-semibold text-gray-800 shrink-0">
              <Star className="w-3.5 h-3.5 fill-gold-500 text-gold-500" />
              <span>{product.rating}</span>
              <span className="text-gray-400 font-normal">({product.reviewCount})</span>
            </span>
          </div>

          {/* Title */}
          <Link to={`/products/${product.id}`}>
            <h3 className="font-semibold text-gray-900 text-base leading-snug group-hover:text-forest-900 transition-colors line-clamp-2 mb-2">
              {product.name}
            </h3>
          </Link>
        </div>

        {/* Pricing & Rent CTA */}
        <div className="pt-3 border-t border-gray-100 mt-4">
          <div className="flex items-baseline justify-between mb-3">
            <div>
              <span className="text-lg font-bold text-forest-900 font-display">
                {formatCurrency(product.pricePerDay)}
              </span>
              <span className="text-xs text-gray-500"> / day</span>
            </div>
            <div className="text-right">
              <span className="text-[11px] text-gray-500 block">
                Refundable Deposit
              </span>
              <span className="text-xs font-medium text-gray-700">
                {formatCurrency(product.deposit)}
              </span>
            </div>
          </div>

          <div className="grid grid-cols-2 gap-2">
            <Link
              to={`/products/${product.id}`}
              className="btn-outline text-xs py-2 px-3 text-center justify-center"
            >
              View Details
            </Link>
            <button
              onClick={handleInstantRent}
              className="btn-primary text-xs py-2 px-3 text-center justify-center flex items-center space-x-1"
            >
              <span>Rent Now</span>
              <ArrowRight className="w-3 h-3" />
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
