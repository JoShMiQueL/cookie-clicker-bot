"""Graphical interface to control the autoclicker."""

import threading
import tomllib
from pathlib import Path

import customtkinter as ctk

from . import config
from .clicker import AutoClicker
from .overlay import ClickOverlay
from .window_finder import CookieClickerWindowFinder


class AutoClickerGUI:
    """Graphical interface to control the autoclicker."""

    def __init__(self):
        # Set appearance
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()

        # Load project metadata from pyproject.toml
        pyproject_path = Path(__file__).parent.parent / "pyproject.toml"
        with pyproject_path.open("rb") as f:
            data = tomllib.load(f)
        self.version = data["project"]["version"]
        self.author = data["project"]["authors"][0]["name"]
        self.license_text = data["project"]["license"]["text"]

        self.root.title(f"Cookie Clicker Autoclicker v{self.version}")
        self.root.geometry("450x650")
        self.root.resizable(False, False)

        # Set window icon
        icon_path = Path(__file__).parent.parent / "cookie.ico"
        if icon_path.exists():
            self.root.iconbitmap(str(icon_path))

        # State variables
        self.is_running = False
        self.stop_event = threading.Event()
        self.clicker_thread = None
        self.overlay = None
        self.clicker = None

        # Configuration variables
        self.cps_var = ctk.StringVar(value=str(config.CPS))
        self.pos_x_var = ctk.DoubleVar(value=config.BIG_COOKIE_RELATIVE_X)
        self.pos_y_var = ctk.DoubleVar(value=config.BIG_COOKIE_RELATIVE_Y)
        self.show_overlay_var = ctk.BooleanVar(value=config.SHOW_OVERLAY)

        self._create_widgets()

    def _create_widgets(self):
        """Create the interface widgets."""
        # Main frame
        main_frame = ctk.CTkFrame(self.root)
        main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Title
        title_label = ctk.CTkLabel(
            main_frame,
            text="🍪 Cookie Clicker Autoclicker",
            font=ctk.CTkFont(size=16, weight="bold"),
        )
        title_label.pack(pady=(0, 20))

        # Status
        self.status_label = ctk.CTkLabel(
            main_frame, text="Status: Stopped", font=ctk.CTkFont(size=10)
        )
        self.status_label.pack(pady=(0, 10))

        # Separator
        sep1 = ctk.CTkFrame(main_frame, height=2, fg_color="gray")
        sep1.pack(fill="x", pady=10)

        # CPS configuration
        cps_label = ctk.CTkLabel(main_frame, text="Clicks per second (CPS):")
        cps_label.pack(anchor="w", pady=(5, 0))

        cps_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        cps_frame.pack(anchor="e", pady=(0, 5))

        # Decrease button
        self.cps_minus_button = ctk.CTkButton(
            cps_frame, text="-", command=self._decrease_cps, width=30, height=30
        )
        self.cps_minus_button.pack(side="left")

        self.cps_entry = ctk.CTkEntry(cps_frame, textvariable=self.cps_var, width=60)
        self.cps_entry.pack(side="left", padx=5)

        # Increase button
        self.cps_plus_button = ctk.CTkButton(
            cps_frame, text="+", command=self._increase_cps, width=30, height=30
        )
        self.cps_plus_button.pack(side="left")

        # X Position
        x_label = ctk.CTkLabel(main_frame, text="X Position (relative):")
        x_label.pack(anchor="w", pady=(5, 0))

        x_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        x_frame.pack(anchor="e", pady=(0, 5))

        self.x_slider = ctk.CTkSlider(
            x_frame, from_=0.0, to=1.0, variable=self.pos_x_var, orientation="horizontal", width=150
        )
        self.x_slider.pack(side="left")

        self.x_display = ctk.CTkLabel(x_frame, text=f"{self.pos_x_var.get():.2f}")
        self.x_display.pack(side="left", padx=(5, 0))
        self.pos_x_var.trace_add("write", self._update_x_display)

        # Y Position
        y_label = ctk.CTkLabel(main_frame, text="Y Position (relative):")
        y_label.pack(anchor="w", pady=(5, 0))

        y_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        y_frame.pack(anchor="e", pady=(0, 5))

        self.y_slider = ctk.CTkSlider(
            y_frame, from_=0.0, to=1.0, variable=self.pos_y_var, orientation="horizontal", width=150
        )
        self.y_slider.pack(side="left")

        self.y_display = ctk.CTkLabel(y_frame, text=f"{self.pos_y_var.get():.2f}")
        self.y_display.pack(side="left", padx=(5, 0))
        self.pos_y_var.trace_add("write", self._update_y_display)

        # Show overlay
        self.overlay_checkbox = ctk.CTkCheckBox(
            main_frame, text="Show visual overlay", variable=self.show_overlay_var
        )
        self.overlay_checkbox.pack(anchor="w", pady=10)

        # Separator
        sep2 = ctk.CTkFrame(main_frame, height=2, fg_color="gray")
        sep2.pack(fill="x", pady=10)

        # Control buttons
        button_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        button_frame.pack(pady=10)

        self.start_button = ctk.CTkButton(
            button_frame, text="▶ Start", command=self._start_clicker, width=120
        )
        self.start_button.pack(side="left", padx=5)

        self.stop_button = ctk.CTkButton(
            button_frame, text="⏹ Stop", command=self._stop_clicker, width=120, state="disabled"
        )
        self.stop_button.pack(side="left", padx=5)

        # Log
        log_label = ctk.CTkLabel(main_frame, text="Log:", font=ctk.CTkFont(size=10, weight="bold"))
        log_label.pack(anchor="w", pady=(10, 5))

        self.log_text = ctk.CTkTextbox(main_frame, height=100, width=400, state="disabled")
        self.log_text.pack(pady=(0, 10))

        # Information
        info_label = ctk.CTkLabel(
            main_frame,
            text="💡 Tip: Adjustments are applied in real-time while the bot is active",
            font=ctk.CTkFont(size=8),
            text_color="gray",
        )
        info_label.pack(pady=(5, 0))

        # Version and author
        version_label = ctk.CTkLabel(
            main_frame,
            text=f"Version {self.version} by {self.author} | License: {self.license_text}",
            font=ctk.CTkFont(size=8),
            text_color="gray",
        )
        version_label.pack(pady=(5, 0))

    def _increase_cps(self):
        """Increase the CPS value by 1."""
        try:
            current_cps = int(self.cps_var.get())
            new_cps = current_cps + 1
            self.cps_var.set(str(new_cps))

            # If the clicker is running, update in real-time
            if self.is_running and self.clicker:
                config.CPS = new_cps
                self.clicker.update_cps()
        except ValueError:
            new_cps = config.CPS + 1
            self.cps_var.set(str(new_cps))
            if self.is_running and self.clicker:
                config.CPS = new_cps
                self.clicker.update_cps()

    def _decrease_cps(self):
        """Decrease the CPS value by 1, minimum 1."""
        try:
            current_cps = int(self.cps_var.get())
            new_cps = max(1, current_cps - 1)
            self.cps_var.set(str(new_cps))

            # If the clicker is running, update in real-time
            if self.is_running and self.clicker:
                config.CPS = new_cps
                self.clicker.update_cps()
        except ValueError:
            new_cps = max(1, config.CPS - 1)
            self.cps_var.set(str(new_cps))
            if self.is_running and self.clicker:
                config.CPS = new_cps
                self.clicker.update_cps()

    def _update_x_display(self, *args):
        """Update the X position display."""
        self.x_display.configure(text=f"{self.pos_x_var.get():.2f}")

        # If the clicker is running, update in real-time
        if self.is_running and self.clicker:
            self._update_position_realtime()

    def _update_y_display(self, *args):
        """Update the Y position display."""
        self.y_display.configure(text=f"{self.pos_y_var.get():.2f}")

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
        self.log_text.configure(state="normal")
        self.log_text.insert("end", f"{message}\n")
        self.log_text.see("end")
        self.log_text.configure(state="disabled")

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
        config.CPS = int(self.cps_var.get()) if self.cps_var.get().isdigit() else config.CPS
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
        self.start_button.configure(state="disabled")
        self.stop_button.configure(state="normal")
        self.status_label.configure(text="Status: ✅ Running")
        self._log(f"🖱️ Autoclicker started ({config.CPS} CPS)")

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
        self.start_button.configure(state="normal")
        self.stop_button.configure(state="disabled")
        self.status_label.configure(text="Status: ⏹️ Stopped")
        self._log("✅ Autoclicker stopped")

    def run(self):
        """Start the graphical interface."""
        self.root.mainloop()


if __name__ == "__main__":
    app = AutoClickerGUI()
    app.run()
