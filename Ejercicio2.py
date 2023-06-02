#Es realizar un programa en python que haga la descomposición canónica de un número
#Librerias-------------------------
import math
#Primos----------------------------
def searchP(n):
    if n<=1:
            return False;
    div = False
    i = 2
    while i<= math.sqrt(n) and not div:
        if n % i == 0:
            div = True
        i+=1
    return not div

def Primos(n):
    while True:
        n = n+1
        if searchP(n):
            return n
#MCM-------------------------------
def MCM(n):
    print(n," = ", end="")
    go = 2
    primer_divisor = True
    cant_fact = 0
    while n>1:
        if n % go == 0:
            cant_fact +=1
            n //= go
        else:           
            primer_divisor, cant_fact = escritura(primer_divisor, go, cant_fact)
            go = Primos(go)  
    primer_divisor, cant_fact = escritura(primer_divisor, go, cant_fact)
#Escritura--------------------------
def escritura(primer_divisor, go, cant_fact):
    if cant_fact > 0:
        if primer_divisor:
            primer_divisor = False
        else:
            print("x", end="")
        if cant_fact==1:
            print(go, end="")
        else:
            print("{:d}^{:d}".format(go, cant_fact), end="")      
        cant_fact = 0        
    return primer_divisor, cant_fact 
#Ingreso de datos------------------
n=int(input("Ingresar un número: "))
if n<=1:
    print("El número 1, por convenio, no se considera ni primo ni compuesto")
else:
    MCM(n)