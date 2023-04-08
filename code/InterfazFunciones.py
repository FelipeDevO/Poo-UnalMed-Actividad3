from tkinter import *
from Clases import *
from InterfazesFiguras import *

def ejerciciosInterfaces(ejer):
    if ejer=="18":
        Interejercicio18()
        return
    if ejer=="19":
        Interejercicio19()
        return
    if ejer=="07":
        Interejercicio07()
        return
    if ejer=="10":
        Interejercicio10()
        return
    if ejer=="22":
        Interejercicio22()
        return
    if ejer=="23":
        Interejercicio23()
        return
    if ejer=="40":
        Interejercicio40()
        return
    if ejer=="41":
        Interejercicio41()
        return
    if ejer=="figuras":
        InterejercicioClases()


def Interejercicio18():
    raiz=Tk()

    frame=Frame(raiz, width=1200, height=500)
    frame.pack()

    def volver():
        raiz.destroy()

    def enviar():
        codigo=cuadroCodigo.get()
        nombre=cuadroNombre.get()
        horas=cuadroHoras.get()
        valor=cuadroValor.get()
        porcentaje=cuadroPorcentaje.get()

        datos=ejercicio_18(int(codigo),nombre,int(horas),int(valor),float(porcentaje))
        info=datos.salarioEmpleado()

        Titulo=Label(frame,text="Respuesta",fg="green")
        Titulo.grid(row=6,column=0,columnspan=4,padx=12,pady=10)
        Titulo.configure(font=("Helvetica", 16,"bold"))
        
        Act1=Label(frame,text="Codigo")
        Act1.grid(row=7,column=0,padx=8,pady=10)
        Act1.configure(font=("Helvetica ", 12,"bold"))
        Act1=Label(frame,text=codigo)
        Act1.grid(row=8,column=0,padx=8,pady=10)
        Act1.configure(font=("Helvetica ", 10,))

        Act1=Label(frame,text="Nombre")
        Act1.grid(row=7,column=1,padx=8,pady=10)
        Act1.configure(font=("Helvetica ", 12,"bold"))
        Act1=Label(frame,text=nombre)
        Act1.grid(row=8,column=1,padx=8,pady=10)
        Act1.configure(font=("Helvetica ", 10,))

        Act1=Label(frame,text="Salario Bruto")
        Act1.grid(row=7,column=2,padx=8,pady=10)
        Act1.configure(font=("Helvetica ", 12,"bold"))
        Act1=Label(frame,text=info["salarioBruto"])
        Act1.grid(row=8,column=2,padx=8,pady=10)
        Act1.configure(font=("Helvetica ", 10,))

        Act1=Label(frame,text="Salario Neto")
        Act1.grid(row=7,column=3,padx=8,pady=10)
        Act1.configure(font=("Helvetica ", 12,"bold"))
        Act1=Label(frame,text=int(info["salarioNeto"]))
        Act1.grid(row=8,column=3,padx=8,pady=10)
        Act1.configure(font=("Helvetica ", 10,))


    Titulo=Label(frame,text="Ejercicio Actividad 18 ")
    Titulo.grid(row=0,column=0,columnspan=4,padx=12,pady=10)
    Titulo.configure(font=("Helvetica", 16,"bold"))

    plant=Label(frame,text="En el siguiente ejercicio se debe introducir la informacion solicitada del empleado")
    plant.grid(row=1,column=0,columnspan=4,padx=12,pady=2)
    plant=Label(frame,text="y se retornara el codigo, nombre, salario bruto y salario neto ")
    plant.grid(row=2,column=0,columnspan=4,padx=12,pady=2)

    textCodigo=Label(frame,text="Codigo Del Empleado")
    textCodigo.grid(row=3,column=0,padx=12,pady=10)
    cuadroCodigo=Entry(frame)
    cuadroCodigo.grid(row=3,column=1,padx=12,pady=10)
    
    textNombre=Label(frame,text="Nombre")
    textNombre.grid(row=3,column=2,padx=12,pady=10)
    cuadroNombre=Entry(frame)
    cuadroNombre.grid(row=3,column=3,padx=12,pady=10)

    textHoras=Label(frame,text="Horas trabajadas al mes")
    textHoras.grid(row=4,column=0,padx=12,pady=10)
    cuadroHoras=Entry(frame)
    cuadroHoras.grid(row=4,column=1,padx=12,pady=10)

    textValor=Label(frame,text="Valor por hora trabajada")
    textValor.grid(row=4,column=2,padx=12,pady=10)
    cuadroValor=Entry(frame)
    cuadroValor.grid(row=4,column=3,padx=12,pady=10)

    textPorcentaje=Label(frame,text="Porcentaje de retencion en la fuente")
    textPorcentaje.grid(row=5,column=0,padx=12,pady=10)
    cuadroPorcentaje=Entry(frame)
    cuadroPorcentaje.grid(row=5,column=1,padx=12,pady=10)

    botonEnviar=Button(frame,text="Enviar",width=20,command=enviar)
    botonEnviar.grid(row=5,column=2,padx=12,pady=4,columnspan=2)

    boton1=Button(frame,text="Regresar",width=10,command=volver)
    boton1.grid(row=9,column=0,padx=12,pady=4,sticky=SW)
    raiz.mainloop()

