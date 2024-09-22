#!/bin/bash

# Array of fake contributors with names and genuine-like domains
declare -a CONTRIBUTORS=(
    "Alice:alice@techwizard.ai"
    "Bob:bob@codegenius.dev"
    "Charlie:charlie@cybernode.io"
    "David:david@buildcore.net"
    "Eve:eve@devspark.co"
    "Frank:frank@nextvision.tech"
    "Grace:grace@openhub.org"
    "Hannah:hannah@pixelcraft.pro"
    "Ivan:ivan@datamatrix.xyz"
    "Judy:judy@cloudforge.app"
    "Kevin:kevin@innovatestudio.io"
    "Laura:laura@thinkstack.ai"
    "Mike:mike@brightlabs.tech"
    "Nina:nina@blockstride.com"
)

# Get the current date
CURRENT_DATE=$(date +%s)

# Loop through contributors
for i in "${!CONTRIBUTORS[@]}"; do
    NAME=$(echo "${CONTRIBUTORS[$i]}" | cut -d':' -f1)
    EMAIL=$(echo "${CONTRIBUTORS[$i]}" | cut -d':' -f2)

    # Calculate a commit date 3 months ago (randomized within the range)
    OFFSET=$((90 * 24 * 3600)) # 3 months in seconds
    RANDOM_OFFSET=$((RANDOM % OFFSET))
    COMMIT_DATE=$(date -d "@$((CURRENT_DATE - OFFSET + RANDOM_OFFSET))" --iso-8601=seconds)

    # Create a fake commit
    GIT_AUTHOR_NAME="$NAME" GIT_AUTHOR_EMAIL="$EMAIL" \
    GIT_COMMITTER_NAME="$NAME" GIT_COMMITTER_EMAIL="$EMAIL" \
    GIT_AUTHOR_DATE="$COMMIT_DATE" GIT_COMMITTER_DATE="$COMMIT_DATE" \
    git commit --allow-empty -m "Fake contribution by $NAME"
done

echo "Fake contributions added!"
