#!/bin/bash

source common.sh

NUM_NODES=`cat $HOSTS | wc -l`
LOG=`pwd`/bandwidth

cd $MX_ROOT/tools/bandwidth

for num_gpus in 1 2 4 8 16; do

    CUR_LOG=$LOG-${num_gpus}-gpus
    new_log_dir $CUR_LOG

    for network in alexnet resnet inception-v3; do
        if [ "$network" == "inception-v3" ]; then
            shape=3,299,299
        else
            shape=3,224,224
        fi

        # for nodes in `seq 1 $NUM_NODES`; do
        for nodes in 1 2 4 8 16; do
            head -n $nodes $HOSTS >hosts
            worker=$((nodes))
            server=$((nodes))
            ../launch.py --launcher ssh -H hosts -n $worker -s $server \
                python measure.py --test-results 0 \
                --kv-store dist_device_sync --network $network \
                --gpus `seq -s , 0 $(($num_gpus-1))` \
                --num-batches 50 --disp-batches 10 \
                --image-shape $shape \
                2>&1 | tee $CUR_LOG/${network}_${nodes}_node
        done
    done

done


            #
    # for gpus in 1 2 4 8 16; do
    #     python measure.py --test-results 0 \
    #         --gpus `seq -s , 0 $(($gpus-1))` \
    #         --kv-store device --network $network \
    #         --image-shape $shape \
    #         2>&1 | tee logs/${network}_g${gpus}
    # done
