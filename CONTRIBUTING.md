# Contributing to chaosPrimer

Thank you for your interest in contributing to chaosPrimer! This document provides guidelines and information for contributors.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Git
- Basic understanding of Python programming
- Familiarity with matplotlib and tkinter (optional but helpful)

### Setting up the Development Environment

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/your-username/chaosPrimer.git
   cd chaosPrimer
   ```
3. **Set up a virtual environment** (recommended):
   ```bash
   python -m venv venv
   # Activate it
   source venv/bin/activate  # On macOS/Linux
   .\venv\Scripts\activate   # On Windows
   ```
4. **Install dependencies**:
   ```bash
   pip install matplotlib
   ```
5. **Run tests** to ensure everything works:
   ```bash
   export MPLBACKEND=Agg  # For headless testing
   python test_grid.py
   ```

## How to Contribute

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include:

- **Clear description** of the problem
- **Steps to reproduce** the behavior
- **Expected behavior**
- **Actual behavior**
- **Environment information** (Python version, OS, etc.)
- **Screenshots** if applicable

### Suggesting Enhancements

Enhancement suggestions are welcome! Please provide:

- **Clear description** of the enhancement
- **Use case** explaining why it would be useful
- **Possible implementation** approach (if you have ideas)

### Pull Requests

1. **Create a feature branch** from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. **Make your changes** following our coding standards
3. **Add tests** for new functionality
4. **Run the test suite** and ensure all tests pass
5. **Update documentation** if needed
6. **Commit your changes** with clear commit messages
7. **Push to your fork** and create a pull request

## Coding Standards

### Code Style

- Follow **PEP 8** Python style guide
- Use **type hints** for all function parameters and return values
- Write **docstrings** for all classes and methods
- Keep line length to **88 characters** (Black formatter standard)

### Example Function Format

```python
def example_function(param1: int, param2: str = "default") -> bool:
    """
    Brief description of the function.
    
    Longer description if needed, explaining the purpose
    and any important details about the function.
    
    Args:
        param1 (int): Description of the first parameter
        param2 (str, optional): Description of the second parameter. Defaults to "default".
        
    Returns:
        bool: Description of the return value
        
    Raises:
        ValueError: Description of when this exception is raised
    """
    # Implementation here
    return True
```

### Testing Guidelines

- **Write tests** for all new functionality
- **Maintain test coverage** for existing features
- Use **descriptive test names** that explain what is being tested
- Follow the **Arrange-Act-Assert** pattern in tests

#### Test Example

```python
def test_toggle_box_changes_state(self):
    """Test that toggling a box changes its state correctly."""
    # Arrange
    grid = Grid(height=5)
    initial_state = grid.get_state()[0]
    
    # Act
    grid.toggle_box(0)
    
    # Assert
    final_state = grid.get_state()[0]
    self.assertNotEqual(initial_state, final_state)
```

### Documentation Guidelines

- Update **README.md** for user-facing changes
- Update **docstrings** for code changes
- Include **examples** in documentation when helpful
- Keep documentation **clear and concise**

## Development Workflow

### Branch Naming

Use descriptive branch names:
- `feature/add-save-functionality`
- `bugfix/fix-toggle-error-handling`
- `docs/update-readme`
- `test/add-grid-tests`

### Commit Messages

Write clear, descriptive commit messages:
- Use **present tense** ("Add feature" not "Added feature")
- Keep first line **under 50 characters**
- Include additional details in the body if needed

#### Good Examples
```
Add save/load functionality for grid state

Implement JSON-based persistence for grid configurations.
Includes error handling for file operations and validation
of loaded data.
```

```
Fix error handling in toggle_box_at_position

Add try-catch block to handle None values from mouse events
and improve robustness of user interactions.
```

### Testing Your Changes

Before submitting a pull request:

1. **Run all tests**:
   ```bash
   export MPLBACKEND=Agg
   python test_grid.py -v
   ```

2. **Test the GUI** (if tkinter is available):
   ```bash
   python visualise.py
   ```

3. **Test import functionality**:
   ```bash
   python -c "from grid import Grid; print('Import successful')"
   ```

## Areas for Contribution

### Current Opportunities

1. **Performance Optimization**
   - Improve rendering for large grids
   - Optimize memory usage for grid state

2. **User Interface Enhancements**
   - Add keyboard shortcuts
   - Implement undo/redo functionality
   - Add color customization options

3. **Additional Features**
   - Pattern generation algorithms
   - Grid export to image formats
   - Animation/playback capabilities

4. **Testing and Quality**
   - Increase test coverage
   - Add integration tests
   - Performance benchmarking

5. **Documentation**
   - Video tutorials
   - More usage examples
   - API documentation improvements

### Skills Needed

- **Python Programming**: Core requirement
- **GUI Development**: For tkinter-related improvements
- **Data Visualization**: For matplotlib enhancements
- **Testing**: For QA contributions
- **Documentation**: For docs improvements

## Code Review Process

All contributions go through code review:

1. **Automated checks** run on pull requests
2. **Manual review** by maintainers
3. **Feedback and iterations** may be requested
4. **Approval and merge** once ready

### Review Criteria

- Code follows project standards
- Tests pass and coverage is maintained
- Documentation is updated appropriately
- Changes are backwards compatible (when possible)
- Performance impact is considered

## Questions and Support

- **Issues**: Use GitHub issues for bug reports and feature requests
- **Discussions**: Use GitHub discussions for questions and ideas
- **Code Questions**: Comment on specific lines in pull requests

## Recognition

Contributors will be:
- **Acknowledged** in commit history
- **Mentioned** in release notes for significant contributions
- **Listed** as contributors in the project

Thank you for contributing to chaosPrimer! Your efforts help make this project better for everyone.