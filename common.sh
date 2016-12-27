#!/bin/bash

# mxnet path, prefer absolution path
MX_ROOT=`pwd`/../mxnet

# hostfile, must absolute path
HOSTS=`pwd`/hosts

# it will create a dir ./logdir-timestamp, and then soft link it to ./logdir
function new_log_dir() {
    if [ $# -ne 1 ]; then
        echo "usage: new_log_dir ./logdir"
        exit -1
    fi

    time=`date +%F-%H-%M-%S`

    rm -rf $1-$time
    rm -rf $1

    mkdir $1-$time
    ln -s $1-$time $1
}
