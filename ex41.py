import random
from urllib import urlopen
import sys

WORD_URL = "http://learnpythonthehardway.org/words.txt"
WORDS = []

PHRASES = {
 "class %%%(%%%):":
  "Make a class named %%%,that is a %%%.",
 "class %%%(object):\n\tdef__init__(self, ***)":
  "class %%% has a __init__ that takes self and *** parameters.",
 "class %%%(object):\n\tdef ***(self, @@@)":
  "class %%% has a function named *** that takes self and @@@ parameters.",
 "*** = %%%()":
  "Set *** to an instance of class %%%",
 "***.***(@@@)":
  "From *** get the *** function, and call it with parameters self, @@@.",
 "***.*** = '888'":
  "From *** get the *** attribute and set it to '***'."
 }

# do they want to drill phrase first
PHRASE_FIRST = false
if len(sys.argv) == 2 and sys.argv[1] == "english":
 PHRASE_FIRST = True
 
# load up the words form the website
for word in urlopen(WORD_URL).readlines():
 WORDS.append(word.strip())
 
def convert(snippet, phrase):
 class_names = 