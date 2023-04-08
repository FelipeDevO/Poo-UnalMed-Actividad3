from tkinter import *
from Clases import *


def interfazFigura(ejer):
    if ejer=="Circulo":
        circulo()
        return
    if ejer=="Rectangulo":
        rectangulo()
        return
    if ejer=="Cuadrado":
        cuadrado()
        return
    if ejer=="Triangulo":
        triangulo()
        return
    if ejer=="Rombo":
        rombo()
        return
    if ejer=="Trapecio":
        trapecio()
        return

def circulo():
    raiz=Tk()

    frame=Frame(raiz, width=1200, height=500)
    frame.pack()

    def volver():
        raiz.destroy()
    def enviar():
        a=cuadroA.get()

        figuras=ejercicio_figuras()
        circulo=figuras.circulo(float(a))

        Titulo=Label(frame,text="Respuesta",fg="green")
        Titulo.grid(row=6,column=0,columnspan=4,padx=12,pady=10)
        Titulo.configure(font=("Helvetica", 16,"bold"))
        
        Act1=Label(frame,text="Area")
        Act1.grid(row=7,column=0,columnspan=2,padx=8,pady=10)
        Act1.configure(font=("Helvetica ", 12,"bold"))
        Act1=Label(frame,text="              "+str(circulo.Area())+"              ")
        Act1.grid(row=8,column=0,columnspan=2,padx=8,pady=10)
        Act1.configure(font=("Helvetica ", 10,))

        Act1=Label(frame,text="Perimetro")
        Act1.grid(row=7,column=2,columnspan=2,padx=8,pady=10)
        Act1.configure(font=("Perimetro ", 12,"bold"))
        Act1=Label(frame,text="              "+str(circulo.Perimetro())+"              ")
        Act1.grid(row=8,column=2,columnspan=2,padx=8,pady=10)
        Act1.configure(font=("Helvetica ", 10,))



    Titulo=Label(frame,text="Valores del Circulo")
    Titulo.grid(row=0,column=0,columnspan=4,padx=12,pady=10)
    Titulo.configure(font=("Helvetica", 16,"bold"))

    plant=Label(frame,text="En el siguiente ejercicio se debe introducir Radio del circulo")
    plant.grid(row=1,column=0,columnspan=4,padx=12,pady=2)
    plant=Label(frame,text="y se devolvera el valor del area y del perimetro")
    plant.grid(row=2,column=0,columnspan=4,padx=12,pady=2)

    textA=Label(frame,text="Radio del Circulo")
    textA.grid(row=3,column=0,padx=12,pady=10,columnspan=2)
    cuadroA=Entry(frame)
    cuadroA.grid(row=3,column=2,padx=12,pady=10,columnspan=2)


    botonEnviar=Button(frame,text="Enviar",width=10,command=enviar)
    botonEnviar.grid(row=4,column=3,padx=12,pady=4,columnspan=3)

    boton1=Button(frame,text="Regresar",width=10,command=volver)
    boton1.grid(row=9,column=0,padx=12,pady=4,sticky=SW)
    raiz.mainloop()

def rectangulo():
    raiz=Tk()

    frame=Frame(raiz, width=1200, height=500)
    frame.pack()

    def volver():
        raiz.destroy()
    def enviar():
        base=cuadroA.get()
        altura=cuadroB.get()


        figuras=ejercicio_figuras()
        rectangulo=figuras.rectangulo(float(base),float(altura))

        Titulo=Label(frame,text="Respuesta",fg="green")
        Titulo.grid(row=6,column=0,columnspan=4,padx=12,pady=10)
        Titulo.configure(font=("Helvetica", 16,"bold"))
        
        Act1=Label(frame,text="Area")
        Act1.grid(row=7,column=0,columnspan=2,padx=8,pady=10)
        Act1.configure(font=("Helvetica ", 12,"bold"))
        Act1=Label(frame,text="              "+str(rectangulo.Area())+"              ")
        Act1.grid(row=8,column=0,columnspan=2,padx=8,pady=10)
        Act1.configure(font=("Helvetica ", 10,))

        Act1=Label(frame,text="Perimetro")
        Act1.grid(row=7,column=2,columnspan=2,padx=8,pady=10)
        Act1.configure(font=("Perimetro ", 12,"bold"))
        Act1=Label(frame,text="              "+str(rectangulo.Perimetro())+"              ")
        Act1.grid(row=8,column=2,columnspan=2,padx=8,pady=10)
        Act1.configure(font=("Helvetica ", 10,))



    Titulo=Label(frame,text="Valores del Rectangulo")
    Titulo.grid(row=0,column=0,columnspan=4,padx=12,pady=10)
    Titulo.configure(font=("Helvetica", 16,"bold"))

    plant=Label(frame,text="En el siguiente ejercicio se debe introducir Base y Altura del Rectangulo")
    plant.grid(row=1,column=0,columnspan=4,padx=12,pady=2)
    plant=Label(frame,text="y se devolvera el valor del area y del perimetro")
    plant.grid(row=2,column=0,columnspan=4,padx=12,pady=2)

    textA=Label(frame,text="Base del rectangulo")
    textA.grid(row=3,column=0,padx=12,pady=10,columnspan=2)
    cuadroA=Entry(frame)
    cuadroA.grid(row=3,column=2,padx=12,pady=10,columnspan=2)

    textB=Label(frame,text="Altura del Rectangulo")
    textB.grid(row=4,column=0,padx=12,pady=10,columnspan=2)
    cuadroB=Entry(frame)
    cuadroB.grid(row=4,column=2,padx=12,pady=10,columnspan=2)

    botonEnviar=Button(frame,text="Enviar",width=10,command=enviar)
    botonEnviar.grid(row=5,column=3,padx=12,pady=4,columnspan=3)

    boton1=Button(frame,text="Regresar",width=10,command=volver)
    boton1.grid(row=9,column=0,padx=12,pady=4,sticky=SW)
    raiz.mainloop()

