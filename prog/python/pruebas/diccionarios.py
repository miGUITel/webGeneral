#1
informacion_personal = {"Nombre":"Ana", "Edad":25, "Ciudad":"Valencia"}
print(informacion_personal)

#2
print(informacion_personal["Edad"])

#3
informacion_personal["Ciudad"]="Madrid"
print(informacion_personal)

#4
informacion_personal["Profesión"]="Ingeniera"
print(informacion_personal)

#5
puntuaciones = {"Juan":90, "María":85, "Pedro":78}
print(puntuaciones.get("Luis",0))

#6
for x in puntuaciones:
    print(puntuaciones[x])