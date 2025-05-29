"""Unit tests for the Grid class functionality."""
import unittest
import sys
import os
import json
import tempfile

# Add the current directory to Python path to import grid module
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Set matplotlib backend to prevent GUI issues in testing
import matplotlib
matplotlib.use('Agg')

from grid import Grid, BoxState


class TestBoxState(unittest.TestCase):
    """Test the BoxState enum."""
    
    def test_box_state_values(self):
        """Test that BoxState has correct values."""
        self.assertEqual(BoxState.ON, 1)
        self.assertEqual(BoxState.OFF, 0)


class TestGrid(unittest.TestCase):
    """Test the Grid class functionality."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.grid = Grid(height=5)
    
    def test_init_default_height(self):
        """Test Grid initialization with default height."""
        grid = Grid()
        self.assertEqual(grid.height, 14)
        self.assertEqual(len(grid.grid), 14)
        self.assertTrue(all(state == BoxState.OFF for state in grid.grid))
    
    def test_init_custom_height(self):
        """Test Grid initialization with custom height."""
        self.assertEqual(self.grid.height, 5)
        self.assertEqual(len(self.grid.grid), 5)
        self.assertTrue(all(state == BoxState.OFF for state in self.grid.grid))
    
    def test_toggle_box(self):
        """Test toggling a box state."""
        # Initially all boxes should be OFF
        self.assertEqual(self.grid.grid[0], BoxState.OFF)
        
        # Toggle to ON
        self.grid.toggle_box(0)
        self.assertEqual(self.grid.grid[0], BoxState.ON)
        
        # Toggle back to OFF
        self.grid.toggle_box(0)
        self.assertEqual(self.grid.grid[0], BoxState.OFF)
    
    def test_toggle_box_multiple_positions(self):
        """Test toggling multiple boxes."""
        # Toggle boxes at positions 1 and 3
        self.grid.toggle_box(1)
        self.grid.toggle_box(3)
        
        self.assertEqual(self.grid.grid[0], BoxState.OFF)
        self.assertEqual(self.grid.grid[1], BoxState.ON)
        self.assertEqual(self.grid.grid[2], BoxState.OFF)
        self.assertEqual(self.grid.grid[3], BoxState.ON)
        self.assertEqual(self.grid.grid[4], BoxState.OFF)
    
    def test_toggle_box_invalid_index(self):
        """Test toggling with invalid index raises IndexError."""
        with self.assertRaises(IndexError):
            self.grid.toggle_box(-1)
        
        with self.assertRaises(IndexError):
            self.grid.toggle_box(5)  # Grid has 5 boxes (0-4)
    
    def test_get_state(self):
        """Test getting grid state."""
        state = self.grid.get_state()
        self.assertEqual(len(state), 5)
        self.assertTrue(all(s == BoxState.OFF for s in state))
        
        # Modify grid and test state
        self.grid.toggle_box(1)
        new_state = self.grid.get_state()
        self.assertEqual(new_state[1], BoxState.ON)
        
        # Ensure get_state returns a copy
        new_state[0] = BoxState.ON
        self.assertEqual(self.grid.grid[0], BoxState.OFF)
    
    def test_set_state(self):
        """Test setting grid state."""
        new_state = [BoxState.ON, BoxState.OFF, BoxState.ON, BoxState.OFF, BoxState.ON]
        success = self.grid.set_state(new_state)
        self.assertTrue(success)
        self.assertEqual(self.grid.grid, new_state)
    
    def test_set_state_invalid_length(self):
        """Test setting state with invalid length."""
        new_state = [BoxState.ON, BoxState.OFF]  # Too short
        success = self.grid.set_state(new_state)
        self.assertFalse(success)
    
    def test_set_state_invalid_values(self):
        """Test setting state with invalid values."""
        new_state = [BoxState.ON, BoxState.OFF, 2, BoxState.OFF, BoxState.ON]  # Invalid value 2
        success = self.grid.set_state(new_state)
        self.assertFalse(success)
    
    def test_save_and_load_state(self):
        """Test saving and loading grid state."""
        # Set up a specific state
        self.grid.toggle_box(0)
        self.grid.toggle_box(2)
        self.grid.toggle_box(4)
        
        original_state = self.grid.get_state()
        
        # Save state to temporary file
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
            temp_filename = f.name
        
        try:
            # Save state
            success = self.grid.save_state(temp_filename)
            self.assertTrue(success)
            
            # Create new grid and load state
            new_grid = Grid(height=5)
            success = new_grid.load_state(temp_filename)
            self.assertTrue(success)
            
            # Compare states
            self.assertEqual(new_grid.get_state(), original_state)
            self.assertEqual(new_grid.height, self.grid.height)
            
        finally:
            # Clean up
            if os.path.exists(temp_filename):
                os.unlink(temp_filename)
    
    def test_load_nonexistent_file(self):
        """Test loading from a nonexistent file."""
        success = self.grid.load_state('nonexistent_file.json')
        self.assertFalse(success)
    
    def test_save_invalid_path(self):
        """Test saving to an invalid path."""
        success = self.grid.save_state('/invalid/path/file.json')
        self.assertFalse(success)


if __name__ == '__main__':
    unittest.main()