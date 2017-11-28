# Create a crude and elementary text file editor.
# Your solution is menudriven, with the following options:
# a. create file [prompt for filename and any number of lines of input]
# b. display file [dump its contents to the screen]
# c. save file
# d. quit.

import os

def file_display(f):
    if os.path.exists(f):
        with open(f,'r') as file:
            for line in file:
                print(line)
    else:
        print("Doesn't exist!\n")


def file_create(n,f):
    if not os.path.exists(f):
        with open(f,'w+') as file:

            for i in range(n):
               file_data=raw_input("-->\n")
               file.write(file_data+"\n")

    else:
       print("Already exists !\n")


def menudriven(n):

   if n=='a':
      name = raw_input("File Name..?\n")
      file_path = '/home/harpreet/Documents/' + name + '.txt'
      n = input("Number of lines")
      file_create(n, file_path)

   elif n == 'b':
       name = raw_input("File Name..?\n")
       file_path ='/home/harpreet/Documents/' + name + '.txt'
       file_display(file_path)

   else:
      print("Save...\n")



i=0

while(i!='d'):
   i=raw_input("\na.create file\nb.display file\nc.save file\n d.quit")
   menudriven(i)

print("Shutdown successful")

