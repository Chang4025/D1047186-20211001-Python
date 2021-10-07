v1,v2 = map(int,input().split())

sdate = [20,19,21,20,21,22,23,23,23,24,23,22]
counts = ['摩羯座','水瓶座','雙魚座','牡羊座','金牛座','双子座','巨蟹座','狮子座','處女座',
'天秤座','天蝎座','射手座']


if int(v2) < sdate[int(v1)-1]:
    print(counts[int(v1)-1])
else:
    print(counts[int(v1)])

