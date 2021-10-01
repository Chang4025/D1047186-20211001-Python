v1,v2 = map (int,input("請輸入身高與性別：").split())

if(v2==1):
   a= float((v1-80)*0.7)
elif(v2==2):
   a= float((v1-70)*0.6)    

print (a)