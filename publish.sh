#!/bin/bash

# Fail on error
set -e

TARGET_REPO="git@github.com:suminb/blog-pub.git"
BUILD_DIR=_site
LAST_COMMIT_MESSAGE=$(git log -1 --pretty=%B)

rm -rf $BUILD_DIR
jekyll build
pushd $BUILD_DIR
rm publish.sh
git init
git remote add origin $TARGET_REPO
git add .
git commit -m "$LAST_COMMIT_MESSAGE"
git push -f origin master
popd
