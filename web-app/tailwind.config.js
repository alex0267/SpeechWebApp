// tailwind.config.js
const defaultTheme = require('tailwindcss/defaultTheme')

module.exports = {
    purge: [],
    theme: {
      screens: {
        'sm': '400px',
        // => @media (min-width: 400px) { ... }
  
        'md': '400px',
        // => @media (min-width: 400px) { ... }
  
        'lg': '1024px',
        // => @media (min-width: 1024px) { ... }
  
        'xl': '1280px',
        // => @media (min-width: 1280px) { ... }
  
        '2xl': '1536px',
        // => @media (min-width: 1536px) { ... }
      },
      extend: {
        colors: {
          'electric-blue': {
            light: '#0023FF',
            DEFAULT: '#0023FF',
            dark: '#0023FF',
          },
          'ftv-yellow': '#FBFC00'
        },
        fontFamily: {
          'sans': ['FranceTVBrown', ...defaultTheme.fontFamily.sans],
        },
      }
    },
    variants: {
      extend: {
       backgroundColor: ['active'],
      }
    }
  }