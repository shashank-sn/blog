#!/bin/sh
# Rebuild downloads/<skill>.zip from skills/<skill>/. Run from the repo root after a skill changes.
set -eu
mkdir -p downloads
for dir in skills/*/; do
  name=$(basename "$dir")
  rm -f "downloads/$name.zip"
  (cd skills && zip -qrX "../downloads/$name.zip" "$name" -x '*.DS_Store')
  echo "built downloads/$name.zip"
done
