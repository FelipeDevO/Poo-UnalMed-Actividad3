from tkinter import *
from InterfazFunciones import ejerciciosInterfaces



def VentanaPrincipal():
    raiz=Tk()

    frame=Frame(raiz, width=1200, height=500)
    frame.pack()

    def EjerciciosInterfaz(ejer):
        raiz.destroy()
        ejerciciosInterfaces(ejer)
        VentanaPrincipal()

    Titulo=Label(frame,text="Ejercicios Actividad 3 ")
    Titulo.grid(row=0,column=0,columnspan=4,padx=12,pady=10)
    Titulo.configure(font=("Helvetica", 16,"bold"))
    #-----------Ejercicios Cap 3------------#
    Act1=Label(frame,text="Capitulo 3")
    Act1.grid(row=2,column=0,padx=8,pady=10)
    Act1.configure(font=("Helvetica ", 11,"bold"))


    boton1=Button(frame,text="Ejercicio 18",width=10,command=lambda:EjerciciosInterfaz("18"))
    boton1.grid(row=3,column=0,padx=12,pady=4)

    boton2=Button(frame,text="Ejercicio 19",width=10,command=lambda:EjerciciosInterfaz("19"))
    boton2.grid(row=4,column=0,padx=12,pady=4)

    #-----------Ejercicios Cap 4------------#
    Act2=Label(frame,text="Capitulo 4")
    Act2.grid(row=2,column=1,padx=12,pady=10)
    Act2.configure(font=("Helvetica ", 11,"bold"))

    boton3=Button(frame,text="Ejercicio 07",width=10,command=lambda:EjerciciosInterfaz("07"))
    boton3.grid(row=3,column=1,padx=12,pady=4)

    boton4=Button(frame,text="Ejercicio 10",width=10,command=lambda:EjerciciosInterfaz("10"))
    boton4.grid(row=4,column=1,padx=12,pady=4)

    boton5=Button(frame,text="Ejercicio 22",width=10,command=lambda:EjerciciosInterfaz("22"))
    boton5.grid(row=5,column=1,padx=12,pady=4)

    boton6=Button(frame,text="Ejercicio 23",width=10,command=lambda:EjerciciosInterfaz("23"))
    boton6.grid(row=6,column=1,padx=12,pady=4)

    #-----------Ejercicios Cap 5------------#

    Act3=Label(frame,text="Capitulo 5")
    Act3.grid(row=2,column=2,padx=12,pady=10)
    Act3.configure(font=("Helvetica", 11,"bold"))


    boton7=Button(frame,text="Ejercicio 40",width=10,command=lambda:EjerciciosInterfaz("40"))
    boton7.grid(row=3,column=2,padx=12,pady=4)

    boton8=Button(frame,text="Ejercicio 41",width=10,command=lambda:EjerciciosInterfaz("41"))
    boton8.grid(row=4,column=2,padx=12,pady=4)

    #-----------Ejercicios Clases Geometricas------------#

    actFig=Label(frame,text="Clases Figuras Geometricas")
    actFig.grid(row=7,column=0,padx=12,pady=10,columnspan=3)
    actFig.configure(font=("Helvetica",  11,"bold"))


    boton8=Button(frame,text="Ejercicio",width=30,command=lambda:EjerciciosInterfaz("figuras"))
    boton8.grid(row=8,column=0,padx=12,pady=4,columnspan=3)


    raiz.mainloop()

VentanaPrincipal()
