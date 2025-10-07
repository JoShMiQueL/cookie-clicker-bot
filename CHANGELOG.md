## [1.1.0] - 2025-10-07

### 🚀 Features

- Add automated changelog management with git-cliff (#10)
- [**breaking**] Implement comprehensive ci/cd pipeline with solid principles (#12)
- Improve cps ui with customtkinter modernization and new cps controls (#13)

### 🐛 Bug Fixes

- *(ci)* Resolve git-cliff command not found error in release pipeline
## [1.0.0] - 2025-10-06

### 🚀 Features

- Add comprehensive ci/cd workflows and conventional commits enforcement (#1)
- Add comprehensive ci/cd workflows and conventional commits enforcement (#2)
- Support window titles with large number formats (#3)
- Optimize release workflow with reusable build and automatic versioning (#7)

### 🐛 Bug Fixes

- Make pywin32 optional for non-Windows platforms
- Install only necessary dependencies for lint workflow
- *(ci)* Update git-cliff-action to v4 (#5)
- Use bash syntax instead of powershell in release type detection (#8)
- Add missing type variable and fix here-string indentation (#9)

### 🚜 Refactor

- Simplify project structure and fix pyinstaller build (#4)
- Standardize pr size labels nomenclature (#6)
