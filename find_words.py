
from scrape import MakeVocabClass
import sys
"""
Expects two sys args - first one is the document to search in
and second arg is the vocabulary.com html filename
"""


if len(sys.argv) >= 2:
	file = open(sys.argv[1], 'r')
	text = file.read()
	file.close()
	name = sys.argv[1]
	
	if len(sys.argv) >= 3:
		vocab_list_filename = sys.argv[2]
else:
	text = "I want to run everyday until the age of twenty four if it isn't too demanding."
	name = "The Default Text"



found_word_dict = {}

if vocab_list_filename:
	engine = MakeVocabClass(filename=vocab_list_filename)
else:	
	engine = MakeVocabClass()
my_dict = engine.get_dict()



for word in my_dict:
    if word in text:
        found_word_dict[word] = my_dict[word]




if len(found_word_dict) > 0:
	print("\n\nWe found " + str(len(found_word_dict)) + " CET4 vocabulary words in " + name + ".\n\n")
else:
	print("\n\nWe found ZERO CET4 vocabulary words in " + name + ".\n\n")


index = 1
for word in found_word_dict:
	print('\t' + str(index) + ") " + word + " - "  + found_word_dict[word] )
	index += 1