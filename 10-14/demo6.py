m = int(input())
result = 1
count = 1
while result<=m:
    count+=1
    result*=count
 
print("{} {}".format(count,result))