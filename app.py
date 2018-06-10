import json
import urllib2
from bs4 import BeautifulSoup
from flask import Flask
from flask import request
import requests
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

def keyConcepts(text):
    subscription_key = "0bfee4bdb89647c98ff905ae4270b71d"
    assert subscription_key

    text_analytics_base_url = "https://westcentralus.api.cognitive.microsoft.com/text/analytics/v2.0/"
    key_phrase_api_url = text_analytics_base_url + "keyPhrases"
    documents = {'documents' : [
      {'id': '1', 'language': 'en', 'text':text}
      ]
    headers   = {"Ocp-Apim-Subscription-Key": subscription_key}
    response  = requests.post(key_phrase_api_url , headers=headers, json=documents)
    resp = response.json()
    keywords = resp["documents"]
    arr=keywords["keyPhrases"][:10]

    ret_arr=[]
    for i in arr:
                 ret_arr.append({"concept":i})

    js = json.dumps(ret_arr)
    return key_phrase_api_url




