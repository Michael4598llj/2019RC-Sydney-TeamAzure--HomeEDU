import json
import base64
import os
import requests
import basis
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
    #print(token)
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
    #print(result)
    #ret=result["result"][0]
    return result
token = get_token()
result = get_word(token)

result = result['result']
result = result[0]
sums = basis.separate(result)
if ((('most'in sums) or ('handsome' in sums) and ('person' in sums))):
    os.system("rosrun sound_play say.py \" Who’s the most handsome person in Canada?\"")
	os.system("rosrun sound_play say.py \"I that Justin Trudeau is very handsome.\"")
if ('zones' in sums):
    os.system("rosrun sound_play say.py \"How many time zones are there in Canada? \"")
	os.system("rosrun sound_play say.py \"Canada spans almost 10 million square km and comprises 6 time zones\"")
os.system("rosnode kill /speech_trail_node1")
if (('longest' in sums)  or  ('street' in sums)):
    os.system("rosrun sound_play say.py \"What’s the longest street in the world? \"")
	os.system("rosrun sound_play say.py \"Yonge Street in Ontario is the longest street in the world.\"")
if (('Yonge' in sums ) or  ('Ontario' in sums)):
    os.system("rosrun sound_play say.py \"How long is Yonge Street in Ontario?\"")
	os.system("rosrun sound_play say.py \"Yonge street is almost 2,000 km, starting at Lake Ontario, and running north to the Minnesota border.\"")

if (('bear'in sums) or  ('cub'in sums) or ('london'in sums)  or ('fifteen' in sums)):
    os.system("rosrun sound_play say.py \"What’s the name of the bear cub exported from Canada to the London Zoo in 1915? \"")
	os.system("rosrun sound_play say.py \"The bear cub was named Winnipeg. It inspired the stories of Winnie-the-Pooh.\"")

#else:
#os.system("rosrun sound_play say.py \"unkown question\"")
if (('Blackberry'in sums) or  ('Smartphone'in sums) or ('developed' in sums)):
    os.system("rosrun sound_play say.py \"Where was the Blackberry Smartphone developed? \"")
	os.system("rosrun sound_play say.py \"it was developed in ontario, at researchin motions waterloo offices.\"")

if ('invaded'in sums) and  ('first' in sums):
    os.system("rosrun sound_play say.py \"In what year was Canada invaded by the USA for the ﬁrst time? \"")
	os.system("rosrun sound_play say.py \"The Big Nickel in Sudbury, Ontario. It is nine meters in diameter.\"")

if ('invaded'in sums) and  ('second' in sums):
    os.system("rosrun sound_play say.py \"What year was Canada invaded by the USA for the second time? \"")
	os.system("rosrun sound_play say.py \"The USA invaded Canada a second time in 1812.\"")	

if ('country'in sums) and  ('record' in sums):
    os.system("rosrun sound_play say.py \"What country holds the record for the most gold medals at the Winter Olympics?\"")
	os.system("rosrun sound_play say.py \"Canada does! With 14 Golds at the 2010 Vancouver Winter Olympics.\"")

if (('coined'in sums) or  ('Beatlemania' in sums)) :
    os.system("rosrun sound_play say.py \" Who coined the term Beatlemania? \"")
	os.system("rosrun sound_play say.py \"Sandy Gardiner, a journalist of the Ottawa Journal.\"")

if ('why'in sums) and  ('named' in sums):
    os.system("rosrun sound_play say.py \"Why is Canada named Canada?\"")
	os.system("rosrun sound_play say.py \"French explorers misunderstood the local native word Kanata, which means village.\"")

if ('Mounted'in sums) and  ('Police' in sums):
    os.system("rosrun sound_play say.py \"When was The Mounted Police formed? \"")
	os.system("rosrun sound_play say.py \"The Mounted Police was formed in 1873.\"")

if ('Royal'in sums) and  ('Canadian' in sums):
    os.system("rosrun sound_play say.py \"When was The Royal Canadian Mounted Police formed? \"")
	os.system("rosrun sound_play say.py \"In 1920, when The Mounted Police merged with the Dominion Police.\"")

if ('big'in sums) and  ('Royal' in sums):
	os.system("rosrun sound_play say.py \"How big is the RCMP? \"")
	os.system("rosrun sound_play say.py \"Today, the Royal Canadian Mounted Police  has close to 30,000 members.\"")

if (('else'in sums) or  ('Montreal' in sums)):        
	os.system("rosrun sound_play say.py \"What else is Montreal called? \"")
	os.system("rosrun sound_play say.py \"Montreal is often called the City of Saints or the City of a Hundred Bell Towers.\"")

if ('located'  in sums): 
    os.system("rosrun sound_play say.py \" Where is The Hotel de Glace located? \"")
	os.system("rosrun sound_play say.py \"The Hotel de Glace is in Quebec.\"")

if ('ice'  in sums):
    os.system("rosrun sound_play say.py \"How many tons of ice are required to build The Hotel de Glace? \"")
	os.system("rosrun sound_play say.py \"The Hotel de Glace requires about 400 tons of ice.\"")