def cuadrado():
    raiz=Tk()

    frame=Frame(raiz, width=1200, height=500)
    frame.pack()

    def volver():
        raiz.destroy()
    def enviar():
        a=cuadroA.get()

        figuras=ejercicio_figuras()
        cuadrado=figuras.cuadrado(float(a))

        Titulo=Label(frame,text="Respuesta",fg="green")
        Titulo.grid(row=6,column=0,columnspan=4,padx=12,pady=10)
        Titulo.configure(font=("Helvetica", 16,"bold"))
        
        Act1=Label(frame,text="Area")
        Act1.grid(row=7,column=0,columnspan=2,padx=8,pady=10)
        Act1.configure(font=("Helvetica ", 12,"bold"))
        Act1=Label(frame,text="              "+str(cuadrado.Area())+"              ")
        Act1.grid(row=8,column=0,columnspan=2,padx=8,pady=10)
        Act1.configure(font=("Helvetica ", 10,))

        Act1=Label(frame,text="Perimetro")
        Act1.grid(row=7,column=2,columnspan=2,padx=8,pady=10)
        Act1.configure(font=("Perimetro ", 12,"bold"))
        Act1=Label(frame,text="              "+str(cuadrado.Perimetro())+"              ")
        Act1.grid(row=8,column=2,columnspan=2,padx=8,pady=10)
        Act1.configure(font=("Helvetica ", 10,))



    Titulo=Label(frame,text="Valores del Cuadrado")
    Titulo.grid(row=0,column=0,columnspan=4,padx=12,pady=10)
    Titulo.configure(font=("Helvetica", 16,"bold"))

    plant=Label(frame,text="En el siguiente ejercicio se debe introducir el lado del cuadrado")
    plant.grid(row=1,column=0,columnspan=4,padx=12,pady=2)
    plant=Label(frame,text="y se devolvera el valor del area y del perimetro")
    plant.grid(row=2,column=0,columnspan=4,padx=12,pady=2)

    textA=Label(frame,text="lado del Circulo")
    textA.grid(row=3,column=0,padx=12,pady=10,columnspan=2)
    cuadroA=Entry(frame)
    cuadroA.grid(row=3,column=2,padx=12,pady=10,columnspan=2)


    botonEnviar=Button(frame,text="Enviar",width=10,command=enviar)
    botonEnviar.grid(row=4,column=3,padx=12,pady=4,columnspan=3)

    boton1=Button(frame,text="Regresar",width=10,command=volver)
    boton1.grid(row=9,column=0,padx=12,pady=4,sticky=SW)
    raiz.mainloop()

