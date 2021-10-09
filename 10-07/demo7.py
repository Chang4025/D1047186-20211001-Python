v1,v2 = map(int,input().split())

date = [21,19,21,21,22,22,23,24,24,24,23,22]
Con = ['摩羯座','水瓶座','雙魚座','牡羊座','金牛座','双子座','巨蟹座','狮子座','處女座',
'天秤座','天蝎座','射手座']


if int(v2) < date[int(v1)-1]:
    print(Con[int(v1)-1])
else:
    print(Con[int(v1)])

