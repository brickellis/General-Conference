from bs4 import BeautifulSoup
import requests
import re
import time

pattern = re.compile(r"[^a-zA-Z0-9]+")
talks = sites = open("/Users/_____/Desktop/General Conference Project/talks.txt","r").readlines()
i = 0
for talk in talks:
    i += 1
    talk = talk.replace("\n", "")
    talk = "http://www.churchofjesuschrist.org" + talk
    response = requests.get(talk)
    soup = BeautifulSoup(response.text, "html.parser")
    text_body = soup.find("div", attrs={"class":"body-block"}).get_text()
    text_body = re.sub(pattern, " ", text_body)
    speaker = soup.find("div", attrs={"class":"byline"}).find("p").get_text()
    *middle, last = speaker.lower().split()
    # For Elder Ballard's first two talks while in 1976, his suffix of jr. was at the end instead of his name.
    if last == "jr.":
        last = "ballard"
    print(str(i) + last)
    speakerfile = open("/Users/_____/Desktop/General Conference Project/text/" + last + ".txt","a", encoding="utf-8")
    speakerfile.write(text_body + "\n") 
    speakerfile.close()
    time.sleep(5)