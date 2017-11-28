import os

def print_file(n,f):
    i=0
    if os.path.exists(f):
        with open(f,'r') as file:
            for line in file:
                if(n>i):
                    print(line)
                    i+=1
                else:
                    break




name = raw_input("File Name..?")
file_path='/home/harpreet/Documents/'+name+'.txt'
n=raw_input("Number of lines")
print_file(n,file_path)
