x={}
x["A"]=((9*8)/(22*21))*((2*3)/(9*8)) #隨機拿兩支拿對
x["D"]=((13*12)/(22*21))*((5*5)/(15*14)) #拿到ＢＣ筆的可能
x["E"]=((9*6)/(22*21))*((2*2)/(9*6)) #紅Ａ藍Ｂ
x["F"]=((9*6)/(22*21))*((3*2)/(9*6)) #紅Ｂ藍Ａ
x["G"]=((9*7)/(22*21))*((2*3)/(9*7)) #紅Ａ藍Ｃ
x["H"]=((9*7)/(22*21))*((3*3)/(9*7)) #紅Ｃ藍Ａ
pro=sum(i for i in x.values())
for i, p in x.items():  #條件機率 拿到紅筆或藍筆的機率
    x[i] =p/pro
print(1-x["A"]) 

y={}
y["A"]=(9/16)*(7/9)
y["C"]=(7/16)*(4/7)
pro1=sum(j for j in y.values())
for j, t in y.items():
    y[j] =t/pro1
if y["A"]>y["C"]:
    print("A較大")
else:
    print("C較大")