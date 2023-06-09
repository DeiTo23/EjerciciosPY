horas=int(input("Ingrese el numero de horas: "))
pago =int(input("El monto por pago de horas:" ))
if 40>=horas:
    sueldo = horas * pago
    print("El sueldo es: ", sueldo) 
else:
     sueldo = (40*pago)+ ((horas-40)*(2*pago))   
     print("El sueldo es: ", sueldo)