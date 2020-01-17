"""Simple script for text statistics experimentation. Counts words for given text. Gets sentence number, orders them and prints the 5 longest words"""


import inflect
import re
import sys

p = inflect.engine()
text= sys.argv[1]

def count_sentences(t):
	split_text=text.split('.') 
	return 'This text contains '+str((len(split_text)-1))+' sentences'

def count_words(t):
	split_text=text.split()
	return 'This text contains '+str((len(split_text)))+' words'

def order_sentences(t):
	split_text=text.split('.')
	split_text.sort(key=len, reverse=True)
	long_to_short=[]
	for i in range(len(split_text)):
		if len(split_text[i]) > 0:
			long_to_short.append('The {} longest sentence in the text contains {} words'.format(str(p.number_to_words(p.ordinal(i+1))),str(len(split_text[i]))))
	for i in long_to_short:
		print(i)
	return ''

def longest_words(t):
	t = t.lower()
	split_text = re.split('\.|\,|\s',t)
	split_text.sort(key=len, reverse=True)
	longest=[]
	for i in split_text:
		if i not in longest:
			longest.append(i)
	longest.sort(key=len, reverse=True)
	longest = longest[:6]
	longest.sort()
	return 'Five longest words in this text ordered alphabetically are: '+ str(longest)


print(count_words(text))
print('')
print(count_sentences(text))
print('')
print(order_sentences(text))
print(longest_words(text))


