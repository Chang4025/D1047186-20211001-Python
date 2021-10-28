word = str(input())
data = {letter:word.count(letter)for letter in set (word)}
for key in data:
    print(key,":",data[key])