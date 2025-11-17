import random

def lanzardados():
    Valor = int(input("¿Cuantas veces quieres lanzar los dados?: "))
    Dados = 0
    Sera = True
    
    print("lanzarás",Valor,"veces")
    
    while Sera:
        print("lanzando los dados...")
        Dados = Dados+random.randint(1,6)
        Valor = Valor-1
        if Valor <1:
            Sera = False
    print("La suma total de todas tus tiradas fué: ",Dados)

print("Jugador 1 empieza")
Jugador1 = lanzardados()
print("Jugador 2 empieza")
Jugador2 = lanzardados()


