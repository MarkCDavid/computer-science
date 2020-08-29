#!/usr/bin/env sh

find . -name "*.html" -print0 | xargs -0 zip "$1"