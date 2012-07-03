import re
import subprocess

infile = open('input.html', 'r')
#outfile = open('output.sh', 'w')
a = 1

for line in infile:
    mp4 = re.findall('"(.*\.mp4)"', line)
    if mp4 != []:
        for filename in mp4:
            b = a
            if a < 10:
                b = '0' + str(a) 
            #scriptline = 'wget http://ipx-vod.s3.amazonaws.com/cisco/ccnp/rs/complete/' + filename + ' -O ' + str(b) + '-' + filename + ' \n'
            #outfile.write(scriptline)
            p = subprocess.call(['wget', 'http://ipx-vod.s3.amazonaws.com/cisco/ccnp/rs/complete/' + filename, '-O', str(b) + '-' + filename])
            a += 1
infile.close()
#outfile.close()
