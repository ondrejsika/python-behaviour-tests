d = {}
d[2] = 'b'
d[1] = 'a'
d[3] = 'c'
d[7] = 'g'
d[4] = 'd'
d[6] = 'f'
d[5] = 'e'
d[8] = 'h'

print 'Items:  ', tuple((k, v) for k, v in d.items())
print 'Keys:   ', tuple(k for k in d.keys())
print 'Values: ', tuple(v for v in d.values())

