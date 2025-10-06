"""Module for the visual overlay showing where clicks are made."""

import threading
import tkinter as tk


class ClickOverlay:
    """Responsible for displaying a visual overlay at the click position."""

    def __init__(self, parent=None):
        self.parent = parent
        self.root = None
        self.canvas = None
        self.running = False
        self.position_ready = threading.Event()
        self.click_x = 0
        self.click_y = 0

    def set_position(self, x: int, y: int):
        """Set the position where the overlay will be created."""
        self.click_x = x
        self.click_y = y
        self.position_ready.set()

    def create_overlay(self):
        """Create a transparent overlay window with a red dot."""
        # Wait for the position to be set
        if not self.position_ready.wait(timeout=10):
            return

        # If there's a parent (GUI), use Toplevel, otherwise Tk
        if self.parent:
            self.root = tk.Toplevel(self.parent)
        else:
            self.root = tk.Tk()

        self.root.title("Click Overlay")

        # Configure the window as transparent and always on top
        self.root.attributes("-transparentcolor", "white")
        self.root.attributes("-topmost", True)
        self.root.overrideredirect(True)  # No borders

        # Overlay size (circle + margin)
        size = 40
        self.root.geometry(f"{size}x{size}+{self.click_x - size // 2}+{self.click_y - size // 2}")

        # Canvas to draw the dot
        self.canvas = tk.Canvas(self.root, width=size, height=size, bg="white", highlightthickness=0)
        self.canvas.pack()

        # Draw a red circle with border
        center = size // 2
        radius = 8
        self.canvas.create_oval(
            center - radius,
            center - radius,
            center + radius,
            center + radius,
            fill="red",
            outline="yellow",
            width=2,
        )

        # Draw a cross in the center
        cross_size = 12
        self.canvas.create_line(center - cross_size, center, center + cross_size, center, fill="yellow", width=2)
        self.canvas.create_line(center, center - cross_size, center, center + cross_size, fill="yellow", width=2)

        self.running = True

    def update_position(self, x: int, y: int):
        """Update the overlay position in real-time."""
        if self.root and self.running:
            self.click_x = x
            self.click_y = y
            size = 40
            try:
                self.root.geometry(f"{size}x{size}+{x - size // 2}+{y - size // 2}")
            except Exception:
                pass  # If there's an error, ignore it

    def run(self):
        """Start the tkinter loop."""
        if self.root:
            self.root.mainloop()

    def close(self):
        """Close the overlay."""
        if self.root and self.running:
            self.running = False
            try:
                self.root.destroy()
            except Exception:
                pass  # If already destroyed, ignore the error
