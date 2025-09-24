# Contributing to Unity MCP Server

Thank you for your interest in contributing to the Unity MCP Server! This document provides guidelines and information for contributors.

## 🚀 Quick Start for Contributors

### Prerequisites

- **Python 3.10+** (3.12 recommended)
- **Unity 2021.3 LTS+**
- **Git**
- **uv** (Python package manager) - [Installation Guide](https://docs.astral.sh/uv/getting-started/installation/)

### Development Setup

1. **Fork and Clone**
   ```bash
   git clone https://github.com/YOUR_USERNAME/unity-mcp.git
   cd unity-mcp
   ```

2. **Install Development Dependencies**
   ```bash
   pip install -r requirements-dev.txt
   ```

3. **Install Pre-commit Hooks**
   ```bash
   pre-commit install
   ```

4. **Install MCP Server in Development Mode**
   ```bash
   cd UnityMcpBridge/UnityMcpServer~/src
   pip install -e .
   ```

## 🔧 Development Workflow

### Code Style and Quality

We maintain high code quality standards using automated tools:

- **Black**: Code formatting (88 character line limit)
- **isort**: Import sorting
- **flake8**: Linting
- **mypy**: Type checking
- **bandit**: Security analysis

#### Running Quality Checks Locally

```bash
# Format code
black UnityMcpBridge/UnityMcpServer~/src

# Sort imports
isort UnityMcpBridge/UnityMcpServer~/src

# Lint code
flake8 UnityMcpBridge/UnityMcpServer~/src

# Type checking
mypy UnityMcpBridge/UnityMcpServer~/src

# Security check
bandit -r UnityMcpBridge/UnityMcpServer~/src
```

#### Pre-commit Hooks

Pre-commit hooks automatically run quality checks before each commit. If you need to bypass them temporarily:

```bash
git commit --no-verify -m "Your commit message"
```

### Testing

#### Running Tests

```bash
# Run all tests
cd tests && python -m pytest -v

# Run with coverage
cd tests && python -m pytest --cov=../UnityMcpBridge/UnityMcpServer~/src --cov-report=html

# Run specific test file
cd tests && python -m pytest test_specific_module.py -v
```

#### Writing Tests

- Place test files in the `tests/` directory
- Name test files with the pattern `test_*.py`
- Use descriptive test function names: `test_function_does_expected_thing`
- Include docstrings for complex test cases
- Mock external dependencies (Unity connections, file system operations)

Example test:
```python
import pytest
from unittest.mock import patch, MagicMock

def test_unity_connection_retries_on_failure():
    """Test that Unity connection retries appropriately on failure."""
    with patch('socket.socket') as mock_socket:
        mock_socket.side_effect = ConnectionRefusedError("Connection failed")
        
        # Your test implementation here
        assert expected_behavior
```

## 📁 Project Structure

```
unity-mcp/
├── UnityMcpBridge/                 # Unity package
│   ├── Editor/                     # Unity Editor scripts (C#)
│   ├── Runtime/                    # Unity runtime scripts (C#)
│   └── UnityMcpServer~/           # Python MCP server
│       └── src/                   # Python source code
│           ├── config.py          # Configuration management
│           ├── server.py          # Main server entry point
│           ├── unity_connection.py # Unity communication
│           ├── telemetry.py       # Analytics (privacy-focused)
│           └── tools/             # MCP tool implementations
├── tests/                         # Python tests
├── TestProjects/                  # Unity test projects
└── .github/workflows/             # CI/CD pipelines
```

## 🔄 Contribution Process

### 1. Create an Issue (Recommended)

Before starting work, create an issue to:
- Describe the problem or enhancement
- Discuss the approach with maintainers
- Get feedback on implementation ideas

### 2. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b bugfix/issue-description
```

### 3. Make Your Changes

- Write clean, well-documented code
- Follow existing code patterns and conventions
- Add or update tests as necessary
- Update documentation if needed

### 4. Commit Your Changes

Use conventional commit messages:

```bash
# Features
git commit -m "feat: add new MCP tool for shader management"

# Bug fixes  
git commit -m "fix: resolve connection timeout in Unity bridge"

# Documentation
git commit -m "docs: update installation instructions"

# Refactoring
git commit -m "refactor: improve error handling in telemetry module"

# Tests
git commit -m "test: add comprehensive tests for script validation"
```

### 5. Push and Create Pull Request

```bash
git push origin feature/your-feature-name
```

Create a pull request with:
- Clear title describing the change
- Detailed description of what was changed and why
- Reference to related issues
- Screenshots for UI changes

## 🧪 Code Quality Standards

### Python Code Guidelines

- **PEP 8 compliance** (enforced by flake8)
- **88-character line limit** (Black formatting)
- **Type hints** for public APIs
- **Comprehensive docstrings** for modules, classes, and functions
- **Error handling** - avoid bare `except:` clauses

Example:
```python
from typing import Optional, Dict, Any
import logging

logger = logging.getLogger(__name__)

def process_unity_message(
    message: Dict[str, Any], 
    timeout: float = 10.0
) -> Optional[Dict[str, Any]]:
    """
    Process a message received from Unity Editor.
    
    Args:
        message: The message dictionary from Unity
        timeout: Maximum time to wait for processing
        
    Returns:
        Processed message dictionary, or None if processing failed
        
    Raises:
        ConnectionError: If Unity connection is lost during processing
        ValueError: If message format is invalid
    """
    try:
        # Implementation here
        return processed_message
    except ConnectionError as e:
        logger.error(f"Unity connection lost: {e}")
        raise
    except Exception as e:
        logger.warning(f"Message processing failed: {e}")
        return None
```

### C# Code Guidelines (Unity)

- Follow Unity's C# style guidelines
- Use Unity's logging system (`Debug.Log`, etc.)
- Handle Unity's async patterns appropriately
- Document public APIs with XML comments

## 🐛 Bug Reports

When reporting bugs, please include:

1. **Environment Information**
   - Unity version
   - Python version
   - Operating system
   - MCP client (Claude, Cursor, etc.)

2. **Steps to Reproduce**
   - Minimal reproducible example
   - Expected vs actual behavior
   - Error messages or logs

3. **Additional Context**
   - Screenshots if applicable
   - Relevant configuration files
   - Any attempted workarounds

## 🔒 Security

- Report security vulnerabilities privately to the maintainers
- Do not commit secrets, API keys, or sensitive data
- Use `secrets` module instead of `random` for security-sensitive operations
- Follow secure coding practices for network communications

## 📖 Documentation

- Update relevant documentation for new features
- Include code examples in docstrings
- Update README.md if installation or usage changes
- Consider adding entries to troubleshooting guides

## 🤝 Code Review Process

- All changes require review before merging
- Reviews focus on code quality, security, and architectural consistency
- Be responsive to reviewer feedback
- Use GitHub's suggestion feature for minor changes

## 📄 License

By contributing, you agree that your contributions will be licensed under the same MIT License as the project.

## 🆘 Getting Help

- **GitHub Issues**: For bug reports and feature requests
- **GitHub Discussions**: For questions and community support  
- **Discord**: [Join our community](https://discord.gg/y4p8KfzrN4)

---

Thank you for contributing to Unity MCP Server! 🎉