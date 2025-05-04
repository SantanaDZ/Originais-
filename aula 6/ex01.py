def definePositivo(numero):
    resultado = ""
    if numero == 0:
        resultado = "Nulo"
    if numero < 0:
        resultado = "Negativo"    
    else:
        resultado = "Positivo"
    return resultado    


print(definePositivo(-5))