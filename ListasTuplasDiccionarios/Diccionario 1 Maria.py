colorgato = {"negro": 21, "blanco": 23, "amarillo": 20, "gris": 22}
tamaños = {"pequeño": 6, "mediano": 2, "grande": 1}
comida = {"pescado": "mucho", "carne": "le gusta", "purina": "aceptable", "frutas": "más o menos"}

print("")

print( colorgato)

print( colorgato)
print(tamaños)

print( comida)
potencias = {(1, 2, 4, 8, 16): 2, (1, 3, 9, 27, 81): 3}

hijos = {"Gómez": ["Vicente", "Sara", "Laura"], "Pérez": ["Carlos", "Fredo", "Sergio"]}

diccionario_vacío = {}

menú = {"avena": 3, "tostada aguacate": 6, "jugo zanahoria": 5, "muffin arándano": 2}
print("Antes: ", menú)
menú["torta queso"] = 8
print("Después", menú)

animales_zoológico = {"dinosaurios": 0}
animales_zoológico = {"caballos": 2}
print(animales_zoológico)

sensores = {"sala": 21, "cocina": 23, "cuarto": 20}
print("Antes", sensores)
sensores.update({"despensa": 22, "cuarto invitados": 25, "patio": 34})
print("Después", sensores)

usuarios = {"codigoTera": 9018293, "proProgramador": 119238}
print(usuarios)
usuarios.update({"bucleador": 138475, "reinaCadenas": 85739})
print(usuarios)

menú = {"avena": 3, "tostada aguacate": 6, "jugo zanahoria": 5, "muffin arándano": 2}
print("Antes: ", menú)
menú["avena"] = 5
print("Después", menú)

ganadores_oscar = {"Mejor Película": "La La Land", "Mejor Actor": "Casey Affleck", "Mejor Actriz": "Emma Stone", "Película Animada": "Zootopia"}
print("Antes", ganadores_oscar)
ganadores_oscar.update({"Actriz de Reparto": "Viola Davis"})
print("Después1", ganadores_oscar)
ganadores_oscar["Mejor Película"] = "Moonlight"
print("Después2", ganadores_oscar)

nombres = ['Jenny', 'Alexus', 'Sam', 'Grace']
alturas = [61, 70, 67, 64]
estudiantes = {nombre: altura for nombre, altura in zip(nombres, alturas)}
print(estudiantes)

bebidas = ["espresso", "chai", "descafeinado", "filtro"]
cafeína = [64, 40, 0, 120]
bebidas_y_cafeína = {bebida: cantidad for bebida, cantidad in zip(bebidas, cafeína)}
print(bebidas_y_cafeína)

canciones = ["Como una Piedra Rodante", "Satisfacción", "Imagina", "Qué Está Pasando", "Respeto", "Buenas Vibraciones"]
reproducciones = [78, 29, 44, 21, 89, 5]
reproducidas = {canción: veces for canción, veces in zip(canciones, reproducciones)}
print(reproducidas)

reproducidas.update({"Niebla Púrpura": 1})
reproducidas.update({"Respeto": 94})
print("Después: ", reproducidas)

biblioteca = {"Las Mejores Canciones": reproducidas, "Domingos Tranquilos": {}}
print(biblioteca)