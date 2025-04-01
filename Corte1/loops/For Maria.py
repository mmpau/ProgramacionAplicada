import time

cadena = "Maria"
letra = ''

for letra in cadena:
    if letra== "t":
        continue 
    print(letra)
    time.sleep(1)