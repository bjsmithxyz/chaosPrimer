"""
Main visualization module for the chaosPrimer application.

This module provides the main entry point for running the grid visualization
application. It imports and uses the Grid class from the grid module to create
an interactive grid that users can click to toggle box states.
"""
from typing import Optional
try:
    import tkinter as tk
    TKINTER_AVAILABLE = True
except ImportError:
    TKINTER_AVAILABLE = False
    tk = None

from grid import Grid  # Ensure this import matches your project structure

try:
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # Import FigureCanvasTkAgg here
    CANVAS_AVAILABLE = True
except ImportError:
    CANVAS_AVAILABLE = False
    FigureCanvasTkAgg = None

def main() -> None:
    """
    Main entry point for the grid visualization application.
    
    Creates a new Grid instance, initializes the visualization, and starts
    the Tkinter application loop.
    
    Raises:
        ImportError: If required GUI libraries are not available
    """
    if not TKINTER_AVAILABLE:
        raise ImportError("tkinter is not available. Cannot run GUI application.")
    if not CANVAS_AVAILABLE:
        raise ImportError("matplotlib.backends.backend_tkagg is not available. Cannot run GUI application.")
    
    g = Grid()
    g.print_grid()
    run_app(g)  # Pass g to run_app

def run_app(g: Grid) -> None:
    """
    Run the Tkinter application with the provided grid.
    
    This function creates a Tkinter window, embeds the matplotlib figure
    from the grid, and starts the main event loop.
    
    Args:
        g (Grid): The Grid instance to display in the application
        
    Raises:
        ImportError: If required GUI libraries are not available
    """
    if not TKINTER_AVAILABLE:
        raise ImportError("tkinter is not available. Cannot run GUI application.")
    if not CANVAS_AVAILABLE:
        raise ImportError("matplotlib.backends.backend_tkagg is not available. Cannot run GUI application.")
    
    root = tk.Tk()
    root.title("Grid Visualization")
    canvas = FigureCanvasTkAgg(g.fig, master=root)  # Now g is accessible
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    tk.mainloop()

if __name__ == "__main__":
    main()
