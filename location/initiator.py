import re, string
import pickle
import nltk
from search import loc, locstates, loccities


def extract2(tagged):
	preselection = []
	i = 0
	while i < len(tagged):
		if tagged[i][1] == "NNP" or tagged[i][1] == "-None-":
			namestr = ""
			while tagged[i][1] == "NNP" or tagged[i][1] == "-None-":
				namestr += tagged[i][0] + " "
				if i == len(tagged)-1: break
				i = i + 1
			preselection.append(namestr)
		i = i + 1
	return loc(locfilter(preselection))

def extract3(tagged):
	preselection = []
	i = 0
	while i < len(tagged):
		if tagged[i][1] == "NNP" or tagged[i][1] == "-None-":
			namestr = ""
			while tagged[i][1] == "NNP" or tagged[i][1] == "-None-":
				namestr += tagged[i][0] + " "
				if i == len(tagged)-1: break
				i = i + 1
			preselection.append(namestr)
		i = i + 1
	return locstates(locfilter(preselection))
def extract4(tagged):
	preselection = []
	i = 0
	while i < len(tagged):
		if tagged[i][1] == "NNP" or tagged[i][1] == "-None-":
			namestr = ""
			while tagged[i][1] == "NNP" or tagged[i][1] == "-None-":
				namestr += tagged[i][0] + " "
				if i == len(tagged)-1: break
				i = i + 1
			preselection.append(namestr)
		i = i + 1
	return loccities(locfilter(preselection))
##does some filtering to get rid of potential trash
def locfilter(locs):
	filtered = []
	for loc in locs:
		loc = loc.strip()
		if len(loc) > 3 and len(re.findall("[A-Z]", loc))>0 and len(re.findall("[A-Z]", loc))<4 and contains_digits(loc) != True:
			filtered.append(loc)
	return set(filtered)
def contains_digits(s):
    return any(char.isdigit() for char in s)

def search(text):
	exclude = set(string.punctuation)
	text = ''.join(ch for ch in text if ch not in exclude)
	tagger = pickle.load(open("../tagger/treebank_brill_aubt.pickle"))
	tokens = nltk.word_tokenize(text)
	tagged = tagger.tag(tokens)
	locarray = extract2(tagged)
	locarray = locarray + extract3(tagged)
	locarray = locarray + extract4(tagged)
	locarray = list(set(locarray))
	return locarray