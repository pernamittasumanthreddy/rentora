import React, { useState, useEffect, useMemo, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import { motion, AnimatePresence } from 'framer-motion';
import {
  Search,
  MapPin,
  Calendar,
  Home,
  Car,
  Camera,
  Building2,
  SlidersHorizontal,
  ArrowRight,
  Star,
  CheckCircle2,
  ShieldCheck,
  Sparkles,
  X,
  Loader2,
} from 'lucide-react';
import { storageService } from '../../services/mockStorage';

const CATEGORY_TABS = [
  {
    id: 'properties',
    label: 'Properties',
    sublabel: 'Bungalows & Villas',
    icon: Home,
    filterCategoryIds: [9],
    defaultPlaceholder: 'Search Portuguese bungalows, mountain chalets, tea estates...',
    quickLocations: ['Goa', 'Manali', 'Alibaug', 'Coorg', 'Udaipur'],
  },
  {
    id: 'vehicles',
    label: 'Vehicles',
    sublabel: 'Cars & Superbikes',
    icon: Car,
    filterCategoryIds: [7, 8],
    defaultPlaceholder: 'Search 4x4 SUVs, luxury sedans, BMW GS, Panigale...',
    quickLocations: ['Bengaluru', 'Mumbai', 'Chennai', 'Delhi', 'Hyderabad'],
  },
  {
    id: 'equipment',
    label: 'Equipment',
    sublabel: 'Cinema, Drones & Tools',
    icon: Camera,
    filterCategoryIds: [1, 2, 3, 4, 5, 6],
    defaultPlaceholder: 'Search Sony FX6, RED, DJI Mavic 3 Pro, Sennheiser...',
    quickLocations: ['Mumbai', 'Bengaluru', 'Chennai', 'Hyderabad'],
  },
  {
    id: 'spaces',
    label: 'Spaces',
    sublabel: 'Studios & Venues',
    icon: Building2,
    filterCategoryIds: [10],
    defaultPlaceholder: 'Search cyclorama studios, film stages, botanical venues...',
    quickLocations: ['Bengaluru', 'Mumbai', 'Delhi NCR', 'Hyderabad'],
  },
];

export default function FloatingRentalSearch() {
  const navigate = useNavigate();
  const [activeTab, setActiveTab] = useState('properties');
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedLocation, setSelectedLocation] = useState('');
  const [dateRange, setDateRange] = useState('Weekend Escape (3 Days)');
  const [filterTag, setFilterTag] = useState('all'); // 'all', 'instant', 'escrow'
  const [isLoading, setIsLoading] = useState(false);
  const [showLiveDropdown, setShowLiveDropdown] = useState(false);
  const dropdownRef = useRef(null);

  const allProducts = useMemo(() => storageService.getProducts(), []);

  const activeTabConfig = useMemo(
    () => CATEGORY_TABS.find((t) => t.id === activeTab) || CATEGORY_TABS[0],
    [activeTab]
  );

  // Dynamic live search results with simulated debounce spinner
  const [liveResults, setLiveResults] = useState([]);

  useEffect(() => {
    setIsLoading(true);
    const timer = setTimeout(() => {
      let filtered = allProducts.filter((p) =>
        activeTabConfig.filterCategoryIds.includes(p.categoryId)
      );

      if (searchQuery.trim()) {
        const q = searchQuery.toLowerCase();
        filtered = filtered.filter(
          (p) =>
            p.name.toLowerCase().includes(q) ||
            p.description.toLowerCase().includes(q) ||
            (p.city && p.city.toLowerCase().includes(q))
        );
      }

      if (selectedLocation) {
        filtered = filtered.filter(
          (p) => p.city && p.city.toLowerCase() === selectedLocation.toLowerCase()
        );
      }

      setLiveResults(filtered.slice(0, 4));
      setIsLoading(false);
    }, 280);

    return () => clearTimeout(timer);
  }, [activeTab, searchQuery, selectedLocation, activeTabConfig, allProducts]);

  // Handle outside click to close live dropdown
  useEffect(() => {
    const handleClickOutside = (event) => {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
        setShowLiveDropdown(false);
      }
    };
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  const handleSearchSubmit = (e) => {
    if (e) e.preventDefault();
    setIsLoading(true);

    setTimeout(() => {
      setIsLoading(false);
      const params = new URLSearchParams();
      if (searchQuery) params.append('search', searchQuery);
      if (selectedLocation) params.append('city', selectedLocation);
      if (activeTabConfig.filterCategoryIds.length === 1) {
        params.append('category', activeTabConfig.filterCategoryIds[0]);
      }
      navigate(`/products?${params.toString()}`);
    }, 450);
  };

  return (
    <div className="relative w-full max-w-4xl mx-auto z-30" ref={dropdownRef}>
      {/* Floating Glassmorphic Container with Layered Elevation */}
      <div className="glass-bungalow-card rounded-3xl p-3 sm:p-4 shadow-elevation-3 border border-bungalow-200/80 transition-all duration-300 hover:shadow-2xl">
        {/* Category Pill Selectors */}
        <div className="flex items-center space-x-1 sm:space-x-2 border-b border-bungalow-200/70 pb-3 mb-3 overflow-x-auto no-scrollbar">
          {CATEGORY_TABS.map((tab) => {
            const Icon = tab.icon;
            const isActive = activeTab === tab.id;
            return (
              <button
                key={tab.id}
                type="button"
                onClick={() => {
                  setActiveTab(tab.id);
                  setShowLiveDropdown(true);
                }}
                className={`relative flex items-center space-x-2 px-3 sm:px-4 py-2 rounded-2xl text-xs sm:text-sm font-semibold transition-all duration-200 shrink-0 ${
                  isActive
                    ? 'bg-hunter-900 text-white shadow-elevation-1'
                    : 'text-hunter-800/80 hover:text-hunter-950 hover:bg-bungalow-100/70'
                }`}
              >
                <Icon className={`w-4 h-4 ${isActive ? 'text-gold-400' : 'text-hunter-600'}`} />
                <span>{tab.label}</span>
                <span
                  className={`hidden md:inline text-[11px] px-1.5 py-0.5 rounded-full font-normal ${
                    isActive ? 'bg-hunter-800 text-gold-300' : 'bg-bungalow-200/60 text-hunter-700'
                  }`}
                >
                  {tab.sublabel}
                </span>
                {isActive && (
                  <motion.div
                    layoutId="activeTabBadge"
                    className="absolute -bottom-3 left-1/2 -translate-x-1/2 w-8 h-1 bg-hunter-900 rounded-full"
                  />
                )}
              </button>
            );
          })}
        </div>

        {/* Search Fields Grid */}
        <form onSubmit={handleSearchSubmit} className="grid grid-cols-1 md:grid-cols-12 gap-2 sm:gap-3 items-center">
          {/* Query Field */}
          <div className="md:col-span-5 relative flex items-center bg-white/90 rounded-2xl px-3.5 py-2.5 border border-bungalow-200/80 focus-within:border-hunter-600 focus-within:ring-2 focus-within:ring-hunter-600/10 transition-all">
            <Search className="w-4 h-4 text-hunter-600 mr-2.5 shrink-0" />
            <div className="flex-1">
              <label className="block text-[10px] font-bold uppercase tracking-wider text-hunter-700">
                Keyword or Name
              </label>
              <input
                type="text"
                placeholder={activeTabConfig.defaultPlaceholder}
                value={searchQuery}
                onFocus={() => setShowLiveDropdown(true)}
                onChange={(e) => {
                  setSearchQuery(e.target.value);
                  setShowLiveDropdown(true);
                }}
                className="w-full bg-transparent text-hunter-950 text-xs sm:text-sm focus:outline-none placeholder:text-gray-400 font-medium truncate"
              />
            </div>
            {searchQuery && (
              <button
                type="button"
                onClick={() => setSearchQuery('')}
                className="p-1 hover:bg-bungalow-100 rounded-full text-gray-400 hover:text-gray-600"
              >
                <X className="w-3.5 h-3.5" />
              </button>
            )}
          </div>

          {/* Location Selector */}
          <div className="md:col-span-3 relative flex items-center bg-white/90 rounded-2xl px-3.5 py-2.5 border border-bungalow-200/80 focus-within:border-hunter-600 focus-within:ring-2 focus-within:ring-hunter-600/10 transition-all">
            <MapPin className="w-4 h-4 text-hunter-600 mr-2.5 shrink-0" />
            <div className="flex-1">
              <label className="block text-[10px] font-bold uppercase tracking-wider text-hunter-700">
                Location
              </label>
              <select
                value={selectedLocation}
                onChange={(e) => {
                  setSelectedLocation(e.target.value);
                  setShowLiveDropdown(true);
                }}
                className="w-full bg-transparent text-hunter-950 text-xs sm:text-sm focus:outline-none font-medium cursor-pointer"
              >
                <option value="">All Destinations</option>
                {activeTabConfig.quickLocations.map((loc) => (
                  <option key={loc} value={loc}>
                    {loc}
                  </option>
                ))}
              </select>
            </div>
          </div>

          {/* Dates / Duration */}
          <div className="md:col-span-2 relative flex items-center bg-white/90 rounded-2xl px-3.5 py-2.5 border border-bungalow-200/80 focus-within:border-hunter-600 focus-within:ring-2 focus-within:ring-hunter-600/10 transition-all">
            <Calendar className="w-4 h-4 text-hunter-600 mr-2.5 shrink-0" />
            <div className="flex-1">
              <label className="block text-[10px] font-bold uppercase tracking-wider text-hunter-700">
                Duration
              </label>
              <select
                value={dateRange}
                onChange={(e) => setDateRange(e.target.value)}
                className="w-full bg-transparent text-hunter-950 text-xs sm:text-sm focus:outline-none font-medium cursor-pointer"
              >
                <option value="Weekend Escape (3 Days)">Weekend (3d)</option>
                <option value="1 Week Rental">1 Week (7d)</option>
                <option value="Extended Shoot (14 Days)">Extended (14d)</option>
                <option value="Monthly Luxury Stay">1 Month</option>
              </select>
            </div>
          </div>

          {/* Dynamic Search Button with Loading Spinner */}
          <div className="md:col-span-2">
            <button
              type="submit"
              disabled={isLoading}
              className="w-full py-3 px-4 rounded-2xl font-semibold text-xs sm:text-sm text-white bg-gradient-to-r from-hunter-950 via-hunter-900 to-hunter-800 hover:from-hunter-900 hover:to-hunter-700 shadow-elevation-1 hover:shadow-elevation-2 active:scale-[0.98] transition-all duration-200 flex items-center justify-center space-x-2"
            >
              {isLoading ? (
                <>
                  <Loader2 className="w-4 h-4 animate-spin text-gold-400" />
                  <span>Searching...</span>
                </>
              ) : (
                <>
                  <span>Explore</span>
                  <ArrowRight className="w-4 h-4 text-gold-400" />
                </>
              )}
            </button>
          </div>
        </form>

        {/* Quick Filter Tag Bar */}
        <div className="mt-3 pt-2.5 border-t border-bungalow-200/60 flex items-center justify-between text-xs text-hunter-800/80">
          <div className="flex items-center space-x-2">
            <span className="font-semibold text-hunter-900 text-[11px] uppercase tracking-wider">
              Filter:
            </span>
            <button
              type="button"
              onClick={() => setFilterTag('all')}
              className={`px-2.5 py-1 rounded-xl text-[11px] font-medium transition-all ${
                filterTag === 'all'
                  ? 'bg-hunter-800 text-white'
                  : 'bg-white/80 hover:bg-white text-hunter-800 border border-bungalow-200'
              }`}
            >
              All Verified
            </button>
            <button
              type="button"
              onClick={() => setFilterTag('instant')}
              className={`px-2.5 py-1 rounded-xl text-[11px] font-medium transition-all flex items-center space-x-1 ${
                filterTag === 'instant'
                  ? 'bg-hunter-800 text-white'
                  : 'bg-white/80 hover:bg-white text-hunter-800 border border-bungalow-200'
              }`}
            >
              <Sparkles className="w-3 h-3 text-gold-500" />
              <span>Instant Reserve</span>
            </button>
            <button
              type="button"
              onClick={() => setFilterTag('escrow')}
              className={`px-2.5 py-1 rounded-xl text-[11px] font-medium transition-all flex items-center space-x-1 ${
                filterTag === 'escrow'
                  ? 'bg-hunter-800 text-white'
                  : 'bg-white/80 hover:bg-white text-hunter-800 border border-bungalow-200'
              }`}
            >
              <ShieldCheck className="w-3 h-3 text-emerald-600" />
              <span>Escrow Protected</span>
            </button>
          </div>

          <div className="hidden sm:flex items-center space-x-2 text-[11px] text-hunter-700">
            <CheckCircle2 className="w-3.5 h-3.5 text-hunter-600" />
            <span>Zero Platform Hidden Fees</span>
          </div>
        </div>
      </div>

      {/* Dynamic Live Matching Dropdown Preview */}
      <AnimatePresence>
        {showLiveDropdown && (
          <motion.div
            initial={{ opacity: 0, y: 10, scale: 0.98 }}
            animate={{ opacity: 1, y: 0, scale: 1 }}
            exit={{ opacity: 0, y: 8, scale: 0.98 }}
            transition={{ duration: 0.2 }}
            className="absolute left-0 right-0 top-full mt-2 bg-white/95 backdrop-blur-xl rounded-3xl p-4 shadow-2xl border border-bungalow-200/90 z-40 max-h-96 overflow-y-auto"
          >
            <div className="flex items-center justify-between pb-2 mb-3 border-b border-bungalow-200">
              <div className="flex items-center space-x-2">
                {isLoading ? (
                  <Loader2 className="w-4 h-4 animate-spin text-hunter-600" />
                ) : (
                  <Sparkles className="w-4 h-4 text-gold-600" />
                )}
                <span className="text-xs font-bold uppercase tracking-wider text-hunter-900">
                  {isLoading ? 'Scanning Inventory...' : `Instant Previews for ${activeTabConfig.label}`}
                </span>
              </div>
              <button
                type="button"
                onClick={() => setShowLiveDropdown(false)}
                className="text-gray-400 hover:text-gray-600 p-1 rounded-full hover:bg-bungalow-100"
              >
                <X className="w-4 h-4" />
              </button>
            </div>

            {isLoading ? (
              <div className="py-8 flex flex-col items-center justify-center space-y-3">
                <div className="relative w-10 h-10">
                  <div className="absolute inset-0 rounded-full border-2 border-hunter-200 border-t-hunter-800 animate-spin" />
                  <div className="absolute inset-2 rounded-full border-2 border-gold-300 border-b-gold-600 animate-spin" style={{ animationDirection: 'reverse' }} />
                </div>
                <p className="text-xs text-hunter-700 font-medium">Filtering live rental availability...</p>
              </div>
            ) : liveResults.length === 0 ? (
              <div className="py-6 text-center text-sm text-gray-500">
                No active listings matched your search in {activeTabConfig.label}. Try broadening your keywords.
              </div>
            ) : (
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                {liveResults.map((product) => (
                  <div
                    key={product.id}
                    onClick={() => {
                      setShowLiveDropdown(false);
                      navigate(`/products/${product.id}`);
                    }}
                    className="flex items-center space-x-3 p-2.5 rounded-2xl bg-bungalow-50/70 hover:bg-bungalow-100/90 border border-bungalow-200/70 hover:border-hunter-500/40 cursor-pointer transition-all duration-200 group"
                  >
                    <img
                      src={product.imageUrl}
                      alt={product.name}
                      className="w-16 h-16 rounded-xl object-cover shrink-0 group-hover:scale-105 transition-transform"
                    />
                    <div className="flex-1 min-w-0">
                      <div className="flex items-center space-x-1.5 mb-1">
                        <span className="text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded-md bg-hunter-900 text-white">
                          {product.categoryName}
                        </span>
                        {product.city && (
                          <span className="text-[10px] text-gray-500 font-medium">
                            • {product.city}
                          </span>
                        )}
                      </div>
                      <h4 className="text-xs font-bold text-hunter-950 truncate group-hover:text-hunter-700">
                        {product.name}
                      </h4>
                      <div className="flex items-center justify-between mt-1">
                        <div className="text-xs font-bold text-hunter-900">
                          ₹{product.pricePerDay?.toLocaleString()}{' '}
                          <span className="text-[10px] text-gray-500 font-normal">/ day</span>
                        </div>
                        <div className="flex items-center space-x-1 text-[11px] text-gold-600 font-semibold">
                          <Star className="w-3 h-3 fill-gold-500 text-gold-500" />
                          <span>{product.rating || '4.9'}</span>
                        </div>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            )}

            <div className="mt-3 pt-3 border-t border-bungalow-200 flex items-center justify-between">
              <span className="text-xs text-hunter-700">
                Showing top verified items with real-time deposit calculation
              </span>
              <button
                type="button"
                onClick={handleSearchSubmit}
                className="inline-flex items-center space-x-1 text-xs font-bold text-hunter-800 hover:text-hunter-950"
              >
                <span>View Full Catalog</span>
                <ArrowRight className="w-3.5 h-3.5" />
              </button>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}