def Interejercicio19():
    raiz=Tk()

    frame=Frame(raiz, width=1200, height=500)
    frame.pack()

    def volver():
        raiz.destroy()
    
    def enviar():
        lado=cuadroLado.get()

        datos=ejercicio_19(float(lado))
        area=datos.Area()
        altura=datos.Altura()
        perimetro=datos.Perimetro()

        Titulo=Label(frame,text="Respuesta",fg="green")
        Titulo.grid(row=6,column=0,columnspan=4,padx=12,pady=10)
        Titulo.configure(font=("Helvetica", 16,"bold"))
        
        Act1=Label(frame,text="Area")
        Act1.grid(row=7,column=0,padx=8,pady=10)
        Act1.configure(font=("Helvetica ", 12,"bold"))
        Act1=Label(frame,text=area)
        Act1.grid(row=8,column=0,padx=8,pady=10)
        Act1.configure(font=("Helvetica ", 10,))

        Act1=Label(frame,text="Altura")
        Act1.grid(row=7,column=1,padx=8,pady=10)
        Act1.configure(font=("Helvetica ", 12,"bold"))
        Act1=Label(frame,text=altura)
        Act1.grid(row=8,column=1,padx=8,pady=10)
        Act1.configure(font=("Helvetica ", 10,))

        Act1=Label(frame,text="Perimetro")
        Act1.grid(row=7,column=2,padx=8,pady=10)
        Act1.configure(font=("Helvetica ", 12,"bold"))
        Act1=Label(frame,text=perimetro)
        Act1.grid(row=8,column=2,padx=8,pady=10)
        Act1.configure(font=("Helvetica ", 10,))

    Titulo=Label(frame,text="Ejercicio Actividad 19 ")
    Titulo.grid(row=0,column=0,columnspan=3,padx=12,pady=10)
    Titulo.configure(font=("Helvetica", 16,"bold"))

    plant=Label(frame,text="En el siguiente ejercicio se debe introducir el valor de un lado de un triangulo equilatero")
    plant.grid(row=1,column=0,columnspan=3,padx=12,pady=2)
    plant=Label(frame,text="y se retornara el area, la altura, y el perimetro del triangulo ")
    plant.grid(row=2,column=0,columnspan=3,padx=12,pady=2)

    textLado=Label(frame,text="Lado del triangulo")
    textLado.grid(row=3,column=0,columnspan=3,padx=12,pady=5)
    textLado.configure(font=("Helvetica", 12,"bold"))

    cuadroLado=Entry(frame)
    cuadroLado.grid(row=4,column=0,columnspan=3,padx=12,pady=10)

    botonEnviar=Button(frame,text="Enviar",width=20,command=enviar)
    botonEnviar.grid(row=5,column=0,padx=12,pady=4,columnspan=3)


    boton1=Button(frame,text="Regresar",width=10,command=volver)
    boton1.grid(row=9,column=0,padx=12,pady=4,sticky=SW)
    raiz.mainloop()

