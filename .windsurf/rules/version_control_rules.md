---
trigger: always_on
---

# Version Control with Conventional Commits

This project follows the [Conventional Commits](https://www.conventionalcommits.org/) specification for commit messages. This provides a standardized way to document what kind of changes are being made in each commit.

## Commit Message Format

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

## Commit Types
- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation only changes
- `style`: Changes that do not affect the meaning of the code (white-space, formatting, etc.)
- `refactor`: A code change that neither fixes a bug nor adds a feature
- `perf`: A code change that improves performance
- `test`: Adding missing tests or correcting existing tests
- `chore`: Changes to the build process or auxiliary tools and libraries

## Examples
```
feat(auth): add login functionality

docs: update README with installation instructions

fix(ui): correct button alignment in mobile view

refactor(api): simplify user authentication logic
```

## Best Practices
- Use the imperative, present tense ("add" not "added" or "adds")
- Do not end the subject line with a period
- Keep the subject line under 72 characters
- Reference issues and pull requests in the footer when applicable
- Consider starting the commit message with an applicable emoji (optional but recommended)
