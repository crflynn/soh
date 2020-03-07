#!/bin/bash
set -ex
# crate version
VERSION=$(cargo metadata --format-version 1 --no-deps | jq '.packages' | jq '.[0]' | jq -r '.version')
# current commit
COMMIT=$(git rev-parse HEAD)

DIST_FOLDER=.dist/$VERSION
# api responses
WORKFLOWS_JSON=.dist/workflows.json
ARTIFACTS_JSON=.dist/artifacts.json

# artifact names
MAC_ARTIFACT=x86_64-apple-darwin
LINUX_ARTIFACT=x86_64-unknown-linux-musl

# create a folder for the binaries
rm -rf "$DIST_FOLDER"
mkdir -p "$DIST_FOLDER"

# pull the artifacts from the most recent build on master
set +x
curl -H "Authorization: token $GITHUB_TOKEN" "https://api.github.com/repos/crflynn/soh/actions/workflows/ci.yml/runs?branch=master" > "$WORKFLOWS_JSON"
curl -H "Authorization: token $GITHUB_TOKEN" "$(jq '.workflow_runs' "$WORKFLOWS_JSON" | jq '.[0]' | jq -r '.artifacts_url')" > "$ARTIFACTS_JSON"
curl -H "Authorization: token $GITHUB_TOKEN" "$(jq '.artifacts' "$ARTIFACTS_JSON"| jq '.[0]' | jq -r '.archive_download_url')" -L > "$DIST_FOLDER/$(jq '.artifacts' "$ARTIFACTS_JSON" | jq '.[0]' | jq -r '.name').zip"
curl -H "Authorization: token $GITHUB_TOKEN" "$(jq '.artifacts' "$ARTIFACTS_JSON" | jq '.[1]' | jq -r '.archive_download_url')" -L > "$DIST_FOLDER/$(jq '.artifacts' "$ARTIFACTS_JSON" | jq '.[1]' | jq -r '.name').zip"
set -x

# rename them to proper values
mv "$DIST_FOLDER"/$MAC_ARTIFACT.zip "$DIST_FOLDER"/soh-"$VERSION"-$MAC_ARTIFACT.zip
mv "$DIST_FOLDER"/$LINUX_ARTIFACT.zip "$DIST_FOLDER"/soh-"$VERSION"-$LINUX_ARTIFACT.zip

# push
ghr -u crflynn -r soh -c "$COMMIT" -delete "$VERSION" "$DIST_FOLDER"

# print these values for the brew recipe
echo "$VERSION"
sha256sum "$DIST_FOLDER"/soh-"$VERSION"-$MAC_ARTIFACT.zip
sha256sum "$DIST_FOLDER"/soh-"$VERSION"-$LINUX_ARTIFACT.zip
