import React, { useState, useMemo } from 'react';
import { useSearchParams } from 'react-router-dom';
import { storageService } from '../../services/mockStorage';
import ProductCard from '../../components/product/ProductCard';
import { Filter, SlidersHorizontal, Search, RotateCcw } from 'lucide-react';
import { formatCurrency } from '../../utils/formatters';

export default function ProductListing() {
  const [searchParams, setSearchParams] = useSearchParams();
  const allProducts = storageService.getProducts();
  const categories = storageService.getCategories();

  // Extract query filters
  const categoryFilter = searchParams.get('category') || '';
  const searchFilter = searchParams.get('search') || '';

  const [selectedCategory, setSelectedCategory] = useState(categoryFilter);
  const [query, setQuery] = useState(searchFilter);
  const [maxPrice, setMaxPrice] = useState(15000);
  const [selectedCity, setSelectedCity] = useState('');
  const [sortBy, setSortBy] = useState('recommended');

  const [wishlist, setWishlist] = useState(storageService.getWishlist());

  const handleWishlistToggle = (id) => {
    const updated = storageService.toggleWishlist(id);
    setWishlist(updated);
  };

  const cities = useMemo(() => {
    const set = new Set(allProducts.map((p) => p.city).filter(Boolean));
    return Array.from(set);
  }, [allProducts]);

  // Filtered & Sorted
  const filteredProducts = useMemo(() => {
    return allProducts.filter((product) => {
      // Category match
      if (selectedCategory) {
        const cat = categories.find((c) => c.slug === selectedCategory);
        if (cat && product.categoryId !== cat.id) return false;
      }
      // Search query
      if (query.trim()) {
        const q = query.toLowerCase();
        const matchesName = product.name.toLowerCase().includes(q);
        const matchesDesc = product.description.toLowerCase().includes(q);
        const matchesVendor = product.vendorName?.toLowerCase().includes(q);
        if (!matchesName && !matchesDesc && !matchesVendor) return false;
      }
      // Max price
      if (product.pricePerDay > maxPrice) return false;
      // City
      if (selectedCity && product.city !== selectedCity) return false;

      return true;
    }).sort((a, b) => {
      if (sortBy === 'price-low') return a.pricePerDay - b.pricePerDay;
      if (sortBy === 'price-high') return b.pricePerDay - a.pricePerDay;
      if (sortBy === 'rating') return b.rating - a.rating;
      return 0; // default
    });
  }, [allProducts, selectedCategory, query, maxPrice, selectedCity, sortBy, categories]);

  const handleResetFilters = () => {
    setSelectedCategory('');
    setQuery('');
    setMaxPrice(15000);
    setSelectedCity('');
    setSortBy('recommended');
    setSearchParams({});
  };

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
      {/* Page Header */}
      <div className="flex flex-col md:flex-row md:items-end justify-between mb-8 pb-6 border-b border-gray-200 gap-4">
        <div>
          <span className="text-xs font-bold uppercase tracking-wider text-emerald-700">
            Hardware Marketplace
          </span>
          <h1 className="text-3xl font-extrabold font-display text-gray-900 mt-1">
            Browse All Commercial Rental Gear
          </h1>
          <p className="text-sm text-gray-500 mt-1">
            Showing {filteredProducts.length} verified available products
          </p>
        </div>

        {/* Sort selector */}
        <div className="flex items-center space-x-3">
          <label className="text-xs font-medium text-gray-500">Sort by:</label>
          <select
            value={sortBy}
            onChange={(e) => setSortBy(e.target.value)}
            className="px-3 py-2 rounded-xl bg-white border border-gray-200 text-sm font-medium text-gray-700 focus:outline-none focus:ring-2 focus:ring-emerald-500/20"
          >
            <option value="recommended">Featured / Recommended</option>
            <option value="price-low">Price: Low to High</option>
            <option value="price-high">Price: High to Low</option>
            <option value="rating">Highest Rated</option>
          </select>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-4 gap-8">
        {/* Sidebar Filters */}
        <aside className="lg:col-span-1 space-y-6">
          <div className="card p-6 bg-white border border-gray-100 rounded-2xl space-y-6">
            <div className="flex items-center justify-between pb-4 border-b border-gray-100">
              <span className="font-bold text-gray-900 text-sm flex items-center space-x-2">
                <SlidersHorizontal className="w-4 h-4 text-emerald-600" />
                <span>Filters</span>
              </span>
              <button
                onClick={handleResetFilters}
                className="text-xs text-gray-400 hover:text-emerald-700 flex items-center space-x-1"
              >
                <RotateCcw className="w-3 h-3" />
                <span>Reset</span>
              </button>
            </div>

            {/* Search filter */}
            <div>
              <label className="text-xs font-semibold text-gray-700 block mb-2">
                Keyword Search
              </label>
              <div className="relative">
                <input
                  type="text"
                  placeholder="e.g. Sony, Drone, PS5..."
                  value={query}
                  onChange={(e) => setQuery(e.target.value)}
                  className="input-field pl-9 text-xs"
                />
                <Search className="w-3.5 h-3.5 text-gray-400 absolute left-3 top-3.5" />
              </div>
            </div>

            {/* Category filter */}
            <div>
              <label className="text-xs font-semibold text-gray-700 block mb-2">
                Category
              </label>
              <div className="space-y-1.5">
                <button
                  onClick={() => setSelectedCategory('')}
                  className={`w-full text-left px-3 py-1.5 rounded-lg text-xs font-medium transition-colors ${
                    selectedCategory === ''
                      ? 'bg-forest-900 text-white'
                      : 'text-gray-600 hover:bg-sand-100'
                  }`}
                >
                  All Categories
                </button>
                {categories.map((c) => (
                  <button
                    key={c.id}
                    onClick={() => setSelectedCategory(c.slug)}
                    className={`w-full text-left px-3 py-1.5 rounded-lg text-xs font-medium transition-colors ${
                      selectedCategory === c.slug
                        ? 'bg-forest-900 text-white'
                        : 'text-gray-600 hover:bg-sand-100'
                    }`}
                  >
                    {c.name}
                  </button>
                ))}
              </div>
            </div>

            {/* Price slider */}
            <div>
              <div className="flex items-center justify-between text-xs font-semibold text-gray-700 mb-2">
                <span>Max Daily Rate</span>
                <span className="text-forest-900 font-bold">{formatCurrency(maxPrice)}</span>
              </div>
              <input
                type="range"
                min="500"
                max="15000"
                step="500"
                value={maxPrice}
                onChange={(e) => setMaxPrice(Number(e.target.value))}
                className="w-full accent-forest-900 cursor-pointer"
              />
              <div className="flex justify-between text-[10px] text-gray-400 mt-1">
                <span>₹500</span>
                <span>₹15,000+</span>
              </div>
            </div>

            {/* City filter */}
            <div>
              <label className="text-xs font-semibold text-gray-700 block mb-2">
                Location / City
              </label>
              <select
                value={selectedCity}
                onChange={(e) => setSelectedCity(e.target.value)}
                className="input-field text-xs cursor-pointer"
              >
                <option value="">All Cities</option>
                {cities.map((city) => (
                  <option key={city} value={city}>
                    {city}
                  </option>
                ))}
              </select>
            </div>
          </div>
        </aside>

        {/* Products Grid */}
        <main className="lg:col-span-3">
          {filteredProducts.length > 0 ? (
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
              {filteredProducts.map((product) => (
                <ProductCard
                  key={product.id}
                  product={product}
                  isWishlisted={wishlist.includes(product.id)}
                  onWishlistToggle={handleWishlistToggle}
                />
              ))}
            </div>
          ) : (
            <div className="card p-12 text-center bg-white rounded-2xl border border-gray-100">
              <Filter className="w-12 h-12 text-gray-300 mx-auto mb-4" />
              <h3 className="text-lg font-bold text-gray-800">No equipment matches your criteria</h3>
              <p className="text-xs text-gray-500 mt-1 max-w-sm mx-auto">
                Try widening your price range or clearing keyword filters to see available gear.
              </p>
              <button onClick={handleResetFilters} className="btn-primary text-xs py-2 px-4 mt-5">
                Reset All Filters
              </button>
            </div>
          )}
        </main>
      </div>
    </div>
  );
}
