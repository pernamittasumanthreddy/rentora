import React, { useState } from 'react';
import { storageService } from '../../services/mockStorage';
import { useNotification } from '../../contexts/NotificationContext';
import { formatCurrency } from '../../utils/formatters';
import { PackageCheck, Trash2, Search, ExternalLink } from 'lucide-react';
import { Link } from 'react-router-dom';

export default function ProductCatalogManagement() {
  const { addToast } = useNotification();
  const [products, setProducts] = useState(storageService.getProducts());
  const [search, setSearch] = useState('');

  const handleDelete = (id) => {
    if (window.confirm('Delete this product permanently from the platform catalog?')) {
      storageService.deleteProduct(id);
      setProducts(storageService.getProducts());
      addToast('Product delisted by Admin moderation', 'warning');
    }
  };

  const filtered = products.filter((p) =>
    p.name.toLowerCase().includes(search.toLowerCase()) ||
    p.vendorName?.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold font-display text-gray-900">
          Catalog Quality Moderation
        </h1>
        <p className="text-xs text-gray-500 mt-1">
          Review, approve, or delist equipment across all participating commercial vendors
        </p>
      </div>

      <div className="card p-4 bg-white border border-gray-100 rounded-2xl flex items-center shadow-sm">
        <Search className="w-4 h-4 text-gray-400 mr-2" />
        <input
          type="text"
          placeholder="Filter by product name, vendor, or category..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          className="w-full bg-transparent text-xs text-gray-900 focus:outline-none placeholder:text-gray-400"
        />
      </div>

      <div className="card p-6 bg-white border border-gray-100 rounded-3xl shadow-sm overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead>
              <tr className="border-b border-gray-100 text-gray-400 uppercase font-semibold text-[10px]">
                <th className="pb-3 px-3">Equipment</th>
                <th className="pb-3 px-3">Vendor</th>
                <th className="pb-3 px-3">Category</th>
                <th className="pb-3 px-3">Price / Day</th>
                <th className="pb-3 px-3">Escrow Deposit</th>
                <th className="pb-3 px-3">Rating</th>
                <th className="pb-3 px-3 text-right">Moderation</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-100">
              {filtered.map((prod) => (
                <tr key={prod.id} className="hover:bg-sand-50/60 transition-colors">
                  <td className="py-4 px-3 font-bold text-gray-900">
                    <div className="flex items-center space-x-3">
                      <img
                        src={prod.imageUrl}
                        alt=""
                        className="w-10 h-10 rounded-xl object-cover border border-gray-100 shrink-0"
                      />
                      <span className="line-clamp-1 max-w-xs">{prod.name}</span>
                    </div>
                  </td>
                  <td className="py-4 px-3 text-gray-700 font-medium">{prod.vendorName}</td>
                  <td className="py-4 px-3 text-gray-600">{prod.categoryName}</td>
                  <td className="py-4 px-3 font-bold text-forest-900">{formatCurrency(prod.pricePerDay)}</td>
                  <td className="py-4 px-3 text-emerald-700 font-semibold">{formatCurrency(prod.deposit)}</td>
                  <td className="py-4 px-3 font-semibold text-gray-800">★ {prod.rating}</td>
                  <td className="py-4 px-3 text-right space-x-2">
                    <Link
                      to={`/products/${prod.id}`}
                      target="_blank"
                      className="text-gray-500 hover:text-forest-900"
                    >
                      <ExternalLink className="w-3.5 h-3.5 inline" />
                    </Link>
                    <button
                      onClick={() => handleDelete(prod.id)}
                      className="text-rose-500 hover:text-rose-700 ml-2 font-medium"
                    >
                      Delist
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
