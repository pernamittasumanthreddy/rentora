/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        forest: {
          50: '#f0fdf4',
          100: '#dcfce7',
          200: '#bbf7d0',
          300: '#86efac',
          400: '#4ade80',
          500: '#22c55e',
          600: '#16a34a',
          700: '#15803d',
          800: '#166534',
          900: '#14532D', // Primary Brand Forest Green
          950: '#052e16',
        },
        emerald: {
          50: '#ecfdf5',
          100: '#d1fae5',
          200: '#a7f3d0',
          300: '#6ee7b7',
          400: '#34d399',
          500: '#10B981', // Secondary Emerald
          600: '#059669',
          700: '#047857',
          800: '#065f46',
          900: '#064e3b',
        },
        gold: {
          50: '#fffbeb',
          100: '#fef3c7',
          200: '#fde68a',
          300: '#fcd34d',
          400: '#fbbf24',
          500: '#f59e0b',
          600: '#D97706', // Accent Gold
          700: '#b45309',
          800: '#92400e',
          900: '#78350f',
        },
        sand: {
          50: '#faf9f6',
          100: '#F8F7F4', // Brand Background
          200: '#efece6',
          300: '#e2ded5',
          400: '#c5bfb4',
          500: '#a69e90',
        },
        bungalow: {
          50: '#FAF8F5',
          100: '#F5F1E8', // Soft bungalow beige base
          200: '#EBE4D5',
          300: '#DFD5C2',
          400: '#C8BCA4',
          500: '#B3A387',
          600: '#9A876A',
        },
        hunter: {
          50: '#F1F7F4',
          100: '#E1EFE8',
          200: '#BFDFD1',
          300: '#92C6B0',
          400: '#5EA78B',
          500: '#40916C',
          600: '#2D6A4F',
          700: '#1F4E3A',
          800: '#173B2B',
          900: '#0F291E', // Deep Hunter Green Accent
          950: '#07190F',
        },
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', '-apple-system', 'sans-serif'],
        display: ['Plus Jakarta Sans', 'Inter', 'sans-serif'],
      },
      boxShadow: {
        'soft': '0 2px 15px -3px rgba(0, 0, 0, 0.05), 0 4px 6px -2px rgba(0, 0, 0, 0.025)',
        'card': '0 4px 20px -2px rgba(20, 83, 45, 0.06), 0 2px 6px -1px rgba(0, 0, 0, 0.04)',
        'glow': '0 0 25px -5px rgba(16, 185, 129, 0.25)',
        'elevation-1': '0 2px 10px -2px rgba(15, 41, 30, 0.05), 0 1px 3px rgba(0, 0, 0, 0.03)',
        'elevation-2': '0 10px 30px -4px rgba(15, 41, 30, 0.08), 0 4px 10px -2px rgba(0, 0, 0, 0.04)',
        'elevation-3': '0 24px 50px -8px rgba(15, 41, 30, 0.14), 0 8px 20px -4px rgba(0, 0, 0, 0.05)',
        'glass': '0 8px 32px 0 rgba(15, 41, 30, 0.08)',
      },
      animation: {
        'sheen': 'sheen 4s cubic-bezier(0.4, 0, 0.2, 1) infinite',
        'pulse-subtle': 'pulseSubtle 6s ease-in-out infinite',
      },
      keyframes: {
        sheen: {
          '0%, 100%': { transform: 'translateX(-120%)' },
          '40%, 60%': { transform: 'translateX(120%)' },
        },
        pulseSubtle: {
          '0%, 100%': { opacity: '0.4', transform: 'scale(1)' },
          '50%': { opacity: '0.7', transform: 'scale(1.05)' },
        },
      },
    },
  },
  plugins: [],
};
