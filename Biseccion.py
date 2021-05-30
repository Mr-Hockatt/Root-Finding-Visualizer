import numpy as np
import csv



def Biseccion(Funcion, Xini, Xdini, Error):

  F=Funcion
  XI_inicial=Xini
  XD_inicial=Xdini
  Error_objetivo= Error

  XI = list()
  XD = list()
  XM = list()
  FXI = list()
  FXD = list()
  FXM = list()

  XI.append(complex(XI_inicial))
  XD.append(complex(XD_inicial))
  error = 10**(-3)

  myFile = open('TablaBiseccion.csv', 'w')

  with myFile:
    writer = csv.writer(myFile)
    writer.writerow(["XI", "XD", "XM", "F(XI)", "F(XD)", "F(XM)", "Error"])


    while abs(error) > abs(Error_objetivo):

      Xi = XI[-1]
      Xd = XD[-1]
      Xm = (Xi+Xd)/2

      Fi = F(Xi)
      Fd = F(Xd)
      Fm = F(Xm)

      if Fi*Fm >0:
        Xi=Xm
      else:
        Xd=Xm

      XI.append(Xi)
      XD.append(Xd)
      XM.append(Xm)
      FXI.append(Fi)
      FXD.append(Fd)
      FXM.append(Fm)

      if len(XM)>1:
        error = Xm - XM[-2]
      #print("Error: " + str(error))
      writer.writerow([Xi, Xd, Xm, Fi, Fd, Fm, error])



    print("Proceso terminado")
    print(XM)
