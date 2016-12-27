#!/bin/sh
cat hosts | \
    xargs -I{} ssh -o StrictHostKeyChecking=no {} \
    killall -9 python