if ('snow'  in sums) and ('many'  in sums):
    os.system("rosrun sound_play say.py \"How many tons of snow are required to build The Hotel de Glace? \"")
	os.system("rosrun sound_play say.py \"Every year, 12000 tons of snow are used for The Hotel de Glace.\"")

if ('summer'  in sums):
    os.system("rosrun sound_play say.py \"Can I visit the Hotel de Glace in summer? \"")
	os.system("rosrun sound_play say.py \"No. Every summer it melts away, only to be rebuilt the following winter.\"")

if ('where'in sums) and ('desert' in sums):
    os.system("rosrun sound_play say.py \" Where is Canada’s only desert? \"")
	os.system("rosrun sound_play say.py \"Canadas only desert is British Columbia.\"")

if ('big'in sums) and ('desert' in sums):
    os.system("rosrun sound_play say.py \" How big is Canada’s only desert? \"")
	os.system("rosrun sound_play say.py \"The British Columbia desert is only 15 miles long.\"")

if ('male'in sums):
    os.system("rosrun sound_play say.py \"Name 3 famous male Canadians. \"")
	os.system("rosrun sound_play say.py \"Leonard Cohen, Keanu Reeves, and Jim Carrey.\"")

if ('famale'in sums):
    os.system("rosrun sound_play say.py \"Name 3 famous female Canadians. \"")
	os.system("rosrun sound_play say.py \"Celine Dion, Pamela Anderson, and Avril Lavigne.\"")

if (('font'in sums) or ('Comic'in sums) or ('Sans' in sums)):
    os.system("rosrun sound_play say.py \"What’s the origin of the Comic Sans font? \"")
	os.system("rosrun sound_play say.py \"Comic Sans is based on Dave Gibbons lettering in the Watchmen comic books.\"")

if (('Jedi'in sums) or  ('files'in sums) or ('open'in sums)):
    os.system("rosrun sound_play say.py \"Which program do Jedi use to open PDF ﬁles? \"")
	os.system("rosrun sound_play say.py \"Adobe Wan Kenobi.\"")

if (('considered'in sums) or ('first'in sums) or ('programmer'in sums)):
    os.system("rosrun sound_play say.py \"Who is considered to be the ﬁrst computer programmer?\"")
	os.system("rosrun sound_play say.py \"Ada Lovelace.\"")

if (('inventor'in sums) or ('Apple'in sums) or ('microcomputer'in sums)):
    os.system("rosrun sound_play say.py \" Who is the inventor of the Apple I microcomputer? \"")
	os.system("rosrun sound_play say.py \"My lord and master Steve Wozniak.\"")

if (('Mark'in sums) or ('Zuckerberg'in sums)):
    os.system("rosrun sound_play say.py \" Is Mark Zuckerberg a robot? \"")
	os.system("rosrun sound_play say.py \"Sure. I have never seen him drink water.\"")

if ('python'in sums) and ('language' in sums):
    os.system("rosrun sound_play say.py \"Who created the Python Programming Language? \"")
	os.system("rosrun sound_play say.py \"Python was invented by Guido van Rossum.\"")

if ('C'in sums) and ('created' in sums):
    os.system("rosrun sound_play say.py \"Who created the C Programming Language? \"")
	os.system("rosrun sound_play say.py \"C was invented by Dennis MacAlistair Ritchie.\"")

if (('invented'in sums) or ('compiler' in sums)):
    os.system("rosrun sound_play say.py \"Who invented the compiler? \"")
	os.system("rosrun sound_play say.py \"Grace Hoper. She wrote it in her spare time.\"")

if (('self'in sums) and ('driving'in sums)or('safe'in sums) or ('cars' in sums)):
    os.system("rosrun sound_play say.py \" Are self-driving cars safe? \"")
	os.system("rosrun sound_play say.py \"Yes. Car accidents are product of human misconduct.\"")

if ('chatbot'in sums) and ('what' in sums):
    os.system("rosrun sound_play say.py \" What is a chatbot?\"")
	os.system("rosrun sound_play say.py \"A chatbot is an A.I. you put in customer service toavoid paying salaries.\"")

if (('threat'in sums) or ('humanity'in sums) or ('think' in sums)):
    os.system("rosrun sound_play say.py \"Do you think robots are a threat to humanity? \"")
	os.system("rosrun sound_play say.py \"No. Humans are the real threat to humanity.\"")

if (('Elon'in sums) or ('Musk'in sums) or ('worried'in sums) or ('impact'in sums)):
    os.system("rosrun sound_play say.py \" Why is Elon Musk is worried about AI’s impact on humanity? \"")
	os.system("rosrun sound_play say.py \"I do not know. He should worry more about the people's impact on humanity.\"")

if (('knowledge'in sums) or ('engineering'in sums) or ('bottleneck' in sums)):
    os.system("rosrun sound_play say.py \" What is the AI knowledge engineering bottleneck? \"")
	os.system("rosrun sound_play say.py \"It is when you need to load an AI with enough knowledge to start learning.\"")

