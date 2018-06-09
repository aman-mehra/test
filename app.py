import json
import urllib2
from bs4 import BeautifulSoup
from flask import Flask
from flask import request
#app = Flask(__name__)

@app.route('/getlinks')
def getvids():
    textToSearch = request.args.get('concept')
    query = urllib2.quote(textToSearch)
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html,"html5lib")
    arr=[]
    for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
        if (not vid['href'].startswith("https://www.googleadservices.com")) and (not vid['href'].startswith("channel/")):
            arr.append( vid['href'].split("=")[-1]})
            if (len(arr)==4):
                break
    dix= {"id1":arr[0],"id2":arr[1],"id3":arr[2],"id4":arr[3]}
    js=json.dumps(dix)
    return js


@approute('/getconcepts')
def getconepts():
    pass


