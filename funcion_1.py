def aplicarAumento(precio: int)->float:
    """
    devuelva el valor de un producto con un aumento del 5%
    """
    aumento = 5

    aumento = (aumento * precio) / 100

    resultado = precio + aumento

    return resultado

print(aplicarAumento(100))