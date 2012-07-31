import requests, re, urllib2, subprocess, sys, os

#infile = open('/home/bryan/.kern', 'r+')

bufsize = 0

r = requests.get('http://finger.kernel.org/kdist/finger_banner')
sweet = r.content.split('\n')
for line in sweet:
    if "3.4" in line:
        blah = re.search(r'(\d+\.\d+\.\d+)', line)

mykernver = subprocess.Popen(['uname', '-r'], stdout=subprocess.PIPE).communicate()
mykernver = re.search(r'(.*)-amd64', mykernver[0].rstrip())

if mykernver.group(1) == blah.group(0):
    print "UP TO DATE"
else:
    print "UPDATE TO VERSION {0}".format(blah.group(0))
    if os.path.exists('/home/bryan/download/linux-' + blah.group(0) + '.tar.bz2') == False:
        print "Downloading..."  
        p = urllib2.urlopen('http://www.kernel.org/pub/linux/kernel/v3.0/linux-' + blah.group(0) + '.tar.bz2')
        outfile = open('/home/bryan/download/linux-' + blah.group(0) + '.tar.bz2', 'w')
        while True:
    	    buffer = p.read(8192)
            if not buffer: break
            outfile.write(buffer)
            bufsize += 8192
            sys.stdout.write("\r({0}/{1})".format(str(bufsize), p.headers['content-length']))
            sys.stdout.flush()
        sys.stdout.write('\n')
        outfile.close()
    else:
        print "file is already downloaded, good luck!"
#    infile.seek(0)
#    infile.write(blah.group(0))
#    infile.close()
