#!/usr/bin/env bash
# Install / refresh vendored html-ppt assets for hardware-insight decks.
set -euo pipefail

VERSION_PIN="1.0.0"
REPO="https://github.com/lewislulu/html-ppt-skill.git"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEST="${SCRIPT_DIR}/../deck-assets"
TMP="${TMPDIR:-/tmp}/html-ppt-skill-install"

echo "hardware-insight: installing deck-assets (pin ${VERSION_PIN})"
rm -rf "$TMP"
git clone --depth 1 "$REPO" "$TMP"

mkdir -p "$DEST/assets/themes"
cp "$TMP/assets/base.css" "$TMP/assets/fonts.css" "$TMP/assets/runtime.js" "$DEST/assets/"
cp "$TMP/assets/themes/blueprint.css" "$TMP/assets/themes/engineering-whiteprint.css" "$DEST/assets/themes/"

# hi-deck.css is maintained in-repo (not overwritten from upstream)
if [[ ! -f "$DEST/assets/hi-deck.css" ]]; then
  echo "WARN: hi-deck.css missing — copy from repo after first commit"
fi

echo "$VERSION_PIN" > "$DEST/VERSION"
rm -rf "$TMP"
echo "Done: $DEST (version $(cat "$DEST/VERSION"))"
