import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class BoxState:
    """Enum representing the two possible states of a box."""
    ON = 1
    OFF = 0

class Grid:
    def __init__(self, height=14):
        self.height = height
        self.grid = [BoxState.OFF for _ in range(height)]
        self.fig, self.ax = self.create_figure()

    def create_figure(self):
        fig, ax = plt.subplots(figsize=(1, self.height * 20))
        return fig, ax

    def toggle_box(self, index):
        """Toggle the state of the box at the given index."""
        self.grid[index] = BoxState.ON if self.grid[index] == BoxState.OFF else BoxState.OFF

    def print_grid(self):
        """Visualize the current state of the grid using matplotlib."""
        for i, state in enumerate(self.grid):
            rect = plt.Rectangle((i*20, 260), 20, 20, edgecolor='black', linewidth=1, facecolor='white' if state == BoxState.OFF else 'darkgray')
            self.ax.add_patch(rect)
        self.ax.set_xlim([0, len(self.grid)*20])
        self.ax.set_ylim([0, self.height*20])
        self.ax.set_aspect('equal', adjustable='box')

        # Remove ticks and labels from both axes
        self.ax.tick_params(axis='both', left=False, bottom=False, labelleft=False, labelbottom=False)

        # Connect the button press event to the toggle_box function
        self.fig.canvas.mpl_connect('button_press_event', lambda event: self.toggle_box_at_position(event))

    def toggle_box_at_position(self, event):
        """Toggle the state of the box at the clicked position."""
        if event.inaxes is None:
            return
        x_data, y_data = event.xdata, event.ydata
        index = int(x_data // 20)
        if 0 <= index < len(self.grid):
            self.toggle_box(index)
            self.print_grid()
            self.fig.canvas.draw()

def run_app():
    root = tk.Tk()
    root.title("Grid Visualization")
    canvas = FigureCanvasTkAgg(g.fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    tk.mainloop()

if __name__ == "__main__":
    g = Grid()
    g.print_grid()
    run_app()
