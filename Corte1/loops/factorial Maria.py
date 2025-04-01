while True:
    valor= int(input("Ingrese un entero positivo:"))
    print("Valor ",  valor)
    a=isinstance(valor, int)
    if a== True and valor>0:
        factorial = 1
        for i in range( 1, valor + 1):
            factorial= factorial*i
        print(f"EL factorial de {valor} es:", factorial)
    else:
        print("Ingrese un número postivo")