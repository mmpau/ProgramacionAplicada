

alturas_edificios = {
    "Burj Khalifa": 828,
    "Torre de Shanghái": 632,
    "Abraj Al Bait": 601,
    "Ping An": 599,
    "Torre Lotte World": 554.5,
    "One World Trade": 541.3
}

print(alturas_edificios["Burj Khalifa"])  
print(alturas_edificios["Ping An"])      

elementos_zodiaco = {
    "agua": ["Cáncer", "Escorpio", "Piscis"],
    "fuego": ["Aries", "Leo", "Sagitario"],
    "tierra": ["Tauro", "Virgo", "Capricornio"],
    "aire": ["Géminis", "Libra", "Acuario"]
}

print(elementos_zodiaco["tierra"])
print(elementos_zodiaco["fuego"])




alturas_edificios = {
    "Burj Khalifa": 828,
    "Torre de Shanghái": 632,
    "Abraj Al Bait": 601,
    "Ping An": 599,
    "Torre Lotte World": 554.5,
    "One World Trade": 541.3
}


clave_a_buscar = "Landmark 81"
if clave_a_buscar in alturas_edificios:
    print(alturas_edificios[clave_a_buscar])

elementos_zodiaco["energía"] = "No es un elemento del zodiaco"

if "energía" in elementos_zodiaco:
    print(elementos_zodiaco["energía"])



print(alturas_edificios.get("Torre de Shanghái"))  # Devuelve 632
print(alturas_edificios.get("Mi Casa"))            


# Ejemplo con usuarios
identificadores_usuarios = {
    "codificadorTera": 100019,
    "chicoPython": 182921,
    "samJavaMaestra": 123112,
    "lazoLyle": 102931,
    "llavesKeith": 129384
}

if identificadores_usuarios.get("codificadorTera") is None:
    id_tc = 1000
else:
    id_tc = identificadores_usuarios.get("codificadorTera")

print(id_tc)

if identificadores_usuarios.get("superGolpePila") is None:
    id_super = 100000
    print(id_super)


# ## Eliminar una clave

sorteo = {
    223842: "Osito de peluche",
    872921: "Entradas para concierto",
    320291: "Cesta de regalo",
    412123: "Collar",
    298787: "Máquina de pasta"
}

print(sorteo.pop(320291, "Sin premio")) 
print(sorteo)

print(sorteo.pop(100000, "Sin premio")) 
print(sorteo)

print(sorteo.pop(872921, "Sin premio"))  
print(sorteo)



objetos_disponibles = {
    "poción de salud": 10,
    "pastel de la cura": 5,
    "elixir verde": 20,
    "sándwich de fuerza": 25,
    "granos de resistencia": 15,
    "estofado de poder": 30
}

puntos_salud = 20

puntos_salud += objetos_disponibles.pop("granos de resistencia", 0)
puntos_salud += objetos_disponibles.pop("estofado de poder", 0)
puntos_salud += objetos_disponibles.pop("pan místico", 0)

print(objetos_disponibles)
print(puntos_salud)




puntajes = {
    "Gracia": [80, 72, 90],
    "Javier": [88, 68, 81],
    "Silvia": [80, 82, 84],
    "Pedro": [98, 96, 95],
    "Martín": [78, 80, 78],
    "Dina": [64, 60, 75]
}

print(list(puntajes)) 

for estudiante in puntajes.keys():
    print(estudiante)

ejercicios_por_tema = {
    "funciones": 10,
    "sintaxis": 13,
    "flujo de control": 15,
    "bucles": 22,
    "listas": 19,
    "clases": 18,
    "diccionarios": 18
}

usuarios = identificadores_usuarios.keys()
lecciones = ejercicios_por_tema.keys()

print(usuarios)
print(lecciones)




for lista_puntajes in puntajes.values():
    print(lista_puntajes)

total_ejercicios = 0
for cantidad in ejercicios_por_tema.values():
    total_ejercicios += cantidad

print(total_ejercicios)



marcas_mas_grandes = {
    "Apple": 184,
    "Google": 141.7,
    "Microsoft": 80,
    "Coca-Cola": 69.7,
    "Amazon": 64.8
}

for empresa, valor in marcas_mas_grandes.items():
    print(empresa + " tiene un valor de " + str(valor) + " mil millones de dólares.")

porcentaje_mujeres_ocupacion = {
    "Directora ejecutiva": 28,
    "Gerente de ingeniería": 9,
    "Farmacéutica": 58,
    "Doctora": 40,
    "Abogada": 37,
    "Ingeniera aeroespacial": 9
}


for ocupacion, porcentaje in porcentaje_mujeres_ocupacion.items():
    print("Las mujeres representan el " + str(porcentaje) + "% de las " + ocupacion + "s.")