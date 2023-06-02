// Solicitar al usuario el tamaño del arreglo
Escribir "Ingrese el tamaño del arreglo:"
Leer tamaño

// Crear un arreglo vacío de tamaño "tamaño"
arreglo = nuevo arreglo de tamaño "tamaño"

// Solicitar al usuario los elementos del arreglo
Para i desde 0 hasta tamaño - 1:
    Escribir "Ingrese el elemento en la posición", i, ":"
    Leer arreglo[i]
Fin Para

// Implementar el algoritmo de selección
Para i desde 0 hasta tamaño - 1:
    // Encontrar el índice del elemento mínimo en el subarreglo no ordenado
    índice_mínimo = i
    Para j desde i+1 hasta tamaño - 1:
        Si arreglo[j] < arreglo[índice_mínimo]:
            índice_mínimo = j
        Fin Si
    Fin Para

    // Intercambiar el elemento mínimo con el elemento en la posición i
    Si índice_mínimo != i:
        temp = arreglo[i]
        arreglo[i] = arreglo[índice_mínimo]
        arreglo[índice_mínimo] = temp
    Fin Si
Fin Para

// Mostrar el arreglo ordenado
Escribir "Arreglo ordenado:"
Para i desde 0 hasta tamaño - 1:
    Escribir arreglo[i]
Fin Para