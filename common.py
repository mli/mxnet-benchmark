import math
def match_res(fname, pattern):
    res = []
    with open(fname, 'r') as f:
        for l in f:
            m = pattern.match(l)
            if m is not None:
                res.append(m.groups())
    return res

def round(x):
    return float(int(x*1e3))/1e3

def stats(arr):
    if len(arr) == 0:
        return (0, 0)
    mean = sum(arr) / len(arr)
    std = math.sqrt(sum([(v-mean)*(v-mean) for v in arr])/len(arr))
    return (round(mean), round(std))
