import tkinter as tk
from tkinter import ttk
from tkinter import *
import PIL
from PIL import ImageTk, Image
from desc import *

BLACK = '#171717'

HEIGHT = 700
WIDTH = 900

root = tk.Tk()
root.title('WELCOME to my app ^_^')


def people(event):
    person = clicked.get()

    if person == option[0]:
        image = Image.open('image/bogd.jpg')
        basewidth = 370

        canvas2 = tk.Canvas(root, height=400, width=400, bg='#171717', bd=0, highlightthickness=0, relief='ridge')
        wpercent = (basewidth / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(wpercent)))
        image = image.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        item4 = canvas2.create_image(225, 210, image=photo)

        canvas2.place(relx=0.06, rely=0.15, relheight=0.6, relwidth=0.5)

        for widget in desc_frame.winfo_children():
            widget.destroy()

        for widget in fact_frame.winfo_children():
            widget.destroy()

        people_label = tk.Label(desc_frame, text=FULL_BOGDAN_DESC, font=('Franklin Gothic', 14), background='#ffba00',
                                fg='black')
        people_label.pack()

        people_fact = tk.Label(fact_frame, text=BOGDAN_FACT, font=('Franklin Gothic', 12), background='#ffba00',
                               fg='black')
        people_fact.pack()

        item4.pack()

    if person == option[1]:
        image = Image.open('image/zeland.jpeg')
        basewidth = 370

        canvas2 = tk.Canvas(root, height=400, width=400, bg='#171717', bd=0, highlightthickness=0, relief='ridge')
        wpercent = (basewidth / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(wpercent)))
        image = image.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        item4 = canvas2.create_image(225, 210, image=photo)

        canvas2.place(relx=0.06, rely=0.15, relheight=0.6, relwidth=0.5)

        for widget in desc_frame.winfo_children():
            widget.destroy()

        for widget in fact_frame.winfo_children():
            widget.destroy()

        people_label = tk.Label(desc_frame, text=ZELAND, font=('Franklin Gothic', 14), background='#ffba00',
                                fg='black')
        people_label.pack()

        people_fact = tk.Label(fact_frame, text=ZELAND_FACT, font=('Franklin Gothic', 12), background='#ffba00',
                               fg='black')
        people_fact.pack()

        item4.pack()



canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, background='#171717')
canvas.pack()

desc_frame = tk.Frame(root, background='#ffba00')
desc_frame.place(relx=0.6, rely=0.14, relheight=0.6, relwidth=0.37)

fact_frame = tk.Frame(root, background='#ffba00')
fact_frame.place(relx=0.15, rely=0.8, relheight=0.16, relwidth=0.7)

option = ['Bogdan Khmelnitsky', 'Volodymyr Zelenskiy']
clicked = StringVar()
clicked.set(option[0])
drop = OptionMenu(root, clicked, *option)
drop.config(background='#ffa812', fg=BLACK, font=('Franklin Gothic', 12))
drop.place(relx=0.04, rely=0.05, relheight=0.05, relwidth=0.24)

button = tk.Button(canvas, text='get info')
button.config(background='#ffa812', fg=BLACK, font=('Franklin Gothic', 12))
button.bind('<Button-1>', people)
button.place(relx=0.3, rely=0.05, relheight=0.05, relwidth=0.1)

text1 = 'Welcome to the Important \n Ukrainian People app! \n \n \n Choose a person to get started... ' \
        '\n \n \n  Project by Vladek'
text2 = 'Facts will show up in the box here!'

initial_label = tk.Label(desc_frame, text=text1, font=('Elephant', 16), background='#ffba00')
initial_label.pack()

initial_label2 = tk.Label(fact_frame, text=text2, font=('Elephant', 16), background='#ffba00')
initial_label2.pack(side='left')

mainloop()
