from typing import List, Tuple, Optional, Any
try:
    import tkinter as tk
    TKINTER_AVAILABLE = True
except ImportError:
    TKINTER_AVAILABLE = False
    tk = None
import matplotlib.pyplot as plt
try:
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    CANVAS_AVAILABLE = True
except ImportError:
    CANVAS_AVAILABLE = False
    FigureCanvasTkAgg = None
from matplotlib.figure import Figure
import json
import os

class BoxState:
    """Enum representing the two possible states of a box."""
    ON: int = 1
    OFF: int = 0

class Grid:
    """
    A grid visualization class that represents a series of toggleable boxes.
    
    This class manages a 1D grid of boxes that can be in either ON or OFF state.
    It provides functionality for toggling boxes, visualizing the grid using
    matplotlib, and handling user interactions through mouse clicks.
    
    Attributes:
        height (int): The number of boxes in the grid
        grid (List[int]): List representing the state of each box
        fig: Matplotlib figure object for visualization
        ax: Matplotlib axes object for drawing
    """
    
    def __init__(self, height: int = 14) -> None:
        """
        Initialize a new Grid instance.
        
        Args:
            height (int, optional): Number of boxes in the grid. Defaults to 14.
        """
        self.height: int = height
        self.grid: List[int] = [BoxState.OFF for _ in range(height)]
        self.fig, self.ax = self.create_figure()

    def create_figure(self) -> Tuple[Any, Any]:
        """
        Create matplotlib figure and axes for the grid visualization.
        
        Returns:
            Tuple[Any, Any]: A tuple containing the matplotlib figure and axes objects
        """
        fig, ax = plt.subplots(figsize=(1, self.height * 20))
        return fig, ax

    def toggle_box(self, index: int) -> None:
        """
        Toggle the state of the box at the given index.
        
        Args:
            index (int): The index of the box to toggle (0-based)
            
        Raises:
            IndexError: If index is out of bounds
        """
        if not (0 <= index < len(self.grid)):
            raise IndexError(f"Index {index} is out of bounds for grid of size {len(self.grid)}")
        
        self.grid[index] = BoxState.ON if self.grid[index] == BoxState.OFF else BoxState.OFF

    def print_grid(self) -> None:
        """
        Visualize the current state of the grid using matplotlib.
        
        This method clears the current axes and redraws all rectangles representing
        the boxes in the grid. It also sets up mouse click event handling for
        interactive toggling of boxes.
        """
        # Clear previous patches to avoid accumulation and improve performance
        self.ax.clear()
        
        for i, state in enumerate(self.grid):
            rect = plt.Rectangle(
                (i*20, 260), 20, 20, 
                edgecolor='black', 
                linewidth=1, 
                facecolor='white' if state == BoxState.OFF else 'darkgray'
            )
            self.ax.add_patch(rect)
            
        self.ax.set_xlim([0, len(self.grid)*20])
        self.ax.set_ylim([0, self.height*20])
        self.ax.set_aspect('equal', adjustable='box')

        # Remove ticks and labels from both axes
        self.ax.tick_params(axis='both', left=False, bottom=False, labelleft=False, labelbottom=False)

        # Connect the button press event to the toggle_box function
        self.fig.canvas.mpl_connect('button_press_event', lambda event: self.toggle_box_at_position(event))

    def toggle_box_at_position(self, event: Any) -> None:
        """
        Toggle the state of the box at the clicked position.
        
        This method handles mouse click events and converts the click coordinates
        to a grid index, then toggles the corresponding box.
        
        Args:
            event: Matplotlib mouse click event object
        """
        try:
            if event.inaxes is None:
                return
            
            x_data, y_data = event.xdata, event.ydata
            
            # Handle potential None values
            if x_data is None or y_data is None:
                return
                
            index = int(x_data // 20)
            if 0 <= index < len(self.grid):
                self.toggle_box(index)
                self.print_grid()
                self.fig.canvas.draw()
        except (TypeError, ValueError, AttributeError) as e:
            # Handle any errors that might occur during event processing
            print(f"Error processing click event: {e}")
    
    def save_state(self, filename: str) -> bool:
        """
        Save the current grid state to a JSON file.
        
        Args:
            filename (str): Path to the file where the state should be saved
            
        Returns:
            bool: True if save was successful, False otherwise
        """
        try:
            state_data = {
                'height': self.height,
                'grid': self.grid
            }
            with open(filename, 'w') as f:
                json.dump(state_data, f, indent=2)
            return True
        except (IOError, OSError, ValueError) as e:
            print(f"Error saving grid state: {e}")
            return False
    
    def load_state(self, filename: str) -> bool:
        """
        Load grid state from a JSON file.
        
        Args:
            filename (str): Path to the file to load the state from
            
        Returns:
            bool: True if load was successful, False otherwise
        """
        try:
            if not os.path.exists(filename):
                print(f"File {filename} does not exist")
                return False
                
            with open(filename, 'r') as f:
                state_data = json.load(f)
            
            if 'height' in state_data and 'grid' in state_data:
                self.height = state_data['height']
                self.grid = state_data['grid']
                # Recreate figure with new dimensions if height changed
                self.fig, self.ax = self.create_figure()
                return True
            else:
                print("Invalid state file format")
                return False
        except (IOError, OSError, json.JSONDecodeError, KeyError) as e:
            print(f"Error loading grid state: {e}")
            return False
    
    def get_state(self) -> List[int]:
        """
        Get a copy of the current grid state.
        
        Returns:
            List[int]: A copy of the current grid state
        """
        return self.grid.copy()
    
    def set_state(self, new_state: List[int]) -> bool:
        """
        Set the grid state to a new configuration.
        
        Args:
            new_state (List[int]): New grid state to set
            
        Returns:
            bool: True if state was set successfully, False otherwise
        """
        try:
            if len(new_state) != self.height:
                print(f"State length {len(new_state)} does not match grid height {self.height}")
                return False
            
            # Validate that all values are valid BoxState values
            for state in new_state:
                if state not in [BoxState.ON, BoxState.OFF]:
                    print(f"Invalid state value: {state}")
                    return False
            
            self.grid = new_state.copy()
            return True
        except (TypeError, AttributeError) as e:
            print(f"Error setting grid state: {e}")
            return False

def run_app(grid: Optional[Grid] = None) -> None:
    """
    Run the Tkinter application with the grid visualization.
    
    Args:
        grid (Optional[Grid]): Grid instance to display. If None, creates a new Grid instance.
        
    Raises:
        ImportError: If tkinter or FigureCanvasTkAgg are not available
    """
    if not TKINTER_AVAILABLE:
        raise ImportError("tkinter is not available. Cannot run GUI application.")
    if not CANVAS_AVAILABLE:
        raise ImportError("matplotlib.backends.backend_tkagg is not available. Cannot run GUI application.")
    
    if grid is None:
        grid = Grid()
        grid.print_grid()
    
    root = tk.Tk()
    root.title("Grid Visualization")
    canvas = FigureCanvasTkAgg(grid.fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    tk.mainloop()

if __name__ == "__main__":
    g = Grid()
    g.print_grid()
    run_app(g)
