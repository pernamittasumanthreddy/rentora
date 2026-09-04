import React, { createContext, useContext, useState, useEffect } from 'react';
import { calculateRentalPricing, calculateDaysBetween } from '../utils/formatters';

const CartContext = createContext(null);

export const CartProvider = ({ children }) => {
  const [cartItem, setCartItem] = useState(null);
  const [rentalDates, setRentalDates] = useState({
    startDate: new Date(Date.now() + 86400000).toISOString().split('T')[0], // tomorrow
    endDate: new Date(Date.now() + 86400000 * 4).toISOString().split('T')[0], // 3 days
  });
  const [deliveryOption, setDeliveryOption] = useState('DELIVERY'); // 'DELIVERY' or 'PICKUP'

  useEffect(() => {
    const saved = localStorage.getItem('rentora_cart');
    if (saved) {
      try {
        const parsed = JSON.parse(saved);
        setCartItem(parsed.product);
        if (parsed.dates) setRentalDates(parsed.dates);
        if (parsed.delivery) setDeliveryOption(parsed.delivery);
      } catch {
        localStorage.removeItem('rentora_cart');
      }
    }
  }, []);

  const saveCart = (product, dates, delivery) => {
    setCartItem(product);
    if (dates) setRentalDates(dates);
    if (delivery) setDeliveryOption(delivery);
    localStorage.setItem(
      'rentora_cart',
      JSON.stringify({
        product,
        dates: dates || rentalDates,
        delivery: delivery || deliveryOption,
      })
    );
  };

  const clearCart = () => {
    setCartItem(null);
    localStorage.removeItem('rentora_cart');
  };

  const days = calculateDaysBetween(rentalDates.startDate, rentalDates.endDate);
  const pricing = cartItem
    ? calculateRentalPricing(cartItem.pricePerDay, cartItem.deposit, days)
    : null;

  return (
    <CartContext.Provider
      value={{
        cartItem,
        rentalDates,
        setRentalDates,
        deliveryOption,
        setDeliveryOption,
        saveCart,
        clearCart,
        pricing,
        days,
      }}
    >
      {children}
    </CartContext.Provider>
  );
};

export const useCart = () => useContext(CartContext);
