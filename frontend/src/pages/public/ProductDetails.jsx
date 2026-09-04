import React, { useState } from 'react';
import { useParams, Link, useNavigate } from 'react-router-dom';
import { storageService } from '../../services/mockStorage';
import { useCart } from '../../contexts/CartContext';
import { formatCurrency, calculateDaysBetween, calculateRentalPricing } from '../../utils/formatters';
import {
  Star,
  ShieldCheck,
  Truck,
  CheckCircle,
  Calendar,
  Heart,
  Share2,
  ChevronRight,
  Package,
  Clock,
  ArrowRight,
} from 'lucide-react';

export default function ProductDetails() {
  const { id } = useParams();
  const navigate = useNavigate();
  const { saveCart } = useCart();
  const product = storageService.getProductById(id);

  const [activeImage, setActiveImage] = useState(0);
  const [startDate, setStartDate] = useState(
    new Date(Date.now() + 86400000).toISOString().split('T')[0]
  );
  const [endDate, setEndDate] = useState(
    new Date(Date.now() + 86400000 * 4).toISOString().split('T')[0]
  );
  const [deliveryOption, setDeliveryOption] = useState('DELIVERY');

  const [wishlist, setWishlist] = useState(storageService.getWishlist());
  const isWishlisted = product ? wishlist.includes(product.id) : false;

  const handleWishlistToggle = () => {
    if (!product) return;
    const updated = storageService.toggleWishlist(product.id);
    setWishlist(updated);
  };

  if (!product) {
    return (
      <div className="max-w-7xl mx-auto px-4 py-20 text-center">
        <h2 className="text-2xl font-bold text-gray-800">Product Not Found</h2>
        <p className="text-sm text-gray-500 mt-2">The requested rental unit does not exist or has been retired.</p>
        <Link to="/products" className="btn-primary text-xs py-2 px-4 mt-6 inline-block">
          Back to Catalog
        </Link>
      </div>
    );
  }

  const gallery = product.gallery && product.gallery.length > 0 ? product.gallery : [product.imageUrl];
  const days = calculateDaysBetween(startDate, endDate);
  const pricing = calculateRentalPricing(product.pricePerDay, product.deposit, days);

  const reviews = storageService.getReviews().filter((r) => r.productId === product.id);
  const relatedProducts = storageService
    .getProducts()
    .filter((p) => p.categoryId === product.categoryId && p.id !== product.id)
    .slice(0, 3);

  const handleBookNow = () => {
    saveCart(product, { startDate, endDate }, deliveryOption);
    navigate('/checkout');
  };

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10 space-y-12">
      {/* Breadcrumb */}
      <nav className="flex items-center space-x-2 text-xs text-gray-500">
        <Link to="/" className="hover:text-forest-900">Home</Link>
        <ChevronRight className="w-3.5 h-3.5" />
        <Link to="/products" className="hover:text-forest-900">Catalog</Link>
        <ChevronRight className="w-3.5 h-3.5" />
        <span className="text-gray-900 font-medium truncate max-w-xs">{product.name}</span>
      </nav>

      <div className="grid grid-cols-1 lg:grid-cols-12 gap-10">
        {/* Left Column: Image Gallery & Description (7 cols) */}
        <div className="lg:col-span-7 space-y-8">
          {/* Gallery */}
          <div className="space-y-4">
            <div className="aspect-[4/3] rounded-3xl overflow-hidden bg-sand-200 border border-gray-100 shadow-sm">
              <img
                src={gallery[activeImage]}
                alt={product.name}
                className="w-full h-full object-cover"
              />
            </div>
            {gallery.length > 1 && (
              <div className="flex space-x-3">
                {gallery.map((img, idx) => (
                  <button
                    key={idx}
                    onClick={() => setActiveImage(idx)}
                    className={`w-20 h-16 rounded-xl overflow-hidden border-2 transition-all ${
                      activeImage === idx ? 'border-forest-900 ring-2 ring-forest-900/20' : 'border-transparent opacity-70 hover:opacity-100'
                    }`}
                  >
                    <img src={img} alt="" className="w-full h-full object-cover" />
                  </button>
                ))}
              </div>
            )}
          </div>

          {/* Overview & Specs */}
          <div className="space-y-6">
            <div>
              <div className="flex items-center space-x-2 text-xs text-emerald-800 font-semibold mb-2">
                <span className="bg-emerald-100 px-2.5 py-0.5 rounded-full">
                  {product.categoryName}
                </span>
                <span>•</span>
                <span>In Stock: {product.stockCount} Units</span>
              </div>
              <h1 className="text-3xl font-extrabold font-display text-gray-900 tracking-tight">
                {product.name}
              </h1>
              <div className="flex items-center space-x-4 mt-3 text-sm text-gray-600">
                <div className="flex items-center space-x-1 font-semibold text-gray-900">
                  <Star className="w-4 h-4 fill-gold-500 text-gold-500" />
                  <span>{product.rating}</span>
                  <span className="text-gray-400 font-normal">({product.reviewCount} reviews)</span>
                </div>
                <span>•</span>
                <span className="flex items-center space-x-1">
                  <Truck className="w-4 h-4 text-gray-400" />
                  <span>{product.city} Hub Dispatch</span>
                </span>
              </div>
            </div>

            {/* Description */}
            <div>
              <h3 className="text-sm font-bold uppercase tracking-wider text-gray-700 mb-2">
                Equipment Description
              </h3>
              <p className="text-sm text-gray-600 leading-relaxed">
                {product.description}
              </p>
            </div>

            {/* Features */}
            {product.features && (
              <div>
                <h3 className="text-sm font-bold uppercase tracking-wider text-gray-700 mb-3">
                  Key Technical Features
                </h3>
                <ul className="grid grid-cols-1 sm:grid-cols-2 gap-2.5 text-xs text-gray-700">
                  {product.features.map((feat, i) => (
                    <li key={i} className="flex items-start space-x-2">
                      <CheckCircle className="w-4 h-4 text-emerald-600 shrink-0 mt-0.5" />
                      <span>{feat}</span>
                    </li>
                  ))}
                </ul>
              </div>
            )}

            {/* Kit inclusions */}
            {product.includes && (
              <div className="bg-sand-50 p-5 rounded-2xl border border-gray-200/80">
                <h3 className="text-xs font-bold uppercase tracking-wider text-gray-700 mb-2 flex items-center space-x-1.5">
                  <Package className="w-4 h-4 text-forest-900" />
                  <span>Package Contents (Included in Rental Kit)</span>
                </h3>
                <div className="flex flex-wrap gap-2 mt-2">
                  {product.includes.map((item, i) => (
                    <span
                      key={i}
                      className="px-2.5 py-1 rounded-md text-xs font-medium bg-white text-gray-800 border border-gray-200"
                    >
                      {item}
                    </span>
                  ))}
                </div>
              </div>
            )}
          </div>
        </div>

        {/* Right Column: Dynamic Booking Card (5 cols) */}
        <div className="lg:col-span-5">
          <div className="sticky top-28 card p-6 sm:p-8 bg-white border border-gray-100 shadow-xl rounded-3xl space-y-6">
            <div className="flex items-baseline justify-between pb-4 border-b border-gray-100">
              <div>
                <span className="text-3xl font-extrabold font-display text-forest-900">
                  {formatCurrency(product.pricePerDay)}
                </span>
                <span className="text-xs text-gray-500"> / day</span>
              </div>
              <button
                onClick={handleWishlistToggle}
                className={`p-2.5 rounded-full border transition-all ${
                  isWishlisted ? 'border-rose-300 bg-rose-50 text-rose-600' : 'border-gray-200 text-gray-400 hover:text-rose-500'
                }`}
                title="Save to Wishlist"
              >
                <Heart className={`w-4 h-4 ${isWishlisted ? 'fill-current' : ''}`} />
              </button>
            </div>

            {/* Date Pickers */}
            <div className="space-y-3">
              <label className="text-xs font-semibold text-gray-700 block">
                Rental Duration Dates
              </label>
              <div className="grid grid-cols-2 gap-3">
                <div>
                  <span className="text-[11px] text-gray-500 block mb-1">Pickup Date</span>
                  <input
                    type="date"
                    value={startDate}
                    min={new Date().toISOString().split('T')[0]}
                    onChange={(e) => setStartDate(e.target.value)}
                    className="input-field text-xs cursor-pointer"
                  />
                </div>
                <div>
                  <span className="text-[11px] text-gray-500 block mb-1">Return Date</span>
                  <input
                    type="date"
                    value={endDate}
                    min={startDate}
                    onChange={(e) => setEndDate(e.target.value)}
                    className="input-field text-xs cursor-pointer"
                  />
                </div>
              </div>
              <p className="text-[11px] text-emerald-800 font-medium bg-emerald-50 px-3 py-1.5 rounded-lg flex items-center justify-between">
                <span>Selected: {days} {days === 1 ? 'day' : 'days'}</span>
                <span>Available for immediate dispatch</span>
              </p>
            </div>

            {/* Delivery option */}
            <div>
              <label className="text-xs font-semibold text-gray-700 block mb-2">
                Fulfillment Mode
              </label>
              <div className="grid grid-cols-2 gap-3">
                <button
                  type="button"
                  onClick={() => setDeliveryOption('DELIVERY')}
                  className={`p-3 rounded-xl border text-left text-xs font-medium transition-all ${
                    deliveryOption === 'DELIVERY'
                      ? 'border-forest-900 bg-forest-50/50 text-forest-900 ring-1 ring-forest-900'
                      : 'border-gray-200 text-gray-600 hover:bg-sand-50'
                  }`}
                >
                  <span className="font-bold block">Doorstep Delivery</span>
                  <span className="text-[10px] text-gray-500">Scheduled courier</span>
                </button>
                <button
                  type="button"
                  onClick={() => setDeliveryOption('PICKUP')}
                  className={`p-3 rounded-xl border text-left text-xs font-medium transition-all ${
                    deliveryOption === 'PICKUP'
                      ? 'border-forest-900 bg-forest-50/50 text-forest-900 ring-1 ring-forest-900'
                      : 'border-gray-200 text-gray-600 hover:bg-sand-50'
                  }`}
                >
                  <span className="font-bold block">Self Hub Pickup</span>
                  <span className="text-[10px] text-gray-500">{product.city} Center</span>
                </button>
              </div>
            </div>

            {/* Price calculation sheet */}
            <div className="bg-sand-50 p-4 rounded-2xl space-y-2 text-xs border border-gray-100">
              <div className="flex justify-between text-gray-600">
                <span>Rental ({formatCurrency(product.pricePerDay)} × {days} days)</span>
                <span className="font-semibold text-gray-900">{formatCurrency(pricing.rentalFee)}</span>
              </div>
              <div className="flex justify-between text-gray-600">
                <span>GST (9% CGST + 9% SGST)</span>
                <span className="font-semibold text-gray-900">{formatCurrency(pricing.totalGst)}</span>
              </div>
              <div className="flex justify-between text-gray-600 border-t border-gray-200/60 pt-2">
                <span>Refundable Escrow Deposit</span>
                <span className="font-semibold text-gray-900">{formatCurrency(pricing.deposit)}</span>
              </div>
              <p className="text-[10px] text-gray-400">
                *Deposit is 100% refunded to your account upon return inspection.
              </p>
              <div className="flex justify-between text-sm font-bold text-gray-900 border-t border-gray-200 pt-3">
                <span>Total Payable Now</span>
                <span className="text-forest-900 font-display text-base">
                  {formatCurrency(pricing.totalPayable)}
                </span>
              </div>
            </div>

            {/* Book Now Button */}
            <button
              onClick={handleBookNow}
              className="w-full btn-primary py-3.5 rounded-xl font-bold flex items-center justify-center space-x-2 text-sm shadow-md"
            >
              <span>Proceed to Checkout</span>
              <ArrowRight className="w-4 h-4" />
            </button>

            {/* Vendor Details badge */}
            <div className="pt-4 border-t border-gray-100 flex items-center justify-between text-xs">
              <div className="flex items-center space-x-2">
                <ShieldCheck className="w-5 h-5 text-emerald-600 shrink-0" />
                <div>
                  <p className="font-semibold text-gray-900">{product.vendorName}</p>
                  <p className="text-gray-400 text-[10px]">Verified Platform Vendor</p>
                </div>
              </div>
              <span className="font-bold text-emerald-800 bg-emerald-50 px-2 py-1 rounded">
                ★ {product.vendorRating}
              </span>
            </div>
          </div>
        </div>
      </div>

      {/* Customer Reviews Section */}
      <section className="pt-10 border-t border-gray-200">
        <h2 className="text-2xl font-bold font-display text-gray-900 mb-6">
          Verified Renter Reviews ({reviews.length})
        </h2>

        {reviews.length > 0 ? (
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {reviews.map((rev) => (
              <div key={rev.id} className="card p-6 bg-white border border-gray-100 rounded-2xl space-y-3">
                <div className="flex items-center justify-between">
                  <div className="flex items-center space-x-3">
                    <img
                      src={rev.customerAvatar}
                      alt={rev.customerName}
                      className="w-9 h-9 rounded-full object-cover"
                    />
                    <div>
                      <p className="text-sm font-semibold text-gray-900">{rev.customerName}</p>
                      <p className="text-[11px] text-gray-400">{rev.date}</p>
                    </div>
                  </div>
                  <div className="flex text-gold-500">
                    {Array.from({ length: rev.rating }).map((_, i) => (
                      <Star key={i} className="w-3.5 h-3.5 fill-current" />
                    ))}
                  </div>
                </div>
                <p className="text-xs text-gray-600 leading-relaxed">{rev.comment}</p>
              </div>
            ))}
          </div>
        ) : (
          <p className="text-xs text-gray-400 italic">No reviews yet for this model.</p>
        )}
      </section>

      {/* Related Products */}
      {relatedProducts.length > 0 && (
        <section className="pt-10 border-t border-gray-200">
          <h2 className="text-xl font-bold font-display text-gray-900 mb-6">
            Similar Gear in {product.categoryName}
          </h2>
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-6">
            {relatedProducts.map((p) => (
              <Link
                key={p.id}
                to={`/products/${p.id}`}
                className="card-hover p-4 bg-white rounded-2xl border border-gray-100 flex items-center space-x-4"
              >
                <img src={p.imageUrl} alt={p.name} className="w-16 h-16 rounded-xl object-cover" />
                <div>
                  <h4 className="text-xs font-bold text-gray-900 line-clamp-1">{p.name}</h4>
                  <p className="text-xs font-bold text-forest-900 mt-1">{formatCurrency(p.pricePerDay)}/day</p>
                </div>
              </Link>
            ))}
          </div>
        </section>
      )}
    </div>
  );
}
