#!/usr/bin/env bash
# Cut a release of the fmpsdk-mcp package (the mcp/ subdirectory), mirroring
# ../deploy_a_release.sh for the SDK. Runs the same gate CI does, sanity-builds
# the package locally, then tags `mcp-v<version>` and pushes -- which triggers
# .github/workflows/publish-mcp.yml to build and publish to PyPI via Trusted
# Publishing (no token stored anywhere).
#
# Run from anywhere; it cd's to the repo root itself. Needs: python (with
# `build`, `black`, `pytest` importable), git, and the working-tree fmpsdk +
# mcp packages installed (`pip install -e . -e ./mcp`).
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."

echo "Building a new release of fmpsdk-mcp!"
echo

for cmd in python git; do
    if ! command -v "$cmd" >/dev/null 2>&1; then
        echo "'$cmd' isn't on PATH."
        exit 1
    fi
done

# --- 1. Formatting + generated-artifact freshness + the mcp test suite. Same
#     three checks publish-mcp.yml runs; catching a failure here is cheaper
#     than catching it on the tag push. ---
echo "Checking formatting (black --check mcp/ tools/)..."
black --check mcp/ tools/
echo "OK."
echo

echo "Checking generated artifacts are in sync with the source..."
python tools/gen_openapi.py --check
python tools/gen_tiers.py --check
echo "OK."
echo

echo "Running the mcp test suite..."
if ! python -m pytest mcp/tests -q; then
    echo
    echo "mcp tests failed. Fix them before releasing."
    exit 1
fi
echo "OK."
echo

# --- 2. Version. Single-sourced from fmpsdk_mcp/__init__.py (pyproject.toml
#     reads it via [tool.hatch.version]), so there's only one place to bump
#     and nothing to keep in sync. Same DATE.PATCH scheme as the SDK; the
#     number is THIS package's release date. ---
VERSION=$(python -c "import mcp.fmpsdk_mcp as m; print(m.__version__)" 2>/dev/null \
    || sed -nE 's/^__version__ = "(.*)"/\1/p' mcp/fmpsdk_mcp/__init__.py)

if [[ -z "$VERSION" ]]; then
    echo "Couldn't read __version__ from mcp/fmpsdk_mcp/__init__.py"
    exit 1
fi

if git rev-parse "mcp-v$VERSION" >/dev/null 2>&1; then
    echo "Tag mcp-v$VERSION already exists -- this version was already released."
    echo "Bump __version__ in mcp/fmpsdk_mcp/__init__.py before releasing again."
    exit 1
fi

# server.json (the MCP Registry metadata) carries the version in two spots.
# publish-mcp.yml rewrites both from the tag, but the committed file should
# still match __version__ so a manual `mcp-publisher publish` is correct too.
SJ_VERSION=$(sed -nE 's/.*"version": "([0-9.]+)".*/\1/p' mcp/server.json | head -1)
if [[ "$SJ_VERSION" != "$VERSION" ]]; then
    echo "Version mismatch:"
    echo "  mcp/fmpsdk_mcp/__init__.py: $VERSION"
    echo "  mcp/server.json:            $SJ_VERSION"
    echo "Set both 'version' fields in mcp/server.json to $VERSION, then re-run."
    exit 1
fi

echo "About to release fmpsdk-mcp $VERSION: tagging mcp-v$VERSION and pushing it"
echo "will trigger .github/workflows/publish-mcp.yml, which builds and publishes"
echo "to PyPI via Trusted Publishing."
read -p "Is that version correct and bumped from the last release? (y/n): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Aborting. Update __version__ in mcp/fmpsdk_mcp/__init__.py, then re-run."
    exit 1
fi
echo

# --- 3. Local build: sanity check that packaging doesn't error. The published
#     artifact is the one publish-mcp.yml builds fresh after the tag push. ---
echo "Building package (sanity check only, not what gets published)..."
rm -rf mcp/dist
python -m build --outdir mcp/dist mcp/
echo

echo "Tagging release mcp-v$VERSION and pushing the tag..."
git tag "mcp-v$VERSION"
git push origin "mcp-v$VERSION"

echo
echo "Tag pushed. GitHub Actions is now building and publishing fmpsdk-mcp"
echo "$VERSION to PyPI: https://github.com/daxm/fmpsdk/actions"
echo "Once that run goes green, verify at https://pypi.org/project/fmpsdk-mcp/$VERSION/"
