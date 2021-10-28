import random 
n = random.randrange(0, 100)
v1 = int(input())
count = 1
while v1!=n:
    if v1>n:
        print("太大")
        v1 = int(input())
        count+=1
    elif v1<n:
        print("太小")
        v1 = int(input())
        count+=1

    else:    
        count+=1
        break

if v1==n:
    print("猜對了,總共猜了",count,"次,答案為：",n)