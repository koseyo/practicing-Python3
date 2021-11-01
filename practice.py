# coding: utf-8

d = {"x": 10, "y": 20}
print(d)
print(type(d))

print(d.keys()) #key's'

print(d.values()) #value's'

d2 = {"x": 1000, "j": 500}
print(d2)

d.update(d2)
print(d)

print(d.get("x"))
print(d.get("z"))
d.pop("x")
print(d)
