'''
Created on Nov 29, 2011

@author: Bowen
'''
#import feedparser
#feed = feedparser.parse( "http://rss.lemonde.fr/c/205/f/3050/index.rss" )
##for i in feed["feed"]:
##    print "Titre: %s"%i
#print feed["items"]

import re

regexp = re.compile(r"\b[A-Z]\w+\b", re.I|re.U)

for n in regexp.finditer("M Marie Ale est nill"):
    print n.group(0)

s = re.findall(r"(\b[A-Z]\w+\b)","M Marie est nill")
print s