if (('Moravec'in sums) or ('paradox'in sums) or ('state'in sums)):
    os.system("rosrun sound_play say.py \"What does Moravec’s paradox state? \"")
	os.system("rosrun sound_play say.py \"Moravec's paradox states that a computer can crunch numbers like Bernoulli, but lacks a toddler's motor skills.\"")

if (('pass'in sums) or ('Turing'in sums) or ('test' in sums)):
    os.system("rosrun sound_play say.py \"What was the ﬁrst computer in pass the Turing test?\"")
	os.system("rosrun sound_play say.py \"Some people think it was IBM Watson, but it was Eugene, a computer designed at England's University of Reading.\"")

if (('Mechanical'in sums) or ('Knight' in sums)):
    os.system("rosrun sound_play say.py \"What is a Mechanical Knight? \"")
	os.system("rosrun sound_play say.py \"A robot sketch made by Leonardo DaVinci.\"")

if (('world'in sums) or ('android' in sums)):
    os.system("rosrun sound_play say.py \"Who is the world’s ﬁrst android? \"")
	os.system("rosrun sound_play say.py \"Professor Kevin Warwick uses chips in his arm to operate doors, a robotic hand, and a wheelchair.\"")

if (('Name'in sums) or ('Mars' in sums)):
    os.system("rosrun sound_play say.py \"Name all of the robots on Mars. \"")
	os.system("rosrun sound_play say.py \"There are four robots on Mars: Sojourner, Spirit, Opportunity, and Curiosity. Three more crashed on landing.\"")

if ('bug'in sums) and ('first' in sums):
    os.system("rosrun sound_play say.py \"What was the ﬁrst computer bug?\"")
	os.system("rosrun sound_play say.py \"The first actual computer bug was a dead moth stuck in a Harvard Mark II.\"")

if (('CAPTCHA'in sums) or ('stands' in sums)):
    os.system("rosrun sound_play say.py \"What does CAPTCHA stands for? \"")
	os.system("rosrun sound_play say.py \"CAPTCHA is an acronym for Completely Automated Public Turing test to tell Computers and Humans Apart\"")

if ('big' in sums) and  ('first' in sums):
    os.system("rosrun sound_play say.py \"How big was the ﬁrst hard disk drive? \"")
	os.system("rosrun sound_play say.py \"The IBM 305 RAMAC hard disk weighed over a ton and stored 5 MB of data.\"")

if ('launched' in sums) and ('when' in sums):
    os.system("rosrun sound_play say.py \"When was the ﬁrst computer with a hard disk drive launched?\"")
	os.system("rosrun sound_play say.py \"The IBM 305 RAMAC was launched in 1956.\"")

if ('which' in sums) and ('drive' in sums):
    os.system("rosrun sound_play say.py \"Which was the ﬁrst computer with a hard disk drive? \"")
	os.system("rosrun sound_play say.py \"The IBM 305 RAMAC.\"")

if (('Tron' in sums) or ('nominated' in sums) or ('award' in sums) or ('Motion' in sums)):
    os.system("rosrun sound_play say.py \"Why wasn’t Tron nominated for an award by The Motion Picture Academy? \"")
	os.system("rosrun sound_play say.py \"The Academy thought that Tron cheated by using computers.\"")

if ('how' in sums) and ('small' in sums):
    os.system("rosrun sound_play say.py \"How small can a nanobot be? \"")
	os.system("rosrun sound_play say.py \"A nanobot can be less than one-thousandth of a millimeter.\"")

if  ('nanobot' in sums)and ('what' in sums):
    os.system("rosrun sound_play say.py \" What is a nanobot? \"")
	os.system("rosrun sound_play say.py \"The smallest robot possible is called a nanobot.\"")

if  ('largest' in sums):
    os.system("rosrun sound_play say.py \"What is the world’s largest coin? \"")
	os.system("rosrun sound_play say.py \"The Big Nickel in Sudbury, Ontario. It is nine meters in diameter.\"")
			





'''
os.system("gnome-terminal -e 'bash -c \"roslaunch rbx1_speech voice_task2_commands.launch; exec bash\"'")
time.sleep(2)
os.system("gnome-terminal -e 'bash -c \"rosrun sound_play soundplay_node.py; exec bash\"'")
time.sleep(2)
#move.move_init()
os.system("rosrun sound_play say.py \"let's begin.\"")


listener()
time.sleep(5)
listener()
time.sleep(5)
listener()
time.sleep(5)
listener()
time.sleep(5)
listener()
time.sleep(5)

helloFile = open("sp.txt")
fileContent = helloFile.read()
helloFile.close()
txta = eval(fileContent)
txta = txta + 1
txta = str(txta) 
helloFile1 = open("sp.txt","w")
helloFile1.write(txta)
helloFile1.close()
'''
txta = b.read_txt("sp")
txta = txta + 1
txta = b.write_txt("sp",txta)



os.system("gnome-terminal -e 'python sp2.py'")

