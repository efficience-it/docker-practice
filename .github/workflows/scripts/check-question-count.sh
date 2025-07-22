#!/bin/bash

threshold=5
base_dir="data"
exit_code=0

find "$base_dir" -type f -name "*.yaml" | while read -r file; do
  count=$(grep -c '^[[:space:]]*question:' "$file")
  if [ "$count" -lt "$threshold" ]; then
    echo "$file → $count question(s)"
    exit_code=1
  fi
done

exit $exit_code
