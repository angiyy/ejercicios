#6
intentos=0
contraseña="contraseña"

while intentos<10000000: 
    ingreso=input("Ingrese la contraseña: ")
    if ingreso == contraseña:
        print("la contraseña es corresta BIENVENIDO")
        break
    else :
        print("contraseña incorrecta intente de nuevo: ")

    intentos +=1

