---
trigger: always_on
---

# Development Rules for CookieAutoClicker

## Package Management with Bun

This workspace uses [Bun](https://bun.sh/) as the package manager. All package management operations should be performed using Bun commands.

### Commands to Use
- Install packages: `bun install`
- Add a dependency: `bun add <package>`
- Add a dev dependency: `bun add -d <package>`
- Run scripts: `bun run <script>`
- Execute a package binary: `bunx <package>`

## Version Control with Conventional Commits

This project follows the [Conventional Commits](https://www.conventionalcommits.org/) specification for commit messages. This provides a standardized way to document what kind of changes are being made in each commit.

### Commit Message Format

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### Commit Types
- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation only changes
- `style`: Changes that do not affect the meaning of the code (white-space, formatting, etc.)
- `refactor`: A code change that neither fixes a bug nor adds a feature
- `perf`: A code change that improves performance
- `test`: Adding missing tests or correcting existing tests
- `chore`: Changes to the build process or auxiliary tools and libraries

### Examples
```
feat(auth): add login functionality

docs: update README with installation instructions

fix(ui): correct button alignment in mobile view

refactor(api): simplify user authentication logic
```

### Best Practices
- Use the imperative, present tense ("add" not "added" or "adds")
- Do not end the subject line with a period
- Keep the subject line under 72 characters
- Reference issues and pull requests in the footer when applicable
- Consider starting the commit message with an applicable emoji (optional but recommended)

## Styling with Tailwind CSS

This project uses [Tailwind CSS](https://tailwindcss.com/) for styling. Follow these guidelines for consistent styling:

### Installation and Setup
- Install Tailwind and its dependencies: `bun add -d tailwindcss postcss autoprefixer`
- Initialize Tailwind: `bunx tailwindcss init -p`

### Best Practices
1. **Utility-First Approach**
   - Use Tailwind's utility classes directly in your HTML/JSX
   - Prefer composition of utility classes over custom CSS
   - Use `@apply` in your CSS only for complex, reusable components

2. **Responsive Design**
   - Use Tailwind's responsive prefixes (e.g., `md:`, `lg:`) for responsive designs
   - Follow mobile-first approach in your styling

3. **Customization**
   - Extend the theme in `tailwind.config.js` for project-specific design tokens
   - Add custom colors, spacing, and other design tokens in the config file

4. **Performance**
   - Configure `content` in `tailwind.config.js` to include only the files that contain Tailwind classes
   - Use PurgeCSS in production builds to remove unused styles

### Example Component
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

## Tauri Development

### Project Structure
- Frontend code: `/src`
- Tauri configuration: `/src-tauri`
  - Rust source: `/src-tauri/src`
  - Icons: `/src-tauri/icons`
  - Configuration: `/src-tauri/tauri.conf.json`

### Development Commands
- Start development server: `bun tauri dev`
- Build application: `bun tauri build`
- Check Rust code: `cargo check` (in `/src-tauri`)
- Format Rust code: `cargo fmt` (in `/src-tauri`)

### Best Practices
1. **Rust Backend**
   - Keep business logic in Rust for better performance
   - Use `#[tauri::command]` to expose Rust functions to the frontend
   - Handle errors properly and return meaningful error messages

2. **Frontend**
   - Use TypeScript for type safety
   - Keep components small and focused
   - Use Tauri's IPC system for frontend-backend communication

3. **Performance**
   - Minimize data transfer between Rust and JavaScript
   - Use web workers for CPU-intensive tasks
   - Optimize asset loading

### Common Tauri Commands
- `tauri info` - Show Tauri environment information
- `tauri dev` - Start development server
- `tauri build` - Build the application
- `tauri version` - Show Tauri version

## Example Workflow
```bash
# Install dependencies
bun install

# Start development server with hot reloading
bun tauri dev

# Build for production
bun tauri build
```

## TypeScript with Bun

When working with TypeScript in a Bun environment, follow these guidelines:

### Environment Variables
- Use `Bun.env` instead of `process.env` for environment variables
- For Vite projects, prefer `import.meta.env` for client-side environment variables
- No need to install `@types/node` as Bun provides its own type definitions

### Type Safety with Bun
- Bun provides built-in TypeScript types for its APIs
- For custom environment variables, extend the global `Bun` namespace:
  ```typescript
  declare global {
    namespace Bun {
      interface Env {
        TAURI_DEV_HOST?: string;
        // Add other environment variables here
      }
    }
  }
  ```

## Linting and Formatting
- Use ESLint for JavaScript/TypeScript linting
- Use Prettier for code formatting
- Configure your editor to format on save
- Run `bun run lint` to check for linting errors
- Run `bun run format` to format all files
