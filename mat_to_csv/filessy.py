import os
from bs4 import BeautifulSoup
# for root, dirs, files in os.walk("Annotation"):
# 	for file in files:
# 		print(os.path.join(root, file))

fl = open("./Annotation/n02085620-Chihuahua/n02085620_10074", "r")
cp = fl.read()
fl.close()

read = read = BeautifulSoup(cp, "html.parser")
article = read.find("annotation")
print(article.text.split("\n"))

# import csv
	
# # field names
# fields = ['Name', 'Branch', 'Year', 'CGPA']
	
# # data rows of csv file
# rows = [ ['Nikhil', 'COE', '2', '9.0'],
# 		['Sanchit', 'COE', '2', '9.1'],
# 		['Aditya', 'IT', '2', '9.3'],
# 		['Sagar', 'SE', '1', '9.5'],
# 		['Prateek', 'MCE', '3', '7.8'],
# 		['Sahil', 'EP', '2', '9.1']]
	
# # name of csv file
# filename = "university_records.csv"
	
# # writing to csv file
# with open(filename, 'w') as csvfile:
# 	# creating a csv writer object
# 	csvwriter = csv.writer(csvfile)
		
# 	# writing the fields
# 	csvwriter.writerow(fields)
		
# 	# writing the data rows
# 	csvwriter.writerows(rows)


