-- ==========================================================
-- RENTORA - Initial Seed Data for MySQL 8.0+
-- Test Accounts:
--   Customer: customer@rentora.in / password123
--   Vendor:   vendor@rentora.in   / password123
--   Admin:    admin@rentora.in    / password123
-- ==========================================================

USE rentora_db;

-- 1. SEED USERS (BCrypt Hash for 'password123': $2a$10$r8Q.VfVj9oJ9wXN9z7Ujce3I6i0nZ1qjZ7B/c5vR7uI5hK1m3vXqW)
INSERT INTO users (id, name, email, password, role, phone, status, city, address) VALUES
(1, 'Rahul Sharma', 'customer@rentora.in', '$2a$10$r8Q.VfVj9oJ9wXN9z7Ujce3I6i0nZ1qjZ7B/c5vR7uI5hK1m3vXqW', 'ROLE_CUSTOMER', '+91 98450 11223', 'ACTIVE', 'Bengaluru', 'Flat 402, Green Glen Layout, Bellandur, Bengaluru 560103'),
(2, 'Vikram Verma', 'vendor@rentora.in', '$2a$10$r8Q.VfVj9oJ9wXN9z7Ujce3I6i0nZ1qjZ7B/c5vR7uI5hK1m3vXqW', 'ROLE_VENDOR', '+91 98201 44521', 'ACTIVE', 'Bengaluru', 'Indiranagar 100ft Road, Bengaluru 560038'),
(3, 'Platform Operations Admin', 'admin@rentora.in', '$2a$10$r8Q.VfVj9oJ9wXN9z7Ujce3I6i0nZ1qjZ7B/c5vR7uI5hK1m3vXqW', 'ROLE_ADMIN', '+91 98111 00000', 'ACTIVE', 'Bengaluru', 'Rentora Corporate HQ, Residency Road, Bengaluru 560025');

-- 2. SEED VENDORS
INSERT INTO vendors (id, user_id, business_name, address, city, rating, trust_score) VALUES
(101, 2, 'Apex Cine Rentals', 'Indiranagar 100ft Road, Bengaluru, Karnataka 560038', 'Bengaluru', 4.9, 98),
(104, 2, 'Velocita Superdrive Hub', 'Koramangala 80ft Road, Bengaluru, Karnataka 560034', 'Bengaluru', 4.9, 99),
(105, 2, 'MotoRide Himalayan Hub', 'Indiranagar Metro, Bengaluru, Karnataka 560038', 'Bengaluru', 4.8, 97);

-- 3. SEED CATEGORIES
INSERT INTO categories (id, name, slug, description) VALUES
(1, 'Cameras & Cinematic Gear', 'cameras-gear', 'Full-frame cinema mirrorless cameras, primes, gimbals, and studio lights.'),
(2, 'Drones & Aerial Video', 'drones-aerial', '4K/8K camera drones, remote controllers, and high-wind outdoor flight gear.'),
(3, 'Pro Audio & Sound', 'pro-audio', 'Wireless UHF lavaliers, shotgun boom mics, and portable field recorders.'),
(4, 'Gaming & Virtual Reality', 'gaming-vr', 'Next-gen PlayStation 5, Meta Quest 3, and racing wheel rigs.'),
(5, 'Power Tools & DIY', 'power-tools', 'Brushless cordless drills, demolition rotary hammers, and pressure washers.'),
(6, 'Outdoor & Adventure Gear', 'outdoor-adventure', '4-season alpine mountaineering tents, expedition backpacks, and kayaks.'),
(7, 'Self-Drive & Luxury Cars', 'cars-vehicles', 'Self-drive 4x4 SUVs, premium German sedans, and electric vehicles for business and weekend road trips.'),
(8, 'Superbikes & Touring Motorcycles', 'bikes-motorcycles', 'Adventure touring motorcycles, high-displacement superbikes, and city cruisers with protective riding gear.');

