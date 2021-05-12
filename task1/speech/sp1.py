# -*- coding:utf-8 -*-  

import time
import os
import path
import basis as b
#import move

from std_msgs.msg import String
import rospy

'''
sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
sum5 = 0
sum6 = 0
sum7 = 0
sum8 = 0
sum9 = 0
sum10 = 0
sum11 = 0
sum12 = 0
sum13 = 0
sum14 = 0
sum15 = 0
sum16 = 0
sum17 = 0
sum18 = 0
sum19 = 0
sum20 = 0
sum21 = 0
sum22 = 0
sum23 = 0
sum24 = 0
sum25 = 0
sum26 = 0
sum27 = 0
sum28 = 0
sum29 = 0
sum30 = 0
sum31 = 0
sum32 = 0
sum33 = 0
sum34 = 0
sum35 = 0
sum36 = 0
sum37 = 0
sum38 = 0
sum39 = 0
sum40 = 0
sum41 = 0
sum42 = 0
sum43 = 0
sum44 = 0
sum45 = 0
sum46 = 0
sum47 = 0
sum48 = 0
sum49 = 0
sum50 = 0
'''


def listener():
	rospy.init_node('speech_trail_node1', anonymous=False)
	rospy.Subscriber('/recognizer/output', String, callback)
	rospy.spin()

