# mxnet-benchmark

Some benchmark scripts for [MXNet](http://mxnet.io)

## How to use

1. Put this repo on the same direcotry as MXNet, or edit `MX_ROOT` in `common.sh`
2. Only required for distributed benchmkaring, prepare a `hosts` file, each line
   contains the hostname or the IP of a worker.

## Training performance on a single GPU for various batch size

Run with `run_vary_batch.sh`, parse results by `python parse_vary_batch.py`
