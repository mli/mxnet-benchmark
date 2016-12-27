import glob
import re


exp=re.compile('.*num_gpus: ([\d]+).*sec: ([.\d]*)')
fns = [fn for fn in glob.glob('speed/*')]
fns = sorted(fns, key=lambda x:[x.split('_')[0], int(x.split('_')[1])])
for fn in fns:
    f = open(fn, 'r')
    print '====== ' + fn + ' ======'
    print '#GPUs\timage/sec\tefficiency'
    base = None
    for l in f:
        m = exp.match(l)
        if m is not None:
            (gpu, speed) = m.groups()
            if base is None:
                base = float(speed)
            print gpu + '\t' + speed + '\t' + str(float(speed)/base/float(gpu))
