def modulo(a,b):
    r=a%b
    if r < 0:
        r=r+ b;
    return r

def EuclidesE(a, b):
    # caso base
    if a == 0 :
        return b,0,1

    mcd,x1,y1 = EuclidesE(b%a, a)

    x = y1 - (b//a) * x1
    y = x1

    return mcd,x,y

def inversa(a,b):
    m,a,y=EuclidesE(a,b)

    if a<0:
      a=modulo(a,b)
    return a

a=int(input("ingrese a: "))
n=int(input("ingrese n: "))
inv=inversa(a,n)
if inv==1:
  print("no existe")
else:
  print("a' = ", inv)
