import React, { useState, useMemo } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { motion, AnimatePresence } from 'framer-motion';
import {
  Search,
  Calendar,
  ShieldCheck,
  Zap,
  RotateCcw,
  Sparkles,
  ArrowRight,
  Star,
  CheckCircle2,
  Camera,
  Plane,
  Mic,
  Gamepad2,
  Wrench,
  Compass,
  Car,
  Bike,
  Home as HomeIcon,
  Building2,
  Quote,
  ThumbsUp,
  Plus,
  X,
  Award,
  ChevronRight,
  Clock,
  MapPin,
  Flame,
} from 'lucide-react';
import { storageService } from '../../services/mockStorage';
import ProductCard from '../../components/product/ProductCard';
import CinematicLogoReveal from '../../components/hero/CinematicLogoReveal';
import FloatingRentalSearch from '../../components/hero/FloatingRentalSearch';

const categoryIcons = {
  'Cameras & Cinematic Gear': Camera,
  'Drones & Aerial Video': Plane,
  'Pro Audio & Sound': Mic,
  'Gaming & Virtual Reality': Gamepad2,
  'Power Tools & DIY': Wrench,
  'Outdoor & Adventure Gear': Compass,
  'Self-Drive & Luxury Cars': Car,
  'Superbikes & Touring Motorcycles': Bike,
  'Bungalows & Heritage Properties': HomeIcon,
  'Creative Studios & Spaces': Building2,
};

const categoryBadges = {
  'Bungalows & Heritage Properties': 'Bungalow Luxury',
  'Creative Studios & Spaces': 'Creative Space',
  'Self-Drive & Luxury Cars': 'Self-Drive',
  'Superbikes & Touring Motorcycles': 'Popular',
  'Cameras & Cinematic Gear': 'Pro Rig',
  'Drones & Aerial Video': '4K / 8K',
};

// Animation variants
const containerVariants = {
  hidden: { opacity: 0 },
  visible: {
    opacity: 1,
    transition: {
      staggerChildren: 0.08,
      delayChildren: 0.1,
    },
  },
};

const itemVariants = {
  hidden: { opacity: 0, y: 20 },
  visible: {
    opacity: 1,
    y: 0,
    transition: { duration: 0.5, ease: 'easeOut' },
  },
};

