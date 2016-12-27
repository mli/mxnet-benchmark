import glob
import re
import math
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument('prefix', default='log directory prefix')
# args = parser.parse_args()

def round(x):
    return float(int(x*1e3))/1e3

def stats(arr):
    if len(arr) == 0:
        return (0, 0)
    mean = sum(arr) / len(arr)
    std = math.sqrt(sum([(v-mean)*(v-mean) for v in arr])/len(arr))
    return (round(mean), round(std))

def parse(dirname, data):
    log_re = re.compile('.*iter (\d+), ([.\d]+)')
    for fn in glob.glob(dirname + '/*'):
        with open(fn, 'r') as f:
            time = []
            for l in f:
                m = log_re.match(l)
                if m is not None:
                    i = int(m.groups()[0])
                    t = float(m.groups()[1])
                    if i > 1:
                        time.append(t)
            a = fn.split('_')
            assert len(a) == 3
            n = a[0].split('/')[-1].replace('-', '_')
            j = int(a[1])
            if n not in data:
                data[n] = {}
            if j not in data[n]:
                data[n][j] = []
            data[n][j] += time

def parse_all(prefix):
    data = {}
    for fn in glob.glob(prefix + '*'):
        print 'parse ' + fn
        parse(fn, data)

    for i in data:
        for j in data[i]:
            data[i][j] = stats(data[i][j])
        print '%s[%s] = %s' % (i, prefix.split('-')[1], data[i])

for i in [1, 2, 4, 8, 16]:
    parse_all('bandwidth-%d-gpus-' % (i,))
