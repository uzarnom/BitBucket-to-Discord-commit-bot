#!/usr/local/bin python3.6
from  Includes.disPost import DisPost
from Includes.bitGet import BitGet
import sys

#Save Node
def saveNode(newNode):
    file = open("./Includes/lastNode", "w")
    file.write(newNode)
    file.close()


#global data to be used
DISCORD_URL = "https://discordapp.com/api/webhooks/[numbers]/[letters and numbers]"
BIT_BUCKET_URL = "https://api.bitbucket.org/1.0/repositories/[user who created]/[repo name]/changesets"

bit_bucket_username = "user"
bit_bucket_password = "password"



Bit = BitGet(BIT_BUCKET_URL)
Dis = DisPost(DISCORD_URL)

#get lastNode posted
file = open("./Includes/lastNode", "r")
lastDoneNode = file.read()
file.close()

#set URL for bitbucket and discord
#Bit.setURL(BIT_BUCKET_URL)
#Dis.setURL(DISCORD_URL)




#get data from bitbucket
data = Bit.getCutData(bit_bucket_username, bit_bucket_password)
dataSize = len(data) -1 ;

#print(dataSize)

#check if last post was latest
if(data[dataSize]["raw_node"] == lastDoneNode):
    sys.exit(0)

#check how many posts need to be made
count = 0
for i in range(dataSize, -1, -1): #this is bad, could look nicer
    if(data[i]["raw_node"] != lastDoneNode):
        count += 1
    else:
        break

numOfPosts = dataSize - count +1 #better name, this is post to start from


#process json send message for everynew node
for i in range(numOfPosts, dataSize+1, 1):
    #print("Sending message: " + data[i]["raw_node"])
    #print(data[i]["message"])
    #print(data[i]["raw_author"])
    Auth = data[i]["raw_author"]
    Nod = data[i]["raw_node"]
    Mes = data[i]["message"]
    Dis.sendMessage(Auth, Nod, Mes)

#we have come here because no old node
saveNode(data[dataSize]["raw_node"])


