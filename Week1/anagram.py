def isAnagram(a, b):
    a=a.lower()
    b=b.lower()

    a=a.replace(" ","")
    b=b.replace(" ", "")

    l1=list(a)
    l2=list(b)

    for i in l1:
        if i in l2:
            l2.remove(i)

    if(l2==[]):
        print("True")
    else:
        print("False")


str1="Tom Marvolo Riddle"
str2="I am Lord Voldemort"

isAnagram(str1,str2)
isAnagram('abcde','edbac')
