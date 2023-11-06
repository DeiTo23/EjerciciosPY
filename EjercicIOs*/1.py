def promedio(notas):#Calcular  promedio
    calificaciones_sin_nota_menor = notas[:]  
    menor_nota = min(calificaciones_sin_nota_menor) 
    calificaciones_sin_nota_menor.remove(menor_nota) 
    print("La nota que no se considera es:",menor_nota)
    return sum(calificaciones_sin_nota_menor) / len(calificaciones_sin_nota_menor) 

def ingresar_datos():#Funcion ingresar  datos
    notas = []
    for i in range(5):
        valor = input("Ingresar la nota " + str(i+1) + ": ")
        notas.append(int(valor))  
    print("Notas ingresadas:", notas)
    return notas  

if __name__ == "__main__": #Principal
    notas_usuario = ingresar_datos()
    promedio_notas = promedio(notas_usuario) 
    print("El promedio es:", promedio_notas)
