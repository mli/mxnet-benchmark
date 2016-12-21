import re

log = "vary_batch/log"

f = open(log, "r")

network = ''
head=re.compile('.*batch_size=([\d]+).*network=\'([\w-]*)\'.*')
body=re.compile('.*40.*Speed: ([.\d]+)')

batch = 'xx'
for l in f:
    m = head.match(l)
    if m is not None:
        if m.groups()[1] != network:
            print '==== ' + m.groups()[1] + ' ===='
            print 'batch\timg/sec'
            network = m.groups()[1]
        batch = m.groups()[0]
    m = body.match(l)
    if m is not None:
        print batch + '\t' + m.groups()[0]
