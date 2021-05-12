import os
def separate(stra):
    stra = stra + ' '
    lista = list(stra)
    count = lista.count(' ')
    end1 = ''
    end2 = ''
    i = 0
    j = 0
    t = 0

    while(t<count):
        while(1):
            if(lista[i] == ' '):
                if(j+1 == 1):
                    sums = [end1]
                elif(j+1 == 2):
                    sums.append(end2)
                    end2 = ''
                i=i+1
                break
            else:
                if(j+1 == 1):
                    end1 = end1 + lista[i]
                elif(j+1 == 2):
                    end2 = end2 + lista[i]
                i=i+1
        j=1
        t=t+1
    return sums

def max_position(list_max):
	list_endmax_position = []
	tuple_max = tuple(list_max)
	max_value = max(list_max)
        for iposition in range(1,len(list_max)+1):
    		if list_max[iposition-1] == max_value:
			list_endmax_position.append(iposition)
	return list_endmax_position

def write_txt(name,content): 
	txt_name1 = name + '.txt'
	helloFile_write = open(txt_name1,"w")
	helloFile_write.write(str(content))
	helloFile_write.close()

def read_txt(name):
	txt_name2 = name + '.txt' 	
	helloFile_read = open(txt_name2)
	fileContent_read = helloFile_read.read()
	helloFile_read.close()
	fileContent_read = eval(fileContent_read)
	return fileContent_read
def lcmd(name_cmd_l):
	name_cmd_l = "gnome-terminal -e \"bash -c '" + name_cmd_l + "; exec bash'\""
	os.system(name_cmd_l)
def cmd(name_cmd):
	name_cmd = "gnome-terminal -e " + name_cmd
	os.system(name_cmd)
	




