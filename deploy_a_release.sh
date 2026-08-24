#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"

echo "Building a new release of fmpsdk!"
echo

for cmd in poetry black pytest git; do
    if ! command -v "$cmd" >/dev/null 2>&1; then
        echo "'$cmd' isn't on PATH. Did you 'source .venv/bin/activate' first?"
        exit 1
    fi
done

# --- 1. Formatting check, fmpsdk/ only -- that's the code that actually ships to
#     PyPI. (tests/ can carry its own independent drift; that's a separate concern
#     from whether a release is safe to cut.) ---
echo "Checking black formatting on fmpsdk/ ..."
if ! black --check fmpsdk/; then
    echo
    echo "fmpsdk/ isn't black-formatted. Run 'black fmpsdk/' and re-run this script."
    exit 1
fi
echo "OK."
echo

# --- 2. Unit tests. No network, no API quota spent -- the whole point of having
#     268 of them is to catch a regression here, not after it's on PyPI. ---
echo "Running unit tests..."
if ! pytest -m unit -q; then
    echo
    echo "Unit tests failed. Fix them before releasing."
    exit 1
fi
echo "OK."
echo

# --- 3. poetry's own sanity check on pyproject.toml ---
echo "Running poetry check..."
if ! poetry check; then
    echo
    echo "poetry check failed -- fix pyproject.toml before releasing."
    exit 1
fi
echo "OK."
echo

# --- 4. The version is declared in two places: pyproject.toml (what actually gets
#     published) and fmpsdk/__init__.py's __version__ (what `import fmpsdk;
#     fmpsdk.__version__` reports at runtime for anyone who installs it). If these
#     drift, the installed package lies about its own version. Both must be bumped
#     and must match -- this project keeps FMP's inherited DATE.PATCH scheme (e.g.
#     20260824.0), not SemVer. ---
PYPROJECT_VERSION=$(grep -m1 '^version = ' pyproject.toml | sed -E 's/version = "(.*)"/\1/')
INIT_VERSION=$(grep -m1 '__version__ = ' fmpsdk/__init__.py | sed -E 's/__version__ = "(.*)"/\1/')

if [[ "$PYPROJECT_VERSION" != "$INIT_VERSION" ]]; then
    echo "Version mismatch:"
    echo "  pyproject.toml:     $PYPROJECT_VERSION"
    echo "  fmpsdk/__init__.py: $INIT_VERSION"
    echo "Update both to match before releasing."
    exit 1
fi

if git rev-parse "v$PYPROJECT_VERSION" >/dev/null 2>&1; then
    echo "Tag v$PYPROJECT_VERSION already exists -- this version was already released."
    echo "Bump the version in pyproject.toml AND fmpsdk/__init__.py before releasing again."
    exit 1
fi

echo "About to publish fmpsdk $PYPROJECT_VERSION to PyPI."
read -p "Is that version correct and bumped from the last release? (y/n): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Aborting. Update the version in pyproject.toml AND fmpsdk/__init__.py, then re-run."
    exit 1
fi
echo

echo "Building package via poetry"
poetry build
echo

echo "Publishing package"
poetry publish
echo

echo "Tagging release v$PYPROJECT_VERSION and pushing the tag"
git tag "v$PYPROJECT_VERSION"
git push origin "v$PYPROJECT_VERSION"

echo
echo "Done. Released fmpsdk $PYPROJECT_VERSION to PyPI, tagged v$PYPROJECT_VERSION."
