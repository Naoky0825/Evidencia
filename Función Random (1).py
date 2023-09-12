import random 

#Generar un número decimal pseudoaleatorio entre 0 y 1
random_decimal=random.random()

#Generar un número entero pseudoaleatorio dentro de un rango específico
random_integer=random.randint(1,100) #Genera un número entre 1 y 100 (ambos inclusive)

#Elegir un elemento aleatorio de una lista
fruits=["manzana","banana","naranja","uva"]
random_fruit=random.choice(fruits)

print("Número decimal pseudoaleatorio:",random_decimal)
print("Número entero pseudoaleatorio:",random_integer)
print("Fruta aleatoria:",random_fruit)
