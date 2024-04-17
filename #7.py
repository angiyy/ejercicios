frase=str(input("Ingrese una frase: ")).lower() #el .lower() convierte todos los caractares en minisculas
letra=str(input("Ingrese una letra: "))

#creo una variable para almacenar el conteo 
numero=frase.count(letra)
print(numero) #se imprime el conteo