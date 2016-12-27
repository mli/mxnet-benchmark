# mxnet-benchmark

Some benchmark scripts for [MXNet](http://mxnet.io)

## How to use

1. Put this repo on the same direcotry as MXNet, or edit `MX_ROOT` in `common.sh`
2. Only required for distributed benchmkaring, prepare a `hosts` file, each line
   contains the hostname or the IP of a worker.
3. For a task `A`, use `run_A.sh` to benchmark, and then `python parse_A.py` to
   parse the results. Results are saved in `log/`. We can often run the
   benchmark multiple times by
   ```bash
   for i in {1..10}; do ./run_A.sh; done
   ```

## Training on a single GPU for various batch size

Run with `run_vary_batch.sh`, parse results by `python parse_vary_batch.py`
