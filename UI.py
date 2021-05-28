from tkinter import *
from tkinter.ttk import Checkbutton
from tkinter import scrolledtext
import logicNLP
import time
from tkinter import * 
from tkinter import ttk

from tkinter.filedialog import asksaveasfile, askopenfile

#readFile = open('savedtext.txt','r')
#text = readFile.read()

window = Tk()
window.state("zoomed")
window.title("NLP")

def open_file():
	global text
	files = [('All Files', '*.*'), 
         ('Python Files', '*.py'),
         ('Text Document', '*.txt')]
	file = askopenfile(mode='r', filetypes=files, defaultextension=files)
	#opened = open('savedtext.txt','r').read()
	
	text = file.read()
	txt.insert("0.0", text)
	file.close()

def save_file():
	files = [('All Files', '*.*'), 
             ('Python Files', '*.py'),
             ('Text Document', '*.txt')]
	file = asksaveasfile(filetypes=files, defaultextension = files )
	#with open()


#TODO: show time of work, save as, parameters.

def clicked(text,name,space=None):
	#try:
	K = int(entry_txt1.get())
	WIN = int(entry_txt2.get())
	KROK = int(entry_txt3.get())

	print("foo called: ",name)
	start_time = time.time()
	while True:
		if name == 'mixing_symbols_global':
			txt.delete("0.0",END)
			tt = logicNLP.mixing_symbols_global(text, K, space)
			txt.insert("0.0", tt[0:10000])
			break
		elif name == 'mixing_words_global':
			txt.delete("0.0",END)
			tt = logicNLP.mixing_words_global(text, K)
			txt.insert("0.0", tt[0:10000])
			break
		elif name == 'mixing_strings_global':
			txt.delete("0.0",END)
			tt = logicNLP.mixing_strings_global(text, K)
			txt.insert("0.0", tt[0:10000])
			break
		elif name == 'lok2_mix_symbols_within_words':
			txt.delete("0.0",END)
			tt = logicNLP.lok2_mix_symbols_within_words(text, K, WIN, KROK)
			txt.insert("0.0", tt[0:10000])
			break
		elif name == 'lok2_mix_words_within_sentences':
			tt = logicNLP.lok2_mix_words_within_sentences(text, K, WIN, KROK)
			txt.delete("0.0",END)
			txt.insert("0.0", tt[0:10000])
			break
		elif name == 'lok1_mix_symbols_in_words':
			txt.delete("0.0",END)
			tt = logicNLP.lok1_mix_symbols_in_words(text, K, WIN, KROK)
			txt.insert("0.0", tt[0:10000])
			break
		elif name == 'lok1_mix_words_in_sentences':
			txt.delete("0.0",END)
			tt = logicNLP.lok1_mix_words_in_sentences(text, K, WIN, KROK)
			txt.insert("0.0", tt[0:10000])
			break
		elif name == 'lok1_mix_sentences_in_text':
			txt.delete("0.0",END)
			tt = logicNLP.lok1_mix_sentences_in_text(text, K, WIN, KROK)
			txt.insert("0.0", tt[0:10000])
			break
	finish_time = time.time()
	time_shower.configure(text=(f'Time: {(finish_time-start_time):.3f}'))
			
	#except:
	#		txt.delete("0.0",END)
	#		txt.insert("0.0", "Введіть змінні")

chk_state = BooleanVar()
chk_state.set(False)
chk = Checkbutton(window, text="Враховувати пробіли", var=chk_state)


txt = scrolledtext.ScrolledText(window,width=169,height=40)

time_shower = Label(window,text="Working time will be here :)")


btn1 = Button(window, text="Глобальне перемішування символів", command=lambda: clicked(text, name='mixing_symbols_global', space=chk_state.get()))
btn2 = Button(window, text="Глобальне перемішування слів", command=lambda: clicked(text, name='mixing_words_global'))
btn3 = Button(window, text="Глобальне перемішування речень", command=lambda: clicked(text, name='mixing_strings_global'))

btn4 = Button(window, text="Локально 2 для символів", command=lambda: clicked(text, name='lok2_mix_symbols_within_words'))
btn5 = Button(window, text="Локально 2 для слів", command=lambda: clicked(text, name='lok2_mix_words_within_sentences'))
btn6 = Button(window, text="Локально 2 речень", command=lambda: clicked(text, name='mixing_strings_global'))

btn7 = Button(window, text="Локально 1 для символів", command=lambda: clicked(text, name='lok1_mix_symbols_in_words'))
btn8 = Button(window, text="Локально 1 для слів", command=lambda: clicked(text, name='lok1_mix_words_in_sentences'))
btn9 = Button(window, text="Локально 1 речень", command=lambda: clicked(text, name='lok1_mix_sentences_in_text'))

btn_del = Button(window, text="delete", command=lambda: txt.delete("0.0", END))
btn_open = Button(window, text='open file', command=open_file)

btn_save = Button(window, text='save as', command=save_file)

lbl1 = Label(window, text="K")
lbl2 = Label(window, text="WIN")
lbl3 = Label(window, text="KROK")

entry_txt1 = Entry(window,  width=10)
entry_txt2 = Entry(window,  width=10)
entry_txt3 = Entry(window,  width=10)


lbl1.place(x=1025, y=645)
lbl2.place(x=1115, y=645)
lbl3.place(x=1215, y=645)

entry_txt1.place(x=1000,y=675)
entry_txt2.place(x=1100,y=675)
entry_txt3.place(x=1200,y=675)

btn1.place(x=350,y=650)
btn2.place(x=350,y=680)
btn3.place(x=350,y=710)
btn4.place(x=600,y=650)
btn5.place(x=600,y=680)
btn6.place(x=600,y=710)
btn7.place(x=800,y=650)
btn8.place(x=800,y=680)
btn9.place(x=800,y=710)

btn_del.place(x=1000,y=710)

btn_open.place(x=1200,y=710)

btn_save.place(x=1200,y=690)

chk.place(x=200, y=653)

time_shower.place(x=200, y=670)
txt.place(x=1,y=1)





window.mainloop()
