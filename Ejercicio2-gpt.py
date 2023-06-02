def descomposicion_canonica(numero):
    factor_primo = 2
    exponente = 0
    descomposicion = []

    while factor_primo <= numero:
        if numero % factor_primo == 0:
            exponente += 1
            numero //= factor_primo
        else:
            if exponente > 0:
                descomposicion.append((factor_primo, exponente))
            factor_primo += 1
            exponente = 0

    if exponente > 0:
        descomposicion.append((factor_primo, exponente))

    return descomposicion


def formato_descomposicion(descomposicion):
    resultado = ""
    for factor, exponente in descomposicion:
        if exponente == 1:
            resultado += str(factor)
        else:
            resultado += str(factor) + "^" + str(exponente)
        resultado += " + "
    return resultado[:-3]  # Eliminar el último " + "


# Entrada de usuario
numero = int(input("Ingrese un número entero positivo: "))

# Descomposición canónica
resultado = descomposicion_canonica(numero)
descomposicion = formato_descomposicion(resultado)

# Salida
print("La descomposición canónica de", numero, "es:", descomposicion)
