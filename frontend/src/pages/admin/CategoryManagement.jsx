import React, { useState } from 'react';
import { storageService } from '../../services/mockStorage';
import { useNotification } from '../../contexts/NotificationContext';
import { FolderTree, Plus, Trash2 } from 'lucide-react';

export default function CategoryManagement() {
  const { addToast } = useNotification();
  const [categories, setCategories] = useState(storageService.getCategories());
  const [newCatName, setNewCatName] = useState('');
  const [newCatDesc, setNewCatDesc] = useState('');

  const handleAddCategory = (e) => {
    e.preventDefault();
    if (!newCatName.trim()) return;

    storageService.addCategory({
      name: newCatName.trim(),
      description: newCatDesc.trim() || 'High-performance commercial equipment.',
    });

    setCategories(storageService.getCategories());
    setNewCatName('');
    setNewCatDesc('');
    addToast('New product category added!', 'success');
  };

  const handleDeleteCategory = (id) => {
    if (window.confirm('Delete this equipment category?')) {
      storageService.deleteCategory(id);
      setCategories(storageService.getCategories());
      addToast('Category deleted', 'warning');
    }
  };

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold font-display text-gray-900">
          Category Hierarchy &amp; Taxonomy
        </h1>
        <p className="text-xs text-gray-500 mt-1">
          Organize equipment discovery classification across cameras, drones, audio, and tools
        </p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Add Category Form */}
        <div className="card p-6 bg-white border border-gray-100 rounded-3xl shadow-sm space-y-4">
          <h3 className="text-sm font-bold text-gray-900 flex items-center space-x-2">
            <Plus className="w-4 h-4 text-emerald-600" />
            <span>Create New Department</span>
          </h3>

          <form onSubmit={handleAddCategory} className="space-y-3 text-xs">
            <div>
              <label className="font-semibold text-gray-700 block mb-1">Category Title</label>
              <input
                type="text"
                required
                placeholder="e.g. Studio Lighting &amp; Flashes"
                value={newCatName}
                onChange={(e) => setNewCatName(e.target.value)}
                className="input-field text-xs"
              />
            </div>

            <div>
              <label className="font-semibold text-gray-700 block mb-1">Description</label>
              <textarea
                rows="3"
                placeholder="Brief summary of hardware included..."
                value={newCatDesc}
                onChange={(e) => setNewCatDesc(e.target.value)}
                className="input-field text-xs resize-none"
              />
            </div>

            <button
              type="submit"
              className="w-full btn-primary py-2.5 rounded-xl font-bold text-xs shadow-sm"
            >
              Add Department
            </button>
          </form>
        </div>

        {/* Existing Categories */}
        <div className="lg:col-span-2 card p-6 bg-white border border-gray-100 rounded-3xl shadow-sm space-y-4">
          <h3 className="text-sm font-bold text-gray-900 flex items-center space-x-2">
            <FolderTree className="w-4 h-4 text-forest-900" />
            <span>Active Categories ({categories.length})</span>
          </h3>

          <div className="space-y-3">
            {categories.map((cat) => (
              <div
                key={cat.id}
                className="p-4 rounded-2xl bg-sand-50 border border-gray-100 flex items-center justify-between text-xs"
              >
                <div>
                  <h4 className="font-bold text-gray-900 text-sm">{cat.name}</h4>
                  <p className="text-gray-500 mt-0.5">{cat.description}</p>
                  <span className="text-[10px] text-emerald-700 font-semibold mt-1 inline-block">
                    Slug: {cat.slug} • {cat.itemCount || 0} catalog items
                  </span>
                </div>
                <button
                  onClick={() => handleDeleteCategory(cat.id)}
                  className="p-2 text-rose-500 hover:text-rose-700 hover:bg-rose-50 rounded-lg transition-colors"
                  title="Delete Category"
                >
                  <Trash2 className="w-4 h-4" />
                </button>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
