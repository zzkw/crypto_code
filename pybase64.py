"""import base64
a = 'demo:demo1234!'
jm = base64.b64encode(a.encode('utf-8'))
b = str(jm)
print(b[2:-1])"""
import base64
a = 'demo:demo1234!'
d = base64.b64encode(a.encode('utf-8'))
print(str(d,'utf-8'))
