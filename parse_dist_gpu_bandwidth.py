import glob
import re
from common import stats, match_res

def parse(dirname, data):
    log_re = re.compile('.*iter (\d+), ([.\d]+)')
    for fn in glob.glob(dirname + '/*'):
        res = match_res(fn, log_re)
        time = [float(i[1]) for i in res[1:-1]]
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
    res = ''
    data = {}
    for fn in glob.glob(prefix + '*'):
        print 'parse ' + fn
        parse(fn, data)

    for i in data:
        for j in data[i]:
            data[i][j] = stats(data[i][j])
        res +=  '%s[%s] = %s\n' % (i, prefix.split('-')[1], data[i])
    return res

if __name__ == '__main__':
    res = ''
    for i in [1, 2, 4, 8, 16]:
        res += parse_all('log/bandwidth-%d-gpus-' % (i,))
    print res
