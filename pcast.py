#!/usr/bin/python

import feedparser, os, urllib2

workdir = '/home/bryan/pcast/'

twitlist = {
'twit': 'http://feeds.twit.tv/twit_video_hd', 
'mbw': 'http://feeds.twit.tv/mbw_video_large',
'tnt': 'http://feeds.twit.tv/tnt_video_large',
'tri': 'http://feeds.twit.tv/tri_video_large', 
'kh': 'http://feeds.twit.tv/kh_video_hd.xml',
'byb': 'http://feeds.twit.tv/byb_video_large',
}

revlist = {
'hak5': 'http://revision3.com/hak5/feed/MP4-hd30?subshow=false', 
'tekzilla': 'http://revision3.com/tekzilla/feed/MP4-hd30?subshow=false',
'benheck': 'http://revision3.com/tbhs/feed/MP4-hd30',
}

for line in twitlist:
    d = feedparser.parse(twitlist[line])
    if os.path.exists(workdir + line) == False:
    	os.makedirs(workdir + line)
    if os.path.exists(workdir + line + '/' + d.entries[0]['link'].split('/')[-1]) == False:
        #p = subprocess.call(['wget', d.entries[0]['link'], '-O', workdir + line + '/' + d.entries[0]['link'].split('/')[-1]])
        p = urllib2.urlopen(d.entries[0]['link'])
        f = open(workdir + line + '/' + d.entries[0]['link'].split('/')[-1], 'wb')
        while True:
            buffer = p.read(8192)
            if not buffer: break
            f.write(buffer)
        f.close()

for line in revlist:
    d = feedparser.parse(revlist[line])
    if os.path.exists(workdir + line) == False:
    	os.makedirs(workdir + line)
    if os.path.exists(workdir + line + '/' + d.entries[0]['media_content'][0]['url'].split('/')[-1]) == False:
        #p = subprocess.call(['wget', d.entries[0]['media_content'][0]['url'], '-O', workdir + line + '/' + d.entries[0]['media_content'][0]['url'].split('/')[-1]])
        p = urllib2.urlopen(d.entries[0]['media_content'][0]['url'])
        f = open(workdir + line + '/' + d.entries[0]['media_content'][0]['url'].split('/')[-1], 'wb')
        while True:
            buffer = p.read(8192)
            if not buffer: break
            f.write(buffer)
        f.close()

