from Tkinter import *
from math import pi, sqrt, acos

def raiz(x,y,z):
    return sqrt( (x**2) + (y**2) + (z**2) )

def sumar():
    x3 = x1.get() + x2.get()
    y3 = y1.get() + y2.get()
    z3 = z1.get() + z2.get()
    suma_lbl = Label(root, text="("+str(x3)+","+str(y3)+","+str(z3)+")")
    suma_lbl.grid(row=5, column=2)

def restar():
    x3 = x1.get() - x2.get()
    y3 = y1.get() - y2.get()
    z3 = z1.get() - z2.get()
    resta_lbl = Label(root, text="("+str(x3)+","+str(y3)+","+str(z3)+")")
    resta_lbl.grid(row=6, column=2)

def producto_vectorial():
    x3=(y1.get()*z2.get())+(z1.get()*y2.get())
    y3=(z1.get()*x2.get())+(x1.get()*z2.get())
    z3=(x1.get()*y2.get())+(y1.get()*x2.get())
    prod_vec_lbl = Label(root, text="("+str(x3)+","+str(y3)+","+str(z3)+")")
    prod_vec_lbl.grid(row=7, column=2)

def producto_escalar():
    x3 = x1.get() * x2.get()
    y3 = y1.get() * y2.get()
    z3 = z1.get() * z2.get()
    producto = x3 + y3 + z3
    prod_esc_lbl = Label(root, text= producto)
    prod_esc_lbl.grid(row=8, column=2)

    
def angulo():
    x3 = x1.get() * x2.get()
    y3 = y1.get() * y2.get()
    z3 = z1.get() * z2.get()
    producto = x3 + y3 + z3
    raiz1 = raiz(x1.get(),y1.get(),z1.get())
    raiz2= raiz(x2.get(), y2.get(), z2.get())
    
    
    try:
        prueba = float(producto) / ( raiz1 * raiz2 )
        angulo = ((180/pi) * acos( prueba)) #Se halla el angulo
        angulo_lbl=Label(root, text= angulo)
        angulo_lbl.grid(row=5, column= 6)
        
    except:
        angulo_lbl=Label(root, text="Error.")
        angulo_lbl.grid(row=5, column=6)

def longitud1():
    longitud = sqrt((x1.get()**2)+(y1.get()**2)+(z1.get()**2))
    long1_lbl=Label(root, text= longitud)
    long1_lbl.grid(row=6, column=6)

def longitud2():
    longitud = sqrt((x2.get()**2)+(y2.get()**2)+(z2.get()**2))
    long2_lbl=Label(root, text= longitud)
    long2_lbl.grid(row=7, column=6)
        
def todos():

    sumar()    

    restar()

    producto_escalar()

    producto_vectorial()

    angulo()

    longitud1()

    longitud2()


    
root = Tk() #inicializacion TK

root.title("Vector Program 1.0 By Rock_Neurotiko") #titulo programa

#DEfinir las variables.
x1 = IntVar()
x2 = IntVar()
y1 = IntVar()
y2 = IntVar()
z1 = IntVar()
z2 = IntVar()

#titulo = Label(root, text = "Programa para calcular con vectores de tres dimensiones.")

#definir labels del vector 1 (top)
vector1_lbl = Label(root, text = "The First Vector:")
vector1x_lbl = Label(root, text = "X = ")
vector1y_lbl = Label(root, text = "Y = ")
vector1z_lbl = Label(root, text = "Z = ")

#definir labels del vector 2
vector2_lbl = Label(root, text = "The Second Vector:")
vector2x_lbl = Label(root, text = "X = ")
vector2y_lbl = Label(root, text = "Y = ")
vector2z_lbl = Label(root, text = "Z = ")

#definir entrada texto vector 1
x1_txt = Entry(root, textvariable=x1, width = 15)
y1_txt = Entry(root, textvariable=y1, width = 15)
z1_txt = Entry(root, textvariable=z1, width = 15)

#definir entrada texto vector 2
x2_txt = Entry(root, textvariable=x2, width = 15)
y2_txt = Entry(root, textvariable=y2, width = 15)
z2_txt = Entry(root, textvariable=z2, width = 15)



sumar_cd = Button(root, text="Adding vectors.", command=sumar, width=17)

restar_cd = Button(root, text="Subtract vectores.", command=restar, width=17)

prod_esc_cd = Button(root, text="Scalar Product.", command= producto_escalar, width=17)

prod_vec_cd = Button(root, text="Vector Product.", command = producto_vectorial, width=17)

ang_cd = Button(root, text="Angle between vectors.", command = angulo, width=19)

long1_cd = Button(root, text="Longitude vector 1.", command = longitud1, width=17)

long2_cd = Button(root, text="Longitude vector 2.", command = longitud2, width=17)


all_cd = Button(root, text="Calculate ALL.", command=todos, width=13)









#EMPIEZA EL PLASMAR LA GRAFICA

#titulo.grid(row=0)

#vector 1
vector1_lbl.grid(row=1, column=0)
vector1x_lbl.grid(row=1, column=1)
x1_txt.grid(row=1, column=2)
vector1y_lbl.grid(row=1, column=3)
y1_txt.grid(row=1, column=4)
vector1z_lbl.grid(row=1, column=5)
z1_txt.grid(row=1, column=6)

#vector 2
vector2_lbl.grid(row=2, column=0)
vector2x_lbl.grid(row=2, column=1)
x2_txt.grid(row=2, column=2)
vector2y_lbl.grid(row=2, column=3)
y2_txt.grid(row=2, column=4)
vector2z_lbl.grid(row=2, column=5)
z2_txt.grid(row=2, column=6)

#lado izquierdo checksboxes
sumar_cd.grid(row=5, column=0)
restar_cd.grid(row=6, column=0)
prod_vec_cd.grid(row=7, column=0)
prod_esc_cd.grid(row=8, column=0)

#lado derecho checkboxes
ang_cd.grid(row=5, column=4)
long1_cd.grid(row=6, column=4)
long2_cd.grid(row=7, column=4)

#Boton calc
all_cd.grid(row=8, column = 4)

root.mainloop()
