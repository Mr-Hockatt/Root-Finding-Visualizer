import numpy as np
import csv



def Newton(Funcion, coeficientes, Xo, Error):

  for grado in range(len(coeficientes)):
    coeficientes[-(grado+1)]=coeficientes[-(grado+1)]*grado

  P = Funcion
  cofi_derivada=coeficientes[:-1]
  D = np.poly1d(cofi_derivada)

  print("Derivada: \n", D)

  X_Inicial = Xo
  Error_objetivo = Error

  X=list()
  FP=list()
  FD=list()

  X.append(complex(X_Inicial))

  error = 10**(-3)


  myFile = open('TablaNewton.csv', 'w')
  with myFile:

    writer = csv.writer(myFile)
    writer.writerow(["Xn", "F(Xn)", "F'(Xn)", "Xn+1", "Error"])

    while abs(error) > abs(Error_objetivo):

      X_ACTUAL = X[-1]
      X_SIGUIENTE = X_ACTUAL-(P(X_ACTUAL)/D(X_ACTUAL))

      X.append(X_SIGUIENTE)
      FP.append(P(X_ACTUAL))
      FD.append(D(X_ACTUAL))

      error= X_SIGUIENTE-X_ACTUAL
      #print("Error: ", error)
      writer.writerow([X_ACTUAL, P(X_ACTUAL), D(X_ACTUAL), X_SIGUIENTE, error])

  print(X)
