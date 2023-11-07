import random

def generar_vector(n):
    return [random.randint(1, 50) for _ in range(n)]

def encontrar_secuencias_ascendentes(vector):
    secuencias = []
    secuencia = [vector[0]]
    for i in range(1, len(vector)):
        if vector[i] > vector[i - 1]:
            secuencia.append(vector[i])
        else:
            if len(secuencia) > 1:
                secuencias.append(secuencia)
            secuencia = [vector[i]]
    if len(secuencia) > 1: 
        secuencias.append(secuencia)
    
    return secuencias

def obtener_numeros_pares(vector):
    return [num for num in vector if num % 2 == 0]

def imprimir_secuencias(secuencias):
    for secuencia in secuencias:
        print(secuencia)

def imprimir_pares(pares):
    print(f"Números pares: {pares}")

def main():
    n = int(input("Ingrese la cantidad de elementos : "))
    vector = generar_vector(n)
    print(f"Vector generado: {vector}")

    secuencias_ascendentes = encontrar_secuencias_ascendentes(vector)
    print("Secuencias ascendentes:")
    imprimir_secuencias(secuencias_ascendentes)

    pares = obtener_numeros_pares(vector)
    imprimir_pares(pares)

if __name__ == '__main__':
    main()
