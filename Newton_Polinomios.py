import re

#230x⁴+18x³+9x²-221x-9

expr = input("Ingrese la funcion: ")
x_0= float(input("Ingrese x0: "))

#Metodo para obtener los exponentes de la funcion
def coefs(entrada):
  regexp = r"(-?\d*)(x?)([¹²³⁴⁵⁶⁷⁸⁹]*)"
  c = {}
  for coef, x, exp in re.findall(regexp, entrada):
    if not coef and not x:
      continue
    if x and not coef:
      coef = '1'
    if x and coef == "-":
      coef = "-1"
    if x and not exp:
      exp = '1'
    if coef and not x:
      exp = '0'
    exp = ord(exp) & 0x000F
    c[exp] = float(coef)
  grado = max(c)
  coeficientes = [0.0] * (grado+1)
  for g, v in c.items():
    coeficientes[g] = v
  return coeficientes


it=0
tol=1.e-3
it_max=100

coeficientes_1 = coefs(expr) # obtiene los coeficientes del polinomio
div_sint_1 = coeficientes_1 # declara el tamaño del arreglo obteniendolo del numero de coeficientes
x_v=1
#print(coeficientes_1)

while abs(x_v-x_0)>tol and it<it_max:
  
  
  #Obtener a_0
  con=len(coeficientes_1)-1
  for k in range(len(coeficientes_1)-1):
  	div_sint_1[con-1] = (x_0*div_sint_1[con])+coeficientes_1[con-1]  
  	con=con-1

  #print(contador)
  #div_sint_1[3] = (x_0*div_sint_1[4])+coeficientes_1[3]
  #div_sint_1[2] = (x_0*div_sint_1[3])+coeficientes_1[2] 
  #div_sint_1[1] = (x_0*div_sint_1[2])+coeficientes_1[1]
  #div_sint_1[0] = (x_0*div_sint_1[1])+coeficientes_1[0]

  a_0=div_sint_1[0]

  div_sint_2=div_sint_1

  con=len(coeficientes_1)-1
  for k in range(len(coeficientes_1)-2):
  	div_sint_2[con-1]=(div_sint_2[con]*x_0)+div_sint_1[con-1]	
  	con=con-1
  	
  #Obtener a_1
  #div_sint_2[3]=(div_sint_2[4]*x_0)+div_sint_1[3]
  #div_sint_2[2]=(div_sint_2[3]*x_0)+div_sint_1[2]
  #div_sint_2[1]=(div_sint_2[2]*x_0)+div_sint_1[1]

  #aplicar formula

  a_1=div_sint_2[1]
  x_v = x_0
  x_0 = x_0-(a_0/a_1)


  print(x_0)
  coeficientes_1 = coefs(expr) # obtiene los coeficientes del polinomio

