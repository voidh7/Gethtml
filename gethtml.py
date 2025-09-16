from urllib import request
import sys

url = sys.argv[1]
web= request.urlopen(url)

print(web.info())
print(web.read().decode("utf-8"))
