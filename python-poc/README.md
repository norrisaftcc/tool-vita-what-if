# Python Proof of Concept

This directory contains Python artifacts from the VITA repository analysis. These files demonstrate how the original VITA application could be simplified from 300+ lines to ~100 lines.

## Files

- `vita_simple.py` - 100-line simplified implementation of VITA
- `requirements_simple.txt` - Minimal 4-package dependencies (vs 40+ in original)
- `requirements-test.txt` - Testing requirements for the Python version
- `pytest.ini` - pytest configuration for Python testing

## Note

These files are **NOT** part of the main TypeScript/React project. They exist solely as proof-of-concept demonstrations showing the potential for radical simplification of the original VITA Panel Testing application.

The main project uses:
- TypeScript/React for frontend
- Vitest for testing
- Vite for building

These Python files are kept for reference and comparison purposes only.