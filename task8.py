#!/usr/bin/python3

import cgi
import subprocess,json

print("content-type: text/html")
print()

#print('Info')

f=cgi.FieldStorage()
num = f.getvalue("x")

#print(str(num))

with open('plate.json') as f:
	data = json.load(f)

c = 0

for plate in data['plates']:
	
	if plate["number"] == str(num):
		c=1
		print("Plate number: " , plate["number"])
		print("Owner: " , plate["name"])
		print("City: " , plate["city"])
		print("Phone: " , plate["phone"])
		break
		

if c == 0:
	print("no data found")


