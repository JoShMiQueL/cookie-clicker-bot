---
trigger: always_on
---

# Package Management with Bun

This workspace uses [Bun](https://bun.sh/) as the package manager. All package management operations should be performed using Bun commands.

## Commands to Use
- Install packages: `bun install`
- Add a dependency: `bun add <package>`
- Add a dev dependency: `bun add -d <package>`
- Run scripts: `bun run <script>`
- Execute a package binary: `bunx <package>`

## Versioning
- Always use exact versions (e.g., `"package": "1.2.3"`) in `package.json`
- Avoid using `^` or `~` version specifiers
- Regularly check for updates using `bun outdated`
- Test thoroughly before updating any dependency
