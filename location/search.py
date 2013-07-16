import re
from datetime import datetime
output = []
def loc(words):
	with open("../datafiles/countries.txt", "r") as f:
		searchlines = f.readlines()
	for word in words:
		word = word + "\t"
		for i, line in enumerate(searchlines):
			if word in line: 
				for l in searchlines[i:i+1]: output.append(l),
	return output
def locstates(words):
	with open("../datafiles/states.txt", "r") as f:
		searchlines = f.readlines()
	for word in words:
		for i, line in enumerate(searchlines):
			if word in line: 
				for l in searchlines[i:i+1]: output.append(l),
	return output
def loccities(words):
	with open("../datafiles/amcities.txt", "r") as f:
		searchlines = f.readlines()
	for word in words:
		word = "  " + word + ","
		for i, line in enumerate(searchlines):
			if word in line: 
				for l in searchlines[i:i+1]: output.append(l),
	return output