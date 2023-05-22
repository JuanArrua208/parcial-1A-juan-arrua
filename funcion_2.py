def reemplazarCaracteres(cadena: str, primer_caracter: chr, segundo_caracter: chr)->int:

    """
    reemplazar cada ocurrencia del segundo parámetro por el tercero
    y devolver la cantidad de veces que se reemplazo ese carácter  en la cadena
    """
    cadena_modificada = cadena.replace(primer_caracter, segundo_caracter)
    cantidad = cadena_modificada.count(segundo_caracter)
    return cantidad

print(reemplazarCaracteres("Holaaaaa", "a", "e"))