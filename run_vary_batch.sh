#!/bin/bash

mx_root=../mxnet
mkdir -p vary_batch
log=`pwd`/"vary_batch/log"

rm -rf $log
touch $log
cd ${mx_root}/example/image-classification/

for network in alexnet resnet inception-v3; do
    if [ "$network" == "inception-v3" ]; then
        shape=3,299,299
    else
        shape=3,224,224
    fi

    for bs in 1 2 4 8 16 32; do
        if [ "$network" == "alexnet" ]; then
            bs=$((bs*16))
        fi
        echo "network = $network, batch size = $bs"
        python train_imagenet.py --benchmark 1 --batch-size $bs \
            --gpus 0 --network $network --image-shape $shape --num-epochs 1 \
            2>&1 | tee -a $log
    done
done
