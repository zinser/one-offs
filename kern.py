import requests, re

infile = open('/home/bryan/.kern', 'r+')

r = requests.get('http://finger.kernel.org/kdist/finger_banner')
sweet = r.content.split('\n')
for line in sweet:
    if "3.4" in line:
        blah = re.search(r'(\d+\.\d+\.\d+)', line)

if infile.read().rstrip() == blah.group(0):
    print "UP TO DATE"
else:
    print "UPDATE TO VERSION {0}".format(blah.group(0))
    infile.seek(0)
    infile.write(blah.group(0))

infile.close()
