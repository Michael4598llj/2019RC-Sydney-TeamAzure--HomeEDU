#/home/mustar/catkin_ws/src/aip-python-sdk-2.0.0/output.wav
import json
import base64
import os
import requests
#import requests1
#chinese 24.01d2c999d6f13639a0b2c2645c8a4692.2592000.1564860709.282335-16716727
#eng 24.01d2c999d6f13639a0b2c2645c8a4692.2592000.1564860709.282335-16716727
RATE = "16000"
FORMAT = "wav"
CUID="wate_play"
DEV_PID="1737"
framerate=16000
def get_token():
    server = "https://openapi.baidu.com/oauth/2.0/token?"
    grant_type = "client_credentials"
    #API Key
    client_id = "xDvImmcWpYksDGbaFF8ARZN0"
    #Secret Key
    client_secret = "0ebheyn10aQsLxwG7RsG2rHDezNZjVyr"
    url ="%sgrant_type=%s&client_id=%s&client_secret=%s"%(server,grant_type,client_id,client_secret)
    #token
    res = requests.post(url)
    token = json.loads(res.text)["access_token"]
   # print(token)
    return token
def get_word(token):
    with open(r'/home/mustar/catkin_ws/src/aip-python-sdk-2.0.0/output.wav', "rb") as f:
        speech = base64.b64encode(f.read()).decode('utf-8')
    size = os.path.getsize(r'/home/mustar/catkin_ws/src/aip-python-sdk-2.0.0/output.wav')
    headers = { 'Content-Type' : 'application/json'} 
    url = "https://vop.baidu.com/server_api"
    data={
            "format":FORMAT,
            "rate":RATE,
            "dev_pid":1737,
            "speech":speech,
            "cuid":CUID,
            "len":size,
            "channel":1,
            "token":token,
        }

    req = requests.post(url,json.dumps(data),headers)
    result = json.loads(req.text)
    print(result)
    #ret=result["result"][0]
    return result
token = get_token()
result = get_word(token)
result = result['result']
result = result[0]
helloFile_write = open('yuju.txt',"w")
#helloFile_write.write(str(content))
helloFile_write.write(result)
helloFile_write.close()
