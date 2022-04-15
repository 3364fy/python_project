import requests
print(chr(97))
print(ord('a'))
print(ord(chr(97)))
x=0
for _ in range(0,50000):
    print(chr(x),ord(chr(x)))
    x+=1