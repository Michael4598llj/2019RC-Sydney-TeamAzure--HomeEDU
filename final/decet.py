from aip import AipBodyAnalysis


APP_ID = '16727619'
API_KEY = 'GZEWDb85oQZodwbTe22aUV6j'
SECRET_KEY = '5ukX9tFzQ4GqFQtFiGXetbspIk9kVkEK'

client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)

def get_token():
    server = "https://openapi.baidu.com/oauth/2.0/token?"
    grant_type = "client_credentials"
    #API Key
    client_id = "GZEWDb85oQZodwbTe22aUV6j"
    #Secret Key
    client_secret = "5ukX9tFzQ4GqFQtFiGXetbspIk9kVkEK"
    url ="%sgrant_type=%s&client_id=%s&client_secret=%s"%(server,grant_type,client_id,client_secret)
    #token
    res = requests.post(url)
    token = json.loads(res.text)["access_token"]
    #print(token)
    return token

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
def decet():
	image = get_file_content('people.jpg')
	client.bodyAttr(image);
	options = {}
	options["type"] = "gender,upper_color"
	result0 = client.bodyAttr(image, options)
	result0 = result0['person_info']
	for i in result0:
		result1 = i['attributes']
	resultg = result1['gender']['name']
	resultc = result1['upper_color']['name']
	print(resultg)
	print(resultc)
	return [resultg,resultc]
#decet()
