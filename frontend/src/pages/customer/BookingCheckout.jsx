import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { useCart } from '../../contexts/CartContext';
import { useAuth } from '../../contexts/AuthContext';
import { useNotification } from '../../contexts/NotificationContext';
import { storageService } from '../../services/mockStorage';
import { formatCurrency, formatDate } from '../../utils/formatters';
import {
  ShieldCheck,
  CheckCircle2,
  Truck,
  CreditCard,
  QrCode,
  Lock,
  ArrowRight,
  Package,
} from 'lucide-react';

export default function BookingCheckout() {
  const { cartItem, rentalDates, deliveryOption, pricing, days, clearCart } = useCart();
  const { user } = useAuth();
  const { addToast } = useNotification();
  const navigate = useNavigate();

  const [paymentMethod, setPaymentMethod] = useState('UPI');
  const [address, setAddress] = useState(
    user?.address || 'Flat 402, Green Glen Layout, Bellandur, Bengaluru 560103'
  );
  const [processing, setProcessing] = useState(false);
  const [confirmedOrder, setConfirmedOrder] = useState(null);

  // If no cart item, redirect to products
  if (!cartItem && !confirmedOrder) {
    return (
      <div className="max-w-4xl mx-auto px-4 py-20 text-center">
        <Package className="w-12 h-12 text-gray-300 mx-auto mb-4" />
        <h2 className="text-xl font-bold text-gray-800">No Item Selected for Booking</h2>
        <p className="text-xs text-gray-500 mt-1">Please select an equipment from the catalog to book.</p>
        <Link to="/products" className="btn-primary text-xs py-2 px-4 mt-6 inline-block">
          Browse Equipment Catalog
        </Link>
      </div>
    );
  }

  const handlePayAndConfirm = (e) => {
    e.preventDefault();
    setProcessing(true);

    setTimeout(() => {
      const newRental = storageService.createRental({
        customerId: user?.id || 1,
        customerName: user?.name || 'Rahul Sharma',
        customerEmail: user?.email || 'customer@rentora.in',
        productId: cartItem.id,
        productName: cartItem.name,
        productImage: cartItem.imageUrl,
        vendorId: cartItem.vendorId,
        vendorName: cartItem.vendorName,
        startDate: rentalDates.startDate,
        endDate: rentalDates.endDate,
        rentalDays: days,
        dailyRate: cartItem.pricePerDay,
        rentalFee: pricing.rentalFee,
        deposit: pricing.deposit,
        tax: pricing.totalGst,
        totalAmount: pricing.totalPayable,
        deliveryAddress: address,
        paymentMethod: paymentMethod === 'UPI' ? 'UPI / NetBanking' : 'Credit Card (Visa)',
      });

      setConfirmedOrder(newRental);
      clearCart();
      setProcessing(false);
      addToast('Order confirmed! Security deposit successfully locked in Escrow.', 'success');
    }, 1200);
  };

  // 1. ORDER CONFIRMATION VIEW
  if (confirmedOrder) {
    return (
      <div className="max-w-2xl mx-auto py-12 px-4 space-y-8">
        <div className="card p-8 bg-white border border-gray-100 rounded-3xl shadow-xl text-center space-y-5">
          <div className="w-16 h-16 rounded-full bg-emerald-100 text-emerald-700 flex items-center justify-center mx-auto">
            <CheckCircle2 className="w-10 h-10" />
          </div>

          <div>
            <span className="text-xs font-bold uppercase tracking-wider text-emerald-800 bg-emerald-50 px-3 py-1 rounded-full">
              Booking Confirmed
            </span>
            <h1 className="text-2xl sm:text-3xl font-extrabold font-display text-gray-900 mt-3">
              Your Rental is Locked &amp; Scheduled!
            </h1>
            <p className="text-xs text-gray-500 mt-1">
              Order ID: <strong>#{confirmedOrder.id}</strong> • Tracking: <strong>{confirmedOrder.trackingNumber}</strong>
            </p>
          </div>

          <div className="bg-sand-50 p-5 rounded-2xl text-left text-xs space-y-2 border border-gray-100">
            <div className="flex justify-between">
              <span className="text-gray-500">Equipment:</span>
              <span className="font-bold text-gray-900">{confirmedOrder.productName}</span>
            </div>
            <div className="flex justify-between">
              <span className="text-gray-500">Rental Period:</span>
              <span className="font-bold text-gray-900">
                {formatDate(confirmedOrder.startDate)} to {formatDate(confirmedOrder.endDate)} ({confirmedOrder.rentalDays} Days)
              </span>
            </div>
            <div className="flex justify-between">
              <span className="text-gray-500">Fulfillment Hub:</span>
              <span className="font-bold text-gray-900">{confirmedOrder.vendorName}</span>
            </div>
            <div className="flex justify-between border-t border-gray-200/60 pt-2">
              <span className="text-gray-500">Total Charged:</span>
              <span className="font-bold text-gray-900">{formatCurrency(confirmedOrder.totalAmount)}</span>
            </div>
            <div className="flex justify-between text-emerald-800 font-semibold">
              <span>Deposit Held in Escrow:</span>
              <span>{formatCurrency(confirmedOrder.deposit)}</span>
            </div>
          </div>

          <div className="flex flex-col sm:flex-row gap-3 pt-2">
            <Link
              to="/customer/rentals"
              className="btn-primary flex-1 py-3 text-xs font-bold text-center justify-center"
            >
              View in My Rentals
            </Link>
            <Link
              to="/products"
              className="btn-outline flex-1 py-3 text-xs font-bold text-center justify-center"
            >
              Back to Catalog
            </Link>
          </div>
        </div>
      </div>
    );
  }

  // 2. CHECKOUT FLOW VIEW
  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
      <div className="mb-8">
        <h1 className="text-2xl font-bold font-display text-gray-900">
          Complete Your Equipment Booking
        </h1>
        <p className="text-xs text-gray-500 mt-1">
          Review dispatch address, rental duration, and authorize secure escrow payment
        </p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-12 gap-10">
        {/* Left Form: Delivery & Payment (7 cols) */}
        <div className="lg:col-span-7 space-y-6">
          {/* Dispatch Details */}
          <div className="card p-6 bg-white border border-gray-100 rounded-3xl space-y-4 shadow-sm">
            <h3 className="text-sm font-bold text-gray-900 flex items-center space-x-2">
              <Truck className="w-4 h-4 text-emerald-600" />
              <span>Fulfillment &amp; Delivery Destination</span>
            </h3>

            <div>
              <label className="text-xs font-semibold text-gray-700 block mb-1">
                {deliveryOption === 'DELIVERY' ? 'Doorstep Delivery Address' : 'Self-Pickup Confirmation'}
              </label>
              <textarea
                rows="2"
                value={address}
                onChange={(e) => setAddress(e.target.value)}
                className="input-field text-xs resize-none"
                placeholder="Enter complete street address, PIN code, and contact person"
              />
              <p className="text-[10px] text-gray-400 mt-1">
                Deliveries are handed over with a secure 6-digit one-time passcode verification.
              </p>
            </div>
          </div>

          {/* Payment Method Selector */}
          <div className="card p-6 bg-white border border-gray-100 rounded-3xl space-y-4 shadow-sm">
            <h3 className="text-sm font-bold text-gray-900 flex items-center space-x-2">
              <CreditCard className="w-4 h-4 text-gold-600" />
              <span>Simulated Payment Gateway</span>
            </h3>

            <div className="grid grid-cols-2 gap-3">
              <button
                type="button"
                onClick={() => setPaymentMethod('UPI')}
                className={`p-4 rounded-2xl border text-left transition-all flex items-center space-x-3 ${
                  paymentMethod === 'UPI'
                    ? 'border-forest-900 bg-forest-50/60 ring-2 ring-forest-900/20'
                    : 'border-gray-200 hover:bg-sand-50'
                }`}
              >
                <QrCode className="w-5 h-5 text-emerald-700 shrink-0" />
                <div>
                  <span className="text-xs font-bold block text-gray-900">Instant UPI</span>
                  <span className="text-[10px] text-gray-400">GPay, PhonePe, Paytm</span>
                </div>
              </button>

              <button
                type="button"
                onClick={() => setPaymentMethod('CARD')}
                className={`p-4 rounded-2xl border text-left transition-all flex items-center space-x-3 ${
                  paymentMethod === 'CARD'
                    ? 'border-forest-900 bg-forest-50/60 ring-2 ring-forest-900/20'
                    : 'border-gray-200 hover:bg-sand-50'
                }`}
              >
                <CreditCard className="w-5 h-5 text-forest-900 shrink-0" />
                <div>
                  <span className="text-xs font-bold block text-gray-900">Credit / Debit Card</span>
                  <span className="text-[10px] text-gray-400">Visa, Mastercard, RuPay</span>
                </div>
              </button>
            </div>

            <div className="bg-emerald-50 p-4 rounded-2xl border border-emerald-100 flex items-center space-x-3 text-xs text-emerald-950">
              <ShieldCheck className="w-6 h-6 text-emerald-600 shrink-0" />
              <div>
                <span className="font-bold block">100% Escrow Deposit Safeguard</span>
                <span className="text-[11px] text-emerald-800">
                  Your deposit of {formatCurrency(pricing?.deposit)} is held securely in trust and automatically refunded once equipment is returned.
                </span>
              </div>
            </div>
          </div>
        </div>

        {/* Right Summary Sheet (5 cols) */}
        <div className="lg:col-span-5 space-y-6">
          <div className="card p-6 sm:p-8 bg-white border border-gray-100 rounded-3xl shadow-lg space-y-6">
            <h3 className="text-sm font-bold text-gray-900 pb-3 border-b border-gray-100">
              Order Summary
            </h3>

            {/* Item detail */}
            <div className="flex items-center space-x-4">
              <img
                src={cartItem.imageUrl}
                alt={cartItem.name}
                className="w-16 h-16 rounded-2xl object-cover border border-gray-100 shrink-0"
              />
              <div className="overflow-hidden">
                <h4 className="font-bold text-gray-900 text-sm truncate">{cartItem.name}</h4>
                <p className="text-xs text-gray-500 mt-0.5">
                  Vendor: <strong>{cartItem.vendorName}</strong>
                </p>
                <p className="text-xs text-forest-900 font-semibold mt-0.5">
                  {formatCurrency(cartItem.pricePerDay)} × {days} days
                </p>
              </div>
            </div>

            {/* Dates */}
            <div className="bg-sand-50 p-3.5 rounded-2xl text-xs space-y-1">
              <div className="flex justify-between text-gray-600">
                <span>Start / Handover:</span>
                <strong className="text-gray-900">{formatDate(rentalDates.startDate)}</strong>
              </div>
              <div className="flex justify-between text-gray-600">
                <span>Expected Return:</span>
                <strong className="text-gray-900">{formatDate(rentalDates.endDate)}</strong>
              </div>
            </div>

            {/* Invoice Breakdown */}
            <div className="space-y-2 text-xs border-t border-gray-100 pt-4">
              <div className="flex justify-between text-gray-600">
                <span>Base Rental Fee</span>
                <span className="font-semibold text-gray-900">{formatCurrency(pricing?.rentalFee)}</span>
              </div>
              <div className="flex justify-between text-gray-600">
                <span>GST (9% CGST + 9% SGST)</span>
                <span className="font-semibold text-gray-900">{formatCurrency(pricing?.totalGst)}</span>
              </div>
              <div className="flex justify-between text-gray-600 border-t border-gray-100 pt-2">
                <span>Refundable Escrow Deposit</span>
                <span className="font-semibold text-emerald-700">{formatCurrency(pricing?.deposit)}</span>
              </div>
              <div className="flex justify-between text-base font-bold text-gray-900 border-t border-gray-200 pt-3">
                <span>Total Payable Now</span>
                <span className="text-forest-900 font-display text-lg">
                  {formatCurrency(pricing?.totalPayable)}
                </span>
              </div>
            </div>

            {/* Submit Button */}
            <button
              onClick={handlePayAndConfirm}
              disabled={processing}
              className="w-full btn-primary py-3.5 rounded-xl font-bold flex items-center justify-center space-x-2 text-sm shadow-md"
            >
              <Lock className="w-4 h-4 text-gold-400" />
              <span>{processing ? 'Processing Escrow Payment...' : 'Pay & Confirm Rental'}</span>
              <ArrowRight className="w-4 h-4" />
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
