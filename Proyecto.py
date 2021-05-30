import numpy as np
import tkinter as tk
import tkinter.messagebox as tkMessageBox
from Newton import Newton
from Biseccion import Biseccion
import csv
from tables import createStandardTable as cst


main_window = tk.Tk()
main_window.title("Proyecto Métodos")
main_window.geometry('500x400')
#main_window.configure(bg='white')


#Grado del Polinomio (SpinBox)

casillas_buffer = list()
labels_buffer = list()

def Generar_Casillas_Coeficientes():
    global casillas_buffer
    global labels_buffer

    if len(casillas_buffer)>1:
        for casilla in casillas_buffer:
            casilla.destroy()
    if len(labels_buffer)>1:
        for label in labels_buffer:
            label.destroy()

    grado = int(spinbox_grado.get()) + 1
    casillas_coef = list()
    labels_coef = list()

    for coeficiente in range(grado):
        boton = tk.Entry(main_window, width=3)
        boton.place(x=5+30*coeficiente, y=50)

        label = tk.Label(main_window, text=str(grado-coeficiente-1))
        label.place(x=5+30*coeficiente, y=30)

        casillas_coef.append(boton)
        labels_coef.append(label)

    casillas_buffer = casillas_coef
    labels_buffer = labels_coef

spinbox_grado = tk.Spinbox(main_window, from_=1, to=20, command= Generar_Casillas_Coeficientes)
spinbox_grado.place(x=250, y=100, anchor='center')
#(SpinBox)

#Grado del Polinomio (Text Box)
def Generar_Polinomio():

    global coeficientes
    coeficientes = list()
    coef_validos = True
    for casilla in casillas_buffer:
        try:
            coeficiente = int(casilla.get())
        except Exception as e:
            coeficiente = None
            coef_validos = False
            casillas_buffer[len(coeficientes)].delete(0, 'end')

        print(coeficiente)
        coeficientes.append(coeficiente)

    if not coef_validos:
        tkMessageBox.showerror("Error", "ERROR\nIngrese coeficientes numéricos")
    print(coeficientes)

    global P
    P = np.poly1d(coeficientes)
    print(P)

def Limpiar_Casillas():

    for casilla in casillas_buffer:
        casilla.delete(0, 'end')


    #Codigo borrar casillas de Isa
    try:

        #Casillas de JuanCa
        for casilla in casillas_buffer:
            casilla.destroy()

        for label in labels_buffer:
            label.destroy()

        #Newton
        Casilla_XI.destroy()
        Casilla_XD.destroy()
        Casilla_ErrorB.destroy()
        label_XI.destroy()
        label_XD.destroy()
        label_ErrorB.destroy()
        button_Biseccion.destroy()

        #Biseccion
        Casilla_Xo.destroy()
        Casilla_ErrorN.destroy()
        label_Xo.destroy()
        label_ErrorN.destroy()
        button_Newton.destroy()


    except Exception as e:
        try:

            #Newton
            Casilla_XI.destroy()
            Casilla_XD.destroy()
            Casilla_ErrorB.destroy()
            label_XI.destroy()
            label_XD.destroy()
            label_ErrorB.destroy()
            button_Biseccion.destroy()

            #Biseccion
            Casilla_Xo.destroy()
            Casilla_ErrorN.destroy()
            label_Xo.destroy()
            label_ErrorN.destroy()
            button_Newton.destroy()


        except Exception as e:
                try:

                    #Biseccion
                    Casilla_Xo.destroy()
                    Casilla_ErrorN.destroy()
                    label_Xo.destroy()
                    label_ErrorN.destroy()
                    button_Newton.destroy()


                except Exception as e:
                    pass

button_generar_polinomio = tk.Button(main_window, text='Generar P(x)', width=10, command=Generar_Polinomio)
button_generar_polinomio.place(x=150, y=130, anchor='nw')
button_clear = tk.Button(main_window, text='Clear', width=10, command=Limpiar_Casillas)
button_clear.place(x=350, y=130, anchor='ne')
#Fin (Text Box)


label_Método = tk.Label(main_window, text='Elija el Método de Solución:')
label_Método.place(x=250, y=200, anchor='center')



#Selecccion del Método
def Get_Parametros_Newton():

    Xo = complex(Casilla_Xo.get())
    Error = complex(Casilla_ErrorN.get())
    '''
    if P(Xo)*P(1000) > 0 or P(Xo)*P(-1000):
        tkMessageBox.showerror("Error", "ERROR\nEl intervalo no contiene raíces")

    else:
    '''
    Newton(P, coeficientes, Xo, Error)


    secondary_windowN = tk.Tk()
    secondary_windowN.title("Tabla Newton")

    tableFrameN = tk.Frame(secondary_windowN)
    f = open("TablaNewton.csv")
    newtableN = cst(f,tableFrameN)
    newtableN.grid()
    tableFrameN.grid()

    import matplotlib.pyplot as plotter
    x = np.arange(-10, 10, 0.05)
    plotter.plot(x, P(x))
    plotter.xlabel("x")
    plotter.ylabel("P(x)")
    plotter.ylim(-10,10)
    title = ""
    for coeficiente in coeficientes:
        if coeficiente >= 0:
            title = title + "+" + str(coeficiente) + "x^" + str(len(coeficientes) - coeficientes.index(coeficiente) - 1)
        else:
            title = title + str(coeficiente) + "x^" + str(len(coeficientes) - coeficientes.index(coeficiente) - 1)

    plotter.title(r'$P(x) = {}$'.format(title))
    plotter.axhline(y=0, color='k')
    plotter.axvline(x=0, color='k')
    plotter.grid(True)
    plotter.show()


