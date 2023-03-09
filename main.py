from tkinter import *
import sqlite3
from sqlite3 import Error
import banco

def gravardados():
    if tb_nome.get() != '':
        vnome = tb_nome.get()
        vtel = tb_tel.get()
        vemail = tb_email.get()
        vquery = f'INSERT INTO tb_contatos(T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO) VALUES({vnome}, {vtel}, {vemail})'
        banco.dml(vquery)
        tb_nome.delete(0,END)
        tb_tel.delete(0, END)
        tb_email.delete(0, END)
        print('Dados Gravados')
    else:
        print('Erro')


app = Tk()
app.title('Cadastro de usários')
app.geometry('500x320')
app.configure(background='#000B1D')




text_nome = Label(app, text='Nome', background='#000B1D', foreground='#fff', anchor=W).place(x=10, y=10, width=100, height=20)
tb_nome = Entry(app)
tb_nome.place(x=10, y=30, width=200, height=20)

text_tel = Label(text='Telefone', background='#000B1D', foreground='#fff', anchor=W).place(x=10, y=60, width=100, height=20)
tb_tel = Entry(app)
tb_tel.place(x=10, y=80, width=100, height=20)

text_email = Label(app, text='E-mail', background='#000B1D', foreground='#fff', anchor=W).place(x=10, y=110, width=100, height=20)
tb_email = Entry(app)
tb_email.place(x=10, y=130, width=300, height=20)

Button(app, text='Cadastrar', background='#ff0', command=gravardados).place(x=10, y=270, width=100, height=25)

app.mainloop()