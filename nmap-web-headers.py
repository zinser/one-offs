import urllib2
import sys

infile = open(sys.argv[1], 'r')
outfile = open(sys.argv[2], 'w')
state = 0

outfile.write('<html>\n<body>\n')

for line in infile:
    if "80/open" in line:
        ipaddr = line.split(' ')[1]
        url = 'http://' + ipaddr + '/'
        try:
            r = urllib2.urlopen(url, timeout=5)
        except:
            state = 1
        if state == 0:
            headers = str(r.headers).split('\r\n')
            outfile.write('====================<br>\n')
            outfile.write('<a href="' + url + '">' + ipaddr + '</a>' + '<br>\n')
            outfile.write('<ul>\n')
            for header in headers:
                outfile.write('<li>' + header + '</li>\n')
            outfile.write('</ul><br>\n')
        else:
            state = 0

outfile.write('</body>\n</html>\n')

infile.close()
outfile.close()
