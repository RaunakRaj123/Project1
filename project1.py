import imp
import PIL
import tkinter
from tkinter import *
from PIL import Image
from tkinter.filedialog import*
from tkinter import messagebox

root = tkinter.Tk()
root.geometry('380x350')
root.config(bg = 'light blue')

def file_convrt():
    file_path=askopenfilename()
    img=PIL.Image.open(file_path)
    myHeight, myWidth =img.size

    img=img.resize((myHeight,myWidth) ,PIL.Image.ANTIALIAS)
    save_path=asksaveasfilename()

    img.save(save_path+" compressed.JPG")
    messagebox.showinfo('Message', 'Your image has compressed')


label_1 = Label(root, text='IMAGE COMPRESSOR', font=('Berlin Sans FB', 19), bg = 'light blue').place(x = 70, y = 100)
button = Button(root, text='Select File', font=(15), borderwidth=6, bg='grey', fg = 'white', command=file_convrt)
button.place(x = 130, y = 180)


root.mainloop()