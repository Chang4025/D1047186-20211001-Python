#費氏數列 0 1 1 2 3 5 8 13
# v1 = int(input())
# count = 1
# while v1 != count:

def feb(n):
    if n <= 1:
        return 1
    else:
        return(feb(n-1)+feb(n-2))


print ("費式數列，是求出第N項的值！")
n = input ("輸入n:")
 
print (feb(int(n)-1))