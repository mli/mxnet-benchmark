#!/bin/bash

np=$1
shift

for (( i = 0; i < np; ++i )); do
    $@
done
