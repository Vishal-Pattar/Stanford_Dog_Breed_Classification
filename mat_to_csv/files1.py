import os
from bs4 import BeautifulSoup

lna = []
ct1 = ct2 = ct3 = ct4 = ct5 = ct6 = 0
for root, dirs, files in os.walk("Annotation"):
	for file in files:
		fl_path = os.path.join(root, file)
		fl = open(fl_path, "r")
		cp = fl.read()
		read = read = BeautifulSoup(cp, "html.parser")
		article = read.find("annotation")
		arr = article.text.split("\n")
		# print(len(arr))
		lna.append(len(arr))
		if len(arr) == 24 and ct1 == 0:
			print(arr)
			ct1 = 1
		if len(arr) == 36 and ct2 == 0:
			print(arr)
			ct2 = 1
		if len(arr) == 48 and ct3 == 0:
			print(arr)
			ct3 = 1
		if len(arr) == 60 and ct4 == 0:
			print(arr)
			ct4 = 1
		if len(arr) == 72 and ct5 == 0:
			print(arr)
			ct5 = 1
		if len(arr) == 84 and ct6 == 0:
			print(arr)
			ct6 = 1
		fl.close()
print(len(list(set(lna))))
a = [[x,lna.count(x)] for x in set(lna)]
print(a)

# [[36, 1205], [72, 2], [48, 122], [84, 1], [24, 19222], [60, 28]]