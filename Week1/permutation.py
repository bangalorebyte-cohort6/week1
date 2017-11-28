def isPermutation(L):
    n=len(L)
    L1=[]

    while(n>0):
        L1.append(n)
        n=n-1

    for i in L:
        if i in L1:
            L1.remove(i)

    if(L1==[]):
        print("True")
    else:
        print("False")


L=[1,2,3,5,4]
isPermutation(L)

