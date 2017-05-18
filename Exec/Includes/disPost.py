import requests
import json

class DisPost:
    Discordurl = ""

    headers = {'content-type': 'application/json'}

    def __init__(self, url):
        self.setURL(url)

    def sendMessage(self, Author, Node, Message):
        message = dict(username="BitBucket Bot", text="Push Made", attachments=[{
            "author_name": Author,
            "color": "#ff0000",
            "title": Node,
            "text": Message,
            "footer": "expect delays"}])
        r = requests.post(self.Discordurl, data=json.dumps(message), headers=self.headers)


    #adds the /slack to a url
    def setURL(self,url):
        self.Discordurl = url +"/slack"