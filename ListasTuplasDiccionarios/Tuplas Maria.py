my_lista=["Carro" , "Esposa" , "Computador" , "Sopa" , "Arbol" , "Cocina"]

print(my_lista)
print(type(my_lista))
print(my_lista[2])
print("El tamaño de mi lista es : " , len(my_lista) )
print(my_lista[0:2])
my_lista.append("Pollo")
print(my_lista)
my_lista.insert(3 , "Casa")
print(my_lista)
my_lista.extend(["Universidad"])#Se pon en llaves para que lleve toda la palabra, no letra por letra
print(my_lista)
print(my_lista.index("Carro"))
my_lista.remove("Esposa")
print(my_lista)
my_lista.insert(8 , "Marron")
print(my_lista)
print(my_lista.pop())

Tamaño= len(my_lista)
print("El tamaño de la lista es:", Tamaño)
my_lista3= my_lista * 3
print("La lista se repetira 3 veces:" , my_lista3)


print("Ordenamiento de listas")
print("Orden alfabético de la lista:")
my_lista.sort()  
print(my_lista)

Listanum = [1, 33, 44, 56, 87, 46, 123]
print("Ordenar números de menor a mayor:")
Listanum.sort()
print(Listanum)


Listanum.sort(reverse=True)
print("De mayor a menor ", Listanum)

print("Tuplas")

mitupla= tuple(my_lista)
print("Mi tupla es ", mitupla)

print(mitupla[0])

print(mitupla[2])

print("carro" in mitupla)
print(mitupla.count("Carro")) #Cuenta cuantas veces esta la palabra

Tuplaunitaria=("Blanco",)
print(Tuplaunitaria)

mitupla= "Maria" , 11 , 11 , 2005
print(mitupla)

nombre, dia, mes , año = mitupla

print(nombre)
print(dia)
print(mes)
print(año)

