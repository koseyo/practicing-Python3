x = {"a": 1}
y = x
y["a"] = 1000
print(x)
print(y)

x = {"a": 1}
y = x.copy()
print(x)
print(y)

fruits = {
    "apple": 100,
    "banana": 200,
    "orange": 300,
}

print(fruits["apple"])#リストは値を探すのに時間がかかる

'''
l = [
    ["apple", 100],
    ["banana", 200],
    ["orange", 300],
]
'''