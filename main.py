import tkinter as tk

import time
import random as rnd

readFile = open('savedtext.txt','r')
readT = readFile.read()

N = 100000
K = 10
WIN = 10
KROK = 30

# def rnd_choice(text):

# 	for i in range(N):
# 		x1 = rnd.randint(0, len(text)-1)
# 		x2 = rnd.randint(0, len(text)-1)

# 		text[x1], text[x2] = text[x2], text[x1]
# 	return text

def L_symbol(text):
	text = text.replace(".",'')
	text = list(text)
	for i in range(100000):
		while True:
			x1 = rnd.randint(0, len(text)-1)
			x2 = rnd.randint(0, len(text)-1)
			if text[x1] != " " and text[x2] != " ":
				break

		
		text[x1], text[x2] = text[x2], text[x1]

	#print(text[0:10])
	return ''.join(text)	

L_symbol(readT)

def L_word(text):
	text = text.replace(".",'')
	text = text.split(" ")
	for i in range(N):
		x1 = rnd.randint(0, len(text)-1)
		x2 = rnd.randint(0, len(text)-1)

		text[x1], text[x2] = text[x2], text[x1]

	return ' '.join(text)

def L_str(text):
	text = text.split(".")

	for i in range(N):
		x1 = rnd.randint(0, len(text)-1)
		x2 = rnd.randint(0, len(text)-1)

		text[x1], text[x2] = text[x2], text[x1]

	return '.'.join(text)

"""
Далі ф-ції для 2-локального перемішування
"""

def lok2_symb(text):
	#Локально 2, перемішуємо символи в межах слова
	text = text.replace(".",'')
	text = text.split(" ")
	for i in range(len(text)):
		text[i] = list(text[i])

	for x in text:
		for k in range(2):
			x1 = rnd.randint(0,len(x)-1)
			x2 = rnd.randint(0,len(x)-1)
			x[x1],x[x2] = x[x2],x[x1]
	for i in range(len(text)):
		text[i] = ''.join(text[i])
	print(text[1])
	return ' '.join(text)
			

			
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

	
def lok2_word(text):
	#Локально 2, перемішуємо слова в межах речення
	#i might have saved myself the message
	text = text.split(". ")
	for i in range(len(text)):
		text[i] = text[i].split(' ')

	for x in text:
		for z in range(1):
			x1 = rnd.randint(0,len(x)-1)
			x2 = rnd.randint(0,len(x)-1)
			x[x1], x[x2] = x[x2], x[x1]

	for i in range(len(text)):
		text[i] = ' '.join(text[i])
	#print(text[35])
	print(text[-40])
	return '. '.join(text)
#what is it said baloo

"""
Далі ф-ції для 1-локального пермішування
"""
def lok1_symb(text):
	#time 782s for K=100000
	WIN = 10
	KROK = 30
	text = list(text.replace(',','').replace('.',' '))
	start = time.time()
	for i in range(KROK,len(text),KROK):
		for z in range(100000):
			while True:
				x1 = rnd.randint(i-WIN, i+WIN)
				x2 = rnd.randint(i-WIN, i+WIN)
				if text[x1] != " " and text[x2] != " ":
					break
			text[x1], text[x2] = text[x2], text[x1]
	finish = time.time()
	print("time: ", finish-start)
	return ''.join(text)

def lok1_word(text):
	# 214s for K = 10000
	text = text.split(" ")
	#start = time.time()
	for words in range(KROK,len(text),KROK):
		for i in range(10):
			while True:
				x1 = rnd.randint(words-WIN,words+WIN)
				x2 = rnd.randint(words-WIN,words+WIN)
				if text[x1] != "." and text[x2] != ".":
					break			
			text[x1], text[x2] = text[x2], text[x1]
	#finish = time.time()

	#print("time: ", finish-start)
	return ' '.join(text)


def lok1_str(text):
	# for K=100000 time is 97s
	text = text.split('. ')
	for sentences in range(KROK, len(text), KROK):
		for i in range(sentences-WIN,sentences+WIN):
			for i in range(100000):
				x1 = rnd.randint(sentences-WIN,sentences+WIN)
				x2 = rnd.randint(sentences-WIN,sentences+WIN)
			text[x1], text[x2] = text[x2], text[x1]
	return '. '.join(text)

print(lok1_str(readT))
# ***Закриваємо файл 
readFile.close()


