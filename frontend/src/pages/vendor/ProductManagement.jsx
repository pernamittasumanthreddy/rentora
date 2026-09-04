import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { storageService } from '../../services/mockStorage';
import { useNotification } from '../../contexts/NotificationContext';
import { formatCurrency } from '../../utils/formatters';
import { PlusCircle, Edit, Trash2, Layers, Search } from 'lucide-react';

export default function ProductManagement() {
  const { addToast } = useNotification();
  const [products, setProducts] = useState(
    storageService.getProducts().filter((p) => p.vendorId === 101)
  );
  const [search, setSearch] = useState('');

  const handleDelete = (id) => {
    if (window.confirm('Are you sure you want to remove this equipment from marketplace listings?')) {
      storageService.deleteProduct(id);
      setProducts(storageService.getProducts().filter((p) => p.vendorId === 101));
      addToast('Product successfully removed from listings', 'success');
    }
  };

  const filtered = products.filter((p) =>
    p.name.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="space-y-6">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h1 className="text-2xl font-bold font-display text-gray-900">
            Listed Equipment Catalog
          </h1>
          <p className="text-xs text-gray-500 mt-1">
            Manage your hardware inventory, pricing tiers, and daily rental rates
          </p>
        </div>

        <Link
          to="/vendor/products/new"
          className="btn-accent py-2.5 px-4 text-xs font-bold flex items-center space-x-2"
        >
          <PlusCircle className="w-4 h-4" />
          <span>Add New Product</span>
        </Link>
      </div>

      {/* Search strip */}
      <div className="card p-4 bg-white border border-gray-100 rounded-2xl flex items-center shadow-sm">
        <Search className="w-4 h-4 text-gray-400 mr-2" />
        <input
          type="text"
          placeholder="Filter equipment by model or keywords..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          className="w-full bg-transparent text-xs text-gray-900 focus:outline-none placeholder:text-gray-400"
        />
      </div>

      {/* Products Table */}
      <div className="card p-6 bg-white border border-gray-100 rounded-3xl shadow-sm overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead>
              <tr className="border-b border-gray-100 text-gray-400 uppercase font-semibold text-[10px]">
                <th className="pb-3 px-3">Equipment</th>
                <th className="pb-3 px-3">Category</th>
                <th className="pb-3 px-3">Rate / Day</th>
                <th className="pb-3 px-3">Escrow Deposit</th>
                <th className="pb-3 px-3">Stock Units</th>
                <th className="pb-3 px-3">Status</th>
                <th className="pb-3 px-3 text-right">Actions</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-100">
              {filtered.map((prod) => (
                <tr key={prod.id} className="hover:bg-sand-50/60 transition-colors">
                  <td className="py-4 px-3">
                    <div className="flex items-center space-x-3">
                      <img
                        src={prod.imageUrl}
                        alt=""
                        className="w-12 h-12 rounded-xl object-cover border border-gray-100 shrink-0"
                      />
                      <span className="font-bold text-gray-900 line-clamp-1 max-w-xs">{prod.name}</span>
                    </div>
                  </td>
                  <td className="py-4 px-3 text-gray-600">{prod.categoryName}</td>
                  <td className="py-4 px-3 font-bold text-forest-900">{formatCurrency(prod.pricePerDay)}</td>
                  <td className="py-4 px-3 text-emerald-700 font-semibold">{formatCurrency(prod.deposit)}</td>
                  <td className="py-4 px-3 text-gray-700 font-medium">{prod.stockCount} Units</td>
                  <td className="py-4 px-3">
                    <span className="badge-active text-[10px]">LISTED</span>
                  </td>
                  <td className="py-4 px-3 text-right space-x-2">
                    <Link
                      to={`/products/${prod.id}`}
                      className="text-gray-500 hover:text-forest-900 font-medium text-xs"
                    >
                      View
                    </Link>
                    <button
                      onClick={() => handleDelete(prod.id)}
                      className="text-rose-500 hover:text-rose-700 font-medium text-xs ml-2"
                    >
                      Delete
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
