/**
 * SHOPLOC TAILWIND DESIGN TOKENS
 * Inspiré d'Ollca : Palette Pastel Naturelle & Artisanat de Proximité
 * Généré automatiquement depuis agent_projet/design/design_tokens.json
 */

module.exports = {
  theme: {
    extend: {
      colors: {
        shoploc: {
          slate: {
            DEFAULT: '#243342',
            soft: '#EBF0F5',
            border: '#8B9EAF',
            text: '#1C2D3D'
          },
          terracotta: {
            DEFAULT: '#C26750',
            soft: '#FBEEEA',
            border: '#D88B77',
            text: '#8E3D2A'
          },
          sage: {
            DEFAULT: '#4A7A5B',
            soft: '#EBF3ED',
            border: '#7EA88D',
            text: '#2E583D'
          },
          honey: {
            DEFAULT: '#C48B28',
            soft: '#FEF7EB',
            border: '#DCB162',
            text: '#845A11'
          },
          plum: {
            DEFAULT: '#6E3946',
            soft: '#F6ECEF'
          },
          canvas: '#FAF9F6',
          warm: '#F5F2EB',
          ink: '#1E252D',
          muted: '#5A6578'
        }
      },
      fontFamily: {
        sans: ['"Poppins"', '"Plus Jakarta Sans"', 'Inter', 'sans-serif'],
        serif: ['"Latin Modern Roman"', 'serif'],
        mono: ['"Fira Code"', 'monospace']
      },
      borderRadius: {
        hero: '20px',
        card: '16px',
        pass: '14px',
        touch: '12px',
        badge: '9999px',
        pill: '9999px',
        avatar: '50%'
      },
      boxShadow: {
        craft: '0 2px 8px rgba(36, 51, 66, 0.04)',
        card: '0 4px 16px rgba(36, 51, 66, 0.06)',
        floating: '0 8px 24px rgba(36, 51, 66, 0.12)',
        avatar: '0 4px 12px rgba(36, 51, 66, 0.15)'
      }
    }
  }
};
