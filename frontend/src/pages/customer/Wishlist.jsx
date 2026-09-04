import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { storageService } from '../../services/mockStorage';
import { useCart } from '../../contexts/CartContext';
import { formatCurrency } from '../../utils/formatters';
import { Heart, ShoppingBag, Trash2, ArrowRight } from 'lucide-react';

export default function Wishlist() {
  const navigate = useNavigate();
  const { saveCart } = useCart();
  const [wishlistIds, setWishlistIds] = useState(storageService.getWishlist());
  const allProducts = storageService.getProducts();

  const wishlistedProducts = allProducts.filter((p) => wishlistIds.includes(p.id));

  const handleRemove = (id) => {
    const updated = storageService.toggleWishlist(id);
    setWishlistIds(updated);
  };

  const handleRentNow = (product) => {
    saveCart(product);
    navigate('/checkout');
  };

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold font-display text-gray-900">
          Saved Wishlist
        </h1>
        <p className="text-xs text-gray-500 mt-1">
          Equipment saved for upcoming shoots, events, and creative projects
        </p>
      </div>

      {wishlistedProducts.length > 0 ? (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {wishlistedProducts.map((product) => (
            <div
              key={product.id}
              className="card p-4 bg-white border border-gray-100 rounded-2xl flex flex-col justify-between shadow-sm group"
            >
              <div>
                <div className="aspect-[4/3] rounded-xl overflow-hidden bg-sand-100 mb-3 relative">
                  <img
                    src={product.imageUrl}
                    alt={product.name}
                    className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300"
                  />
                  <button
                    onClick={() => handleRemove(product.id)}
                    className="absolute top-2 right-2 p-1.5 rounded-full bg-white/90 text-rose-500 hover:bg-rose-50 shadow-sm transition-all"
                    title="Remove from Wishlist"
                  >
                    <Trash2 className="w-4 h-4" />
                  </button>
                </div>

                <span className="text-[10px] font-bold text-emerald-800 bg-emerald-50 px-2 py-0.5 rounded">
                  {product.categoryName}
                </span>
                <h3 className="font-bold text-gray-900 text-sm mt-1 line-clamp-1">
                  {product.name}
                </h3>
                <p className="text-xs font-bold text-forest-900 mt-1">
                  {formatCurrency(product.pricePerDay)} / day
                </p>
              </div>

              <div className="pt-3 border-t border-gray-100 mt-4 flex space-x-2">
                <Link
                  to={`/products/${product.id}`}
                  className="btn-outline flex-1 text-xs py-2 text-center justify-center"
                >
                  View Details
                </Link>
                <button
                  onClick={() => handleRentNow(product)}
                  className="btn-primary flex-1 text-xs py-2 text-center justify-center flex items-center space-x-1"
                >
                  <span>Rent Now</span>
                  <ArrowRight className="w-3 h-3" />
                </button>
              </div>
            </div>
          ))}
        </div>
      ) : (
        <div className="card p-12 text-center bg-white rounded-2xl border border-gray-100">
          <Heart className="w-10 h-10 text-gray-300 mx-auto mb-3" />
          <p className="text-sm font-semibold text-gray-700">Your wishlist is empty</p>
          <p className="text-xs text-gray-400 mt-1">Save gear as you browse to easily book when needed.</p>
          <Link to="/products" className="btn-primary text-xs py-2 px-4 mt-4 inline-block">
            Explore Equipment
          </Link>
        </div>
      )}
    </div>
  );
}
