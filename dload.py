import urllib2, sys

urll = sys.argv[1]

r = urllib2.urlopen(urll)
f = open(urll.split('/')[-1], 'w')
sweet = int(r.headers['Content-Length'])
while True:
    buffer = r.read(8192)
    if not buffer: break
    f.write(buffer)
    sweet -= 8192
    print str(sweet) + '/' + r.headers['Content-Length']
f.close()
