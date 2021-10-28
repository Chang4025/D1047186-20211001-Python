v1,v2,v3 = map(int,input().split())
if v1<=v2<=v3:
    if v1+v2>v3:
        print("true")
    elif v2+v3>v1:
        print("true")
    elif v1+v3>v2:
        print("true")
    else:
        print("false")
else:
    print("false")