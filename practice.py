# coding: utf-8

list = [] #配列の数は宣言しなくていい
for i in range(0, 10):
    list.append(i) #.appendメソッドで一つずつ加えていく

list.reverse()
print(list)
list.sort()
print(list)

s = "My name is Mike"
s_split = s.split(" ")
print(s_split)
x = " ".join(s_split)
print(x)