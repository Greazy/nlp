import tkinter as tk

import time
import random as rnd


N = 1
K = 10
WIN = 10
KROK = 30


readFile = open('savedtext.txt','r')


def mixing_symbols_global(text,space=False):
	# test done!
	text = text.replace(".",'')
	text = list(text)


	for i in range(1):
		while True:
			x1 = rnd.randint(0, len(text)-1)
			x2 = rnd.randint(0, len(text)-1)
			if space == True:
				break
			if text[x1] != " " and text[x2] != " ":
				break

		
		text[x1], text[x2] = text[x2], text[x1]

	fileforsave = open('testtext.txt','w')
	fileforsave.write(''.join(text))
	fileforsave.close()
	return open('testtext.txt','r').read()



def mixing_words_global(text):
	# test done!

	text = text.replace(".",'')
	text = text.split(" ")

	print(text)

	for i in range(N):
		x1 = rnd.randint(0, len(text)-1)
		x2 = rnd.randint(0, len(text)-1)

		text[x1], text[x2] = text[x2], text[x1]
	print(text)
	fileforsave = open('testtext.txt','w')
	fileforsave.write(' '.join(text))

	fileforsave.close()
	return open('testtext.txt','r').read()

def mixing_strings_global(text):
	# 
	print(text)
	text = text.split(".")

	for i in range(3):
		print(len(text))
		x1 = rnd.randint(0, len(text)-1)
		print(x1)
		x2 = rnd.randint(0, len(text)-1)

		text[x1], text[x2] = text[x2], text[x1]
	#print(text)
	fileforsave = open('testtext.txt','w')
	fileforsave.write('.'.join(text))
	fileforsave.close()
	return open('testtext.txt','r').read()

"""
Далі ф-ції для 2-локального перемішування
"""

def lok2_mix_symbols_within_words(text):
	#Локально 2, перемішуємо символи в межах слова
	text = text.replace(".",'')
	text = text.split(" ")
	for i in range(len(text)):
		text[i] = list(text[i])

	for x in text:
		for k in range(1):
			x1 = rnd.randint(0,len(x)-1)
			x2 = rnd.randint(0,len(x)-1)
			x[x1],x[x2] = x[x2],x[x1]
	for i in range(len(text)):
		text[i] = ''.join(text[i])

	fileforsave = open('testtext.txt','w')
	fileforsave.write(' '.join(text))
	fileforsave.close()
	return open('testtext.txt','r').read()
			

			
	# 	'''
	# 	for y in x:
	# 		for z in range(1):
	# 			x1 = rnd.randint(0,len(x)-1)
	# 			x2 = rnd.randint(0,len(x)-1)
	# 		x[x1], x[x2] = x[x2], x[x1]
	# 	'''

	# # for i in range(len(text)):
	# # 	text[i] = ''.join(text[i])
	# # print(text[-1])
	# # return ' '.join(text)

	
def lok2_mix_words_within_sentences(text):
	#Локально 2, перемішуємо слова в межах речення

	text = text.split(". ")

	for i in range(len(text)):
		text[i] = text[i].split(' ')

	for x in text:
		for z in range(10):
			x1 = rnd.randint(0,len(x)-1)
			x2 = rnd.randint(0,len(x)-1)
			x[x1], x[x2] = x[x2], x[x1]

	for i in range(len(text)):
		text[i] = ' '.join(text[i])

	fileforsave = open('testtext.txt','w')
	fileforsave.write(' '.join(text))
	fileforsave.close()
	return open('testtext.txt','r').read()


"""
Далі ф-ції для 1-локального пермішування
"""
def lok1_mix_symbols_in_words(text):
	#time 782s for K=100000

	text = list(text.replace(',','').replace('.',' '))

	for i in range(KROK,len(text),KROK):
		for z in range(10):
			while True:
				x1 = rnd.randint(i-WIN, i+WIN)
				x2 = rnd.randint(i-WIN, i+WIN)
				if text[x1] != " " and text[x2] != " ":
					break
			text[x1], text[x2] = text[x2], text[x1]

	fileforsave = open('testtext.txt','w')
	fileforsave.write(''.join(text))
	fileforsave.close()
	return open('testtext.txt','r').read()

def lok1_mix_words_in_sentences(text):
	# 214s for K = 10000
	text = text.split(" ")

	for words in range(KROK,len(text),KROK):
		for i in range(1000):
			while True:
				x1 = rnd.randint(words-WIN,words+WIN)
				x2 = rnd.randint(words-WIN,words+WIN)
				if text[x1] != "." and text[x2] != ".":
					break			
			text[x1], text[x2] = text[x2], text[x1]

	fileforsave = open('testtext.txt','w')
	fileforsave.write(' '.join(text))
	fileforsave.close()
	return open('testtext.txt','r').read()


def lok1_mix_sentences_in_text(text):
	# for K=100000 time is 97s
	text = text.split('. ')

	for sentences in range(KROK, len(text), KROK):
		for i in range(sentences-WIN,sentences+WIN):
			for i in range(1000):
				x1 = rnd.randint(sentences-WIN,sentences+WIN)
				x2 = rnd.randint(sentences-WIN,sentences+WIN)
			text[x1], text[x2] = text[x2], text[x1]

	fileforsave = open('testtext.txt','w')
	fileforsave.write('. '.join(text))
	fileforsave.close()
	return open('testtext.txt','r').read()


# ***Закриваємо файл 

if __name__ == "__main__":
	readFile = open('savedtext.txt','r')

	N = 100000
	K = 10
	WIN = 10
	KROK = 30
	
	readFile.close()