def Interejercicio07():
    raiz=Tk()

    frame=Frame(raiz, width=1200, height=500)
    frame.pack()

    def volver():
        raiz.destroy()
    def enviar():
        a=cuadroA.get()
        b=cuadroB.get()

        datos=ejercicio_7(int(a),int(b))
        mensaje=datos.desicion()

        Titulo=Label(frame,text="Respuesta",fg="green")
        Titulo.grid(row=6,column=0,columnspan=4,padx=12,pady=10)
        Titulo.configure(font=("Helvetica", 16,"bold"))
        
        Act1=Label(frame,text="Mensaje")
        Act1.grid(row=7,column=0,padx=8,columnspan=4,pady=10)
        Act1.configure(font=("Helvetica ", 12,"bold"))
        Act1=Label(frame,text=mensaje)
        Act1.grid(row=8,column=0,padx=8,pady=10,columnspan=4)
        Act1.configure(font=("Helvetica ", 10,))



    Titulo=Label(frame,text="Ejercicio Actividad 07 ")
    Titulo.grid(row=0,column=0,columnspan=4,padx=12,pady=10)
    Titulo.configure(font=("Helvetica", 16,"bold"))

    plant=Label(frame,text="En el siguiente ejercicio se debe introducir dos valores numericos")
    plant.grid(row=1,column=0,columnspan=4,padx=12,pady=2)
    plant=Label(frame,text="y se un mensaje diciendo si A es mayor,menor o igual que B")
    plant.grid(row=2,column=0,columnspan=4,padx=12,pady=2)

    textA=Label(frame,text="Valor de A")
    textA.grid(row=3,column=0,padx=12,pady=10)
    cuadroA=Entry(frame)
    cuadroA.grid(row=3,column=1,padx=12,pady=10)
    
    textB=Label(frame,text="Valor de B")
    textB.grid(row=3,column=2,padx=12,pady=10)
    cuadroB=Entry(frame)
    cuadroB.grid(row=3,column=3,padx=12,pady=10)

    botonEnviar=Button(frame,text="Enviar",width=10,command=enviar)
    botonEnviar.grid(row=4,column=3,padx=12,pady=4,columnspan=3)

    boton1=Button(frame,text="Regresar",width=10,command=volver)
    boton1.grid(row=9,column=0,padx=12,pady=4,sticky=SW)
    raiz.mainloop()

