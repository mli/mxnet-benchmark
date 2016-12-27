#!/bin/bash
source common.sh
LOG=`pwd`/log/bandwidth-0
new_log_dir $LOG
cd $MX_ROOT/tools/bandwidth


for network in alexnet resnet inception-v3; do
    if [ "$network" == "inception-v3" ]; then
        shape=3,299,299
    else
        shape=3,224,224
    fi

    for gpus in 1 2 4 8 16; do
        python measure.py --test-results 0 \
            --gpus `seq -s , 0 $(($gpus-1))` \
            --kv-store device --network $network \
            --image-shape $shape \
            --num-batches 50 --disp-batches 10 \
            2>&1 | tee $LOG/${network}_${gpus}_gpus
    done

done
