#!/usr/bin/env bash
# fetch-assets.sh — pull the ASCEND headshot + lab logo into assets/.
# The deck must render offline, so every image has to live on disk.
#
#   ./fetch-assets.sh list                      # show every image URL on the lab site
#   ./fetch-assets.sh get HEADSHOT_URL LOGO_URL # download them to the names the deck expects
set -euo pipefail

SITE="https://ascend3.cs.vt.edu/"
BASE="${SITE%/}"
DEST="$(cd "$(dirname "$0")" && pwd)/assets"

die() { printf 'error: %s\n' "$*" >&2; exit 1; }
command -v curl >/dev/null || die "curl not found"

resolve() {
  case "$1" in
    http://*|https://*) printf '%s\n' "$1" ;;
    //*) printf 'https:%s\n' "$1" ;;
    /*)  printf '%s%s\n' "$BASE" "$1" ;;
    *)   printf '%s/%s\n' "$BASE" "$1" ;;
  esac
}

list() {
  curl -fsSL "$SITE" \
    | grep -oiE '(src|href|content)="[^"]+\.(jpe?g|png|svg|webp)[^"]*"' \
    | sed -E 's/^[a-zA-Z]+="//; s/"$//' \
    | while read -r u; do resolve "$u"; done \
    | sort -u
}

get_one() {
  local url="$1" stem="$2" ext out
  ext="${url##*.}"; ext="${ext%%\?*}"
  case "$ext" in
    jpg|jpeg|png|svg|webp) ;;
    *) die "unexpected extension '.$ext' in $url" ;;
  esac
  out="$DEST/$stem.$ext"
  mkdir -p "$DEST"
  curl -fsSL --max-time 30 -o "$out.part" "$url" || die "download failed: $url"
  [ -s "$out.part" ] || { rm -f "$out.part"; die "empty file: $url"; }
  mv "$out.part" "$out"
  printf '  %-28s %s\n' "assets/$stem.$ext" "$(du -h "$out" | cut -f1)"
}

case "${1:-}" in
  list) list ;;
  get)
    [ $# -eq 3 ] || die "usage: $0 get HEADSHOT_URL LOGO_URL"
    printf 'downloading into %s\n' "$DEST"
    get_one "$2" headshot-dhs4
    get_one "$3" ascend-logo
    printf 'done. if an extension differs from the slide, tell Slide Studio to update the data-src.\n'
    ;;
  *) sed -n '2,7p' "$0"; exit 1 ;;
esac