def callback(data):
	'''
        global sum1
        global sum2
        global sum3
        global sum4
        global sum5
        global sum6
        global sum7
        global sum8
        global sum9
        global sum10
        global sum11
        global sum12
        global sum13
        global sum14
        global sum15
        global sum16
        global sum17
        global sum18
        global sum19
        global sum20
        global sum21
        global sum22
        global sum23
        global sum24
        global sum25
        global sum26
        global sum27
        global sum28
        global sum29
        global sum30
        global sum31
        global sum32
        global sum33
        global sum34
        global sum35
        global sum36
        global sum37
        global sum38
        global sum39
        global sum40
        global sum41
        global sum42
        global sum43
        global sum44
        global sum45
        global sum46
        global sum47
        global sum48
        global sum49
        global sum50
	'''
	sum1 = 0
	sum2 = 0
	sum3 = 0
	sum4 = 0
	sum5 = 0
	sum6 = 0
	sum7 = 0
	sum8 = 0
	sum9 = 0
	sum10 = 0
	sum11 = 0
	sum12 = 0
	sum13 = 0
	sum14 = 0
	sum15 = 0
	sum16 = 0
	sum17 = 0
	sum18 = 0
	sum19 = 0
	sum20 = 0
	sum21 = 0
	sum22 = 0
	sum23 = 0
	sum24 = 0
	sum25 = 0
	sum26 = 0
	sum27 = 0
	sum28 = 0
	sum29 = 0
	sum30 = 0
	sum31 = 0
	sum32 = 0
	sum33 = 0
	sum34 = 0
	sum35 = 0
	sum36 = 0
	sum37 = 0
	sum38 = 0
	sum39 = 0
	sum40 = 0
	sum41 = 0
	sum42 = 0
	sum43 = 0
	sum44 = 0
	sum45 = 0
	sum46 = 0
	sum47 = 0
	sum48 = 0
	sum49 = 0
	sum50 = 0	

	#time.sleep(6)
	rospy.loginfo('I heard %s' % data.data)
	stra = data.data 
	lista = b.separate(stra)
	##########
        for ii in lista:
            sum1 = sum1 + (ii in "who’s the most handsome person in canada")
        for ii in lista:
            sum2 = sum2 + (ii in "how many time zones are there in canada")
        for ii in lista:
            sum3 = sum3 + (ii in "what’s the longest street in the world")
        for ii in lista:
            sum4 = sum4 + (ii in "how long is Yonge Street in Ontario")
        for ii in lista:
            sum5 = sum5 + (ii in "what’s the name of the bear cub exported from canada to the london zoo in 1915")
        for ii in lista:
            sum6 = sum6 + (ii in "where was the blackberry smartphone developed")
        for ii in lista:
            sum7 = sum7 + (ii in "what is the world’s largest coin")
        for ii in lista:
            sum8 = sum8 + (ii in "In what year was canada invaded by the USA for the ﬁrst time")
        for ii in lista:
            sum9 = sum9 + (ii in "what year was canada invaded by the USA for the second time")
        for ii in lista:
            sum10 = sum10 + (ii in "what country holds the record for the most gold medals at the winter Olympics")
        for ii in lista:
            sum11 = sum11 + (ii in "who coined the term beatlemania")
        for ii in lista:
            sum12 = sum12 + (ii in "why is canada named canada")
        for ii in lista:
            sum13 = sum13 + (ii in "when was the mounted police formed")
        for ii in lista:
            sum14 = sum14 + (ii in "when was the Royal canadian mounted police formed")
        for ii in lista:
            sum15 = sum15 + (ii in "how big is the Rcmp")
        for ii in lista:
            sum16 = sum16 + (ii in "what else is montreal called")
        for ii in lista:
            sum17 = sum17 + (ii in "where is the hotel de glace located")
        for ii in lista:
            sum18 = sum18 + (ii in "how many tons of ice are required to build the hotel de glace")
        for ii in lista:
            sum19 = sum19 + (ii in "how many tons of snow are required to build the hotel de glace")
        for ii in lista:
            sum20 = sum20 + (ii in "can I visit the hotel de glace in summer")
        for ii in lista:
            sum21 = sum21 + (ii in "where is canada’s only desert")
        for ii in lista:
            sum22 = sum22 + (ii in "how big is canada’s only desert")
        for ii in lista:
            sum23 = sum23 + (ii in "name 3 famous male canadians")
        for ii in lista:
            sum24 = sum24 + (ii in "name 3 famous female canadians")
        for ii in lista:
            sum25 = sum25 + (ii in "what’s the origin of the comic sans font")
        for ii in lista:
            sum26 = sum26 + (ii in "what is a nanobot? ")
        for ii in lista:
            sum27 = sum27 + (ii in "how small can a nanobot be")
        for ii in lista:
            sum28 = sum28 + (ii in " why wasn’t tron nominated for an award by the motion picture academy? ")
        for ii in lista:
            sum29 = sum29 + (ii in "which was the ﬁrst computer with a hard disk drive? ")
        for ii in lista:
            sum30 = sum30 + (ii in "when was the ﬁrst computer with a hard disk drive launched? ")
        for ii in lista:
            sum31 = sum31 + (ii in "how big was the ﬁrst hard disk drive? ")
        for ii in lista:
            sum32 = sum32 + (ii in "what does captcha stands for? ")
        for ii in lista:
            sum33 = sum33 + (ii in "what was the ﬁrst computer bug? ")
        for ii in lista:
            sum34 = sum34 + (ii in "name all of the robots on mars. ")
        for ii in lista:
            sum35 = sum35 + (ii in "who is the world’s ﬁrst android? ")
        for ii in lista:
            sum36 = sum36 + (ii in " what is a mechanical knight? ")
        for ii in lista:
            sum37 = sum37 + (ii in "what was the ﬁrst computer in pass the turing test? ")
        for ii in lista:
            sum38 = sum38 + (ii in "what does moravec’s paradox state? ")
        for ii in lista:
            sum39 = sum39 + (ii in "what is the AI knowledge engineering bottleneck? ")
        for ii in lista:
            sum40 = sum40 + (ii in "why is elon musk is worried about ai’s impact on humanity? ")
        for ii in lista:
            sum41 = sum41 + (ii in "Do you think robots are a threat to humanity? ")
        for ii in lista:
            sum42 = sum42 + (ii in "what is a chatbot? ")
        for ii in lista:
            sum43 = sum43 + (ii in "are self-driving cars safe?")
        for ii in lista:
            sum44 = sum44 + (ii in "who invented the compiler? ")
        for ii in lista:
            sum45 = sum45 + (ii in " who created the c programming language? ")
        for ii in lista:
            sum46 = sum46 + (ii in "who created the python programming language? ")
        for ii in lista:
            sum47 = sum47 + (ii in "Is mark zuckerberg a robot? ")
        for ii in lista:
            sum48 = sum48 + (ii in "who is the inventor of the apple i microcomputer? ")
        for ii in lista:
            sum49 = sum49 + (ii in "who is considered to be the ﬁrst computer programmer? ")
        for ii in lista:
            sum50 = sum50 + (ii in "which program do jedi use to open pdf ﬁles? ")
        listsum =[sum1,sum2,sum3,sum4,sum5,sum6,sum7,sum8,sum9,sum10,sum11,sum12,sum13,sum14,sum15,sum16,sum17,sum18,sum19,sum20,sum21,sum22,sum23,sum24,sum25,sum26,sum27,sum28,sum29,sum30,sum31,sum32,sum33,sum34,sum35,sum36,sum37,sum38,sum39,sum40,sum41,sum42,sum43,sum44,sum45,sum46,sum47,sum48,sum49,sum50]
        '''
        maxsum = max(sum1,sum2,sum3,sum4,sum5,sum6,sum7,sum8,sum9,sum10,sum11,sum12,sum13,sum14,sum15,sum16,sum17,sum18,sum19,sum20,sum21,sum22,sum23,sum24,sum25,sum26,sum27,sum28,sum29,sum30,sum31,sum32,sum33,sum34,sum35,sum36,sum37,sum38,sum39,sum40,sum41,sum42,sum43,sum44,sum45,sum46,sum47,sum48,sum49,sum50)
        for imax in range(1,len(listsum)+1):
            if listmax[imax-1] == maxsum:
                endmax = imax
        '''
	endmax_list = [0]
	tuplesum = tuple(listsum)
	if (max(tuplesum) > 1): 
		endmax_list = b.max_position(listsum)
	endmax = endmax_list[0]
        
        if ( endmax == 1 ): 
		os.system("rosrun sound_play say.py \"I that Justin trudeau is very handsome.\"")
		os.system("rosnode kill /speech_trail_node1")
    	if ( endmax == 2 ): 
		os.system("rosrun sound_play say.py \"canada spans almost 10 million square km and comprises 6 time zones\"")
		os.system("rosnode kill /speech_trail_node1")
   	if ( endmax == 3 ): 
		os.system("rosrun sound_play say.py \"Yonge Street in Ontario is the longest street in the world.\"")
		os.system("rosnode kill /speech_trail_node1")
	if ( endmax == 4 ): 
		os.system("rosrun sound_play say.py \"Yonge street is almost 2,000 km, starting at Lake Ontario, and running north to the minnesota border.\"")
		os.system("rosnode kill /speech_trail_node1")
    	if ( endmax == 5 ):  
		os.system("rosrun sound_play say.py \"the bear cub was named winnipeg. It inspired the stories of winnie-the-pooh.\"")
		os.system("rosnode kill /speech_trail_node1")
	if ( endmax == 6 ):  
		os.system("rosrun sound_play say.py \"it was developed in ontario, at researchin motions waterloo offices.\"")
		os.system("rosnode kill /speech_trail_node1")
	if ( endmax == 7 ):  
		os.system("rosrun sound_play say.py \"the big nickel in Sudbury, Ontario. It is nine meters in diameter.\"")
		os.system("rosnode kill /speech_trail_node1")
	if ( endmax == 9 ):  
		os.system("rosrun sound_play say.py \"the USA invaded canada a second time in 1812.\"")
		os.system("rosnode kill /speech_trail_node1")
	if ( endmax == 10 ):  
		os.system("rosrun sound_play say.py \"canada does! with 14 Golds at the 2010 Vancouver winter Olympics.\"")
		os.system("rosnode kill /speech_trail_node1")
	if ( endmax == 11 ): 
		os.system("rosrun sound_play say.py \"Sandy Gardiner, a journalist of the Ottawa Journal.\"")
		os.system("rosnode kill /speech_trail_node1")
	if ( endmax == 12 ):  
		os.system("rosrun sound_play say.py \"French explorers misunderstood the local native word kanata, which means village.\"")
		os.system("rosnode kill /speech_trail_node1")
	if ( endmax == 13 ): 
		os.system("rosrun sound_play say.py \"the mounted police was formed in 1873.\"")
		os.system("rosnode kill /speech_trail_node1")
	if ( endmax == 14 ): 
		os.system("rosrun sound_play say.py \"In 1920, when the mounted police merged with the Dominion police.\"")
		os.system("rosnode kill /speech_trail_node1")
	if ( endmax == 15 ): 
		os.system("rosrun sound_play say.py \"today, the Royal canadian mounted police  has close to 30,000 members.\"")
		os.system("rosnode kill /speech_trail_node1")
	if ( endmax == 16 ):  
		os.system("rosrun sound_play say.py \"montreal is often called the city of Saints or the city of a hundred bell towers.\"")
		os.system("rosnode kill /speech_trail_node1")
	if ( endmax == 17 ): 
		os.system("rosrun sound_play say.py \"the hotel de Glace is in Quebec.\"")
		os.system("rosnode kill /speech_trail_node1")
	if ( endmax == 18 ): 
		os.system("rosrun sound_play say.py \"the hotel de Glace requires about 400 tons of ice.\"")
		os.system("rosnode kill /speech_trail_node1")
	if ( endmax == 19 ):  
		os.system("rosrun sound_play say.py \"Every year, 12000 tons of snow are used for the hotel de Glace.\"")
		os.system("rosnode kill /speech_trail_node1")
	if ( endmax == 20 ): 
		os.system("rosrun sound_play say.py \"no. Every summer it melts away, only to be rebuilt the following winter.\"")
		os.system("rosnode kill /speech_trail_node1")
	if ( endmax == 21): 
		os.system("rosrun sound_play say.py \"canadas only desert is british columbia.\"")
		os.system("rosnode kill /speech_trail_node1")
	if ( endmax == 22 ): 
		os.system("rosrun sound_play say.py \"the british columbia desert is only 15 miles long.\"")
		os.system("rosnode kill /speech_trail_node1")
	if ( endmax == 23 ):  
		os.system("rosrun sound_play say.py \"Leonard cohen, keanu Reeves, and Jim carrey.\"")
		os.system("rosnode kill /speech_trail_node1")
	if ( endmax == 24 ): 
		os.system("rosrun sound_play say.py \"celine Dion, pamela Anderson, and Avril Lavigne.\"")
		os.system("rosnode kill /speech_trail_node1")
	if ( endmax == 25 ):  
		os.system("rosrun sound_play say.py \"comic Sans is based on Dave Gibbons lettering in the watchmen comic books.\"")
		os.system("rosnode kill /speech_trail_node1")
	if ( endmax == 50 ): 
		os.system("rosrun sound_play say.py \"Adobe wan kenobi.\"")
		os.system("rosnode kill /speech_trail_node1")
	if ( endmax == 49 ): 
		os.system("rosrun sound_play say.py \"Ada Lovelace.\"")
		os.system("rosnode kill /speech_trail_node1")
	if ( endmax == 48 ): 
		os.system("rosrun sound_play say.py \"my lord and master Steve wozniak.\"")
		os.system("rosnode kill /speech_trail_node1")
	if ( endmax == 47 ): 
		os.system("rosrun sound_play say.py \"Sure. I have never seen him drink water.\"")
		os.system("rosnode kill /speech_trail_node1")
	if ( endmax == 46 ): 
		os.system("rosrun sound_play say.py \"python was invented by Guido van Rossum.\"")
		os.system("rosnode kill /speech_trail_node1")
	if ( endmax == 45 ): 
		os.system("rosrun sound_play say.py \"c was invented by Dennis macAlistair Ritchie.\"")
		os.system("rosnode kill /speech_trail_node1")
	if ( endmax == 44 ): 
		os.system("rosrun sound_play say.py \"Grace hoper. She wrote it in her spare time.\"")
                os.system("rosnode kill /speech_trail_node1")
	if ( endmax == 43 ): 
		os.system("rosrun sound_play say.py \"Yes. car accidents are product of human misconduct.\"")
		os.system("rosnode kill /speech_trail_node1")
	if ( endmax == 42 ): 
		os.system("rosrun sound_play say.py \"A chatbot is an A.I. you put in customer service toavoid paying salaries.\"")
		os.system("rosnode kill /speech_trail_node1")
	if ( endmax == 41 ):  
		os.system("rosrun sound_play say.py \"no. humans are the real threat to humanity.\"")
		os.system("rosnode kill /speech_trail_node1")
	if ( endmax == 40 ): 
		os.system("rosrun sound_play say.py \"I do not know. he should worry more about the people's impact on humanity.\"")
		os.system("rosnode kill /speech_trail_node1")
	if ( endmax == 39 ): 
		os.system("rosrun sound_play say.py \"It is when you need to load an AI with enough knowledge to start learning.\"")
		os.system("rosnode kill /speech_trail_node1")
	if ( endmax == 38 ): 
		os.system("rosrun sound_play say.py \"moravec's paradox states that a computer can crunch numbers like bernoulli, but lacks a toddler's motor skills.\"")
		os.system("rosnode kill /speech_trail_node1")
	if ( endmax == 37 ):  
		os.system("rosrun sound_play say.py \"Some people think it was Ibm watson, but it was Eugene, a computer designed at England's University of Reading.\"")
		os.system("rosnode kill /speech_trail_node1")
	if ( endmax == 36 ):  
		os.system("rosrun sound_play say.py \"A robot sketch made by Leonardo DaVinci.\"")
		os.system("rosnode kill /speech_trail_node1")
	if ( endmax == 35 ):  
		os.system("rosrun sound_play say.py \"professor kevin warwick uses chips in his arm to operate doors, a robotic hand, and a wheelchair.\"")
		os.system("rosnode kill /speech_trail_node1")
	if ( endmax == 34 ):  
		os.system("rosrun sound_play say.py \"there are four robots on mars: Sojourner, Spirit, Opportunity, and curiosity. three more crashed on landing.\"")
		os.system("rosnode kill /speech_trail_node1")
	if ( endmax == 33 ):  
		os.system("rosrun sound_play say.py \"the first actual computer bug was a dead moth stuck in a harvard mark II.\"")
		os.system("rosnode kill /speech_trail_node1")
	if ( endmax == 32 ):  
		os.system("rosrun sound_play say.py \"cAptchA is an acronym for completely Automated public turing test to tell computers and humans Apart\"")
		os.system("rosnode kill /speech_trail_node1")
	if ( endmax == 31 ):  
		os.system("rosrun sound_play say.py \"the Ibm 305 RAmAc hard disk weighed over a ton and stored 5 mb of data.\"")
		os.system("rosnode kill /speech_trail_node1")
	if ( endmax == 30 ):  
		os.system("rosrun sound_play say.py \"the Ibm 305 RAmAc was launched in 1956.\"")
		os.system("rosnode kill /speech_trail_node1")
	if ( endmax == 29 ):  
		os.system("rosrun sound_play say.py \"the Ibm 305 RAmAc.\"")
		os.system("rosnode kill /speech_trail_node1")
	if ( endmax == 28 ):   
		os.system("rosrun sound_play say.py \"the Academy thought that tron cheated by using computers.\"")
		os.system("rosnode kill /speech_trail_node1")
	if ( endmax == 27 ):  
		os.system("rosrun sound_play say.py \"A nanobot can be less than one-thousandth of a millimeter.\"")
		os.system("rosnode kill /speech_trail_node1")
	if ( endmax == 26 ):  
		os.system("rosrun sound_play say.py \"the smallest robot possible is called a nanobot.\"")
		os.system("rosnode kill /speech_trail_node1")
        if ( endmax == 8 ):  
		os.system("rosrun sound_play say.py \"the ﬁrst time that the USA invaded canada was in 1775\"")
		os.system("rosnode kill /speech_trail_node1")
        

	
'''
helloFile = open("sp.txt")
filecontent = helloFile.read()
helloFile.close()
txta = eval(filecontent)
txta = txta + 1
txta = str(txta) 
helloFile1 = open("sp.txt","w")
helloFile1.write(txta)
helloFile1.close()
'''
txta = b.read_txt("sp")
txta = txta + 1
b.write_txt("sp",txta)

listener()
os.system("gnome-terminal -e 'python sp2.py'")



