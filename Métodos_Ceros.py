import numpy as np

XI_inicial = input("Ingrese el XI inicial: ")
XD_inicial = input("Ingrese el XD inicial: ")
Error_objetivo = 10**(-4)

coeficientes = [3, -5, 1]
F = np.poly1d(coeficientes)

XI = list()
XD = list()
XM = list()
FXI = list()
FXD = list()
FXM = list()

XI.append(float(XI_inicial))
XD.append(float(XD_inicial))
error = 10**(-3)



while error > Error_objetivo:

  Xi = XI[-1]
  Xd = XD[-1]
  Xm = (Xi+Xd)/2

  Fi = F(Xi)
  Fd = F(Xd)
  Fm = F(Xm)

  if Fi*Fm > 0:
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
    error = np.abs(Xm - XM[-2])
  print("Error: " + str(error))



print("Proceso terminado")
print(XM)
