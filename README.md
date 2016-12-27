# mxnet-benchmark

Some benchmark scripts for [MXNet](http://mxnet.io)

## How to use

1. Put this repo on the same direcotry as MXNet, or edit `MX_ROOT` in `common.sh`
2. Prepare a `hosts` file, each line
   contains the hostname or the IP of a worker. It is only required for benchmarking
   distributed performance
3. For a task `A`, use `run_A.sh` to benchmark. Results are saved in `log/`. To
   benchmark 10 times we can `./repeat.sh 10 ./run_A.sh`
4. Use `python parse_A.py` to parse the results.


## Training on a single GPU for various batch size

Run with `run_vary_batch.sh`, parse results by `python parse_vary_batch.py`
