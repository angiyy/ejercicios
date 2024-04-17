#8 
intentos=0

while intentos<10000000: 
    ingreso=str(input("Ingrese lo que desee: ")).lower()
    if ingreso=="salir":
     print("Usted salio del programa, que pase feliz dia :D")
     break
    else :
        print(ingreso)
    intentos +=1
