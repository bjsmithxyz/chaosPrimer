# chaosPrimer

An interactive grid visualization application built with Python, matplotlib, and tkinter. Create and manipulate a visual grid where you can toggle boxes between ON and OFF states with simple mouse clicks.

## Project Overview

chaosPrimer is a simple yet engaging application that demonstrates fundamental concepts in GUI programming, event handling, and data visualization. Users can interact with a grid of boxes, toggling their states by clicking on them. The application also supports saving and loading grid configurations for future use.

### Features

- **Interactive Grid**: Click on any box to toggle between ON (dark gray) and OFF (white) states
- **Save/Load State**: Persist your grid configurations to JSON files and reload them later
- **Flexible Grid Size**: Create grids of any height (default is 14 boxes)
- **Real-time Visualization**: See changes immediately as you interact with the grid
- **Error Handling**: Robust error handling for file operations and user interactions
- **Type Safety**: Full type hints for better code maintainability

## Installation and Setup

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Required Dependencies

```bash
pip install matplotlib
```

**Note**: `tkinter` is included with most Python installations. If you encounter import errors, you may need to install it separately depending on your system.

### Quick Start

1. **Clone or download the repository**
2. **Install dependencies**:
   ```bash
   pip install matplotlib
   ```
3. **Run the application**:
   ```bash
   python visualise.py
   ```

## Usage

### Basic Usage

```bash
# Run the main application
python visualise.py

# Or run the grid module directly
python grid.py
```

### Interactive Controls

- **Left Click**: Toggle any box between ON and OFF states
- **Window Controls**: Use standard window controls to resize or close the application

### Programmatic Usage

```python
from grid import Grid

# Create a new grid with default size (14 boxes)
grid = Grid()

# Create a grid with custom size
grid = Grid(height=10)

# Toggle specific boxes programmatically
grid.toggle_box(0)  # Toggle first box
grid.toggle_box(5)  # Toggle sixth box

# Save the current state
grid.save_state('my_pattern.json')

# Load a previously saved state
grid.load_state('my_pattern.json')

# Get current state as a list
current_state = grid.get_state()

# Set a specific state
new_state = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]  # Alternating pattern
grid.set_state(new_state)
```

### Save/Load Example

```python
from grid import Grid

# Create and modify a grid
grid = Grid(height=5)
grid.toggle_box(0)
grid.toggle_box(2)
grid.toggle_box(4)

# Save the pattern
grid.save_state('alternating_pattern.json')

# Later, load the pattern into a new grid
new_grid = Grid(height=5)
new_grid.load_state('alternating_pattern.json')
```

## File Structure

```
chaosPrimer/
├── README.md              # This file
├── CONTRIBUTING.md        # Contribution guidelines
├── grid.py               # Main Grid class and logic
├── visualise.py          # Main application entry point
├── test_grid.py          # Unit tests
└── .gitignore           # Git ignore file
```

## Development

### Running Tests

```bash
# Run all tests
python test_grid.py

# Run tests with verbose output
python test_grid.py -v
```

### Code Quality

The codebase includes:
- **Type hints** for all functions and methods
- **Comprehensive docstrings** following Python conventions
- **Error handling** for robust operation
- **Unit tests** covering core functionality

## API Reference

### Grid Class

#### Constructor
```python
Grid(height: int = 14) -> None
```
Creates a new grid with the specified number of boxes.

#### Methods

- `toggle_box(index: int) -> None`: Toggle the state of a specific box
- `get_state() -> List[int]`: Get a copy of the current grid state
- `set_state(new_state: List[int]) -> bool`: Set the grid to a specific state
- `save_state(filename: str) -> bool`: Save current state to a JSON file
- `load_state(filename: str) -> bool`: Load state from a JSON file
- `print_grid() -> None`: Render the grid visualization

### BoxState Class

Simple enum-like class defining box states:
- `BoxState.ON` = 1 (Dark gray boxes)
- `BoxState.OFF` = 0 (White boxes)

## Examples

### Creating Patterns

```python
from grid import Grid

# Create a checkerboard pattern
grid = Grid(height=8)
for i in range(0, 8, 2):
    grid.toggle_box(i)

# Save it for later
grid.save_state('checkerboard.json')
```

### Loading and Modifying Patterns

```python
from grid import Grid

# Load an existing pattern
grid = Grid(height=8)
if grid.load_state('checkerboard.json'):
    # Modify the pattern
    grid.toggle_box(1)
    grid.toggle_box(3)
    
    # Save the modified version
    grid.save_state('modified_checkerboard.json')
```

## Virtual Environment Setup (Optional)

For isolated development:

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
.\venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate

# Install dependencies
pip install matplotlib

# Run the application
python visualise.py

# Deactivate when done
deactivate
```

## Troubleshooting

### Common Issues

1. **"No module named 'tkinter'"**
   - On Ubuntu/Debian: `sudo apt-get install python3-tk`
   - On CentOS/RHEL: `sudo yum install tkinter`
   - On macOS: Usually included with Python

2. **"No module named 'matplotlib'"**
   - Install with: `pip install matplotlib`

3. **Display issues in headless environments**
   - Set matplotlib backend: `export MPLBACKEND=Agg`

### Performance Tips

- For large grids (>50 boxes), the rendering may slow down
- The application automatically clears and redraws on each interaction for optimal performance
- Save files are lightweight JSON format for fast loading

## License

This project is open source and available under standard open source terms.

## Contributing

Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute to this project.