def Parametros_Newton():

    global Casilla_Xo
    global Casilla_ErrorN
    global label_Xo
    global label_ErrorN
    global button_Newton

    try:
        Casilla_XI.destroy()
        Casilla_XD.destroy()
        Casilla_ErrorB.destroy()
        label_XI.destroy()
        label_XD.destroy()
        label_ErrorB.destroy()
        button_Biseccion.destroy()
    except Exception as e:
        pass

    Casilla_Xo = tk.Entry(main_window, width=10)
    Casilla_Xo.place(x=150, y=240)

    Casilla_ErrorN = tk.Entry(main_window, width=10)
    Casilla_ErrorN.place(x=150, y=270)

    label_Xo = tk.Label(main_window, text="Xo: ")
    label_Xo.place(x=100, y=240)
    label_ErrorN = tk.Label(main_window, text="Error: ")
    label_ErrorN.place(x=100, y=270)

    button_Newton = tk.Button(main_window, text='Resolver', width=10,command=Get_Parametros_Newton)
    button_Newton.place(x=130, y=295)



def Get_Parametros_Biseccion():

    XI = complex(Casilla_XI.get())
    XD = complex(Casilla_XD.get())
    Error = complex(Casilla_ErrorB.get())

    '''
    if P(XI)*P(XD) > 0:
        tkMessageBox.showerror("Error", "ERROR\nEl intervalo no contiene raíces")

    else:
        '''
    Biseccion(P, XI, XD, Error)

    secondary_windowB = tk.Tk()
    secondary_windowB.title("Tabla Biseccion")

    tableFrameB = tk.Frame(secondary_windowB)
    f = open("TablaBiseccion.csv")
    newtableB = cst(f,tableFrameB)
    newtableB.grid()
    tableFrameB.grid()


    import matplotlib.pyplot as plotter
    x = np.arange(-10, 10, 0.05)
    plotter.plot(x, P(x))
    plotter.xlabel("x")
    plotter.ylabel("P(x)")
    plotter.ylim(-10,10)
    title = ""
    for coeficiente in coeficientes:
        if coeficiente >= 0:
            title = title + "+" + str(coeficiente) + "x^" + str(len(coeficientes) - coeficientes.index(coeficiente) - 1)
        else:
            title = title + str(coeficiente) + "x^" + str(len(coeficientes) - coeficientes.index(coeficiente) - 1)

    plotter.title(r'$P(x) = {}$'.format(title))
    plotter.axhline(y=0, color='k')
    plotter.axvline(x=0, color='k')
    plotter.grid(True)
    plotter.show()



def Parametros_Biseccion():

    global Casilla_XI
    global Casilla_XD
    global Casilla_ErrorB
    global label_XI
    global label_XD
    global label_ErrorB
    global button_Biseccion

    try:
        Casilla_Xo.destroy()
        Casilla_ErrorN.destroy()
        label_Xo.destroy()
        label_ErrorN.destroy()
        button_Newton.destroy()
    except Exception as e:
        pass

    Casilla_XI = tk.Entry(main_window, width=10)
    Casilla_XI.place(x=370, y=240)

    Casilla_XD = tk.Entry(main_window, width=10)
    Casilla_XD.place(x=370, y=270)

    Casilla_ErrorB = tk.Entry(main_window, width=10)
    Casilla_ErrorB.place(x=370, y=300)

    label_XI = tk.Label(main_window, text="XI: ")
    label_XI.place(x=320, y=240)
    label_XD = tk.Label(main_window, text="XD: ")
    label_XD.place(x=320, y=270)
    label_ErrorB = tk.Label(main_window, text="Error: ")
    label_ErrorB.place(x=320, y=300)

    button_Biseccion = tk.Button(main_window, text='Resolver', width=10, command=Get_Parametros_Biseccion)
    button_Biseccion.place(x=350, y=325)




#END Selecccion del Método

radio_button_Newton = tk.Radiobutton(main_window, text="Newton-Raphson", value=1, command=Parametros_Newton)
radio_button_Biseccion = tk.Radiobutton(main_window, text="Biseccion", value=2, command=Parametros_Biseccion)
radio_button_Newton.place(x=150, y=220, anchor='center')
radio_button_Biseccion.place(x=350, y=220, anchor='center')





main_window.mainloop()
