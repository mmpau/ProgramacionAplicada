toperango = 30
n = 0
primo = True
while (n < toperango):  
    for div in range(2, n):  
        if (n % div == 0): 
            primo = False
    if (primo):
        print(n) 
    else:
        primo = True  
    n += 1  



    
    #optimizacion con el break
n = 0
primo = True
while (n < toperango):
    for div in range(2, n):
        if (n % div == 0):
            primo = False
            break 
    if (primo):
        print(n)
    else:
        primo = True
    n += 1

    ciclossinbreak = 0
n = 0
primo = True
while (n < toperango):
    for div in range(2, n):
        ciclossinbreak += 1  # Contamos cada iteración del for
        if (n % div == 0):
            primo = False
    if (primo):
        print(n)
    else:
        primo = True
    n += 1
print('Cantidad de ciclos: ' + str(ciclossinbreak))

ciclosconbreak = 0
n = 0
primo = True
while (n < toperango):
    for div in range(2, n):
        ciclosconbreak += 1  
        if (n % div == 0):
            primo = False
            break  
    if (primo):
        print(n)
    else:
        primo = True
    n += 1
print('Cantidad de ciclos: ' + str(ciclosconbreak))
print('Se optimizó a un ' + str(ciclosconbreak / ciclossinbreak) + '% de ciclos aplicando break')

toperango = 100
ciclossinbreak = 0
n = 0
primo = True
while (n < toperango):
    for div in range(2, n):
        ciclos_sin_break += 1
        if (n % div == 0):
            primo = False
    if (primo):
        print(n)
    else:
        primo = True
    n += 1
print('Cantidad de ciclos: ' + str(ciclossinbreak))

ciclosconbreak = 0
n = 0
primo = True
while (n < toperango):
    for div in range(2, n):
        ciclosconbreak += 1
        if (n % div == 0):
            primo = False
            break
    if (primo):
        print(n)
    else:
        primo = True
    n += 1
print('Cantidad de ciclos: ' + str(ciclosconbreak))
print('Se optimizó a un ' + str(ciclosconbreak / ciclossinbreak) + '% de ciclos aplicando break')

