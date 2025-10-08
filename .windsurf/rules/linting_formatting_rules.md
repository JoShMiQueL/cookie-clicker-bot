---
trigger: always_on
---

# Code Style and Formatting Rules

## General Guidelines
- **Indentation**: 2 spaces
- **Quotes**: Single quotes (`'`) for JavaScript/TypeScript
- **Semicolons**: Always use semicolons
- **Line Length**: Maximum 100 characters
- **Trailing Commas**: Required in multi-line objects and arrays
- **Parentheses**: Required for arrow function parameters with more than one parameter

## Linting Rules
- TypeScript strict mode is enabled
- No unused variables
- Avoid `any` type (use proper types instead)
- No `console.log` in production code
- Prefer `const` over `let`
- Use strict equality (`===` and `!==`)

## Import/Export
- Group imports in this order:
  1. External dependencies
  2. Internal absolute imports
  3. Internal relative imports
  4. Type imports (with `type` keyword)
- Use named exports over default exports
- Sort imports alphabetically within each group

## React Specific
- Use functional components with TypeScript interfaces for props
- Follow React Hooks rules
- Destructure props in function parameters
- Use `React.FC` type for functional components or explicitly type props

## File Naming
- **Components**: `PascalCase.tsx` (e.g., `Button.tsx`)
- **Utilities/Helpers**: `kebab-case.ts` (e.g., `format-date.ts`)
- **Tests**: `*.test.ts` or `*.test.tsx`
- **Type Definitions**: `*.d.ts`

## TypeScript Best Practices
- Use interfaces for object shapes
- Prefer `type` over `interface` for simple types
- Use `readonly` for immutable properties
- Use `as const` for literal types when appropriate
- Avoid `@ts-ignore` or `@ts-expect-error` without explanation

## Comments
- Use JSDoc for public APIs and complex functions
- Keep comments up-to-date with the code
- Prefer self-documenting code over comments
- Use `// TODO:` for temporary notes

## Biome Configuration
This project uses Biome with the following key configurations:
- Single quotes for strings
- 2 spaces indentation
- 100 characters line length
- Semicolons required
- Trailing commas in multi-line objects/arrays
- JSX/TSX uses single quotes
- Organized imports

## Auto-formatting
- The project is configured to automatically format code on save
- The pre-commit hook will format and fix linting issues
- No manual formatting should be necessary if the editor is properly configured
