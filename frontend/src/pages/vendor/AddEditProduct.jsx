import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { storageService } from '../../services/mockStorage';
import { useNotification } from '../../contexts/NotificationContext';
import { useAuth } from '../../contexts/AuthContext';
import { PlusCircle, ArrowLeft, Image as ImageIcon, Sparkles } from 'lucide-react';

export default function AddEditProduct() {
  const navigate = useNavigate();
  const { user } = useAuth();
  const { addToast } = useNotification();
  const categories = storageService.getCategories();

  const [name, setName] = useState('');
  const [categoryId, setCategoryId] = useState(1);
  const [pricePerDay, setPricePerDay] = useState(2500);
  const [deposit, setDeposit] = useState(8000);
  const [stockCount, setStockCount] = useState(2);
  const [description, setDescription] = useState('');
  const [imageUrl, setImageUrl] = useState(
    'https://images.unsplash.com/photo-1516035069371-29a1b244cc32?auto=format&fit=crop&w=900&q=80'
  );

  const handleSubmit = (e) => {
    e.preventDefault();
    const category = categories.find((c) => c.id === Number(categoryId));

    storageService.addProduct({
      name,
      categoryId: Number(categoryId),
      categoryName: category ? category.name : 'Cameras & Gear',
      vendorId: 101,
      vendorName: user?.businessName || 'Apex Cine Rentals',
      vendorRating: 4.9,
      pricePerDay: Number(pricePerDay),
      deposit: Number(deposit),
      stockCount: Number(stockCount),
      description,
      imageUrl,
      city: user?.city || 'Bengaluru',
      features: ['Factory calibrated', 'Includes hard transport case', 'Fully tested before dispatch'],
    });

    addToast('Product successfully published to the Rentora catalog!', 'success');
    navigate('/vendor/products');
  };

  return (
    <div className="max-w-3xl space-y-6">
      <div>
        <button
          onClick={() => navigate('/vendor/products')}
          className="text-xs text-gray-500 hover:text-forest-900 inline-flex items-center space-x-1 mb-2"
        >
          <ArrowLeft className="w-3 h-3" />
          <span>Back to Product List</span>
        </button>
        <h1 className="text-2xl font-bold font-display text-gray-900">
          List New Rental Equipment
        </h1>
        <p className="text-xs text-gray-500 mt-1">
          Publish cinema gear, drones, gaming systems, or power tools to verified renters
        </p>
      </div>

      <form onSubmit={handleSubmit} className="card p-8 bg-white border border-gray-100 rounded-3xl shadow-sm space-y-6 text-xs">
        <div>
          <label className="font-semibold text-gray-700 block mb-1">Equipment Name / Model</label>
          <input
            type="text"
            required
            placeholder="e.g. Canon EOS R5 C Cinema Mirrorless Camera"
            value={name}
            onChange={(e) => setName(e.target.value)}
            className="input-field text-xs"
          />
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div>
            <label className="font-semibold text-gray-700 block mb-1">Equipment Category</label>
            <select
              value={categoryId}
              onChange={(e) => setCategoryId(e.target.value)}
              className="input-field text-xs cursor-pointer"
            >
              {categories.map((c) => (
                <option key={c.id} value={c.id}>
                  {c.name}
                </option>
              ))}
            </select>
          </div>

          <div>
            <label className="font-semibold text-gray-700 block mb-1">Available Fleet Stock</label>
            <input
              type="number"
              min="1"
              max="50"
              value={stockCount}
              onChange={(e) => setStockCount(e.target.value)}
              className="input-field text-xs"
            />
          </div>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div>
            <label className="font-semibold text-gray-700 block mb-1">Daily Rental Price (₹ / Day)</label>
            <input
              type="number"
              min="100"
              step="50"
              value={pricePerDay}
              onChange={(e) => setPricePerDay(e.target.value)}
              className="input-field text-xs"
            />
          </div>

          <div>
            <label className="font-semibold text-gray-700 block mb-1">Refundable Escrow Deposit (₹)</label>
            <input
              type="number"
              min="500"
              step="100"
              value={deposit}
              onChange={(e) => setDeposit(e.target.value)}
              className="input-field text-xs"
            />
          </div>
        </div>

        <div>
          <label className="font-semibold text-gray-700 block mb-1">Equipment Description &amp; Condition</label>
          <textarea
            rows="3"
            required
            placeholder="Provide condition details, sensor specifications, inclusions, and best use cases..."
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            className="input-field text-xs resize-none"
          />
        </div>

        <div>
          <label className="font-semibold text-gray-700 block mb-1">High-Resolution Photo URL</label>
          <input
            type="url"
            required
            value={imageUrl}
            onChange={(e) => setImageUrl(e.target.value)}
            className="input-field text-xs"
          />
          {imageUrl && (
            <div className="mt-3 flex items-center space-x-3 p-3 bg-sand-50 rounded-2xl border border-gray-100">
              <img src={imageUrl} alt="" className="w-14 h-14 rounded-xl object-cover border border-gray-200" />
              <span className="text-[11px] text-gray-500">Image Preview Verified</span>
            </div>
          )}
        </div>

        <div className="pt-4 flex justify-end space-x-3">
          <button
            type="button"
            onClick={() => navigate('/vendor/products')}
            className="btn-outline text-xs py-2 px-4"
          >
            Cancel
          </button>
          <button
            type="submit"
            className="btn-accent text-xs py-2 px-6 font-bold flex items-center space-x-2"
          >
            <Sparkles className="w-4 h-4" />
            <span>Publish to Marketplace</span>
          </button>
        </div>
      </form>
    </div>
  );
}
