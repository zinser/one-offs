import re, urllib2, os, tarfile


datadir = '/home/bryan/linkern/'

if os.path.exists(datadir) == True:
    os.chdir(datadir)
else:
    os.makedirs(datadir)
    os.chdir(datadir)

p = re.compile('\d+\.\d+\.\d+')
r = urllib2.urlopen('http://kernel.org/kdist/finger_banner').read().split('\n')

for line in r:
    if "stable" in line:
        kernver = p.search(line).group(0)
        break

kernfname = 'linux-' + kernver + '.tar.bz2'

if os.path.exists(kernfname) == False and os.path.exists('linux-' + kernver) == False:
    print "Downloading " + kernfname
    kernfile = open(kernfname, 'w')
    dload = urllib2.urlopen('http://www.kernel.org/pub/linux/kernel/v3.0/' + kernfname)
    while True:
        buffer = dload.read(8192)
        if not buffer: break
        kernfile.write(buffer)
    kernfile.close()
    if int(dload.headers['content-length']) == int(len(open(kernfname).read())):
        print "Extracting " + kernfname
        tarfile.open(kernfname, mode='r:bz2').extractall()
    print "Deleting " + kernfname
    os.remove(kernfname)

