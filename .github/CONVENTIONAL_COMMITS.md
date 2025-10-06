# Conventional Commits Quick Reference

This project **requires** [Conventional Commits](https://conventionalcommits.org/) for all commits and PR titles.

## Format

```
<type>(<scope>): <description>

[optional body]

[optional footer(s)]
```

## Types

| Type | When to Use | Example |
|------|-------------|---------|
| `feat` | New feature | `feat: add visual overlay` |
| `fix` | Bug fix | `fix: resolve click position bug` |
| `docs` | Documentation only | `docs: update README installation` |
| `style` | Code style/formatting | `style: format with ruff` |
| `refactor` | Code change (no bug fix or feature) | `refactor: simplify clicker logic` |
| `perf` | Performance improvement | `perf: optimize click rate calculation` |
| `test` | Adding/updating tests | `test: add overlay unit tests` |
| `build` | Build system/dependencies | `build: update pyinstaller to 6.0` |
| `ci` | CI/CD changes | `ci: add CodeQL workflow` |
| `chore` | Maintenance tasks | `chore: update pre-commit hooks` |

## Scopes (Optional)

| Scope | Description |
|-------|-------------|
| `gui` | GUI-related changes |
| `core` | Core functionality |
| `overlay` | Overlay system |
| `config` | Configuration files |
| `build` | Build system |
| `ci` | CI/CD |
| `deps` | Dependencies |

## Examples

### Simple Commits

```bash
git commit -m "feat: add click counter display"
git commit -m "fix: resolve button alignment issue"
git commit -m "docs: add installation instructions"
```

### With Scope

```bash
git commit -m "feat(gui): add transparency slider"
git commit -m "fix(overlay): correct position calculation"
git commit -m "refactor(core): simplify click logic"
```

### With Body

```bash
git commit -m "feat(gui): add settings panel

- Add transparency control
- Add position adjustment
- Save settings to config file"
```

### Breaking Changes

Use `!` after type or add `BREAKING CHANGE:` in footer:

```bash
git commit -m "feat!: change config file format"
```

Or:

```bash
git commit -m "feat: change config file format

BREAKING CHANGE: Config file now uses TOML instead of JSON.
Users must migrate their config files."
```

### Multiple Changes

```bash
git commit -m "feat(gui): add settings panel

- Add transparency slider (0-100%)
- Add position controls (X/Y)
- Add save/load functionality
- Update UI layout

Closes #42"
```

## PR Titles

PR titles **must** also follow conventional commits:

✅ **Valid:**
- `feat: add visual overlay indicator`
- `fix(gui): resolve button alignment`
- `docs: update installation guide`

❌ **Invalid:**
- `Add feature` (missing type)
- `Feat: Add feature` (type should be lowercase)
- `feat: Add feature` (description should start lowercase)
- `feature: add feature` (invalid type)

## Rules

1. **Type**: Must be one of the valid types (lowercase)
2. **Scope**: Optional, must be lowercase if used
3. **Description**:
   - Must start with lowercase letter
   - No period at the end
   - Imperative mood ("add" not "added" or "adds")
4. **Body**: Optional, separated by blank line
5. **Footer**: Optional, for breaking changes or issue references

## Validation

### Local (Pre-commit)

When you commit, `commitlint` validates your message:

```bash
$ git commit -m "Add feature"
❌ type must be one of [feat, fix, docs, ...]

$ git commit -m "feat: add feature"
✅ Commit successful
```

### CI (GitHub Actions)

When you open a PR:
1. PR title is validated
2. All commits are validated
3. If invalid, you'll get a comment with help

## Common Mistakes

### ❌ Wrong Type Case

```bash
git commit -m "Feat: add feature"  # Type should be lowercase
```

✅ **Correct:**
```bash
git commit -m "feat: add feature"
```

### ❌ Wrong Description Case

```bash
git commit -m "feat: Add feature"  # Description should start lowercase
```

✅ **Correct:**
```bash
git commit -m "feat: add feature"
```

### ❌ Invalid Type

```bash
git commit -m "feature: add feature"  # 'feature' is not a valid type
```

✅ **Correct:**
```bash
git commit -m "feat: add feature"
```

### ❌ Missing Colon

```bash
git commit -m "feat add feature"  # Missing colon after type
```

✅ **Correct:**
```bash
git commit -m "feat: add feature"
```

### ❌ Period at End

```bash
git commit -m "feat: add feature."  # No period at end
```

✅ **Correct:**
```bash
git commit -m "feat: add feature"
```

## Tips

1. **Use imperative mood**: "add" not "added" or "adds"
2. **Be concise**: Keep description under 50 characters
3. **Use body for details**: Explain what and why, not how
4. **Reference issues**: Use `Fixes #123` in footer
5. **Test locally**: Run `pre-commit run --all-files` before pushing

## Need Help?

- **Full Guide**: [CONTRIBUTING.md](../CONTRIBUTING.md#commit-guidelines)
- **Specification**: [conventionalcommits.org](https://conventionalcommits.org/)
- **Examples**: Check the commit history of this repo

## Troubleshooting

### Pre-commit hook fails?

```bash
# Check your commit message format
git commit -m "feat: your message here"

# Skip hooks (not recommended)
git commit --no-verify
```

### PR validation fails?

1. Check PR title format
2. Check all commit messages
3. Read the auto-comment for specific errors
4. Amend commits if needed:
   ```bash
   git commit --amend -m "feat: correct message"
   git push --force
   ```

---

**Remember**: Conventional Commits are **required**. PRs with invalid commits will be rejected by CI.
