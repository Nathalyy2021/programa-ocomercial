import tkinter
import sqlite3
from contapaci4 import *
from formularios5 import *
from quart2 import *
from reserv3 import *
from formularios5 import *
from contapaci4 import *


import tkinter.messagebox


def menu():
  global root1,button1,button2,button3,button4,button5,button6

  root1=tkinter.Tk()
  root1.geometry("380x350")
  root1.title("Sistema clinica Estrela Guia: MENU ")
  m=tkinter.Label(root1,text="MENU",font='Times 14 bold',fg='black')

  button1 = tkinter.Button(root1,text="REGISTRAR PACIENTES ",bg='light blue',fg='black',command=PAT)
  button2 = tkinter.Button(root1,text="Nº QUARTO ",bg='light blue',fg='black',command=quarto)
  button3 = tkinter.Button(root1,text="RESERVAS ",bg='light blue',fg='black',command=reserva)
  button4 = tkinter.Button(root1,text="CONTA DO PACIENTE ",bg='light blue',fg='black',command=conta)
  button5 = tkinter.Button(root1,text="FUNCIONARIOS ",bg='light blue',fg='black',command=funcionarios)
     
  m.place(x=75,y=5)
  button1.pack(side=tkinter.TOP)
  button1.place(x=80,y=50)

  button2.pack(side=tkinter.TOP)
  button2.place(x=80,y=100)

  button3.pack(side=tkinter.TOP)
  button3.place(x=80,y=150)

  button4.pack(side=tkinter.TOP)
  button4.place(x=80,y=200)

  button5.pack(side=tkinter.TOP)
  button5.place(x=80,y=250)
  root1.mainloop()


def PAT():
  rootp=tkinter.Tk()
  rootp.geometry("420x510")
  rootp.title("FORMULARIO PACIENTES")
  regfrom=tkinter.Label(rootp,text="FORMULARIO PACIENTES",font="Times 14 bold",fg="black")

  id = tkinter.Label(rootp,text="ID PACIENTE: ",font="arial 8 bold",fg="black")
  pat_ID = tkinter.Entry(rootp,width=12)
  
  name = tkinter.Label(rootp,text="NOME PACIENTE: ",font="arial 8 bold",fg="black")
  pat_name = tkinter.Entry(rootp,width=50)
  
  sex = tkinter.Label(rootp,text="SEXO: ",font="arial 8 bold",fg="black")
  pat_sex = tkinter.Entry(rootp,width=12)

  dob = tkinter.Label(rootp,text="DATA NASC. (DD-MM-YYYY): ",font="arial 8 bold",fg="black")
  pat_dob = tkinter.Entry(rootp,width=26)

  id = tkinter.Label(rootp,text="ID PACIENTE: ",font="arial 8 bold",fg="black")
  pat_ID = tkinter.Entry(rootp,width=12)

  bg = tkinter.Label(rootp,text="GRUPO SANGUINEO: ",font="arial 8 bold",fg="black")
  pat_BG = tkinter.Entry(rootp,width=10)

  c1 = tkinter.Label(rootp,text="CELULAR: ",font="arial 8 bold",fg="black")
  pat_contact = tkinter.Entry(rootp,width=26)

  c2 = tkinter.Label(rootp,text="TELEFONE: ",font="arial 8 bold",fg="black")
  pat_contactalt = tkinter.Entry(rootp,width=26)

  email = tkinter.Label(rootp,text="EMAIL: ",font="arial 8 bold",fg="black")
  pat_email = tkinter.Entry(rootp,width=50)

  ct = tkinter.Label(rootp,text="EQUIPE ENFERMEIROS / DOUTOR: ",font="arial 8 bold",fg="black")
  pat_CT = tkinter.Entry(rootp,width=30)

  addr = tkinter.Label(rootp,text="ENDERECO: ",font="arial 8 bold",fg="black")
  pat_address = tkinter.Entry(rootp,width=50)
  
  button1 = tkinter.Button(rootp,text="SALVAR " ,bg='light blue',fg='black')
  button2 = tkinter.Button(rootp,text="SAIR " ,bg='light blue',fg='black')

  button1.pack(side=tkinter.TOP)
  button1.place(x=130,y=430)

  button2.pack(side=tkinter.TOP)
  button2.place(x=230,y=430)

  regfrom.pack()
  id.pack()
  pat_ID.pack()
  name.pack()
  pat_name.pack()
  sex.pack()
  pat_sex.pack()
  dob.pack()
  pat_dob.pack()
  bg.pack()
  pat_BG.pack()
  c1.pack()
  pat_contact.pack()
  c2.pack()
  pat_contactalt.pack()
  email.pack()
  pat_email.pack()
  ct.pack()
  pat_CT.pack()
  addr.pack()
  pat_address.pack()
  rootp.mainloop()
