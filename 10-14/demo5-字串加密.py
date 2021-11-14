v1 = list(input("請輸入文字："))
v2 = int(input("加密："))
cipher = list()

for c in v1:
    cipher.append(chr(ord(c)+v2))

stra = ("".join(cipher))
print(stra)

# for i in range(27):
#     strb = chr(ord(c)+i)
    
# print(strb)

