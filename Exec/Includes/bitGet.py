import requests
import json
import sys

class BitGet:
    bitBucketurl = ""

    def __init__(self, url):
        self.bitBucketurl = url

    def setURL(self, url):
        self.bitBucketurl = url

    def getRawData(self, user, password):
        req = requests.get(self.bitBucketurl, auth=(user, password))
        parse = json.loads(req.content)
        return(parse)

    def getCutData(self,user, password):
        req = requests.get(self.bitBucketurl, auth=(user, password))
        parse = json.loads(req.content)
        data = parse["changesets"]
        return(data)

