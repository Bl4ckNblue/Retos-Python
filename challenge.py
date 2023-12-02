#RETO 0
"""
for i in range (1,101):
    if i%3 == 0 and i%5 == 0:
        i = "fizzbuzz"
    elif i%3 == 0:
        i = "fizz"
    elif i%5 == 0:
        i = "buzz"
    else:
        i = i
    print ("\n",i)
"""

#RETO 1 
"""
word1 = input("Ingresa una palabra: ")
word2 = input("Ingresa una palabra: ")

if word1 == word2:
    print (False)
else:
    print (True)    


#RETO 2 

var0 = 0
var1 = 1
for i in range (0,51):
    print (var0)
    i = var0+var1
    var0 = var1
    var1 = i
 
#RETO 3

for var in range (1,101):
    divisores = 0
    for i in range (1,101):
        if var%i == 0:
            divisores+=1
    if divisores == 2:
        print (f"{var} es un numero primo")

#RETO 4

poli = input("Ingrese el poligono del cual hallara el area(triangulo,cuadrado,rectangulo): ")

if poli.lower() == "triangulo": 
    base = int(input("Ingrese la base: "))
    altura = int(input("Ingrese la altura: "))
    
    print (f"El area es {(base*altura)/2}")
       
elif poli.lower() == "cuadrado":
    lado = int(input("Ingrese el lado: "))
    
    print (f"El area es {lado**2}")

elif poli.lower() == "rectangulo":
    base = int(input("Ingrese la base: "))
    altura = int(input("Ingrese la altura: "))
    
    print (f"El area es {base*altura}")
"""
#RETO 6

inver = input("Ingresa una frase o palabra: ")

print("".join(reversed(inver)))




    
    

    
    

       

 
    


