from tkinter import *
from tkinter.ttk import Checkbutton
from tkinter import scrolledtext
import logicNLP

readFile = open('savedtext.txt','r')
readT = readFile.read()

window = Tk()
window.state("zoomed")
window.title("NLP")


def clicked(readT,name):
	print("foo called: ",name)
	if name == 'mixing_symbols_global':
		tt = logicNLP.mixing_symbols_global(readT)
		txt.insert("0.0", tt)
	elif name == 'mixing_words_global':
		tt = logicNLP.mixing_words_global(readT)
		txt.insert("0.0", tt)
	elif name == 'mixing_strings_global':
		tt = logicNLP.mixing_strings_global(readT)
		txt.insert("0.0", tt)
	elif name == 'lok2_symb':
		tt = logicNLP.lok2_symb(readT)
		txt.insert('0.0', tt)


btn1 = Button(window, text="Глобальне перемішування символів", command=lambda: clicked(readT, name='mixing_symbols_global'))
btn2 = Button(window, text="Глобальне перемішування слів", command=lambda: clicked(readT, name='mixing_words_global'))
btn3 = Button(window, text="Глобальне перемішування речень", command=lambda: clicked(readT, name='mixing_strings_global'))

btn4 = Button(window, text="Локально 1 для символів", command=lambda: clicked(readT, name='lok2_symb'))
btn5 = Button(window, text="Локально 1 для слів", command=lambda: clicked(readT, name='lok2_symb'))
btn6 = Button(window, text="Локально 1 речень", command=lambda: clicked(readT, name='lok2_symb'))

btn7 = Button(window, text="Локально 2 для символів", command=lambda: clicked(readT, name='lok2_symb'))
btn8 = Button(window, text="Локально 2 для слів", command=lambda: clicked(readT, name='lok2_symb'))
btn9 = Button(window, text="Локально 2 речень", command=lambda: clicked(readT, name='lok2_symb'))

btn10 = Button(window, text="delete", command=lambda: txt.delete("0.0", END))

btn10.grid(column=17, row=5)

chk_state = BooleanVar()
chk_state.set(False)
chk = Checkbutton(window, text="Враховувати пробіли", var=chk_state)
chk.grid(column=13, row=7)

txt = scrolledtext.ScrolledText(window,width=100,height=40)
txt.insert(INSERT, "")
txt.grid(column=5, row=5)


#btn1.grid(column=14,row=1)
x_cor = 1100
btn1.grid(column=10, row=10)
'''
btn2.place(x=x_cor,y=100)
btn3.place(x=x_cor,y=150)
btn4.place(x=x_cor,y=200)
btn5.place(x=x_cor,y=250)
btn6.place(x=x_cor,y=300)
btn7.place(x=x_cor,y=350)
btn8.place(x=x_cor,y=400)
btn9.place(x=x_cor,y=450)
'''

window.mainloop()
readT = readFile.read()