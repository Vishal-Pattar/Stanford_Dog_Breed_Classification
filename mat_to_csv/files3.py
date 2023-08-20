import os
from bs4 import BeautifulSoup
import csv

feat = []
f_arr = []
obj_arr = []
data_arr = []
ct = 0

for root, dirs, files in os.walk("Annotation"):
	for file in files:
		fl_path = os.path.join(root, file)
		fl = open(fl_path, "r")
		cp = fl.read()
		read = read = BeautifulSoup(cp, "html.parser")
		annot = read.find("annotation")
		if ct == 0:
			allTags = read.findAll(True)
			for e in allTags:
				feat.append(e.name)
			ct = 1
		arr = annot.text.split("\n")
		objct = read.find_all("object")
		if len(objct) == 1:
			f_arr.append(arr[:10])
			ob_arr = objct[0].text.split("\n")
			obj_arr.append(ob_arr)
			data_arr.append(arr[:10]+ob_arr)
		else:
			for lx in range(len(objct)):
				f_arr.append(arr[:10])
				ob_arr = objct[lx].text.split("\n")
				obj_arr.append(ob_arr)
				data_arr.append(arr[:10]+ob_arr)
with open("stanford_dogs.csv", 'w') as csvfile:
	csvwriter = csv.writer(csvfile)
	csvwriter.writerow(feat)
	csvwriter.writerows(data_arr)