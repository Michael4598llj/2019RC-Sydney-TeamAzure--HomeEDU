import time
import os
import path
import basis as b
#import move

from std_msgs.msg import String
import rospy


a=[0]*50

def listener():
	rospy.init_node('speech_trail_node1', anonymous=False)
	rospy.Subscriber('/recognizer/output', String, callback)
	rospy.spin()

def callback(data):
	global a
	#time.sleep(6)
	rospy.loginfo('I heard %s' % data.data)
	stra = data.data 
	sums = b.separate(stra)
	##########
	if (len(sums) > 2):
		if ((('most'in sums) or ('handsome' in sums) and ('person' in sums)) and (a[1] == 0 )): 
			os.system("rosrun sound_play say.py \"I that Justin Trudeau is very handsome.\"")
			a[1]=1
			os.system("rosnode kill /speech_trail_node1")
		if ('zones' in sums)and (a[2]==0): 
			os.system("rosrun sound_play say.py \"Canada spans almost 10 million square km and comprises 6 time zones\"")
			a[2]=1
			os.system("rosnode kill /speech_trail_node1")
	   	if (('longest' in sums)  or  ('street' in sums))and (a[3]==0): 
			os.system("rosrun sound_play say.py \"Yonge Street in Ontario is the longest street in the world.\"")
			a[3]=1
			os.system("rosnode kill /speech_trail_node1")
		if (('Yonge' in sums ) or  ('Ontario' in sums))and (a[4]==0): 
			os.system("rosrun sound_play say.py \"Yonge street is almost 2,000 km, starting at Lake Ontario, and running north to the Minnesota border.\"")
			a[4]=1
			os.system("rosnode kill /speech_trail_node1")
		if (('bear'in sums) or  ('cub'in sums) or ('london'in sums)  or ('fifteen' in sums))and (a[5]==0): 
			os.system("rosrun sound_play say.py \"The bear cub was named Winnipeg. It inspired the stories of Winnie-the-Pooh.\"")
			a[5]=1
			os.system("rosnode kill /speech_trail_node1")
		#else:
			#os.system("rosrun sound_play say.py \"unkown question\"")
		if (('Blackberry'in sums) or  ('Smartphone'in sums) or ('developed' in sums))and (a[6]==0): 
			os.system("rosrun sound_play say.py \"it was developed in ontario, at researchin motions waterloo offices.\"")
			a[6]=1
			os.system("rosnode kill /speech_trail_node1")
		if ('invaded'in sums) and  ('first' in sums)and (a[7]==0): 
			os.system("rosrun sound_play say.py \"The Big Nickel in Sudbury, Ontario. It is nine meters in diameter.\"")
			a[7]=1
			os.system("rosnode kill /speech_trail_node1")
		if ('invaded'in sums) and  ('second' in sums)and (a[8]==0): 
			os.system("rosrun sound_play say.py \"The USA invaded Canada a second time in 1812.\"")
			a[8]=1
			os.system("rosnode kill /speech_trail_node1")
		if ('countryin sums') and  ('record' in sums)and (a[9]==0): 
			os.system("rosrun sound_play say.py \"Canada does! With 14 Golds at the 2010 Vancouver Winter Olympics.\"")
			a[9]=1
			os.system("rosnode kill /speech_trail_node1")
		if (('coined'in sums) or  ('Beatlemania' in sums))and (a[10]==0): 
			os.system("rosrun sound_play say.py \"Sandy Gardiner, a journalist of the Ottawa Journal.\"")
			a[10]=1
			os.system("rosnode kill /speech_trail_node1")
		if ('why'in sums) and  ('named' in sums)and (a[11]==0): 
			os.system("rosrun sound_play say.py \"French explorers misunderstood the local native word Kanata, which means village.\"")
			a[11]=1
			os.system("rosnode kill /speech_trail_node1")
		if ('Mounted'in sums) and  ('Police' in sums)and (a[12]==0): 
			os.system("rosrun sound_play say.py \"The Mounted Police was formed in 1873.\"")
			a[12]=1
			os.system("rosnode kill /speech_trail_node1")
		if ('Royal'in sums) and  ('Canadian' in sums)and (a[13]==0): 
			os.system("rosrun sound_play say.py \"In 1920, when The Mounted Police merged with the Dominion Police.\"")
			a[13]=1
			os.system("rosnode kill /speech_trail_node1")
		if ('big'in sums) and  ('Royal' in sums)and(a[14]==0): 
			os.system("rosrun sound_play say.py \"Today, the Royal Canadian Mounted Police  has close to 30,000 members.\"")
			a[14]=1
			os.system("rosnode kill /speech_trail_node1")
		if (('else'in sums) or  ('Montreal' in sums))and(a[15]==0): 
			os.system("rosrun sound_play say.py \"Montreal is often called the City of Saints or the City of a Hundred Bell Towers.\"")
			a[15]=1
			os.system("rosnode kill /speech_trail_node1")
		if ('located'  in sums)and(a[16]==0): 
			os.system("rosrun sound_play say.py \"The Hotel de Glace is in Quebec.\"")
			a[16]=1
			os.system("rosnode kill /speech_trail_node1")
		if ('ice'  in sums)and(a[17]==0): 
			os.system("rosrun sound_play say.py \"The Hotel de Glace requires about 400 tons of ice.\"")
			a[17]=1
			os.system("rosnode kill /speech_trail_node1")
		if ('snow'  in sums)and(a[18]==0): 
			os.system("rosrun sound_play say.py \"Every year, 12000 tons of snow are used for The Hotel de Glace.\"")
			a[18]=1
			os.system("rosnode kill /speech_trail_node1")
		if ('summer'  in sums)and(a[19]==0): 
			os.system("rosrun sound_play say.py \"No. Every summer it melts away, only to be rebuilt the following winter.\"")
			a[19]=1
			os.system("rosnode kill /speech_trail_node1")
		if ('where'in sums) and ('desert' in sums)and(a[20]==0): 
			os.system("rosrun sound_play say.py \"Canadas only desert is British Columbia.\"")
			a[20]=1
			os.system("rosnode kill /speech_trail_node1")
		if ('big'in sums) and ('desert' in sums)and(a[21]==0): 
			os.system("rosrun sound_play say.py \"The British Columbia desert is only 15 miles long.\"")
			a[21]=1
			os.system("rosnode kill /speech_trail_node1")
		if ('male'in sums)and(a[22]==0): 
			os.system("rosrun sound_play say.py \"Leonard Cohen, Keanu Reeves, and Jim Carrey.\"")
			a[22]=1
			os.system("rosnode kill /speech_trail_node1")
		if ('famale'in sums)and(a[23]==0): 
			os.system("rosrun sound_play say.py \"Celine Dion, Pamela Anderson, and Avril Lavigne.\"")
			a[23]=1
			os.system("rosnode kill /speech_trail_node1")
		if (('font'in sums) or ('Comic'in sums) or ('Sans' in sums))and(a[24]==0): 
			os.system("rosrun sound_play say.py \"Comic Sans is based on Dave Gibbons lettering in the Watchmen comic books.\"")
			a[24]=1
			os.system("rosnode kill /speech_trail_node1")
		if (('Jedi'in sums) or  ('files'in sums) or ('open'in sums))and(a[25]==0): 
			os.system("rosrun sound_play say.py \"Adobe Wan Kenobi.\"")
			a[25]=1
			os.system("rosnode kill /speech_trail_node1")
		if (('considered'in sums) or ('first'in sums) or ('programmer'in sums))and(a[26]==0): 
			os.system("rosrun sound_play say.py \"Ada Lovelace.\"")
			a[26]=1
			os.system("rosnode kill /speech_trail_node1")
		if (('inventor'in sums) or ('Apple'in sums) or ('microcomputer'in sums))and(a[27]==0): 
			os.system("rosrun sound_play say.py \"My lord and master Steve Wozniak.\"")
			a[27]=1
			os.system("rosnode kill /speech_trail_node1")
		if (('Mark'in sums) or ('Zuckerberg'in sums))and(a[28]==0): 
			os.system("rosrun sound_play say.py \"Sure. I have never seen him drink water.\"")
			a[28]=1
			os.system("rosnode kill /speech_trail_node1")
		if ('python'in sums) and ('language' in sums)and(a[29]==0): 
			os.system("rosrun sound_play say.py \"Python was invented by Guido van Rossum.\"")
			a[29]=1
			os.system("rosnode kill /speech_trail_node1")
		if ('C'in sums) and ('created' in sums)and(a[30]==0): 
			os.system("rosrun sound_play say.py \"C was invented by Dennis MacAlistair Ritchie.\"")
			a[30]=1
			os.system("rosnode kill /speech_trail_node1")
		if (('invented'in sums) or ('compiler' in sums))and(a[31]==0): 
			os.system("rosrun sound_play say.py \"Grace Hoper. She wrote it in her spare time.\"")
			a[31]=1
			os.system("rosnode kill /speech_trail_node1")
		if (('self-driving'in sums) or ('safe'in sums) or ('cars' in sums))and(a[32]==0): 
			os.system("rosrun sound_play say.py \"Yes. Car accidents are product of human misconduct.\"")
			a[32]=1
			os.system("rosnode kill /speech_trail_node1")
		if ('chatbot'in sums) and ('what' in sums)and(a[33]==0): 
			os.system("rosrun sound_play say.py \"A chatbot is an A.I. you put in customer service toavoid paying salaries.\"")
			a[33]=1
			os.system("rosnode kill /speech_trail_node1")
		if (('threat'in sums) or ('humanity'in sums) or ('think' in sums))and(a[34]==0): 
			os.system("rosrun sound_play say.py \"No. Humans are the real threat to humanity.\"")
			a[34]=1
			os.system("rosnode kill /speech_trail_node1")
		if (('Elon'in sums) or ('Musk'in sums) or ('worried'in sums) or ('impact'in sums))and(a[35]==0): 
			os.system("rosrun sound_play say.py \"I do not know. He should worry more about the people's impact on humanity.\"")
			a[35]=1
			os.system("rosnode kill /speech_trail_node1")
		if (('knowledge'in sums) or ('engineering'in sums) or ('bottleneck' in sums))and(a[36]==0): 
			os.system("rosrun sound_play say.py \"It is when you need to load an AI with enough knowledge to start learning.\"")
			a[36]=1
			os.system("rosnode kill /speech_trail_node1")
		if (('Moravec'in sums) or ('paradox'in sums) or ('state'in sums))and(a[37]==0): 
			os.system("rosrun sound_play say.py \"Moravec's paradox states that a computer can crunch numbers like Bernoulli, but lacks a toddler's motor skills.\"")
			a[37]=1
			os.system("rosnode kill /speech_trail_node1")
		if (('pass'in sums) or ('Turing'in sums) or ('test' in sums))and(a[38]==0): 
			os.system("rosrun sound_play say.py \"Some people think it was IBM Watson, but it was Eugene, a computer designed at England's University of Reading.\"")
			a[38]=1
			os.system("rosnode kill /speech_trail_node1")
		if (('Mechanical'in sums) or ('Knight' in sums))and(a[39]==0): 
			os.system("rosrun sound_play say.py \"A robot sketch made by Leonardo DaVinci.\"")
			a[39]=1
			os.system("rosnode kill /speech_trail_node1")
		if (('world'in sums) or ('android' in sums))and(a[40]==0): 
			os.system("rosrun sound_play say.py \"Professor Kevin Warwick uses chips in his arm to operate doors, a robotic hand, and a wheelchair.\"")
			a[40]=1
			os.system("rosnode kill /speech_trail_node1")
		if (('Name'in sums) or ('Mars' in sums))and(a[41]==0): 
			os.system("rosrun sound_play say.py \"There are four robots on Mars: Sojourner, Spirit, Opportunity, and Curiosity. Three more crashed on landing.\"")
			a[41]=1
			os.system("rosnode kill /speech_trail_node1")
		if ('bug'in sums) and ('first' in sums)and(a[42]==0): 
			os.system("rosrun sound_play say.py \"The first actual computer bug was a dead moth stuck in a Harvard Mark II.\"")
			a[42]=1
			os.system("rosnode kill /speech_trail_node1")
		if (('CAPTCHA'in sums) or ('stands' in sums))and(a[43]==0): 
			os.system("rosrun sound_play say.py \"CAPTCHA is an acronym for Completely Automated Public Turing test to tell Computers and Humans Apart\"")
			a[43]=1
			os.system("rosnode kill /speech_trail_node1")
		if ('big' in sums) and  ('first' in sums)and(a[44]==0): 
			os.system("rosrun sound_play say.py \"The IBM 305 RAMAC hard disk weighed over a ton and stored 5 MB of data.\"")
			a[44]=1
			os.system("rosnode kill /speech_trail_node1")
		if ('launched' in sums) and ('when' in sums)and(a[45]==0): 
			os.system("rosrun sound_play say.py \"The IBM 305 RAMAC was launched in 1956.\"")
			a[45]=1
			os.system("rosnode kill /speech_trail_node1")
		if ('which' in sums) and ('drive' in sums)and(a[46]==0): 
			os.system("rosrun sound_play say.py \"The IBM 305 RAMAC.\"")
			a[46]=1
			os.system("rosnode kill /speech_trail_node1")
		if (('Tron' in sums) or ('nominated' in sums) or ('award' in sums) or ('Motion' in sums))and(a[47]==0): 
			os.system("rosrun sound_play say.py \"The Academy thought that Tron cheated by using computers.\"")
			a[47]=1
			os.system("rosnode kill /speech_trail_node1")
		if ('how' in sums) and ('small' in sums)and(a[48]==0): 
			os.system("rosrun sound_play say.py \"A nanobot can be less than one-thousandth of a millimeter.\"")
			a[48]=1
			os.system("rosnode kill /speech_trail_node1")
		if  ('nanobot' in sums)and(a[49]==0): 
			os.system("rosrun sound_play say.py \"The smallest robot possible is called a nanobot.\"")
			a[49]=1
			os.system("rosnode kill /speech_trail_node1")
		if  ('largest' in sums)and(a[0]==0): 
			os.system("rosrun sound_play say.py \"The Big Nickel in Sudbury, Ontario. It is nine meters in diameter.\"")
			a[0]=1
			os.system("rosnode kill /speech_trail_node1")





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


listener()
os.system("gnome-terminal -e 'python sp2.py'")



