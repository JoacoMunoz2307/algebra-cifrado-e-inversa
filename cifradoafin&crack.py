def Euclides(a, b):
  if b == 0:
    return a
  else:
    return Euclides(b, a%b)

def EuclidesE(a, b):
  if b == 0:
    return (a, 1, 0)
  else:
    d, xp, yp = EuclidesE(b, a%b)
    x, y = yp, xp - int(a/b)*yp
    return (d, x, y)

def inversa(a, n):
  if Euclides(a, n) == 1:
    mcd, x, y = EuclidesE(a, n)
    return x % n
  else:
    print("No existe la inversa, ingresa otro número")

def cifrado(oracion):
  Oracion = ""
  for i in oracion:
    Oracion += abecedario[ (a * abecedario.index(i) + b) % 27]
  return Oracion

def descifrado(oraciones):
  ainv = inversa(a, 27)
  Oracion = ""
  for i in oraciones:
    Oracion += abecedario[ (ainv * (abecedario.index(i) - b)) % 27]
  return Oracion




abecedario="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
print("ejercicio 2 primera parte")
print("Utilizando la clave {a, b} = {4, 7} – Cifrar ELEMENTALMIQUERIDOWATSON– Descifrar OKHFSNKFNWFCWJHSNCHQYWFSWF")
a=int(input("ingrese a: "))
b=int(input("ingrese b: "))
for i in range(2):
    pregunta=input("desea descifrar(2) o cifrar(1): ")
    if pregunta=="1":
        mensaje1a=input("ingrese el texto que va a cifrar: ")
        print(cifrado(mensaje1a))
    elif pregunta=="2":
        mensaje1b=input("ingrese el texto que va a descifrar: ")
        print(descifrado(mensaje1b))


print("ejercicio 2 segunda parte")
#clave{23,17} palbra es NOEXISTENPREGUNTASSINRESPUESTASOLOPREGUNTASMALFORMULADAS

A=[1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23, 25, 26]
B=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]

ultimomensaje = "SLBCMVRBSHZBTÑSRQVVMSZBVHÑBVRQVLALHZBTÑSRQVWQAXLZWÑAQFQV"
for a in A:
  for b in B:
    print("clave= ", "(",a,b,")", descifrado(ultimomensaje))