def Interejercicio10():
    raiz=Tk()

    frame=Frame(raiz, width=1200, height=500)
    frame.pack()

    def volver():
        raiz.destroy()
    def enviar():
        inscripcion=cuadroNum.get()
        nombre=cuadroNombre.get()
        patrimonio=cuadroPatr.get()
        estrato=cuadroEstrato.get()

        datos=ejercicio_10(inscripcion,nombre,int(patrimonio),int(estrato))
        total=datos.pago()

        Titulo=Label(frame,text="Respuesta",fg="green")
        Titulo.grid(row=6,column=0,columnspan=4,padx=12,pady=10)
        Titulo.configure(font=("Helvetica", 16,"bold"))
        
        Act1=Label(frame,text="Inscripcion")
        Act1.grid(row=7,column=0,padx=8,pady=10)
        Act1.configure(font=("Helvetica ", 12,"bold"))
        Act1=Label(frame,text=inscripcion)
        Act1.grid(row=8,column=0,padx=8,pady=10)
        Act1.configure(font=("Helvetica ", 10,))

        Act1=Label(frame,text="Nombre")
        Act1.grid(row=7,column=1,padx=8,pady=10)
        Act1.configure(font=("Helvetica ", 12,"bold"))
        Act1=Label(frame,text=nombre)
        Act1.grid(row=8,column=1,padx=8,pady=10)
        Act1.configure(font=("Helvetica ", 10,))

        Act1=Label(frame,text="Patrimonio")
        Act1.grid(row=7,column=2,padx=8,pady=10)
        Act1.configure(font=("Helvetica ", 12,"bold"))
        Act1=Label(frame,text=patrimonio)
        Act1.grid(row=8,column=2,padx=8,pady=10)
        Act1.configure(font=("Helvetica ", 10,))

        Act1=Label(frame,text="Pago Total")
        Act1.grid(row=7,column=3,padx=8,pady=10)
        Act1.configure(font=("Helvetica ", 12,"bold"))
        Act1=Label(frame,text=int(total))
        Act1.grid(row=8,column=3,padx=8,pady=10)
        Act1.configure(font=("Helvetica ", 10,))


    Titulo=Label(frame,text="Ejercicio Actividad 10 ")
    Titulo.grid(row=0,column=0,columnspan=4,padx=12,pady=10)
    Titulo.configure(font=("Helvetica", 16,"bold"))

    plant=Label(frame,text="En el siguiente ejercicio se debe introducir la informacion socioeconomica de un estudiante")
    plant.grid(row=1,column=0,columnspan=4,padx=12,pady=2)
    plant=Label(frame,text="y se retornara el valor que debe pagar el estudiante de su matricula ")
    plant.grid(row=2,column=0,columnspan=4,padx=12,pady=2)

    textNum=Label(frame,text="Numero de Inscripcion")
    textNum.grid(row=3,column=0,padx=12,pady=10)
    cuadroNum=Entry(frame)
    cuadroNum.grid(row=3,column=1,padx=12,pady=10)
    
    textNombre=Label(frame,text="Nombre")
    textNombre.grid(row=3,column=2,padx=12,pady=10)
    cuadroNombre=Entry(frame)
    cuadroNombre.grid(row=3,column=3,padx=12,pady=10)

    textPatr=Label(frame,text="Patrimonio")
    textPatr.grid(row=4,column=0,padx=12,pady=10)
    cuadroPatr=Entry(frame)
    cuadroPatr.grid(row=4,column=1,padx=12,pady=10)

    textEstrato=Label(frame,text="Estrato Social")
    textEstrato.grid(row=4,column=2,padx=12,pady=10)
    cuadroEstrato=Entry(frame)
    cuadroEstrato.grid(row=4,column=3,padx=12,pady=10)


    botonEnviar=Button(frame,text="Enviar",width=10,command=enviar)
    botonEnviar.grid(row=5,column=3,padx=12,pady=4,columnspan=3)


    boton1=Button(frame,text="Regresar",width=10,command=volver)
    boton1.grid(row=9,column=0,padx=12,pady=4,sticky=SW)
    raiz.mainloop()

