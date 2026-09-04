/**
 * RENTORA - Formatting & Business Calculation Utilities
 */

export const formatCurrency = (amount) => {
  return new Intl.NumberFormat('en-IN', {
    style: 'currency',
    currency: 'INR',
    maximumFractionDigits: 0,
  }).format(amount || 0);
};

export const formatDate = (dateString) => {
  if (!dateString) return '';
  const date = new Date(dateString);
  return new Intl.DateTimeFormat('en-IN', {
    day: 'numeric',
    month: 'short',
    year: 'numeric',
  }).format(date);
};

export const calculateDaysBetween = (startDate, endDate) => {
  if (!startDate || !endDate) return 1;
  const start = new Date(startDate);
  const end = new Date(endDate);
  const diffTime = Math.abs(end - start);
  const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
  return Math.max(1, diffDays);
};

export const calculateRentalPricing = (pricePerDay, deposit, days) => {
  const rentalFee = (pricePerDay || 0) * (days || 1);
  // GST @ 18% (9% CGST + 9% SGST)
  const gst = Math.round(rentalFee * 0.18);
  const totalPayable = rentalFee + (deposit || 0) + gst;

  return {
    days: days || 1,
    dailyRate: pricePerDay,
    rentalFee,
    deposit: deposit || 0,
    cgst: Math.round(gst / 2),
    sgst: Math.round(gst / 2),
    totalGst: gst,
    totalPayable,
  };
};
