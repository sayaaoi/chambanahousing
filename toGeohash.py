import Geohash
f = open('coodinates.txt','r')
st = ''
ar = []
for line in f:
    coord = line.strip(';\n').split(',')
    geohash = Geohash.encode(float(coord[1]),float(coord[0]))
    st += geohash + ','
    if geohash not in ar:
        ar.append(geohash)
print(st)
print(ar)
with open('geohashes.txt', 'w') as geohash_file:
    for g in ar:
        geohash_file.write(g + '\n')