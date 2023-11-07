def ingresar_datos():  # Función ingresar datos
    n = int(input("Ingresar la cantidad de estudiantes: "))  
    edades = []
    for i in range(n):
        valor = input("Ingresar la edad del estudiante " + str(i+1) + ": ")
        edades.append(int(valor))
    print("Edades ingresadas:", edades)
    return edades

def promedio(edades):  # Calcular promedio
    if len(edades) == 0:  
        return 0
    return sum(edades) / len(edades)

def mayor_edad(edades):  # Edad mayor
    edad_maxima = max(edades)
    return edad_maxima

def ordenar_burbuja(edades):  # Ordenamiento de burbuja
    n = len(edades)
    for i in range(n):
        for j in range(0, n-i-1):
            if edades[j] > edades[j+1]:
                edades[j], edades[j+1] = edades[j+1], edades[j]

def edadesm_16(edades): # Cantidad de edades menores a 16
    menores_a_16 = [edad for edad in edades if edad < 16]
    cantidad_menores_a_16 = len(menores_a_16)
    return cantidad_menores_a_16

def edadesma_16_20(edades):# Cantidad de edades entre 16 a 20
    entre_16_20 = [edad for edad in edades if 16<=edad<=20]
    cantidad_16_20 = len(entre_16_20)
    return cantidad_16_20

if __name__ == "__main__":  # Principal
    edades_usuario = ingresar_datos()
    promedio_edades = promedio(edades_usuario)
    edad_mayor = mayor_edad(edades_usuario)
    menores_16 = edadesm_16(edades_usuario)
    edades_16_20=edadesma_16_20(edades_usuario)
    ordenar_burbuja(edades_usuario)
    print("El promedio de edades es:", promedio_edades)
    print("La edad mayor es: ", edad_mayor)
    print("La cantidad de edades menores a 16 es:", menores_16)
    print("La cantidad de edades entre 16 a 20 son: ", edades_16_20)
    print("Edades ordenadas:", edades_usuario)