def Interejercicio22():
    raiz=Tk()

    frame=Frame(raiz, width=1200, height=500)
    frame.pack()

    cont=0

    def volver():
        raiz.destroy()

    def enviar():

        nombre=cuadroNombre.get()
        horas=cuadroHoras.get()
        salario=cuadroSalario.get()

        datos=ejercicio_22(nombre,int(salario),int(horas))
        total=datos.pago()
        if total:
            Titulo=Label(frame,text="Respuesta",fg="green")
            Titulo.grid(row=5,column=0,columnspan=4,padx=12,pady=10)
            Titulo.configure(font=("Helvetica", 16,"bold"))

            Act1=Label(frame,text="Nombre")
            Act1.grid(row=6,column=1,padx=8,pady=10)
            Act1.configure(font=("Helvetica ", 12,"bold"))
            Act1=Label(frame,text=nombre)
            Act1.grid(row=7,column=1,padx=8,pady=10)
            Act1.configure(font=("Helvetica ", 10,))

            Act1=Label(frame,text="Salario Mensual")
            Act1.grid(row=6,column=2,padx=8,pady=10)
            Act1.configure(font=("Helvetica ", 12,"bold"))
            Act1=Label(frame,text="         "+str(total)+"         ")
            Act1.grid(row=7,column=2,padx=8,pady=10)
            Act1.configure(font=("Helvetica ", 10,))
        
        else:
            Titulo=Label(frame,text="Respuesta",fg="green")
            Titulo.grid(row=5,column=0,columnspan=4,padx=12,pady=10)
            Titulo.configure(font=("Helvetica", 16,"bold"))

            Act1=Label(frame,text="Nombre")
            Act1.grid(row=6,column=1,padx=8,pady=10)
            Act1.configure(font=("Helvetica ", 12,"bold"))
            Act1=Label(frame,text=nombre)
            Act1.grid(row=7,column=1,padx=8,pady=10)
            Act1.configure(font=("Helvetica ", 10,))

            Act1=Label(frame,text="Salario Mensual")
            Act1.grid(row=6,column=2,padx=8,pady=10)
            Act1.configure(font=("Helvetica ", 12,"bold"))
            Act1=Label(frame,text="No habil para mostrar")
            Act1.grid(row=7,column=2,padx=8,pady=10)
            Act1.configure(font=("Helvetica ", 10,))

        # Titulo=Label(frame,text="Respuesta",fg="green")
        # Titulo.grid(row=6,column=0,columnspan=4,padx=12,pady=10)
        # Titulo.configure(font=("Helvetica", 16,"bold"))
        
        # Act1=Label(frame,text="Inscripcion")
        # Act1.grid(row=7,column=0,padx=8,pady=10)
        # Act1.configure(font=("Helvetica ", 12,"bold"))
        # Act1=Label(frame,text=inscripcion)
        # Act1.grid(row=8,column=0,padx=8,pady=10)
        # Act1.configure(font=("Helvetica ", 10,))

        # Act1=Label(frame,text="Nombre")
        # Act1.grid(row=7,column=1,padx=8,pady=10)
        # Act1.configure(font=("Helvetica ", 12,"bold"))
        # Act1=Label(frame,text=nombre)
        # Act1.grid(row=8,column=1,padx=8,pady=10)
        # Act1.configure(font=("Helvetica ", 10,))

        # Act1=Label(frame,text="Patrimonio")
        # Act1.grid(row=7,column=2,padx=8,pady=10)
        # Act1.configure(font=("Helvetica ", 12,"bold"))
        # Act1=Label(frame,text=patrimonio)
        # Act1.grid(row=8,column=2,padx=8,pady=10)
        # Act1.configure(font=("Helvetica ", 10,))

    
    Titulo=Label(frame,text="Ejercicio Actividad 22 ")
    Titulo.grid(row=0,column=0,columnspan=4,padx=12,pady=10)
    Titulo.configure(font=("Helvetica", 16,"bold"))

    plant=Label(frame,text="En el siguiente ejercicio se debe introducir la informacion  de un empleado")
    plant.grid(row=1,column=0,columnspan=4,padx=12,pady=2)
    plant=Label(frame,text="y se retornara el nombre y salario mensual sie ste es mayor a 450000, si no lo es, solo se mostrara el nombre ")
    plant.grid(row=2,column=0,columnspan=4,padx=12,pady=2)

    textNombre=Label(frame,text="Nombre del Empleado")
    textNombre.grid(row=3,column=0,padx=12,pady=10)
    cuadroNombre=Entry(frame)
    cuadroNombre.grid(row=3,column=1,padx=12,pady=10)
    
    textSalario=Label(frame,text="Salario Basico por Hora")
    textSalario.grid(row=3,column=2,padx=12,pady=10)
    cuadroSalario=Entry(frame)
    cuadroSalario.grid(row=3,column=3,padx=12,pady=10)

    textHoras=Label(frame,text="Horas trabjadas en el Mes")
    textHoras.grid(row=4,column=0,padx=12,pady=10)
    cuadroHoras=Entry(frame)
    cuadroHoras.grid(row=4,column=1,padx=12,pady=10)


    botonEnviar=Button(frame,text="Enviar",width=10,command=enviar)
    botonEnviar.grid(row=4,column=3,padx=12,pady=4,columnspan=3)


    boton1=Button(frame,text="Regresar",width=10,command=volver)
    boton1.grid(row=9,column=0,padx=12,pady=4,sticky=SW)

    raiz.mainloop()

