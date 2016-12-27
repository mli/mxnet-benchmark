#!/bin/bash
source common.sh

LOG=`pwd`/speed
new_log_dir $LOG

cd $MX_ROOT/example/image-classification

for network in alexnet inception-v3 resnet ; do
    if [ "$network" == "inception-v3" ]; then
        shape=299
    else
        shape=224
    fi

    for bs in 1 2 4 8 16 32; do
        if [ "$network" == "alexnet" ]; then
            bs=$((bs*16))
        fi

        python benchmark.py --worker_file $HOSTS --worker_count 16 --gpu_count 16 \
            --networks ${network}:${bs}:${shape} \
            2>&1 | tee $LOG/${network}_${bs}
    done
done
