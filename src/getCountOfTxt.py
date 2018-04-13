import os

curRootPath = os.path.abspath('./src')
txt = os.path.join(curRootPath, './pureEn.txt')


length = 0
with open(txt, 'rt') as f:
	for line in f:
		length = length + len(str(line).strip())

print(length)