def Interejercicio23():
    raiz=Tk()

    frame=Frame(raiz, width=1200, height=500)
    frame.pack()

    def volver():
        raiz.destroy()

    def enviar():
        Va=cuadroA.get()
        Vb=cuadroB.get()
        Vc=cuadroC.get()

        datos=ejercicio_23(float(Va),float(Vb),float(Vc))
        total=datos.solucion()

        Titulo=Label(frame,text="Respuesta",fg="green")
        Titulo.grid(row=6,column=0,columnspan=4,padx=12,pady=10)
        Titulo.configure(font=("Helvetica", 16,"bold"))

        Act1=Label(frame,text="Valor 1")
        Act1.grid(row=7,column=1,padx=8,pady=10)
        Act1.configure(font=("Helvetica ", 12,"bold"))
        Act1=Label(frame,text="         "+str(total["valor1"])+"         ")
        Act1.grid(row=8,column=1,padx=8,pady=10)
        Act1.configure(font=("Helvetica ", 10,))

        Act1=Label(frame,text="Valor 2")
        Act1.grid(row=7,column=2,padx=8,pady=10)
        Act1.configure(font=("Helvetica ", 12,"bold"))
        Act1=Label(frame,text="         "+str(total["valor2"])+"         ")
        Act1.grid(row=8,column=2,padx=8,pady=10)
        Act1.configure(font=("Helvetica ", 10,))
        
    

    Titulo=Label(frame,text="Ejercicio Actividad 23 ")
    Titulo.grid(row=0,column=0,columnspan=4,padx=12,pady=10)
    Titulo.configure(font=("Helvetica", 16,"bold"))

    
    plant=Label(frame,text="En el siguiente ejercicio se debe introducir los los parametros de la ecuacion AX^2+BX+C")
    plant.grid(row=1,column=0,columnspan=4,padx=12,pady=2)
    plant=Label(frame,text="y se retornara las posibles soluciones a la ecuacion cuadratica ")
    plant.grid(row=2,column=0,columnspan=4,padx=12,pady=2)

    textA=Label(frame,text="Valor de A")
    textA.grid(row=3,column=0,padx=12,pady=10)
    cuadroA=Entry(frame)
    cuadroA.grid(row=3,column=1,padx=12,pady=10)
    
    textB=Label(frame,text="Valor de B")
    textB.grid(row=3,column=2,padx=12,pady=10)
    cuadroB=Entry(frame)
    cuadroB.grid(row=3,column=3,padx=12,pady=10)

    textC=Label(frame,text="Valor de C")
    textC.grid(row=4,column=0,padx=12,pady=10)
    cuadroC=Entry(frame)
    cuadroC.grid(row=4,column=1,padx=12,pady=10)

    botonEnviar=Button(frame,text="Enviar",width=20,command=enviar)
    botonEnviar.grid(row=4,column=2,padx=12,pady=4,columnspan=2)

    boton1=Button(frame,text="Regresar",width=10,command=volver)
    boton1.grid(row=9,column=0,padx=12,pady=4)
    raiz.mainloop()

