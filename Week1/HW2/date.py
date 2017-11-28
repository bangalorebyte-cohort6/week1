from datetime import datetime
from datetime import date

def birthday(bd):
    #bd=["date-0","month-1"]
    bd[0]=bd[0]-1
    d = datetime.now()
    #print(d)

    t=d.timetuple()
    l=[]
    for i in t:
        l.append(i)

    age = l[0] - bd[2]

    print("Age:%d" % age)

    #print(l[2],l[1])#date and month

    dict={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

    #print(dict[l[1]])
    total_days=0
    day_left=0
    day_add = 0

    if(bd[1] == l[1] and bd[0]>=l[2]):
        total_days=bd[0]-l[2]
        print(total_days)

    else:
        day_left=dict[l[1]]-l[2]-1#current month days-given days
        #print(day_left)
        m1=l[1]+1
        m2=bd[1]

        if(m1>m2):
            m2=m2+12

        l2=[x for x in range(m1,m2)]
        #print(l2)


        for i in range(len(l2)):

            #print("For")
            if (l2[i]>12):
                l2[i]=l2[i]-12
                day_add+=dict[l2[i]]

            else:
                day_add+=dict[l2[i]]

        # print(day_left)
        # print(day_add)
        # print(bd[0])
        total_days=day_left+day_add+bd[0]

        print('Days left: %d'%total_days)

    hours_today = 24 - l[3]
    min = 60 - l[4]
    sec = 60 - l[5]

    hours_total = (total_days * 24) + hours_today
    total_time = []
    total_time.append(hours_total)
    total_time.append(min)
    total_time.append(sec)

    print('Total time left(hours/min/seconds): %s' % total_time)


bd=[15,7,1947]
birthday(bd)