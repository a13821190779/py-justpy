import json

d = dict(name = 'fox', age = 23, sex = 'man')
print(d)
temp = json.dumps(d)
print(temp)
print(type(temp))
print(json.loads(temp))
print(type(json.loads(temp)))