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
my_lista.extend("Comida ", "Universidad ")
print(my_lista)
print(my_lista.index("Carro"))
my_lista.remove("Esposa")
print(my_lista)
my_lista.insert(8 , "Marron")
print(my_lista)
print(my_lista.pop)

Tamaño= len(my_lista)
print("El tamaño de la lista es:", Tamaño)
my_lista3= my_lista * 3
print("La lista se repetira 3 veces:" , my_lista3)


print("Ordenamiento de listas")
print("Orden alfabetico de la lista: ")
my_listasort=my_lista.sort
print(my_listasort)

Listanum=[1 , 33 ,44 ,56 , 87, 46, 123]
print("Ordenar números de menor a mayor: ")
Listanumsort= Listanum.sort
print(Listanumsort)


Listanum.sort(reverse=True)
print("De mayor a menor ", Listanum)

print("Tuplas")

mitupla= tuple(my_lista)
print("Mi tupla es ", mitupla)

print(mitupla[0])

print(mitupla[2])
