# GitHub Actions Workflows

This document describes all automated workflows in this repository.

## 📋 Table of Contents

- [CI Pipeline Hierarchy](#ci-pipeline-hierarchy)
- [Code Quality](#code-quality)
- [Build & Release](#build--release)
- [PR Automation](#pr-automation)
- [Maintenance](#maintenance)
- [Issue Templates](#issue-templates)

## CI Pipeline Hierarchy

The CI/CD pipeline follows a hierarchical structure to ensure quality:

```
┌─────────────────────────────────────┐
│  Stage 1: Quality Checks (Parallel) │
├─────────────────────────────────────┤
│  • Lint & Format (pre-commit)       │
│  • PR Validation (title, branch)    │
└─────────────────────────────────────┘
              ↓ (only if all pass)
┌─────────────────────────────────────┐
│  Stage 2: Build                      │
├─────────────────────────────────────┤
│  • Build Executable                  │
│  • Generate Checksums                │
│  • Upload Artifacts                  │
│  • Comment PR with Build Info        │
└─────────────────────────────────────┘
```

**Key Benefits:**
- ⚡ Fast feedback (parallel checks)
- 🛡️ No builds on failing code
- 💰 Saves CI minutes
- ✅ Ensures quality before build

**Main Workflow:** `ci-pipeline.yml`

## Code Quality

### CI Pipeline (`ci-pipeline.yml`)
**Triggers:** Push, Pull Request, Manual
**Purpose:** Orchestrates all quality checks and build process

**Stage 1 - Quality Checks (Parallel):**
- Lint & Format with pre-commit
- PR validation (title, branch name)

**Stage 2 - Build (Only if Stage 1 passes):**
- Build executable
- Generate checksums
- Upload artifacts
- Comment PR with build info

### CodeQL (`codeql.yml`)
**Triggers:** Push, Pull Request, Weekly schedule
**Purpose:** Security and quality analysis

- Scans for security vulnerabilities
- Detects code quality issues
- Runs security-and-quality queries
- Weekly automated scans

### Dependency Review (`dependency-review.yml`)
**Triggers:** Pull Request
**Purpose:** Reviews dependency changes

- Checks for vulnerable dependencies
- Fails on moderate+ severity issues
- Comments summary in PR

## Build & Release

### CI Pipeline (`ci-pipeline.yml`)
**Triggers:** Push, Pull Request, Manual
**Purpose:** Main CI/CD pipeline with hierarchical execution

**Stage 1 - Quality Checks (Parallel):**
- Lint & Format with pre-commit
- PR validation (title, branch name)

**Stage 2 - Build (Only if Stage 1 passes):**
- Builds with PyInstaller
- Calculates executable size
- Generates SHA256 checksum
- Uploads artifacts (30 days retention)
- Comments PR with build info

**Artifacts:**
- `CookieClickerBot-{sha}.exe`
- `build-info-{sha}.txt`

### Release (`release.yml`)
**Triggers:** Tags (`v*.*.*`, `v*.*.*-beta.*`, `v*.*.*-alpha.*`, `v*.*.*-rc.*`), Manual
**Purpose:** Automated releases

**Release Types:**

| Trigger | Type | Prerelease | Example |
|---------|------|------------|---------|
| `v*.*.*` tag | Production | No | `v1.0.0` |
| `v*.*.*-beta.*` tag | Beta | Yes | `v1.0.0-beta.1` |
| `v*.*.*-alpha.*` tag | Alpha | Yes | `v1.0.0-alpha.1` |
| `v*.*.*-rc.*` tag | Release Candidate | Yes | `v1.0.0-rc.1` |
| Manual workflow | Custom | Configurable | Any version |

**Features:**
- Generates detailed release notes with badges (🚀 🧪 ⚗️ 🎯)
- Includes SHA256 checksum verification
- Auto-updates `latest` tag for production releases
- Warns users about pre-release versions

**Release Assets:**
- `CookieClickerBot.exe`
- `CookieClickerBot.exe.sha256`

**Manual Release:**
1. Go to Actions → Release
2. Click "Run workflow"
3. Enter version (e.g., `v1.0.0-beta.1`)
4. Check "Mark as pre-release" if needed
5. Click "Run workflow"

### Changelog (`changelog.yml`)
**Triggers:** Tags (`v*.*.*`), Manual
**Purpose:** Generates changelog

- Uses git-cliff
- Follows conventional commits
- Auto-commits to repository

## PR Automation

### PR Labeler & Statistics (`pr-labeler.yml`)
**Triggers:** PR opened/updated
**Purpose:** Auto-labels pull requests and generates statistics

**Features:**

**1. Auto-Labeling:**

**By Size:**
- `size/xs` - < 10 lines
- `size/s` - 10-100 lines
- `size/m` - 100-500 lines
- `size/l` - 500-1000 lines
- `size/xl` - > 1000 lines

**By Area:**
- `area/gui` - GUI changes
- `area/core` - Core functionality
- `area/build` - Build system
- `area/ci` - CI/CD
- `area/docs` - Documentation
- `area/tests` - Tests

**By Type (from PR title):**
- `type/feature` - `feat:`
- `type/bug` - `fix:`
- `type/documentation` - `docs:`
- `type/style` - `style:`
- `type/refactor` - `refactor:`
- `type/performance` - `perf:`
- `type/test` - `test:`
- `type/chore` - `chore:`
- `type/ci` - `ci:`
- `type/build` - `build:`

**Special:**
- `breaking-change` - Contains `!:` or `BREAKING CHANGE`
- `needs-description` - PR body < 10 chars

**2. PR Statistics Comment:**

Automatically posts a beautiful statistics comment with:
- 📈 Changes overview table (additions, deletions, net change)
- 📁 Files changed/added/modified/deleted
- 📝 Commit count
- 📦 PR size indicator (🟢 XS/S / 🟡 M / 🟠 L / 🔴 XL)
- 📄 Top 5 file types
- 💡 Auto-updates on each push (no spam)

### PR Checks (`pr-checks.yml`)
**Triggers:** PR opened/updated
**Purpose:** Validates PR quality and enforces standards

**Checks:**

1. **Conventional Commits Validation** ⚠️ **REQUIRED**
   - **PR Title**: Must follow conventional commits format
   - **All Commits**: Validates every commit in the PR
   - **Format**: `type(scope): description`
   - **Valid Types**: feat, fix, docs, style, refactor, perf, test, build, ci, chore
   - **Valid Scopes**: gui, core, overlay, config, build, ci, deps (optional)
   - **Case**: Type and description must be lowercase
   - **Breaking Changes**: Use `!` or `BREAKING CHANGE:` in footer
   - **Auto-comment**: Posts detailed help if validation fails
   - **Config**: Uses `.commitlintrc.json`

2. **Merge Conflicts**
   - Detects merge conflicts
   - Adds `merge-conflict` label if conflicts exist
   - Uses `eps1lon/actions-label-merge-conflict`

3. **Branch Naming** ⚠️ **REQUIRED**
   - **Format**: `type/description`
   - **Valid Types**: feat, fix, docs, style, refactor, perf, test, build, ci, chore, hotfix
   - **Rules**: Lowercase, hyphens only, min 5 chars
   - **Examples**: `feat/add-overlay`, `fix/button-click`
   - **Exceptions**: `main`, `develop`
   - **Auto-comment**: Posts help if invalid
   - Uses `deepakputhraya/action-branch-name`

4. **Linked Issue**
   - Checks for issue references (#123, fixes #123, closes #123)
   - Adds `no-issue-linked` label if missing
   - Skips for draft PRs
   - Posts helpful comment with examples

## Maintenance

### Stale (`stale.yml`)
**Triggers:** Daily schedule, Manual
**Purpose:** Manages inactive issues/PRs

**Issues:**
- Stale after 60 days
- Closed after 7 more days
- Exempt: `pinned`, `security`, `bug`

**Pull Requests:**
- Stale after 30 days
- Closed after 7 more days
- Exempt: `pinned`, `security`, `work-in-progress`

### Auto-merge (`auto-merge.yml`)
**Triggers:** Dependabot PRs
**Purpose:** Auto-merges dependency updates

**Conditions:**
- Only Dependabot PRs
- Only patch/minor updates
- Auto-approves and enables auto-merge

### Welcome (`welcome.yml`)
**Triggers:** First issue/PR from contributor
**Purpose:** Welcomes new contributors

- Friendly welcome message
- Links to contribution guidelines
- Provides helpful tips

## Issue Templates

### Bug Report (`bug_report.yml`)
**Fields:**
- Bug description
- Steps to reproduce
- Expected vs actual behavior
- Version information
- Operating system
- Logs/error messages

**Auto-labels:** `bug`, `needs-triage`

### Feature Request (`feature_request.yml`)
**Fields:**
- Problem statement
- Proposed solution
- Alternatives considered
- Priority level
- Contribution willingness

**Auto-labels:** `enhancement`, `needs-triage`

### Configuration (`config.yml`)
**Links:**
- Discussions
- Documentation
- Security advisories

## Labels

All labels are defined in `.github/labels.yml`.

**Sync labels:**
```bash
gh label sync -f .github/labels.yml
```

**Categories:**
- **Type** - Feature, bug, docs, etc.
- **Size** - XS, S, M, L, XL
- **Area** - GUI, core, build, CI, docs, tests
- **Priority** - Critical, high, medium, low
- **Status** - Needs triage, in progress, blocked, etc.
- **Special** - Breaking change, security, good first issue, etc.

## Workflow Permissions

All workflows use minimal required permissions following the principle of least privilege.

**Common permissions:**
- `contents: read` - Read repository contents
- `contents: write` - Commit changes (changelog, releases)
- `pull-requests: write` - Comment and label PRs
- `issues: write` - Label and comment issues
- `security-events: write` - CodeQL results

## Secrets Required

- `GITHUB_TOKEN` - Automatically provided by GitHub Actions

No additional secrets needed for basic functionality.

## Conventional Commits Enforcement

This repository **strictly enforces** [Conventional Commits](https://conventionalcommits.org/) at multiple levels:

### Local Validation (Pre-commit)

**File**: `.pre-commit-config.yaml`

{{ ... }}
```bash
git commit -m "feat: add new feature"
```

The `commitlint` hook validates your commit message **before** it's created.

**Configuration**: `.commitlintrc.json`

### CI Validation (GitHub Actions)

**Workflow**: `pr-checks.yml`

When you open a PR:
1. **PR Title** is validated (must be conventional commit)
2. **All commits** in the PR are validated
3. **Auto-comment** posted if validation fails with detailed help

### Why Conventional Commits?

✅ **Automatic changelog generation**
✅ **Automatic semantic versioning**
✅ **Clear commit history**
✅ **Auto-labeling of PRs**
✅ **Easy to understand changes**
✅ **Better collaboration**

### Quick Reference

**Format**: `type(scope): description`

**Types**: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`

**Examples**:
- `feat: add visual overlay`
- `fix(gui): resolve button alignment`
- `docs: update installation guide`
- `feat!: change API structure` (breaking change)

**See**: [CONTRIBUTING.md](../CONTRIBUTING.md#commit-guidelines) for detailed guide

## Best Practices

1. ⚠️ **REQUIRED: Use conventional commits** - PRs will be rejected otherwise
2. **Link PRs to issues** using keywords (fixes #123)
3. **Follow branch naming convention** (`type/description`)
4. **Add PR descriptions** to avoid `needs-description` label
5. **Keep PRs small** to get better size labels (< 500 lines)
6. **Tag releases properly** for automatic changelog generation
7. **Test locally** before pushing (`pre-commit run --all-files`)

## Troubleshooting

### Workflow not running?
- Check branch protection rules
- Verify workflow permissions
- Check workflow file syntax

### Labels not applying?
- Sync labels: `gh label sync -f .github/labels.yml`
- Check PR title format
- Verify file paths in `labeler.yml`

### Build failing?
- Check Python version (3.12 required)
- Verify dependencies in `pyproject.toml`
- Check PyInstaller spec file

## Contributing

To add or modify workflows:

1. Create/edit workflow in `.github/workflows/`
2. Test locally with `act` (if possible)
3. Submit PR with `ci:` prefix
4. Update this documentation

---

**Last Updated:** 2025-10-06
**Maintained by:** @JoShMiQueL
