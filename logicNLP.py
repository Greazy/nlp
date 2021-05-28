import tkinter as tk

import time
import random as rnd


readFile = open('savedtext.txt','r')


def mixing_symbols_global(text, K, space=False):
	# test done!
	text = text.replace(".",'')
	text = list(text)


	for i in range(K):
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



def mixing_words_global(text, K):
	# test done!
	
	start = time.time()
	text = text.replace(".",'')
	text = text.split(" ")

	for i in range(K):
		x1 = rnd.randint(0, len(text)-1)
		x2 = rnd.randint(0, len(text)-1)

		text[x1], text[x2] = text[x2], text[x1]
	fileforsave = open('testtext.txt','w')
	fileforsave.write(' '.join(text))

	fileforsave.close()
	print("time: ", time.time() - start)
	return open('testtext.txt','r').read()

def mixing_strings_global(text, K):
	# test done!
	text = text.split(".")

	for i in range(K):
		x1 = rnd.randint(0, len(text)-1)
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

def lok2_mix_symbols_within_words(text, K, WIN, KROK):
	#Локально 2, перемішуємо символи в межах слова
	# test done!
	text = text.replace(".",'')
	text = text.split(" ")
	for i in range(len(text)):
		text[i] = list(text[i])

	for x in text:
		if len(x) in [0,1]:
			continue
		for k in range(K):
			print("len: ", len(x))
			x1 = rnd.randint(0,len(x)-1)
			print(x1)
			x2 = rnd.randint(0,len(x)-1)
			x[x1],x[x2] = x[x2],x[x1]
	for i in range(len(text)):
		text[i] = ''.join(text[i])

	fileforsave = open('testtext.txt','w')
	fileforsave.write(' '.join(text))
	fileforsave.close()
	return open('testtext.txt','r').read()
			
	
def lok2_mix_words_within_sentences(text, K, WIN, KROK):
	#Локально 2, перемішуємо слова в межах речення
	# test done!
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
def lok1_mix_symbols_in_words(text, K, WIN, KROK):
	#time 782s for K=100000


	text = list(text.replace(',','').replace('.',' '))

	for i in range(KROK,len(text),KROK):
		for z in range(K):
			x = 0
			while True:
				x+=1
				x1 = rnd.randint(i-WIN, i+WIN-1)
				x2 = rnd.randint(i-WIN, i+WIN-1)
				print(x)
				# print(x1,x2)
				# print(len(text))
				# print(text[x1], text[x2])
				if x == 5:
					break
				if text[x1] != " " and text[x2] != " ":
					break
			text[x1], text[x2] = text[x2], text[x1]

	fileforsave = open('testtext.txt','w')
	fileforsave.write(''.join(text))
	fileforsave.close()
	return open('testtext.txt','r').read()

def lok1_mix_words_in_sentences(text, K, WIN, KROK):
	# 214s for K = 10000
	# test done!

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


def lok1_mix_sentences_in_text(text, K, WIN, KROK):
	# for K=100000 time is 97s
	# test done!
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
readFile.close()

if __name__ == "__main__":
	readFile = open('savedtext.txt','r')
	readT = readFile.read()
	print(mixing_words_global(readT))

	N = 100000
	K = 10
	WIN = 10
	KROK = 30
	
	readFile.close()


