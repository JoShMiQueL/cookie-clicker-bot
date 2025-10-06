"""Cookie Clicker Autoclicker - Main orchestrator."""

import threading
from ctypes import windll

import keyboard

from . import config
from .clicker import AutoClicker
from .overlay import ClickOverlay
from .window_finder import CookieClickerWindowFinder


def autoclicker_thread(stop_event: threading.Event, overlay: ClickOverlay | None = None):
    """Main autoclicker thread."""
    # Find the game window
    finder = CookieClickerWindowFinder()
    hwnd = finder.find_window()

    if not hwnd:
        print("❌ Please make sure Cookie Clicker is open")
        if overlay:
            overlay.position_ready.set()  # Unblock the main thread
        return

    # Create the autoclicker
    clicker = AutoClicker(hwnd, stop_event)

    print(
        f"🖱️ Autoclicker started ({config.CPS} clicks/second). Press {config.STOP_KEY.upper()} to stop."
    )
    print(
        "💡 You can continue working normally, this autoclicker doesn't affect your physical cursor."
    )
    print("📌 Note: If the game is in fullscreen, run it in borderless window mode")

    # Configure the overlay if enabled
    if config.SHOW_OVERLAY and overlay:
        print("🎯 Visual overlay activated - you'll see a red dot where clicks are made")
        screen_x, screen_y = clicker.get_screen_position()
        overlay.set_position(screen_x, screen_y)

    # Execute the autoclicker
    clicker.run()

    print("\n⏹️ Autoclicker stopped")

    # Close the overlay
    if config.SHOW_OVERLAY and overlay:
        overlay.close()


def monitor_stop_key(stop_event: threading.Event, overlay: ClickOverlay | None = None):
    """Monitor the key to stop the autoclicker."""
    keyboard.wait(config.STOP_KEY)
    stop_event.set()
    if overlay:
        overlay.close()


def main():
    """Main entry point."""
    # Check administrative privileges
    is_admin = windll.shell32.IsUserAnAdmin() != 0
    if not is_admin:
        print("⚠️ Warning: Run this script as administrator for better compatibility")

    # Create an event to stop the autoclicker
    stop_event = threading.Event()

    print("🔍 Searching for Cookie Clicker window (Steam)...")
    print(
        "💡 The title changes dynamically based on your cookies (e.g., '123 cookies - Cookie Clicker')"
    )

    # Create the overlay if enabled
    overlay = ClickOverlay() if config.SHOW_OVERLAY else None

    # Start the autoclicker thread
    clicker_thread = threading.Thread(
        target=autoclicker_thread, args=(stop_event, overlay), daemon=True
    )
    clicker_thread.start()

    # Start the stop key monitor thread
    stop_thread = threading.Thread(target=monitor_stop_key, args=(stop_event, overlay), daemon=True)
    stop_thread.start()

    # If there's an overlay, create it in the main thread and run its loop
    if config.SHOW_OVERLAY and overlay:
        overlay.create_overlay()
        if overlay.root:
            overlay.run()
        else:
            # If the overlay couldn't be created, wait for the thread normally
            clicker_thread.join()
    else:
        # Wait for the autoclicker to stop
        clicker_thread.join()


if __name__ == "__main__":
    main()
