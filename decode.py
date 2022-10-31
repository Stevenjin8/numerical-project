import unidecode
import sys

with open(sys.argv[0]) as f:
	data = f.read()
udata = data.decode("utf-8")
asciidata=udata.encode("ascii","ignore")
print(asciidata)

