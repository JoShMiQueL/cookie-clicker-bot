# Quick Start Guide

Get started with Cookie Clicker Autoclicker in 5 minutes!

## 🎯 For End Users

### Windows Executable (Easiest)

1. **Download**
   - Go to [Releases](https://github.com/JoShMiQueL/cookie-clicker-bot/releases)
   - Download `CookieClickerBot.exe`

2. **Run**
   - Double-click `CookieClickerBot.exe`
   - No installation needed!

3. **Use**
   - Open Cookie Clicker in Steam
   - Click "Start" in the bot
   - Adjust settings in real-time
   - Click "Stop" when done

## 👨‍💻 For Developers

### Quick Setup

```bash
# Clone and setup
git clone https://github.com/JoShMiQueL/cookie-clicker-bot.git
cd cookie-clicker-bot

# For development (with hooks)
pip install -e ".[dev]"

# For just running (no development)
pip install -r requirements.txt

# Run GUI
python -m src.gui

# Or run CLI
python -m src.main
```

### Quick Build

```bash
# Install build tools
pip install pyinstaller

# Build executable
python scripts/build.py

# Find executable in dist/CookieClickerBot.exe
```

## ⚙️ Basic Configuration

Edit `src/config.py`:

```python
CPS = 15                      # Clicks per second (1-50)
BIG_COOKIE_RELATIVE_X = 0.15  # X position (0.0-1.0)
BIG_COOKIE_RELATIVE_Y = 0.39  # Y position (0.0-1.0)
SHOW_OVERLAY = True           # Show visual indicator
```

## 🎮 Usage Tips

### Finding the Right Position

1. Start the bot with overlay enabled
2. See the red dot indicator
3. Adjust X/Y sliders in real-time
4. Watch the overlay move
5. Fine-tune until it's on the cookie

### Optimal Settings

- **CPS**: 15-20 for best performance
- **Position**: Adjust based on window size
- **Overlay**: Enable for initial setup, disable for performance

### Troubleshooting

**Bot doesn't find the game?**
- Make sure Cookie Clicker is running
- Use windowed mode (not fullscreen)
- Check the window title matches: "X cookies - Cookie Clicker"

**Clicks in wrong position?**
- Enable overlay to see where it clicks
- Adjust X/Y position sliders
- Changes apply in real-time

**Bot stops immediately?**
- Run as administrator for better compatibility
- Check antivirus isn't blocking it

## 📚 Next Steps

- Read the full [README.md](README.md)
- Check [CONTRIBUTING.md](CONTRIBUTING.md) to contribute
- See [CHANGELOG.md](CHANGELOG.md) for version history

## 🆘 Need Help?

- [Open an Issue](https://github.com/JoShMiQueL/cookie-clicker-bot/issues)
- [Start a Discussion](https://github.com/JoShMiQueL/cookie-clicker-bot/discussions)

---

Happy clicking! 🍪
