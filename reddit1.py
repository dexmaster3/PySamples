import json
import urllib2
from collections import Counter

req = urllib2.Request('http://www.reddit.com/comments/1lix1m/.json')
req.add_header('User-Agent', 'r/learnpython example')
response = urllib2.urlopen(req)
data = json.load(response)
submission_text=data[0]["data"]["children"][0]["data"]["selftext"]
c=Counter(submission_text)
for k,v in c.items():
    print "Letter '{}' is used {} times".format(k,v)
