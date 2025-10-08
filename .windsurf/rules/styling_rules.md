---
trigger: always_on
---

# Styling with Tailwind CSS

This project uses [Tailwind CSS](https://tailwindcss.com/) for styling. Follow these guidelines for consistent styling:

## Best Practices

### 1. Utility-First Approach
- Use Tailwind's utility classes directly in your HTML/JSX
- Prefer composition of utility classes over custom CSS
- Use `@apply` in your CSS only for complex, reusable components

### 2. Responsive Design
- Use Tailwind's responsive prefixes (e.g., `md:`, `lg:`) for responsive designs
- Follow mobile-first approach in your styling

### 3. Customization
- Extend the theme in `tailwind.config.js` for project-specific design tokens
- Add custom colors, spacing, and other design tokens in the config file

### 4. Performance
- Configure `content` in `tailwind.config.js` to include only the files that contain Tailwind classes
- Use PurgeCSS in production builds to remove unused styles

## Example Component

```tsx
import React, { ReactNode } from 'react';

type ButtonVariant = 'primary' | 'secondary' | 'danger';

interface ButtonProps {
  children: ReactNode;
  variant?: ButtonVariant;
  onClick?: () => void;
  className?: string;
}

export const Button: React.FC<ButtonProps> = ({
  children,
  variant = 'primary',
  onClick,
  className = ''
}) => {
  const baseClasses = 'px-4 py-2 rounded font-medium transition-colors';
  const variantClasses: Record<ButtonVariant, string> = {
    primary: 'bg-blue-600 text-white hover:bg-blue-700',
    secondary: 'bg-gray-200 text-gray-800 hover:bg-gray-300',
    danger: 'bg-red-600 text-white hover:bg-red-700'
  };

  return (
    <button
      type="button"
      className={`${baseClasses} ${variantClasses[variant]} ${className}`}
      onClick={onClick}
    >
      {children}
    </button>
  );
};
```
