---
trigger: always_on
---

# TypeScript with Bun

## Environment Variables
- Use `Bun.env` instead of `process.env` for environment variables
- For Vite projects, prefer `import.meta.env` for client-side environment variables
- No need to install `@types/node` as Bun provides its own type definitions

## Type Safety with Bun
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

## TypeScript Configuration
- Use `strict: true` in `tsconfig.json` for better type safety
- Configure module resolution as needed for your project
- Consider using path aliases for cleaner imports
