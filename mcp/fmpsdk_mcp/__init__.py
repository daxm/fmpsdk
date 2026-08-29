"""fmpsdk-mcp — a Model Context Protocol server wrapping the fmpsdk library.

Lives in the fmpsdk repo (mcp/ subdirectory), published to PyPI as its own
package. Uses the same DATE.PATCH version scheme as fmpsdk itself; the number
is this package's own release date, not the fmpsdk release it targets (that
floor is the ``fmpsdk>=`` pin in pyproject.toml).
"""

__version__ = "20260829.0"
