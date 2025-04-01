import time

inicio = time.time()

for i in range(0, 31):  
    contador = 0  # Reinicia el contador para cada número
    for n in range(1, i + 1): 
        if i % n == 0:  
            contador += 1
    if contador == 2:  
        print(f'{i} es un primo')

fin = time.time()
print("t =", (fin - inicio) * 1000, "ms")
