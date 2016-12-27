import re
import glob
from common import match_res, stats

def parse(fname, data):
    print 'parsing ' + fname
    exp = re.compile('.*40.*Speed: ([.\d]+)')
    res = match_res(fname, exp)
    (net, bs) = fname.split('/')[-1].split('_')
    bs = int(bs)
    if net not in data:
        data[net] = {}
    if bs not in data[net]:
        data[net][bs] = []
    data[net][bs] += [float(e[0]) for e in res]

def parse_all(dirname, data):
    for fn in glob.glob(dirname+'/*'):
        parse(fn, data)

data = {}
for i in glob.glob('log/vary_batch-*'):
    parse_all(i, data)

for d in data:
    print '=== network : ' + d + ' ==='
    print 'batch\timages/sec'
    for b in sorted(data[d]):
        v = stats(data[d][b])
        print('%s\t%.2f (+- %.2f)' % (b, v[0], v[1]))
