import requests
import re

sites = open("/Users/Brick/Desktop/General Conference Project/sites.txt","r").readlines()
pattern = re.compile(r"\"(?P<link>.*)\?.*class=\"lumen-tile__link\"")
i = 0
for site in sites:
    i += 1
    site = site.replace("\n", "")
    response = requests.get(site).text
    talks = re.findall(pattern, response)
    talkdoc = open("/Users/Brick/Desktop/General Conference Project/talks.txt","a") 
    for talk in talks:
        talkdoc.write(talk + '\n')
    talkdoc.close()
    print(str(i) + " is done.")