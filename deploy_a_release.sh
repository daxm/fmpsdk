#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"

echo "Building a new release of fmpsdk!"
echo

for cmd in poetry pytest git; do
    if ! command -v "$cmd" >/dev/null 2>&1; then
        echo "'$cmd' isn't on PATH. Did you 'source .venv/bin/activate' first?"
        exit 1
    fi
done

# --- 1. Unit tests. No network, no API quota spent -- the whole point of having
#     268 of them is to catch a regression here, not after it's on PyPI.
#     (Formatting isn't checked here anymore -- .github/workflows/publish.yml runs
#     black --check as a real gate on the tag push this script ends with, so a
#     second local copy of that check would just be duplicated effort.) ---
echo "Running unit tests..."
if ! pytest -m unit -q; then
    echo
    echo "Unit tests failed. Fix them before releasing."
    exit 1
fi
echo "OK."
echo

# --- 2. poetry's own sanity check on pyproject.toml ---
echo "Running poetry check..."
if ! poetry check; then
    echo
    echo "poetry check failed -- fix pyproject.toml before releasing."
    exit 1
fi
echo "OK."
echo

# --- 3. The version is declared in two places: pyproject.toml (what actually gets
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

echo "About to release fmpsdk $PYPROJECT_VERSION: tagging v$PYPROJECT_VERSION and"
echo "pushing it will trigger .github/workflows/publish.yml, which builds and"
echo "publishes to PyPI via Trusted Publishing (no token stored anywhere)."
read -p "Is that version correct and bumped from the last release? (y/n): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Aborting. Update the version in pyproject.toml AND fmpsdk/__init__.py, then re-run."
    exit 1
fi
echo

# Local build is just a sanity check that packaging itself doesn't error --
# the artifact that actually gets published is the one CI builds fresh after
# this tag triggers publish.yml, not this one.
echo "Building package via poetry (sanity check only, not what gets published)"
poetry build
echo

echo "Tagging release v$PYPROJECT_VERSION and pushing the tag"
git tag "v$PYPROJECT_VERSION"
git push origin "v$PYPROJECT_VERSION"

echo
echo "Tag pushed. GitHub Actions is now building and publishing fmpsdk"
echo "$PYPROJECT_VERSION to PyPI: https://github.com/daxm/fmpsdk/actions"
echo "Once that run goes green, verify at https://pypi.org/project/fmpsdk/$PYPROJECT_VERSION/"
