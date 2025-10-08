---
trigger: always_on
---

# Tauri Development

## Project Structure
- Frontend code: `/src`
- Tauri configuration: `/src-tauri`
  - Rust source: `/src-tauri/src`
  - Icons: `/src-tauri/icons`
  - Configuration: `/src-tauri/tauri.conf.json`

## Development Commands
- Start development server: `bun tauri dev`
- Build application: `bun tauri build`
- Check Rust code: `cargo check` (in `/src-tauri`)
- Format Rust code: `cargo fmt` (in `/src-tauri`)

## Best Practices

### 1. Rust Backend
- Keep business logic in Rust for better performance
- Use `#[tauri::command]` to expose Rust functions to the frontend
- Handle errors properly and return meaningful error messages

### 2. Frontend
- Use TypeScript for type safety
- Keep components small and focused
- Use Tauri's IPC system for frontend-backend communication

### 3. Performance
- Minimize data transfer between Rust and JavaScript
- Use web workers for CPU-intensive tasks
- Optimize asset loading

## Common Tauri Commands
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
