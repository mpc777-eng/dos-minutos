#!/usr/bin/env bash
# Publish Dos Minutos to GitHub Pages. Safe to re-run: the first run creates the repo
# and turns on Pages; later runs just commit and push changes (Pages redeploys in ~1 min).
# Needs: gh CLI signed in (`gh auth status`), with the repo scope.
set -euo pipefail
cd "$(dirname "$0")"
REPO="${REPO:-dos-minutos}"
OWNER="$(gh api user --jq .login)"

if [ ! -d .git ]; then
  git init -q -b main
  git config user.name  >/dev/null || git config user.name  "$OWNER"
  git config user.email >/dev/null || git config user.email "$OWNER@users.noreply.github.com"
fi
touch .nojekyll
git add -A
git commit -q -m "${1:-Update Dos Minutos ($(date +%F))}" || echo "Nothing new to commit."

if ! gh repo view "$OWNER/$REPO" >/dev/null 2>&1; then
  gh repo create "$OWNER/$REPO" --public --source . --remote origin --push \
    --description "Dos Minutos: 2-minute Spanish listen & speak practice (PWA)"
  gh api -X POST "repos/$OWNER/$REPO/pages" -f "source[branch]=main" -f "source[path]=/" >/dev/null
else
  git remote get-url origin >/dev/null 2>&1 || git remote add origin "https://github.com/$OWNER/$REPO.git"
  git push -q origin main
fi
echo "Live (after about a minute): https://$OWNER.github.io/$REPO/"