def triangulo():
    raiz=Tk()

    frame=Frame(raiz, width=1200, height=500)
    frame.pack()

    def volver():
        raiz.destroy()
    def enviar():
        base=cuadroA.get()
        altura=cuadroB.get()


        figuras=ejercicio_figuras()
        triangulo=figuras.triangulo(float(base),float(altura))

        Titulo=Label(frame,text="Respuesta",fg="green")
        Titulo.grid(row=6,column=0,columnspan=4,padx=12,pady=10)
        Titulo.configure(font=("Helvetica", 16,"bold"))
        
        Act1=Label(frame,text="Area")
        Act1.grid(row=7,column=0,columnspan=1,padx=8,pady=10)
        Act1.configure(font=("Helvetica ", 12,"bold"))
        Act1=Label(frame,text="              "+str(triangulo.Area())+"              ")
        Act1.grid(row=8,column=0,columnspan=1,padx=8,pady=10)
        Act1.configure(font=("Helvetica ", 10,))

        Act1=Label(frame,text="Tipo de Triangulo")
        Act1.grid(row=7,column=1,columnspan=2,padx=8,pady=10)
        Act1.configure(font=("Helvetica ", 12,"bold"))
        Act1=Label(frame,text="              "+str(triangulo.TipoTriangulo())+"              ")
        Act1.grid(row=8,column=1,columnspan=2,padx=8,pady=10)
        Act1.configure(font=("Helvetica ", 10,))

        Act1=Label(frame,text="Perimetro")
        Act1.grid(row=7,column=3,columnspan=1,padx=8,pady=10)
        Act1.configure(font=("Helvetica ", 12,"bold"))
        Act1=Label(frame,text="              "+str(triangulo.Perimetro())+"              ")
        Act1.grid(row=8,column=3,columnspan=1,padx=8,pady=10)
        Act1.configure(font=("Helvetica ", 10,))

    Titulo=Label(frame,text="Valores del Triangulo")
    Titulo.grid(row=0,column=0,columnspan=4,padx=12,pady=10)
    Titulo.configure(font=("Helvetica", 16,"bold"))

    plant=Label(frame,text="En el siguiente ejercicio se debe introducir Base y Altura de un Triangulo Rectangulo")
    plant.grid(row=1,column=0,columnspan=4,padx=12,pady=2)
    plant=Label(frame,text="y se devolvera el valor del area, el perimetro y el tipo de triangulo")
    plant.grid(row=2,column=0,columnspan=4,padx=12,pady=2)

    textA=Label(frame,text="Base del Triangulo")
    textA.grid(row=3,column=0,padx=12,pady=10,columnspan=2)
    cuadroA=Entry(frame)
    cuadroA.grid(row=3,column=2,padx=12,pady=10,columnspan=2)

    textB=Label(frame,text="Altura del Triangulo")
    textB.grid(row=4,column=0,padx=12,pady=10,columnspan=2)
    cuadroB=Entry(frame)
    cuadroB.grid(row=4,column=2,padx=12,pady=10,columnspan=2)

    botonEnviar=Button(frame,text="Enviar",width=10,command=enviar)
    botonEnviar.grid(row=5,column=3,padx=12,pady=4,columnspan=3)

    boton1=Button(frame,text="Regresar",width=10,command=volver)
    boton1.grid(row=9,column=0,padx=12,pady=4,sticky=SW)
    raiz.mainloop()

def rombo():
    raiz=Tk()

    frame=Frame(raiz, width=1200, height=500)
    frame.pack()

    def volver():
        raiz.destroy()
    def enviar():
        ancho=cuadroA.get()
        largo=cuadroB.get()
        lado=cuadroC.get()

        figuras=ejercicio_figuras()
        rombo=figuras.rombo(float(lado),float(ancho),float(largo))

        Titulo=Label(frame,text="Respuesta",fg="green")
        Titulo.grid(row=6,column=0,columnspan=4,padx=12,pady=10)
        Titulo.configure(font=("Helvetica", 16,"bold"))
        
        Act1=Label(frame,text="Area")
        Act1.grid(row=7,column=0,columnspan=2,padx=8,pady=10)
        Act1.configure(font=("Helvetica ", 12,"bold"))
        Act1=Label(frame,text="              "+str(rombo.Area())+"              ")
        Act1.grid(row=8,column=0,columnspan=2,padx=8,pady=10)
        Act1.configure(font=("Helvetica ", 10,))

        Act1=Label(frame,text="Perimetro")
        Act1.grid(row=7,column=2,columnspan=2,padx=8,pady=10)
        Act1.configure(font=("Perimetro ", 12,"bold"))
        Act1=Label(frame,text="              "+str(rombo.Perimetro())+"              ")
        Act1.grid(row=8,column=2,columnspan=2,padx=8,pady=10)
        Act1.configure(font=("Helvetica ", 10,))



    Titulo=Label(frame,text="Valores del Rombo")
    Titulo.grid(row=0,column=0,columnspan=4,padx=12,pady=10)
    Titulo.configure(font=("Helvetica", 16,"bold"))

    plant=Label(frame,text="En el siguiente ejercicio se debe introducir Ancho, Largo y el lado de un Rombo")
    plant.grid(row=1,column=0,columnspan=4,padx=12,pady=2)
    plant=Label(frame,text="y se devolvera el valor del area y del perimetro")
    plant.grid(row=2,column=0,columnspan=4,padx=12,pady=2)

    textA=Label(frame,text="Ancho del Rombo")
    textA.grid(row=3,column=0,padx=12,pady=10,columnspan=2)
    cuadroA=Entry(frame)
    cuadroA.grid(row=3,column=2,padx=12,pady=10,columnspan=2)

    textB=Label(frame,text="Largo del Rombo")
    textB.grid(row=4,column=0,padx=12,pady=10,columnspan=2)
    cuadroB=Entry(frame)
    cuadroB.grid(row=4,column=2,padx=12,pady=10,columnspan=2)

    textC=Label(frame,text="Lado del Rombo")   
    textC.grid(row=5,column=0,padx=12,pady=10,columnspan=2)
    cuadroC=Entry(frame)
    cuadroC.grid(row=5,column=2,padx=12,pady=10,columnspan=2)

    botonEnviar=Button(frame,text="Enviar",width=10,command=enviar)
    botonEnviar.grid(row=6,column=3,padx=12,pady=4,columnspan=3)

    boton1=Button(frame,text="Regresar",width=10,command=volver)
    boton1.grid(row=15,column=0,padx=12,pady=4,sticky=SW)
    raiz.mainloop()

