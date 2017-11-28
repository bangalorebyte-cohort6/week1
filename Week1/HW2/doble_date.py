def calculateday(l1,l2):

    dict={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

    num_day1=l1[0]
    for i in range(1,l1[1]):
        num_day1+=dict[i]

    num_day2 = l2[0]
    for i in range(1, l2[1]):
        num_day2 +=dict[i]

    double_day1=0
    double_day2=0

    for i in range(num_day2,365):
        a=num_day2/num_day1
        if a is 2:
            double_day1=num_day1
            double_day2=num_day2
            break
        num_day2+=1
        num_day1+=1
    print(double_day1)
    print(double_day2)

l1=[3,02]
l2=[4,05]
calculateday(l1,l2)