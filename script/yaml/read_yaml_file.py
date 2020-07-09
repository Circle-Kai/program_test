#! /bin/usr/python3
import yaml
with open(r'./config/map.yaml') as stream:
    data = yaml.safe_load(stream)
print(type(data))
print(data)
print(data['map'])
a = data['map']['width']
print(type(a))
print(a)
