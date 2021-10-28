v1,v2 = map(int,input().split())
if v2==1:
    print(round((float(v1-80)*0.7), 2))

elif v2==2:
    print(round((float(v1-70)*0.6), 2))

else:
    print("error")
