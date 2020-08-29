#!/usr/bin/env sh

TRIES=0
while true; do
    TRIES=$((TRIES+1))
    if ! ./faultyscript.sh 1>>stdout.log 2>>stderr.log ; then
        cat stdout.log stderr.log
        echo "Program ran $TRIES times before an error occured"
        break
    fi
done