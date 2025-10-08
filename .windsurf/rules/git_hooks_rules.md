---
trigger: always_on
---

# Git Hooks with Husky

This project uses [Husky](https://typicode.github.io/husky/) to manage Git hooks. Hooks are scripts that run automatically when certain Git events occur.

## Available Hooks

### Pre-commit Hook
Runs before each commit to ensure code quality:
1. Applies Biome's formatting and linting to staged files
2. Automatically stages any formatting changes
3. Prevents commit if there are linting errors

### Pre-push Hook
Runs before pushing to the remote repository:
1. Runs the linter on the entire codebase
2. Runs the test suite
3. Prevents push if any checks fail

## Configuration

### `package.json`
```json
"scripts": {
  "lint": "biome check",
  "lint:fix": "biome check --write",
  "test": "bun test"
},
"lint-staged": {
  "*.{js,jsx,ts,tsx,json,css,md}": [
    "bun run lint:fix --no-errors-on-unmatched",
    "bun run lint --no-errors-on-unmatched"
  ]
}
```

### `.husky/pre-commit`
```bash
#!/usr/bin/env sh
. "$(dirname "$0")/_/husky.sh"

bunx lint-staged
```

### `.husky/pre-push`
```bash
#!/usr/bin/env sh
. "$(dirname "$0")/_/husky.sh"

bun run lint
echo "✅ Linting passed!"

# Uncomment when tests are added
# bun test
# echo "✅ Tests passed!"
```

## Adding New Hooks

To add a new hook, use the Husky CLI:

```bash
bunx husky add .husky/pre-rebase "bun run lint"
```

## Skipping Hooks (When Needed)

To temporarily bypass hooks, use the `--no-verify` flag:

```bash
git commit -m "WIP: Work in progress" --no-verify
```

## Troubleshooting

- If hooks aren't running, ensure they're executable:
  ```bash
  chmod +x .husky/*
  ```
- To see debug output, run with:
  ```bash
  HUSKY_DEBUG=1 git commit -m "Your message"
  ```
