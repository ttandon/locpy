import sys
sys.path.append('../location')
from initiator import search

text = "A few days ago I went to Las Vegas and had a ton of fun gambling. Unfortunately I am now back home in Cupertino, California not doing much."
locations = search(text)
print locations