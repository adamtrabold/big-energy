#!/usr/bin/env bash
# Rebuild the project site and push it to the gh-pages branch (GitHub Pages serves that branch).
# Run from anywhere: bash site/publish.sh
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SRC="$ROOT/site/design/concepts/herbarium/prototype"
python3 "$SRC/build.py"
TMP="$(mktemp -d)"
cp -r "$SRC/index.html" "$SRC/media" "$TMP/"
touch "$TMP/.nojekyll"
cd "$TMP"
git init -q -b gh-pages
git add -A
# Owner rule: never credit Claude on GitHub. Commit as the owner, no co-author lines.
export GIT_AUTHOR_NAME="Adam Trabold" GIT_AUTHOR_EMAIL="adamtrabold@users.noreply.github.com"
export GIT_COMMITTER_NAME="$GIT_AUTHOR_NAME" GIT_COMMITTER_EMAIL="$GIT_AUTHOR_EMAIL"
git commit -qm "Site build from main $(git -C "$ROOT" rev-parse --short HEAD)"
git remote add origin "$(git -C "$ROOT" remote get-url origin)"
git push -q -f origin gh-pages
echo "Published to gh-pages: https://adamtrabold.github.io/big-energy/"