export default function Home() {
  const navigate = useNavigate();
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('');
  const categories = storageService.getCategories();
  const products = storageService.getProducts();

  // Featured category filter tab: 'all', 'bungalows', 'vehicles', 'spaces', 'gear'
  const [featuredTab, setFeaturedTab] = useState('all');

  // Reviews state & modal
  const [reviews, setReviews] = useState(() => storageService.getReviews());
  const [reviewFilter, setReviewFilter] = useState('all');
  const [isReviewModalOpen, setIsReviewModalOpen] = useState(false);
  const [newReview, setNewReview] = useState({
    productId: products[0]?.id || 1,
    customerName: '',
    rating: 5,
    comment: '',
  });
  const [reviewSuccessMsg, setReviewSuccessMsg] = useState('');

  // Wishlist
  const [wishlist, setWishlist] = useState(storageService.getWishlist());

  const handleWishlistToggle = (id) => {
    const updated = storageService.toggleWishlist(id);
    setWishlist(updated);
  };

  const handleSearchSubmit = (e) => {
    e.preventDefault();
    const params = new URLSearchParams();
    if (searchTerm) params.append('search', searchTerm);
    if (selectedCategory) params.append('category', selectedCategory);
    navigate(`/products?${params.toString()}`);
  };

  // Filtered featured products based on tabs
  const filteredFeaturedProducts = useMemo(() => {
    if (featuredTab === 'bungalows') {
      return products.filter((p) => p.categoryId === 9);
    }
    if (featuredTab === 'vehicles') {
      return products.filter((p) => p.categoryId === 7 || p.categoryId === 8);
    }
    if (featuredTab === 'spaces') {
      return products.filter((p) => p.categoryId === 10);
    }
    if (featuredTab === 'gear') {
      return products.filter((p) => [1, 2, 3, 4, 5, 6].includes(p.categoryId));
    }
    // 'all': curated mix of bungalows, vehicles, cinema gear and studios
    const curatedIds = [13, 14, 9, 11, 15, 1, 2, 10];
    const picked = products.filter((p) => curatedIds.includes(p.id));
    return picked.length >= 4 ? picked : products.slice(0, 8);
  }, [products, featuredTab]);

  // Filtered reviews
  const filteredReviews = useMemo(() => {
    if (reviewFilter === 'bungalows') {
      return reviews.filter((r) => r.productId === 13 || r.productId === 14);
    }
    if (reviewFilter === 'cars') {
      return reviews.filter((r) => r.productId === 9 || r.productId === 10);
    }
    if (reviewFilter === 'bikes') {
      return reviews.filter((r) => r.productId === 11 || r.productId === 12);
    }
    if (reviewFilter === 'gear') {
      return reviews.filter((r) => [1, 2, 3, 4, 5, 6, 15, 16].includes(r.productId));
    }
    return reviews;
  }, [reviews, reviewFilter]);

  // Submit new review
  const handleReviewSubmit = (e) => {
    e.preventDefault();
    if (!newReview.customerName.trim() || !newReview.comment.trim()) return;

    const saved = storageService.addReview({
      productId: Number(newReview.productId),
      customerId: 1,
      customerName: newReview.customerName.trim(),
      customerAvatar: `https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=100&q=80`,
      rating: Number(newReview.rating),
      comment: newReview.comment.trim(),
    });

    setReviews([saved, ...reviews]);
    setReviewSuccessMsg('Thank you! Your verified review has been published.');
    setNewReview({
      productId: products[0]?.id || 1,
      customerName: '',
      rating: 5,
      comment: '',
    });
    setTimeout(() => {
      setIsReviewModalOpen(false);
      setReviewSuccessMsg('');
    }, 1800);
  };

  const getProductName = (productId) => {
    const product = products.find((p) => p.id === productId);
    return product ? product.name : 'Verified Rental Product';
  };

  const getProductCategory = (productId) => {
    const product = products.find((p) => p.id === productId);
    return product ? product.categoryName : 'Equipment';
  };

  return (
    <div className="space-y-20 pb-20 overflow-x-hidden">
      {/* 1. CINEMATIC HERO & LOGO REVEAL SECTION (LIGHT BUNGALOW BEIGE & HUNTER GREEN) */}
      <section className="relative overflow-hidden bg-gradient-to-b from-bungalow-100 via-bungalow-50 to-bungalow-100/90 text-hunter-950 pt-8 pb-20 lg:pt-12 lg:pb-28 bg-grain border-b border-bungalow-200/70">
        {/* Multi-layered Ambient Background Glow & Gradients */}
        <div className="absolute top-10 left-1/4 -translate-x-1/2 w-[34rem] h-[34rem] rounded-full bg-hunter-600/10 blur-3xl pointer-events-none animate-pulse-subtle" />
        <div className="absolute top-1/3 right-10 w-[28rem] h-[28rem] rounded-full bg-gold-500/15 blur-3xl pointer-events-none animate-pulse-subtle" />
        <div className="absolute -bottom-10 left-10 w-96 h-96 rounded-full bg-hunter-500/10 blur-3xl pointer-events-none" />

        {/* Faint Architectural Network Lines Pattern */}
        <div className="absolute inset-0 opacity-[0.035] bg-[radial-gradient(#0F291E_1px,transparent_1px)] [background-size:32px_32px] pointer-events-none" />

        <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center z-10">
          {/* CINEMATIC LOGO REVEAL COMPONENT */}
          <CinematicLogoReveal />

          {/* Sequential Headline & Subtitle Reveal */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.7, delay: 0.35 }}
            className="mt-3 max-w-4xl mx-auto"
          >
            {/* Tagline Badge */}
            <div className="inline-flex items-center space-x-2 px-4 py-1.5 rounded-full bg-white/85 border border-hunter-800/15 text-hunter-900 text-xs font-semibold mb-5 backdrop-blur-md shadow-elevation-1">
              <Sparkles className="w-3.5 h-3.5 text-gold-600 animate-spin-slow" />
              <span>Architectural Bungalows</span>
              <span className="text-bungalow-400">•</span>
              <span>Expedition 4x4 Fleet</span>
              <span className="text-bungalow-400">•</span>
              <span className="text-hunter-700 font-bold">Cinema &amp; Sound Stages</span>
            </div>

            {/* Headline */}
            <h2 className="text-3xl sm:text-5xl lg:text-6xl font-extrabold font-display tracking-tight text-hunter-950 leading-tight sm:leading-none">
              Rent Exceptional Spaces &amp; High-Spec Hardware{' '}
              <br className="hidden sm:inline" />
              <span className="text-transparent bg-clip-text bg-gradient-to-r from-hunter-900 via-hunter-700 to-gold-600">
                Without The Cost of Ownership.
              </span>
            </h2>

            <p className="mt-5 text-sm sm:text-base lg:text-lg text-hunter-800/80 max-w-2xl mx-auto leading-relaxed font-normal">
              Curated architectural bungalows, self-drive luxury SUVs, touring motorcycles, cinema cameras, and creative stages — backed by automated bank-grade escrow security deposits.
            </p>
          </motion.div>

          {/* INTERACTIVE FLOATING RENTAL SEARCH CONSOLE */}
          <motion.div
            initial={{ opacity: 0, y: 25 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.7, delay: 0.5 }}
            className="mt-8"
          >
            <FloatingRentalSearch />
          </motion.div>

          {/* Layered Elevation Value Props Cards (Crisp White Surfaces) */}
          <motion.div
            initial={{ opacity: 0, y: 25 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 0.65 }}
            className="mt-14 pt-8 border-t border-bungalow-200/80 grid grid-cols-2 md:grid-cols-4 gap-4 sm:gap-6 max-w-5xl mx-auto text-left"
          >
            <div className="bg-white/95 p-4 rounded-2xl border border-bungalow-200/90 shadow-elevation-1 hover:shadow-elevation-2 transition-all duration-200 flex items-center space-x-3.5">
              <div className="w-11 h-11 rounded-xl bg-hunter-100 text-hunter-900 flex items-center justify-center shrink-0">
                <ShieldCheck className="w-5 h-5 text-hunter-800" />
              </div>
              <div>
                <p className="text-xs sm:text-sm font-bold text-hunter-950">Escrow Protected</p>
                <p className="text-[11px] text-gray-500">100% Refundable Deposits</p>
              </div>
            </div>

            <div className="bg-white/95 p-4 rounded-2xl border border-bungalow-200/90 shadow-elevation-1 hover:shadow-elevation-2 transition-all duration-200 flex items-center space-x-3.5">
              <div className="w-11 h-11 rounded-xl bg-gold-100 text-gold-800 flex items-center justify-center shrink-0">
                <Zap className="w-5 h-5 text-gold-600" />
              </div>
              <div>
                <p className="text-xs sm:text-sm font-bold text-hunter-950">Curated &amp; Tested</p>
                <p className="text-[11px] text-gray-500">Rigorous 40-pt Inspection</p>
              </div>
            </div>

            <div className="bg-white/95 p-4 rounded-2xl border border-bungalow-200/90 shadow-elevation-1 hover:shadow-elevation-2 transition-all duration-200 flex items-center space-x-3.5">
              <div className="w-11 h-11 rounded-xl bg-hunter-100 text-hunter-900 flex items-center justify-center shrink-0">
                <RotateCcw className="w-5 h-5 text-hunter-800" />
              </div>
              <div>
                <p className="text-xs sm:text-sm font-bold text-hunter-950">Flexible Terms</p>
                <p className="text-[11px] text-gray-500">Daily, Weekend or Monthly</p>
              </div>
            </div>

            <div className="bg-white/95 p-4 rounded-2xl border border-bungalow-200/90 shadow-elevation-1 hover:shadow-elevation-2 transition-all duration-200 flex items-center space-x-3.5">
              <div className="w-11 h-11 rounded-xl bg-gold-100 text-gold-800 flex items-center justify-center shrink-0">
                <CheckCircle2 className="w-5 h-5 text-gold-600" />
              </div>
              <div>
                <p className="text-xs sm:text-sm font-bold text-hunter-950">Zero Hidden Fees</p>
                <p className="text-[11px] text-gray-500">Transparent GST Invoicing</p>
              </div>
            </div>
          </motion.div>
        </div>
      </section>

      {/* 2. CURATED CATEGORIES SECTION (INCLUDING CARS & BIKES) */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-end justify-between mb-8">
          <div>
            <span className="text-xs font-bold uppercase tracking-wider text-hunter-700 flex items-center space-x-1.5">
              <Sparkles className="w-3.5 h-3.5 text-gold-600" />
              <span>Curated Marketplace Departments</span>
            </span>
            <h2 className="text-2xl sm:text-3xl font-bold font-display text-hunter-950 mt-1">
              Explore by Stays, Fleet &amp; Hardware Category
            </h2>
          </div>
          <Link
            to="/products"
            className="hidden sm:inline-flex items-center space-x-1 text-sm font-semibold text-hunter-900 hover:text-hunter-700 transition-colors"
          >
            <span>View All ({categories.length})</span>
            <ArrowRight className="w-4 h-4" />
          </Link>
        </div>

        <motion.div
          variants={containerVariants}
          initial="hidden"
          whileInView="visible"
          viewport={{ once: true, margin: '-50px' }}
          className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-4 sm:gap-5"
        >
          {categories.map((category) => {
            const IconComponent = categoryIcons[category.name] || Camera;
            const badge = categoryBadges[category.name];
            const isHighlight =
              category.slug === 'properties-bungalows' ||
              category.slug === 'cars-vehicles' ||
              category.slug === 'studios-spaces';

            return (
              <motion.div
                key={category.id}
                variants={itemVariants}
                whileHover={{ y: -6, scale: 1.02 }}
                transition={{ type: 'spring', stiffness: 350, damping: 25 }}
              >
                <Link
                  to={`/products?category=${category.slug}`}
                  className={`relative p-5 text-center flex flex-col items-center justify-center group bg-white border rounded-2xl shadow-elevation-1 transition-all duration-300 hover:shadow-elevation-2 ${
                    isHighlight
                      ? 'border-hunter-300 ring-1 ring-hunter-500/20 bg-gradient-to-b from-bungalow-50/60 to-white'
                      : 'border-bungalow-200/90 hover:border-hunter-400'
                  }`}
                >
                  {badge && (
                    <span className="absolute top-2.5 right-2.5 text-[9px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-hunter-900 text-gold-300 shadow-sm">
                      {badge}
                    </span>
                  )}

                  <div
                    className={`w-13 h-13 p-3 rounded-2xl flex items-center justify-center mb-3 transition-all duration-300 ${
                      isHighlight
                        ? 'bg-hunter-900 text-gold-300 group-hover:bg-hunter-950 group-hover:scale-110'
                        : 'bg-bungalow-100 text-hunter-900 group-hover:bg-hunter-900 group-hover:text-white group-hover:scale-110'
                    }`}
                  >
                    <IconComponent className="w-6 h-6" />
                  </div>

                  <h3 className="text-xs sm:text-sm font-bold text-hunter-950 group-hover:text-hunter-800 transition-colors line-clamp-1">
                    {category.name}
                  </h3>
                  <span className="text-[11px] text-gray-500 mt-1 flex items-center space-x-1">
                    <span>{category.itemCount} available</span>
                    <span className="text-hunter-600 font-semibold">• Escrow</span>
                  </span>
                </Link>
              </motion.div>
            );
          })}
        </motion.div>
      </section>

      {/* 3. FEATURED PRODUCTS, BUNGALOWS & FLEET */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex flex-col md:flex-row md:items-end justify-between mb-8 gap-4">
          <div>
            <span className="text-xs font-bold uppercase tracking-wider text-gold-700 flex items-center space-x-1.5">
              <Flame className="w-4 h-4 text-gold-500" />
              <span>Curated Selection</span>
            </span>
            <h2 className="text-2xl sm:text-3xl font-bold font-display text-hunter-950 mt-1">
              Featured Commercial Rentals &amp; Stays
            </h2>
          </div>

          {/* Interactive Filter Tabs */}
          <div className="flex items-center space-x-1.5 bg-white p-1.5 rounded-2xl text-xs font-semibold overflow-x-auto shadow-elevation-1 border border-bungalow-200">
            <button
              onClick={() => setFeaturedTab('all')}
              className={`px-3 py-1.5 rounded-xl transition-all ${
                featuredTab === 'all'
                  ? 'bg-hunter-900 text-white shadow-sm'
                  : 'text-hunter-800 hover:text-hunter-950 hover:bg-bungalow-100/60'
              }`}
            >
              All Featured
            </button>
            <button
              onClick={() => setFeaturedTab('bungalows')}
              className={`px-3 py-1.5 rounded-xl transition-all flex items-center space-x-1 ${
                featuredTab === 'bungalows'
                  ? 'bg-hunter-900 text-white shadow-sm'
                  : 'text-hunter-800 hover:text-hunter-950 hover:bg-bungalow-100/60'
              }`}
            >
              <HomeIcon className="w-3.5 h-3.5 text-gold-400" />
              <span>Bungalows</span>
            </button>
            <button
              onClick={() => setFeaturedTab('vehicles')}
              className={`px-3 py-1.5 rounded-xl transition-all flex items-center space-x-1 ${
                featuredTab === 'vehicles'
                  ? 'bg-hunter-900 text-white shadow-sm'
                  : 'text-hunter-800 hover:text-hunter-950 hover:bg-bungalow-100/60'
              }`}
            >
              <Car className="w-3.5 h-3.5" />
              <span>Vehicles &amp; Rides</span>
            </button>
            <button
              onClick={() => setFeaturedTab('spaces')}
              className={`px-3 py-1.5 rounded-xl transition-all flex items-center space-x-1 ${
                featuredTab === 'spaces'
                  ? 'bg-hunter-900 text-white shadow-sm'
                  : 'text-hunter-800 hover:text-hunter-950 hover:bg-bungalow-100/60'
              }`}
            >
              <Building2 className="w-3.5 h-3.5" />
              <span>Studios &amp; Spaces</span>
            </button>
            <button
              onClick={() => setFeaturedTab('gear')}
              className={`px-3 py-1.5 rounded-xl transition-all ${
                featuredTab === 'gear'
                  ? 'bg-hunter-900 text-white shadow-sm'
                  : 'text-hunter-800 hover:text-hunter-950 hover:bg-bungalow-100/60'
              }`}
            >
              Cinema &amp; Tech
            </button>
          </div>
        </div>

        <motion.div
          layout
          className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6"
        >
          <AnimatePresence>
            {filteredFeaturedProducts.map((product) => (
              <motion.div
                key={product.id}
                layout
                initial={{ opacity: 0, scale: 0.95 }}
                animate={{ opacity: 1, scale: 1 }}
                exit={{ opacity: 0, scale: 0.95 }}
                transition={{ duration: 0.3 }}
              >
                <ProductCard
                  product={product}
                  isWishlisted={wishlist.includes(product.id)}
                  onWishlistToggle={handleWishlistToggle}
                />
              </motion.div>
            ))}
          </AnimatePresence>
        </motion.div>

        <div className="mt-8 text-center">
          <Link
            to="/products"
            className="inline-flex items-center space-x-2 px-6 py-3 rounded-full bg-hunter-900 text-white text-sm font-semibold hover:bg-hunter-800 transition-colors shadow-elevation-1 hover:shadow-elevation-2"
          >
            <span>Explore Entire Fleet &amp; Stays</span>
            <ArrowRight className="w-4 h-4 text-gold-400" />
          </Link>
        </div>
      </section>

      {/* 4. VERIFIED REVIEWS & RATINGS (ANIMATED SHOWCASE) */}
      <section className="bg-bungalow-100/70 py-16 border-y border-bungalow-200 relative overflow-hidden bg-grain">
        {/* Subtle ambient decorative circles */}
        <div className="absolute -bottom-20 -left-20 w-80 h-80 rounded-full bg-hunter-600/10 blur-2xl pointer-events-none" />
        <div className="absolute -top-20 -right-20 w-80 h-80 rounded-full bg-gold-400/15 blur-2xl pointer-events-none" />

        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
          {/* Header & Rating Summary */}
          <div className="flex flex-col lg:flex-row lg:items-end justify-between mb-12 gap-6">
            <div>
              <div className="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-hunter-100 text-hunter-900 text-xs font-bold uppercase tracking-wider mb-2 border border-hunter-200/60">
                <Award className="w-3.5 h-3.5 text-hunter-700" />
                <span>Verified Renter Reviews &amp; Ratings</span>
              </div>
              <h2 className="text-3xl font-extrabold font-display text-hunter-950">
                What Renters Say About Rentora
              </h2>
              <p className="text-sm text-hunter-800/80 mt-2 max-w-xl">
                Real feedback from filmmakers, road-trippers, event planners, and vacationers across India.
              </p>
            </div>

            {/* Scorecard Box & Write Review Button */}
            <div className="flex flex-wrap items-center gap-4">
              <div className="flex items-center space-x-3 bg-white px-5 py-3 rounded-2xl shadow-elevation-1 border border-bungalow-200">
                <div className="text-3xl font-extrabold font-display text-hunter-950">
                  4.9
                </div>
                <div>
                  <div className="flex text-gold-500">
                    {Array.from({ length: 5 }).map((_, i) => (
                      <Star key={i} className="w-4 h-4 fill-current" />
                    ))}
                  </div>
                  <p className="text-[11px] text-gray-500 mt-0.5 font-medium">
                    2,800+ Verified Bookings
                  </p>
                </div>
              </div>

              <motion.button
                whileHover={{ scale: 1.03 }}
                whileTap={{ scale: 0.97 }}
                onClick={() => setIsReviewModalOpen(true)}
                className="btn-primary py-3 px-5 rounded-2xl text-xs font-bold flex items-center space-x-2 shadow-elevation-1"
              >
                <Plus className="w-4 h-4" />
                <span>Write a Review</span>
              </motion.button>
            </div>
          </div>

          {/* Category Filter Pills for Reviews */}
          <div className="flex items-center space-x-2 mb-8 overflow-x-auto pb-2">
            <button
              onClick={() => setReviewFilter('all')}
              className={`px-4 py-2 rounded-xl text-xs font-bold transition-all ${
                reviewFilter === 'all'
                  ? 'bg-hunter-900 text-white shadow-elevation-1'
                  : 'bg-white text-hunter-900 border border-bungalow-200 hover:bg-bungalow-50'
              }`}
            >
              All Reviews ({reviews.length})
            </button>
            <button
              onClick={() => setReviewFilter('bungalows')}
              className={`px-4 py-2 rounded-xl text-xs font-bold transition-all flex items-center space-x-1.5 ${
                reviewFilter === 'bungalows'
                  ? 'bg-hunter-900 text-white shadow-elevation-1'
                  : 'bg-white text-hunter-900 border border-bungalow-200 hover:bg-bungalow-50'
              }`}
            >
              <HomeIcon className="w-3.5 h-3.5 text-gold-500" />
              <span>Bungalows &amp; Stays</span>
            </button>
            <button
              onClick={() => setReviewFilter('cars')}
              className={`px-4 py-2 rounded-xl text-xs font-bold transition-all flex items-center space-x-1.5 ${
                reviewFilter === 'cars'
                  ? 'bg-hunter-900 text-white shadow-elevation-1'
                  : 'bg-white text-hunter-900 border border-bungalow-200 hover:bg-bungalow-50'
              }`}
            >
              <Car className="w-3.5 h-3.5" />
              <span>Cars &amp; 4x4 SUVs</span>
            </button>
            <button
              onClick={() => setReviewFilter('bikes')}
              className={`px-4 py-2 rounded-xl text-xs font-bold transition-all flex items-center space-x-1.5 ${
                reviewFilter === 'bikes'
                  ? 'bg-hunter-900 text-white shadow-elevation-1'
                  : 'bg-white text-hunter-900 border border-bungalow-200 hover:bg-bungalow-50'
              }`}
            >
              <Bike className="w-3.5 h-3.5" />
              <span>Superbikes &amp; Tourers</span>
            </button>
            <button
              onClick={() => setReviewFilter('gear')}
              className={`px-4 py-2 rounded-xl text-xs font-bold transition-all ${
                reviewFilter === 'gear'
                  ? 'bg-hunter-900 text-white shadow-elevation-1'
                  : 'bg-white text-hunter-900 border border-bungalow-200 hover:bg-bungalow-50'
              }`}
            >
              Cinema Gear &amp; Studios
            </button>
          </div>

          {/* Reviews Grid */}
          <motion.div
            variants={containerVariants}
            initial="hidden"
            animate="visible"
            className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6"
          >
            {filteredReviews.map((rev) => (
              <motion.div
                key={rev.id}
                variants={itemVariants}
                whileHover={{ y: -6, scale: 1.01 }}
                className="bg-white p-6 rounded-3xl border border-gray-200/80 shadow-card flex flex-col justify-between relative group hover:border-emerald-300 transition-all duration-300"
              >
                <div className="space-y-4">
                  {/* Top Bar: Stars + Verified Badge */}
                  <div className="flex items-center justify-between">
                    <div className="flex text-gold-500">
                      {Array.from({ length: rev.rating }).map((_, i) => (
                        <Star key={i} className="w-4 h-4 fill-current" />
                      ))}
                    </div>
                    <div className="flex items-center space-x-1 bg-emerald-50 text-emerald-800 text-[10px] font-bold px-2.5 py-0.5 rounded-full border border-emerald-200/60">
                      <CheckCircle2 className="w-3 h-3 text-emerald-600" />
                      <span>Verified Renter</span>
                    </div>
                  </div>

                  {/* Rented Product Pill */}
                  <div className="inline-flex items-center space-x-1.5 px-3 py-1 rounded-lg bg-gray-50 border border-gray-100 text-xs font-semibold text-gray-800">
                    {getProductCategory(rev.productId).includes('Car') ? (
                      <Car className="w-3.5 h-3.5 text-forest-900" />
                    ) : getProductCategory(rev.productId).includes('Motorcycle') ? (
                      <Bike className="w-3.5 h-3.5 text-forest-900" />
                    ) : (
                      <Camera className="w-3.5 h-3.5 text-forest-900" />
                    )}
                    <span className="truncate max-w-[220px]">
                      {getProductName(rev.productId)}
                    </span>
                  </div>

                  {/* Review Text */}
                  <div className="relative pt-1">
                    <Quote className="w-6 h-6 text-emerald-200 absolute -top-2 -left-1 -z-0 opacity-60" />
                    <p className="text-xs sm:text-sm text-gray-700 leading-relaxed relative z-10 font-normal italic">
                      "{rev.comment}"
                    </p>
                  </div>
                </div>

                {/* Author Info */}
                <div className="pt-5 mt-5 border-t border-gray-100 flex items-center justify-between text-xs">
                  <div className="flex items-center space-x-3">
                    <img
                      src={rev.customerAvatar}
                      alt={rev.customerName}
                      className="w-9 h-9 rounded-full object-cover ring-2 ring-emerald-500/20"
                    />
                    <div>
                      <h4 className="font-bold text-gray-900">{rev.customerName}</h4>
                      <p className="text-[10px] text-gray-400 flex items-center space-x-1">
                        <Clock className="w-3 h-3" />
                        <span>{rev.date}</span>
                      </p>
                    </div>
                  </div>
                  <div className="flex items-center space-x-1 text-emerald-700 font-semibold text-[11px]">
                    <ThumbsUp className="w-3.5 h-3.5" />
                    <span>Helpful</span>
                  </div>
                </div>
              </motion.div>
            ))}
          </motion.div>
        </div>
      </section>

      {/* 5. HOW RENTORA WORKS */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center max-w-2xl mx-auto mb-12">
          <span className="text-xs font-bold uppercase tracking-wider text-emerald-700 flex items-center justify-center space-x-1.5">
            <Sparkles className="w-3.5 h-3.5" />
            <span>Simple &amp; Frictionless</span>
          </span>
          <h2 className="text-3xl font-bold font-display text-gray-900 mt-1">
            How the Rentora Lifecycle Works
          </h2>
          <p className="text-sm text-gray-600 mt-2">
            From online reservation to automated escrow deposit release — transparent at every checkpoint.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
          <motion.div
            whileHover={{ y: -6 }}
            className="bg-white p-6 rounded-3xl shadow-sm border border-gray-200/70 relative group"
          >
            <span className="text-3xl font-black text-emerald-100 group-hover:text-emerald-200 transition-colors absolute top-4 right-4">
              01
            </span>
            <div className="w-11 h-11 rounded-2xl bg-forest-900 text-white flex items-center justify-center font-bold mb-4 shadow-md shadow-forest-900/20">
              1
            </div>
            <h3 className="text-base font-bold text-gray-900 mb-2">
              Choose Dates &amp; Unit
            </h3>
            <p className="text-xs text-gray-500 leading-relaxed">
              Browse cars, superbikes, or cinema rigs. Check live availability calendars and book with instant daily/weekly discounts.
            </p>
          </motion.div>

          <motion.div
            whileHover={{ y: -6 }}
            className="bg-white p-6 rounded-3xl shadow-sm border border-gray-200/70 relative group"
          >
            <span className="text-3xl font-black text-emerald-100 group-hover:text-emerald-200 transition-colors absolute top-4 right-4">
              02
            </span>
            <div className="w-11 h-11 rounded-2xl bg-forest-900 text-white flex items-center justify-center font-bold mb-4 shadow-md shadow-forest-900/20">
              2
            </div>
            <h3 className="text-base font-bold text-gray-900 mb-2">
              Escrow Checkout
            </h3>
            <p className="text-xs text-gray-500 leading-relaxed">
              Pay the rental fee plus security deposit via UPI/Card. Your deposit is locked safely in a regulated escrow account.
            </p>
          </motion.div>

          <motion.div
            whileHover={{ y: -6 }}
            className="bg-white p-6 rounded-3xl shadow-sm border border-gray-200/70 relative group"
          >
            <span className="text-3xl font-black text-emerald-100 group-hover:text-emerald-200 transition-colors absolute top-4 right-4">
              03
            </span>
            <div className="w-11 h-11 rounded-2xl bg-forest-900 text-white flex items-center justify-center font-bold mb-4 shadow-md shadow-forest-900/20">
              3
            </div>
            <h3 className="text-base font-bold text-gray-900 mb-2">
              OTP Handover &amp; Drive
            </h3>
            <p className="text-xs text-gray-500 leading-relaxed">
              Pick up or receive delivery with 6-digit handover OTP. Complete a rapid 5-point physical check and hit the road or set.
            </p>
          </motion.div>

          <motion.div
            whileHover={{ y: -6 }}
            className="bg-white p-6 rounded-3xl shadow-sm border border-gray-200/70 relative group"
          >
            <span className="text-3xl font-black text-emerald-100 group-hover:text-emerald-200 transition-colors absolute top-4 right-4">
              04
            </span>
            <div className="w-11 h-11 rounded-2xl bg-forest-900 text-white flex items-center justify-center font-bold mb-4 shadow-md shadow-forest-900/20">
              4
            </div>
            <h3 className="text-base font-bold text-gray-900 mb-2">
              Return &amp; Auto-Refund
            </h3>
            <p className="text-xs text-gray-500 leading-relaxed">
              Return the vehicle or gear. After quick inspection, 100% of your deposit is credited back into your account in &lt; 24h.
            </p>
          </motion.div>
        </div>
      </section>

      {/* 6. PLATFORM STATISTICS (ANIMATED) */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <motion.div
          initial={{ opacity: 0, scale: 0.98 }}
          whileInView={{ opacity: 1, scale: 1 }}
          viewport={{ once: true }}
          className="bg-gradient-to-r from-forest-950 via-forest-900 to-forest-950 rounded-3xl p-8 sm:p-12 text-white shadow-2xl relative overflow-hidden border border-forest-800"
        >
          <div className="relative z-10 grid grid-cols-2 lg:grid-cols-4 gap-8 text-center">
            <div>
              <p className="text-3xl sm:text-4xl font-extrabold font-display text-emerald-400">
                ₹3.4 Cr+
              </p>
              <p className="text-xs uppercase tracking-wider text-gray-300 mt-1 font-semibold">
                Fleet &amp; Gear Value Rented
              </p>
            </div>
            <div>
              <p className="text-3xl sm:text-4xl font-extrabold font-display text-gold-400">
                99.8%
              </p>
              <p className="text-xs uppercase tracking-wider text-gray-300 mt-1 font-semibold">
                Dispute-Free Returns
              </p>
            </div>
            <div>
              <p className="text-3xl sm:text-4xl font-extrabold font-display text-emerald-400">
                2,100+
              </p>
              <p className="text-xs uppercase tracking-wider text-gray-300 mt-1 font-semibold">
                Cars, Bikes &amp; Rigs Available
              </p>
            </div>
            <div>
              <p className="text-3xl sm:text-4xl font-extrabold font-display text-gold-400">
                &lt; 4 Hours
              </p>
              <p className="text-xs uppercase tracking-wider text-gray-300 mt-1 font-semibold">
                Average Deposit Refund SLA
              </p>
            </div>
          </div>
        </motion.div>
      </section>

      {/* 7. PARTNER VENDOR CTA */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="bg-white border border-gray-200 rounded-3xl p-8 sm:p-12 flex flex-col lg:flex-row items-center justify-between gap-8 shadow-card">
          <div className="max-w-xl">
            <span className="text-xs font-bold uppercase tracking-wider text-gold-700">
              For Fleet Owners, Studios &amp; Tool Hubs
            </span>
            <h2 className="text-3xl font-bold font-display text-gray-900 mt-1">
              Have Idle SUVs, Superbikes, or Cinematic Gear?
            </h2>
            <p className="text-sm text-gray-600 mt-3 leading-relaxed">
              Monetize your premium assets on Rentora with automated escrow deposits, identity-verified renters, and full transit insurance. Earn steady rental income while retaining complete asset ownership.
            </p>
          </div>

          <div className="flex flex-col sm:flex-row gap-3 shrink-0">
            <Link to="/register" className="btn-accent py-3.5 px-7 text-sm font-semibold rounded-2xl shadow-md">
              List Your Gear or Vehicle
            </Link>
            <Link to="/about" className="btn-outline py-3.5 px-6 text-sm font-semibold rounded-2xl">
              Learn Vendor Benefits
            </Link>
          </div>
        </div>
      </section>

      {/* 8. INTERACTIVE REVIEW SUBMISSION MODAL */}
      <AnimatePresence>
        {isReviewModalOpen && (
          <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm">
            <motion.div
              initial={{ opacity: 0, scale: 0.95, y: 15 }}
              animate={{ opacity: 1, scale: 1, y: 0 }}
              exit={{ opacity: 0, scale: 0.95, y: 15 }}
              transition={{ duration: 0.2 }}
              className="bg-white rounded-3xl shadow-2xl max-w-lg w-full p-6 sm:p-8 relative border border-gray-100"
            >
              <button
                type="button"
                onClick={() => setIsReviewModalOpen(false)}
                className="absolute top-5 right-5 text-gray-400 hover:text-gray-700 transition-colors p-1"
              >
                <X className="w-5 h-5" />
              </button>

              <div className="mb-6">
                <div className="inline-flex items-center space-x-1.5 px-3 py-1 rounded-full bg-emerald-100 text-emerald-800 text-xs font-bold mb-2">
                  <Star className="w-3.5 h-3.5 fill-current text-gold-500" />
                  <span>Verified Customer Experience</span>
                </div>
                <h3 className="text-xl font-bold font-display text-gray-900">
                  Write a Verified Rental Review
                </h3>
                <p className="text-xs text-gray-500 mt-1">
                  Share your experience with vehicles or hardware to guide other renters.
                </p>
              </div>

              {reviewSuccessMsg ? (
                <div className="p-4 rounded-2xl bg-emerald-50 border border-emerald-200 text-emerald-800 text-center space-y-2">
                  <CheckCircle2 className="w-8 h-8 mx-auto text-emerald-600 animate-bounce" />
                  <p className="text-sm font-bold">{reviewSuccessMsg}</p>
                </div>
              ) : (
                <form onSubmit={handleReviewSubmit} className="space-y-4">
                  {/* Select Product */}
                  <div>
                    <label className="text-xs font-bold text-gray-700 block mb-1.5">
                      Select Rented Vehicle or Gear
                    </label>
                    <select
                      value={newReview.productId}
                      onChange={(e) => setNewReview({ ...newReview, productId: e.target.value })}
                      className="w-full px-3.5 py-2.5 rounded-xl border border-gray-200 text-xs text-gray-800 font-medium focus:outline-none focus:ring-2 focus:ring-emerald-500/20"
                    >
                      {products.map((p) => (
                        <option key={p.id} value={p.id}>
                          {p.name} ({p.categoryName})
                        </option>
                      ))}
                    </select>
                  </div>

                  {/* Customer Name */}
                  <div>
                    <label className="text-xs font-bold text-gray-700 block mb-1.5">
                      Your Full Name
                    </label>
                    <input
                      type="text"
                      required
                      placeholder="e.g. Aditi Rao"
                      value={newReview.customerName}
                      onChange={(e) => setNewReview({ ...newReview, customerName: e.target.value })}
                      className="w-full px-3.5 py-2.5 rounded-xl border border-gray-200 text-xs text-gray-800 focus:outline-none focus:ring-2 focus:ring-emerald-500/20"
                    />
                  </div>

                  {/* Star Rating Selector */}
                  <div>
                    <label className="text-xs font-bold text-gray-700 block mb-1.5">
                      Rating ({newReview.rating} of 5 Stars)
                    </label>
                    <div className="flex items-center space-x-2">
                      {[1, 2, 3, 4, 5].map((star) => (
                        <button
                          key={star}
                          type="button"
                          onClick={() => setNewReview({ ...newReview, rating: star })}
                          className="p-1 text-gold-400 hover:scale-125 transition-transform"
                        >
                          <Star
                            className={`w-7 h-7 ${
                              star <= newReview.rating ? 'fill-gold-400 text-gold-400' : 'text-gray-300'
                            }`}
                          />
                        </button>
                      ))}
                    </div>
                  </div>

                  {/* Comments */}
                  <div>
                    <label className="text-xs font-bold text-gray-700 block mb-1.5">
                      Your Detailed Experience
                    </label>
                    <textarea
                      required
                      rows={3}
                      placeholder="Describe vehicle condition, pickup handover, equipment performance, or deposit return..."
                      value={newReview.comment}
                      onChange={(e) => setNewReview({ ...newReview, comment: e.target.value })}
                      className="w-full px-3.5 py-2.5 rounded-xl border border-gray-200 text-xs text-gray-800 focus:outline-none focus:ring-2 focus:ring-emerald-500/20"
                    />
                  </div>

                  <div className="pt-2 flex justify-end space-x-3">
                    <button
                      type="button"
                      onClick={() => setIsReviewModalOpen(false)}
                      className="px-4 py-2.5 rounded-xl border border-gray-200 text-xs font-bold text-gray-600 hover:bg-gray-50"
                    >
                      Cancel
                    </button>
                    <button
                      type="submit"
                      className="btn-primary px-6 py-2.5 rounded-xl text-xs font-bold shadow-md"
                    >
                      Publish Review
                    </button>
                  </div>
                </form>
              )}
            </motion.div>
          </div>
        )}
      </AnimatePresence>
    </div>
  );
}
