import os
def file_datagathering(f,l1):

    if os.path.exists(f):
        with open(f,'r') as file:
            for line in file:
                l1.append(line)
    else:
        print("Doesn't exist!\n")

def comparefile(l1,l2):
   count=1
   for i in l1:

      if i in l2:
         count += 1

      else:
         print("Changes detected:%s"%i)

   print("Changes occured at line:/t",count)


l1=[]
l2=[]
name = raw_input("File Name.1.?\n")
file_path = '/home/harpreet/Documents/' + name
print(file_path)
file_datagathering(file_path,l1)#check1
#print(l1)

name=""
file_path=""
name = raw_input("File Name.2.?\n")
file_path = '/home/harpreet/Documents/' + name
print(file_path)
file_datagathering(file_path,l2)
#print(l2)

comparefile(l1,l2)
