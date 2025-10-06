"""Graphical interface to control the autoclicker."""

import threading
import tkinter as tk
from tkinter import ttk

from . import config
from .clicker import AutoClicker
from .overlay import ClickOverlay
from .window_finder import CookieClickerWindowFinder


class AutoClickerGUI:
    """Graphical interface to control the autoclicker."""

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Cookie Clicker Autoclicker")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        # State variables
        self.is_running = False
        self.stop_event = threading.Event()
        self.clicker_thread = None
        self.overlay = None
        self.clicker = None

        # Configuration variables
        self.cps_var = tk.IntVar(value=config.CPS)
        self.pos_x_var = tk.DoubleVar(value=config.BIG_COOKIE_RELATIVE_X)
        self.pos_y_var = tk.DoubleVar(value=config.BIG_COOKIE_RELATIVE_Y)
        self.show_overlay_var = tk.BooleanVar(value=config.SHOW_OVERLAY)

        self._create_widgets()

    def _create_widgets(self):
        """Create the interface widgets."""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Title
        title_label = ttk.Label(
            main_frame, text="🍪 Cookie Clicker Autoclicker", font=("Arial", 16, "bold")
        )
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Status
        self.status_label = ttk.Label(main_frame, text="Status: Stopped", font=("Arial", 10))
        self.status_label.grid(row=1, column=0, columnspan=2, pady=(0, 10))

        # Separator
        ttk.Separator(main_frame, orient="horizontal").grid(
            row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10
        )

        # CPS configuration
        ttk.Label(main_frame, text="Clicks per second (CPS):").grid(
            row=3, column=0, sticky=tk.W, pady=5
        )
        cps_frame = ttk.Frame(main_frame)
        cps_frame.grid(row=3, column=1, sticky=tk.E, pady=5)

        ttk.Spinbox(cps_frame, from_=1, to=50, textvariable=self.cps_var, width=10).pack(
            side=tk.LEFT
        )
        self.cps_display = ttk.Label(cps_frame, text=f"{self.cps_var.get()}")
        self.cps_display.pack(side=tk.LEFT, padx=(5, 0))
        self.cps_var.trace_add("write", self._update_cps_display)

        # X Position
        ttk.Label(main_frame, text="X Position (relative):").grid(
            row=4, column=0, sticky=tk.W, pady=5
        )
        x_frame = ttk.Frame(main_frame)
        x_frame.grid(row=4, column=1, sticky=tk.E, pady=5)

        ttk.Scale(
            x_frame, from_=0.0, to=1.0, variable=self.pos_x_var, orient=tk.HORIZONTAL, length=150
        ).pack(side=tk.LEFT)
        self.x_display = ttk.Label(x_frame, text=f"{self.pos_x_var.get():.2f}")
        self.x_display.pack(side=tk.LEFT, padx=(5, 0))
        self.pos_x_var.trace_add("write", self._update_x_display)

        # Y Position
        ttk.Label(main_frame, text="Y Position (relative):").grid(
            row=5, column=0, sticky=tk.W, pady=5
        )
        y_frame = ttk.Frame(main_frame)
        y_frame.grid(row=5, column=1, sticky=tk.E, pady=5)

        ttk.Scale(
            y_frame, from_=0.0, to=1.0, variable=self.pos_y_var, orient=tk.HORIZONTAL, length=150
        ).pack(side=tk.LEFT)
        self.y_display = ttk.Label(y_frame, text=f"{self.pos_y_var.get():.2f}")
        self.y_display.pack(side=tk.LEFT, padx=(5, 0))
        self.pos_y_var.trace_add("write", self._update_y_display)

        # Show overlay
        ttk.Checkbutton(
            main_frame, text="Show visual overlay", variable=self.show_overlay_var
        ).grid(row=6, column=0, columnspan=2, sticky=tk.W, pady=10)

        # Separator
        ttk.Separator(main_frame, orient="horizontal").grid(
            row=7, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10
        )

        # Control buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=8, column=0, columnspan=2, pady=10)

        self.start_button = ttk.Button(
            button_frame, text="▶ Start", command=self._start_clicker, width=15
        )
        self.start_button.pack(side=tk.LEFT, padx=5)

        self.stop_button = ttk.Button(
            button_frame, text="⏹ Stop", command=self._stop_clicker, width=15, state=tk.DISABLED
        )
        self.stop_button.pack(side=tk.LEFT, padx=5)

        # Log
        ttk.Label(main_frame, text="Log:", font=("Arial", 10, "bold")).grid(
            row=9, column=0, columnspan=2, sticky=tk.W, pady=(10, 5)
        )

        log_frame = ttk.Frame(main_frame)
        log_frame.grid(
            row=10, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10)
        )

        scrollbar = ttk.Scrollbar(log_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.log_text = tk.Text(
            log_frame, height=8, width=45, state=tk.DISABLED, yscrollcommand=scrollbar.set
        )
        self.log_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.log_text.yview)

        # Information
        info_label = ttk.Label(
            main_frame,
            text="💡 Tip: Adjustments are applied in real-time while the bot is active",
            font=("Arial", 8),
            foreground="gray",
        )
        info_label.grid(row=11, column=0, columnspan=2, pady=(5, 0))

    def _update_cps_display(self, *args):
        """Update the CPS display."""
        self.cps_display.config(text=f"{self.cps_var.get()}")

        # If the clicker is running, update in real-time
        if self.is_running and self.clicker:
            config.CPS = self.cps_var.get()
            self.clicker.update_cps()

    def _update_x_display(self, *args):
        """Update the X position display."""
        self.x_display.config(text=f"{self.pos_x_var.get():.2f}")

        # If the clicker is running, update in real-time
        if self.is_running and self.clicker:
            self._update_position_realtime()

    def _update_y_display(self, *args):
        """Update the Y position display."""
        self.y_display.config(text=f"{self.pos_y_var.get():.2f}")

        # If the clicker is running, update in real-time
        if self.is_running and self.clicker:
            self._update_position_realtime()

    def _update_position_realtime(self):
        """Update the clicker and overlay position in real-time."""
        config.BIG_COOKIE_RELATIVE_X = self.pos_x_var.get()
        config.BIG_COOKIE_RELATIVE_Y = self.pos_y_var.get()

        # Update the clicker position
        self.clicker.update_position()

        # Update the overlay position
        if self.overlay and self.overlay.running:
            screen_x, screen_y = self.clicker.get_screen_position()
            self.overlay.update_position(screen_x, screen_y)

    def _log(self, message: str):
        """Add a message to the log."""
        self.log_text.config(state=tk.NORMAL)
        self.log_text.insert(tk.END, f"{message}\n")
        self.log_text.see(tk.END)
        self.log_text.config(state=tk.DISABLED)

    def _start_clicker(self):
        """Start the autoclicker."""
        if self.is_running:
            return

        self._log("🔍 Searching for Cookie Clicker window...")

        # Find the window
        finder = CookieClickerWindowFinder()
        hwnd = finder.find_window()

        if not hwnd:
            self._log("❌ Game window not found")
            return

        self._log("✅ Window found")

        # Update config with GUI values
        config.CPS = self.cps_var.get()
        config.BIG_COOKIE_RELATIVE_X = self.pos_x_var.get()
        config.BIG_COOKIE_RELATIVE_Y = self.pos_y_var.get()

        # Create overlay if enabled
        if self.show_overlay_var.get():
            self.overlay = ClickOverlay(parent=self.root)
            self._log("🎯 Visual overlay activated")

        # Reset stop event
        self.stop_event = threading.Event()

        # Start the autoclicker thread
        self.clicker_thread = threading.Thread(target=self._run_clicker, args=(hwnd,), daemon=True)
        self.clicker_thread.start()

        # Update UI
        self.is_running = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.status_label.config(text="Status: ✅ Running")
        self._log(f"🖱️ Autoclicker started ({self.cps_var.get()} CPS)")

    def _run_clicker(self, hwnd: int):
        """Execute the autoclicker in a separate thread."""
        # Create the autoclicker
        self.clicker = AutoClicker(hwnd, self.stop_event)

        # Configure the overlay
        if self.show_overlay_var.get() and self.overlay:
            screen_x, screen_y = self.clicker.get_screen_position()
            self.overlay.set_position(screen_x, screen_y)

            # Create the overlay in the main thread using after
            self.root.after(0, self._create_overlay)

        # Execute the autoclicker
        self.clicker.run()

        # Cleanup when finished
        self.root.after(0, self._on_clicker_stopped)

    def _create_overlay(self):
        """Create the overlay in the main thread."""
        if self.overlay:
            self.overlay.create_overlay()

    def _stop_clicker(self):
        """Stop the autoclicker."""
        if not self.is_running:
            return

        self._log("⏹️ Stopping autoclicker...")
        self.stop_event.set()

        # Close the overlay safely
        if self.overlay:
            try:
                self.overlay.close()
            except Exception:
                pass  # Ignore errors when closing the overlay
            finally:
                self.overlay = None

    def _on_clicker_stopped(self):
        """Callback when the autoclicker stops."""
        self.is_running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.status_label.config(text="Status: ⏹️ Stopped")
        self._log("✅ Autoclicker stopped")

    def run(self):
        """Start the graphical interface."""
        self.root.mainloop()


if __name__ == "__main__":
    app = AutoClickerGUI()
    app.run()
