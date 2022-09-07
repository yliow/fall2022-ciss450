height = {}
height['john'] = 5.15
height['tom'] = 6.15
height['sue'] = 5.75
print(height)
height['john'] = 4.2
print(height)
del height['sue']
print(height)

if 'mary' in height.keys():
    print(height['mary'])
else:
    print("no mary")

if 'mary' in height:
    print(height['mary'])
else:
    print("no mary")

for key in height.keys():
    print('%s: %s' % (key, height[key]))

for key in height:
    print('%s: %s' % (key, height[key]))

for key,value in height.items():
    print('%s: %s' % (key, value))

#print(height.has_key('tom')) <-- OLD
print('tom' in height) 
