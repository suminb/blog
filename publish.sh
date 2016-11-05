#!/bin/bash

TARGET_REPO="git@github.com:suminb/blog-pub.git"
BUILD_DIR=_site
LAST_COMMIT_MESSAGE=$(git log -1 --pretty=%B)

git clone $TARGET_REPO $BUILD_DIR
jekyll build
pushd $BUILD_DIR
rm publish.sh
git add .
git commit -m "$LAST_COMMIT_MESSAGE"
git push
popd
