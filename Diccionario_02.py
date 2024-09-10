numbers={1:"uno",2:"dos",3:"tres"}
print(numbers)

print(numbers[1])
print(numbers[2])
print(numbers[3])


information = {"nombre":"yazmin",
               "apellidos":"teran",
               "estatura":"1.53cm",
               "animo feliz" :"True"}
print(information)
del information["apellidos"]
print(information)
claves= information.keys()
print(claves)
print(type(claves))
values=information.values()
print(values)
pairs = information.items()
print(pairs)

contacts= {"Dioseny":{"Apellido":"Teran Guerrero",
                     "Altura" : 1.53,
                     "Edad": 24,
                     "Telefono": 3184510394,
                     "signo Zodiacal": "Sagitario",
                     "serie favorita": "one pice",
                     "Cancion favorita":"hasta que amanesca",
                     "comida favorita" : "jugo de mora , sancocho, papas fritas",
                     "Lugar soñado vacaciones":"Peru",
                     "habilidad secreta":"crear amigurumis",
                     "pasatiempo": "camir",
                     "heroe o persona que admiras" : "mis padres",
                     "Libro que mas me ha impactado" : "libro de paulo cohelo",
                     "Cenar con alguien" : "con mi novio",
                     "super poder": "Poder volar",
                     "que logro personal te enorgullese" : "poder aprender a programar",
                   }}
print(contacts)
