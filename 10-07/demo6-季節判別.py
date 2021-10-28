v1 = int(input("請輸入月份:"))

if 3<=v1<=5:
    print("春季")
elif 6<=v1<=8:
    print("夏季")
elif 9<=v1<=11:
    print("秋季")
elif v1==12 or 1<=v1<=2:
    print("冬季")
else:
    print("error")