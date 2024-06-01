import tkinter as tk
from grid import Grid  # Ensure this import matches your project structure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # Import FigureCanvasTkAgg here

def main():
    g = Grid()
    g.print_grid()
    run_app(g)  # Pass g to run_app

def run_app(g):  # Accept g as an argument
    root = tk.Tk()
    root.title("Grid Visualization")
    canvas = FigureCanvasTkAgg(g.fig, master=root)  # Now g is accessible
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    tk.mainloop()

if __name__ == "__main__":
    main()
