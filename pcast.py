import feedparser, subprocess, os

twitlist = {
'twit': 'http://feeds.twit.tv/twit_video_hd', 
'mbw': 'http://feeds.twit.tv/mbw_video_large',
'tnt': 'http://feeds.twit.tv/tnt_video_large',
'tri': 'http://feeds.twit.tv/tri_video_large', 
'kh': 'http://feeds.twit.tv/kh_video_hd.xml',
}

revlist = {
'hak5': 'http://revision3.com/hak5/feed/MP4-hd30?subshow=false', 
'tekzilla': 'http://revision3.com/tekzilla/feed/MP4-hd30?subshow=false',
}

for line in twitlist:
    d = feedparser.parse(twitlist[line])
    if os.path.exists('/home/bryan/pcast/' + line + '/' + d.entries[0]['link'].split('/')[-1]) == False:
        p = subprocess.call(['wget', d.entries[0]['link'], '-O', '/home/bryan/pcast/' + line + '/' + d.entries[0]['link'].split('/')[-1]])

for line in revlist:
    d = feedparser.parse(revlist[line])
    if os.path.exists('/home/bryan/pcast/' + line + '/' + d.entries[0]['media_content'][0]['url'].split('/')[-1]) == False:
        p = subprocess.call(['wget', d.entries[0]['media_content'][0]['url'], '-O', '/home/bryan/pcast/' + line + '/' + d.entries[0]['media_content'][0]['url'].split('/')[-1]])