def Interejercicio40():
    raiz=Tk()

    listaNum=StringVar()
    reset=StringVar()
    listaNormal=[]

    frame=Frame(raiz, width=1200, height=500)
    frame.pack()
    
    def volver():
        raiz.destroy()

    def add(num):
        listaNum.set(listaNum.get()+str(num)+",")
        listaNormal.append(int(num))
        print(listaNormal)
        reset.set("")

    def enviar(listaNormal):
        datos=ejercicio_40(listaNormal)
        operaciones=datos.solucion()

        cubos=operaciones["cubos"]
        raicez=operaciones["raicez"]
        cuadrados=operaciones["cuadrados"]
        
        Titulo=Label(frame,text="Respuesta",fg="green")
        Titulo.grid(row=7,column=0,columnspan=4,padx=12,pady=10)
        Titulo.configure(font=("Helvetica", 16,"bold"))

        plant=Label(frame,text="Cuadrados")
        plant.grid(row=8,column=1,padx=12,pady=2)
        plant=Label(frame,text="Cubos")
        plant.grid(row=8,column=2,padx=12,pady=2)
        plant=Label(frame,text="Raicez")
        plant.grid(row=8,column=3,padx=12,pady=2)
        
        fila=9

        for i in range(len(listaNormal)):
            plant=Label(frame,text=listaNormal[i])
            plant.grid(row=fila,column=0,padx=12,pady=2)

            plant=Label(frame,text=cuadrados[i])
            plant.grid(row=fila,column=1,padx=12,pady=2)

            plant=Label(frame,text=cubos[i])
            plant.grid(row=fila,column=2,padx=12,pady=2)

            plant=Label(frame,text=raicez[i])
            plant.grid(row=fila,column=3,padx=12,pady=2)
            fila+=1


    Titulo=Label(frame,text="Ejercicio Actividad 40 ")
    Titulo.grid(row=0,column=0,columnspan=4,padx=12,pady=10)
    Titulo.configure(font=("Helvetica", 16,"bold"))


    plant=Label(frame,text="En el siguiente ejercicio se debe introducir una lista de numeros")
    plant.grid(row=1,column=0,columnspan=4,padx=12,pady=2)
    plant=Label(frame,text="y se retornara la raiz cuadrada, el cuadrado, y el cubo de cada numero ")
    plant.grid(row=2,column=0,columnspan=4,padx=12,pady=2)

    plant=Label(frame,text="Lista de numeros:")
    plant.grid(row=3,column=0,columnspan=4,padx=12,pady=2)
    plantList=Label(frame,textvariable=listaNum)
    plantList.grid(row=4,column=0,columnspan=4,padx=12,pady=2)

    textA=Label(frame,text="Numero a añadir a la lista")
    textA.grid(row=5,column=0,padx=12,pady=10)
    cuadroA=Entry(frame,textvariable=reset)
    cuadroA.grid(row=5,column=1,padx=12,pady=10)
    boton1=Button(frame,text="Añadir",width=10,command=lambda:add(cuadroA.get()))
    boton1.grid(row=5,column=2,padx=12,pady=4)

    boton1=Button(frame,text="Enviar",width=10,command=lambda:enviar(listaNormal))
    boton1.grid(row=6,column=0,padx=12,pady=4)

    boton1=Button(frame,text="Regresar",width=10,command=volver)
    boton1.grid(row=99,column=0,padx=12,pady=4)

    raiz.mainloop()