-- 4. SEED PRODUCTS
INSERT INTO products (id, vendor_id, category_id, name, description, price_per_day, deposit, availability, stock_count, image_url, rating, review_count) VALUES
(1, 101, 1, 'Sony FX3 Cinema Line Full-Frame Camera', 'Compact cinema camera with 12.1MP full-frame sensor, 4K 120p, dual CFexpress slots, and XLR top handle.', 2800.00, 8500.00, TRUE, 3, 'https://images.unsplash.com/photo-1516035069371-29a1b244cc32?auto=format&fit=crop&w=900&q=80', 4.9, 42),
(2, 101, 2, 'DJI Mavic 3 Pro Cine Combo Drone', 'Tri-camera drone with Hasselblad 4/3 CMOS, Apple ProRes 422 HQ, and 43-min flight time.', 3500.00, 12000.00, TRUE, 2, 'https://images.unsplash.com/photo-1508614589041-895b88991e3e?auto=format&fit=crop&w=900&q=80', 4.9, 38),
(3, 101, 3, 'Sennheiser EW-DP ME2 Wireless Microphone System', 'Digital UHF wireless microphone system with 134 dB input dynamic range and magnetic receiver.', 1200.00, 3500.00, TRUE, 5, 'https://images.unsplash.com/photo-1590602847861-f357a9332bbc?auto=format&fit=crop&w=900&q=80', 4.8, 29),
(4, 101, 1, 'DJI RS 3 Pro 3-Axis Gimbal Stabilizer', 'Automated axis locks, carbon fiber arms, 4.5kg tested payload, and LiDAR focusing.', 1500.00, 4500.00, TRUE, 4, 'https://images.unsplash.com/photo-1584006682522-dc17d6c0d9ac?auto=format&fit=crop&w=900&q=80', 4.7, 31),
(5, 101, 4, 'Sony PlayStation 5 Disc Edition + 2 Controllers', '825GB Ultra-High Speed SSD, 4K 120Hz output, Ray Tracing, and DualSense haptics.', 950.00, 5000.00, TRUE, 3, 'https://images.unsplash.com/photo-1606813907291-d86efa9b94db?auto=format&fit=crop&w=900&q=80', 4.9, 56),
(9, 104, 7, 'Mahindra Thar 4x4 Hard-Top Diesel Auto', 'Iconic 4x4 off-road SUV featuring 2.2L mHawk Turbo Diesel, 6-speed auto, mechanical locking differential, and Apple CarPlay.', 3800.00, 10000.00, TRUE, 4, 'https://images.unsplash.com/photo-1533473359331-0135ef1b58bf?auto=format&fit=crop&w=900&q=80', 4.9, 64),
(10, 104, 7, 'BMW 330i M-Sport Luxury Sedan', 'Premier executive sport sedan with 2.0L TwinPower Turbo (258 HP), rear-wheel drive, Harman Kardon audio, and launch control.', 7500.00, 25000.00, TRUE, 2, 'https://images.unsplash.com/photo-1555215695-3004980ad54e?auto=format&fit=crop&w=900&q=80', 5.0, 41),
(11, 105, 8, 'Royal Enfield Himalayan 450 Adventure Tourer', 'All-new Sherpa 450cc liquid-cooled engine (40 PS), Showa USD suspension, Tripper TFT navigation, and dual-purpose luggage.', 1400.00, 4000.00, TRUE, 5, 'https://images.unsplash.com/photo-1558981403-c5f9899a28bc?auto=format&fit=crop&w=900&q=80', 4.9, 53),
(12, 105, 8, 'Kawasaki Ninja ZX-6R 636cc Supersport', 'Race-bred inline-4 engine (130 PS), bi-directional quickshifter, Showa SFF-BP forks, and Brembo M4.32 radial monobloc calipers.', 3200.00, 12000.00, TRUE, 2, 'https://images.unsplash.com/photo-1568772585407-9361f9bf3a87?auto=format&fit=crop&w=900&q=80', 4.8, 35);

-- 5. SEED RENTALS
INSERT INTO rentals (id, customer_id, product_id, start_date, end_date, status, total_amount, deposit, delivery_address, tracking_number) VALUES
(1001, 1, 1, '2026-09-08', '2026-09-11', 'ACTIVE', 18412.00, 8500.00, 'Flat 402, Green Glen Layout, Bellandur, Bengaluru 560103', 'TRK-2026-892144'),
(1002, 1, 2, '2026-09-15', '2026-09-18', 'PENDING', 24390.00, 12000.00, 'Flat 402, Green Glen Layout, Bellandur, Bengaluru 560103', 'TRK-2026-903125'),
(1003, 1, 5, '2026-08-20', '2026-08-24', 'COMPLETED', 9484.00, 5000.00, 'Flat 402, Green Glen Layout, Bellandur, Bengaluru 560103', 'TRK-2026-778210');

-- 6. SEED RETURNS
INSERT INTO returns (id, rental_id, status, damage_report, damage_fee, deposit_refunded, return_date) VALUES
(501, 1003, 'SETTLED', 'No damage. All controllers and cables returned in original packaging.', 0.00, 5000.00, '2026-08-24');

-- 7. SEED PAYMENTS
INSERT INTO payments (id, rental_id, amount, payment_status, payment_method, transaction_ref, payment_date) VALUES
(901, 1001, 18412.00, 'PAID', 'UPI / NetBanking', 'UPI-RENT-993814', '2026-09-02 14:32:00'),
(902, 1002, 24390.00, 'HELD_IN_ESCROW', 'Credit Card (Visa)', 'CC-RENT-881290', '2026-09-03 09:15:00'),
(903, 1003, 9484.00, 'REFUNDED', 'UPI / NetBanking', 'UPI-RENT-771829', '2026-08-18 16:45:00');

-- 8. SEED REVIEWS
INSERT INTO reviews (id, customer_id, product_id, rating, comment, created_at) VALUES
(1, 1, 1, 5, 'The Sony FX3 was in brand new condition with 3 freshly charged batteries. Pickup was effortless!', '2026-08-12 11:30:00'),
(2, 4, 2, 5, 'Used the Mavic 3 Pro for an aerial wedding shoot in Goa. Drone had latest firmware and the ProRes footage was jaw-dropping!', '2026-08-25 15:10:00'),
(3, 2, 9, 5, 'Rented the Mahindra Thar 4x4 for a weekend drive to Chikmagalur. Handled slushy estate trails effortlessly. 100% deposit refunded in 4 hours!', '2026-08-30 18:20:00'),
(4, 3, 10, 5, 'Booked the BMW 330i M-Sport for our wedding entry in Mumbai. Delivered right on time, sparkling clean, polite OTP verification.', '2026-08-28 10:45:00'),
(5, 1, 11, 5, 'Took the Himalayan 450 for a 4-day Nilgiris loop. Showa suspension eats potholes for breakfast and panniers kept gear dry.', '2026-08-15 17:00:00'),
(6, 4, 12, 5, 'Rented the Ninja ZX-6R for an open track day at Irungattukottai circuit. Quickshifter and Diablo Rosso tyres gave intense confidence.', '2026-07-22 14:15:00');
