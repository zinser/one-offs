import re

infile = open('input.html', 'r')
outfile = open('output.sh', 'w')

for line in infile:
    mp4 = re.findall('"(.*\.mp4)"', line)
    if mp4 != []:
        for filename in mp4:
            scriptline = 'wget http://ipx-vod.s3.amazonaws.com/cisco/ccnp/rs/complete/' + filename + ' \n'
            outfile.write(scriptline)

infile.close()
outfile.close()