def trapecio():
    raiz=Tk()

    frame=Frame(raiz, width=1200, height=500)
    frame.pack()

    def volver():
        raiz.destroy()
    def enviar():
        base1=cuadroA.get()
        base2=cuadroB.get()
        lado=cuadroC.get()
        altura=cuadroD.get()

        figuras=ejercicio_figuras()
        trapecio=figuras.trapecio(float(lado),float(altura),float(base1),float(base2))

        Titulo=Label(frame,text="Respuesta",fg="green")
        Titulo.grid(row=8,column=0,columnspan=4,padx=12,pady=10)
        Titulo.configure(font=("Helvetica", 16,"bold"))
        
        Act1=Label(frame,text="Area")
        Act1.grid(row=9,column=0,columnspan=2,padx=8,pady=10)
        Act1.configure(font=("Helvetica ", 12,"bold"))
        Act1=Label(frame,text="              "+str(trapecio.Area())+"              ")
        Act1.grid(row=10,column=0,columnspan=2,padx=8,pady=10)
        Act1.configure(font=("Helvetica ", 10,))

        Act1=Label(frame,text="Perimetro")
        Act1.grid(row=9,column=2,columnspan=2,padx=8,pady=10)
        Act1.configure(font=("Perimetro ", 12,"bold"))
        Act1=Label(frame,text="              "+str(trapecio.Perimetro())+"              ")
        Act1.grid(row=10,column=2,columnspan=2,padx=8,pady=10)
        Act1.configure(font=("Helvetica ", 10,))



    Titulo=Label(frame,text="Valores del Trapecio")
    Titulo.grid(row=0,column=0,columnspan=4,padx=12,pady=10)
    Titulo.configure(font=("Helvetica", 16,"bold"))

    plant=Label(frame,text="En el siguiente ejercicio se debe introducir las 2 bases, la altura y el lado de un Trapecio")
    plant.grid(row=1,column=0,columnspan=4,padx=12,pady=2)
    plant=Label(frame,text="y se devolvera el valor del area y del perimetro")
    plant.grid(row=2,column=0,columnspan=4,padx=12,pady=2)

    textA=Label(frame,text="Base 1 del Trapecio")
    textA.grid(row=3,column=0,padx=12,pady=10,columnspan=2)
    cuadroA=Entry(frame)
    cuadroA.grid(row=3,column=2,padx=12,pady=10,columnspan=2)

    textB=Label(frame,text="Base 2 del Trapecio")
    textB.grid(row=4,column=0,padx=12,pady=10,columnspan=2)
    cuadroB=Entry(frame)
    cuadroB.grid(row=4,column=2,padx=12,pady=10,columnspan=2)

    textC=Label(frame,text="Lado del Trapecio")   
    textC.grid(row=5,column=0,padx=12,pady=10,columnspan=2)
    cuadroC=Entry(frame)
    cuadroC.grid(row=5,column=2,padx=12,pady=10,columnspan=2)

    textD=Label(frame,text="Altura del Trapecio")   
    textD.grid(row=6,column=0,padx=12,pady=10,columnspan=2)
    cuadroD=Entry(frame)
    cuadroD.grid(row=6,column=2,padx=12,pady=10,columnspan=2)

    botonEnviar=Button(frame,text="Enviar",width=10,command=enviar)
    botonEnviar.grid(row=7,column=3,padx=12,pady=4,columnspan=3)

    boton1=Button(frame,text="Regresar",width=10,command=volver)
    boton1.grid(row=15,column=0,padx=12,pady=4,sticky=SW)
    raiz.mainloop()
