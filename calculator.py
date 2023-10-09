from tkinter import *

root=Tk()
root.title("Calculator")

e = Entry(root, width=50, borderwidth=5)
e.grid(row=0, column=0, columnspan=3)



def button_click(num):
	current=e.get()
	e.delete(0, END)
	e.insert(0, str(current)+ str(num))

def adding():
	first_number= e.get()
	e.delete(0, END)
	global f_num
	global operator
	operator="Adding"
	f_num= first_number
def dividing():
	first_number= e.get()
	e.delete(0, END)
	global f_num
	global operator
	operator="Dividing"
	f_num=first_number
def subtracting():
	first_number=e.get()
	e.delete(0, END)
	global f_num
	global operator
	operator="Subtracting"
	f_num=first_number
def mult():
	first_number=e.get()
	e.delete(0, END)
	global f_num
	global operator
	operator="Multiplying"
	f_num=first_number
def clearing():
	e.delete(0, END)
def equals():
	second_number= e.get()
	e.delete(0, END)
	if operator=="Adding":
		e.insert(0, int(f_num)+int(second_number))
	if operator=="Subtracting":
		e.insert(0, int(f_num)-int(second_number))
	if operator=="Dividing":
		e.insert(0, int(f_num)/int(second_number))
	if operator=="Multiplying":
		e.insert(0, int(f_num)*int(second_number))
button_1= Button(root,text ="1", padx=40, pady=20, command= lambda: button_click(1))
button_2= Button(root,text ="2", padx=40, pady=20, command= lambda: button_click(2))
button_3= Button(root,text ="3", padx=40, pady=20, command= lambda: button_click(3))
button_4= Button(root,text ="4", padx=40, pady=20, command= lambda: button_click(4))
button_5= Button(root,text ="5", padx=40, pady=20, command= lambda: button_click(5))
button_6= Button(root,text ="6", padx=40, pady=20, command= lambda: button_click(6))
button_7= Button(root,text ="7", padx=40, pady=20, command= lambda: button_click(7))
button_8= Button(root,text ="8", padx=40, pady=20, command= lambda: button_click(8))
button_9= Button(root,text ="9", padx=40, pady=20, command= lambda: button_click(9))
button_0= Button(root,text ="0", padx=40, pady=20, command= lambda: button_click(0))
button_add= Button(root,text ="+", padx=40, pady=20, command= adding)
button_mul= Button(root,text ="*", padx=40, pady=20, command= mult)
button_sub= Button(root,text ="-", padx=40, pady=20, command= subtracting)
button_div= Button(root,text ="/", padx=40, pady=20, command= dividing)
button_eq= Button(root,text ="=", padx=40, pady=20, command= equals)
button_clear= Button(root,text ="Clear", padx=40, pady=20, command= clearing)

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_0.grid(row=4, column=0)
button_add.grid(row=4, column=1)
button_sub.grid(row=4, column=2)
button_div.grid(row=5, column=0)
button_mul.grid(row=5, column=1)
button_eq.grid(row=5, column=2)
button_clear.grid(row=6, column=0)

root.mainloop()