Vida = int(input("Ha iniciado una nueva partida, ingrese la cantidad de vidas que desee: "))

if Vida >= 5:
       print("Tienes",Vida,"De vida, la dificultad cambió a: FACIL")
elif Vida > 2 and Vida <= 4:
    print("Tienes",Vida,"De vida, la dificultad cambió a: MEDIO")
elif Vida <= 2:
     print("Tienes",Vida,"De vida, la dificultad cambió a: DIFICIL")