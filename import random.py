import random 
SEPARADOR = ("*" * 20) + "\n"

#Creacion de una lista con diez valores aleatorios entre 1 y 100 
lista = [random. randrange(1,101) for valor in range(10)]
print(type(lista))
print(f"el primer elemento es{lista[0]} y el ultimo es {lista[9]}")
print(type(lista))
print(SEPARADOR)

#Creacion de una lista de cinco listas con diez elementos cada una
listas_de_listas = [[random. randrange(1,101) for valor in range(10)] for valor in range(5)]
print(listas_de_listas)
print(f"el primer elemento es {listas_de_listas[0][0]} y el ultimo es {listas_de_listas[4][9]}")
#print(lista_de_lista[0][:])
print(listas_de_listas[0])
for lista_interna in listas_de_listas:
    print(lista_interna[0])

print(type(listas_de_listas))

print("[")
for lista_primer_nivel in listas_de_listas:
    #print(f"lista interna: {lista_primer_nivel}")
    print("[", end="")
    for elemento in lista_primer_nivel:
        print(f"{elemento}", end="\t")
    print("]", end="")
    print("")
print("]")
print(SEPARADOR)

print(f"el elemento 0,2 es {listas_de_listas[0][2]}")
print(f"el elemento 2,7 es {listas_de_listas[2][7]}")
#print(lista_de_lista[0,4])#ESTO ES UN ERROR!