def Interejercicio41():
    raiz=Tk()

    listaNum=StringVar()
    reset=StringVar()
    listaNormal=[]

    frame=Frame(raiz, width=1200, height=500)
    frame.pack()
    
    def volver():
        raiz.destroy()

    def add(num):
        listaNum.set(listaNum.get()+str(num)+",")
        listaNormal.append(int(num))
        print(listaNormal)
        reset.set("")

    def enviar(listaNormal):
            datos=ejercicio_41(listaNormal)
            operaciones=datos.solucion()

            Titulo=Label(frame,text="Respuesta",fg="green")
            Titulo.grid(row=7,column=0,columnspan=4,padx=12,pady=10)
            Titulo.configure(font=("Helvetica", 16,"bold"))

            plant=Label(frame,text="El numero mayor de la lista es")
            plant.grid(row=8,column=0,columnspan=2,padx=12,pady=2)
            plant1=Label(frame,text=operaciones)
            plant1.grid(row=8,column=2,padx=12,pady=2,sticky=W)  
            plant1.configure(font=("Helvetica", 14,"bold"))
  


    Titulo=Label(frame,text="Ejercicio Actividad 41 ")
    Titulo.grid(row=0,column=0,columnspan=4,padx=12,pady=10)
    Titulo.configure(font=("Helvetica", 16,"bold"))


    plant=Label(frame,text="En el siguiente ejercicio se debe introducir una lista de numeros")
    plant.grid(row=1,column=0,columnspan=4,padx=12,pady=2)
    plant=Label(frame,text="y se retornara el numero mayor entre todos")
    plant.grid(row=2,column=0,columnspan=4,padx=12,pady=2)

    plant=Label(frame,text="Lista de numeros:")
    plant.grid(row=3,column=0,columnspan=4,padx=12,pady=2)
    plantList=Label(frame,textvariable=listaNum)
    plantList.grid(row=4,column=0,columnspan=4,padx=12,pady=2)

    textA=Label(frame,text="Numero a añadir a la lista")
    textA.grid(row=5,column=0,padx=12,pady=10)
    cuadroA=Entry(frame,textvariable=reset)
    cuadroA.grid(row=5,column=1,padx=12,pady=10)
    boton1=Button(frame,text="Añadir",width=10,command=lambda:add(cuadroA.get()))
    boton1.grid(row=5,column=2,padx=12,pady=4)

    boton1=Button(frame,text="Enviar",width=10,command=lambda:enviar(listaNormal))
    boton1.grid(row=6,column=0,padx=12,pady=4)

    boton1=Button(frame,text="Regresar",width=10,command=volver)
    boton1.grid(row=99,column=0,padx=12,pady=4)

    raiz.mainloop()

def InterejercicioClases():
    raiz=Tk()

    frame=Frame(raiz, width=1200, height=500)
    frame.pack()

    def volver():
        raiz.destroy()
    
    def EjerciciosInterfaz(ejer):
        raiz.destroy()
        interfazFigura(ejer)
        InterejercicioClases()

    Titulo=Label(frame,text="Ejercicio Actividad Clases Geometricas ")
    Titulo.grid(row=0,column=0,columnspan=4,padx=12,pady=10)
    Titulo.configure(font=("Helvetica", 16,"bold"))

    plant=Label(frame,text="En el siguiente ejercicio se debe elegir una de las figuras geometricas")
    plant.grid(row=1,column=0,columnspan=4,padx=12,pady=2)
    plant=Label(frame,text="para poder hallar sus datos insertando un valor especifico")
    plant.grid(row=2,column=0,columnspan=4,padx=12,pady=2)

    boton1=Button(frame,text="Circulo",width=20,command=lambda:EjerciciosInterfaz("Circulo"))
    boton1.grid(row=3,column=0,columnspan=2,padx=16,pady=12)

    boton1=Button(frame,text="Rectangulo",width=20,command=lambda:EjerciciosInterfaz("Rectangulo"))
    boton1.grid(row=3,column=2,columnspan=2,padx=16,pady=12)

    boton1=Button(frame,text="Cuadrado",width=20,command=lambda:EjerciciosInterfaz("Cuadrado"))
    boton1.grid(row=4,column=0,columnspan=2,padx=16,pady=12)

    boton1=Button(frame,text="Triangulo",width=20,command=lambda:EjerciciosInterfaz("Triangulo"))
    boton1.grid(row=4,column=2,columnspan=2,padx=16,pady=12)

    boton1=Button(frame,text="Rombo",width=20,command=lambda:EjerciciosInterfaz("Rombo"))
    boton1.grid(row=5,column=0,columnspan=2,padx=16,pady=12)

    boton1=Button(frame,text="Trapecio",width=20,command=lambda:EjerciciosInterfaz("Trapecio"))
    boton1.grid(row=5,column=2,columnspan=2,padx=16,pady=12)

    boton1=Button(frame,text="Regresar",width=10,command=volver)
    boton1.grid(row=99,column=0,padx=12,pady=4)
    raiz.mainloop()