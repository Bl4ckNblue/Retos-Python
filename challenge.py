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

#RETO 6

inver = input("Ingresa una frase o palabra: ")

print("".join(reversed(inver)))

#RETO 7
st = "Hola me llamo hola"
tex = st.split()
frecuencia = {}

for palabra in tex:
    palabra = palabra.lower()  # Convertir a minúsculas para considerar mayúsculas y minúsculas como iguales
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] =2+
#RETO 8    
    
n = 255
b = []
while n > 0:
    residuo = n % 2
    b.append(str(residuo))
    n = n // 2
b.reverse()

st = ' '.join(b)
print (st)


#RETO 9

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}

tex = input("Ingrese un texto: ")
morse = " "
for char in tex.upper():
    if char == " ":
        morse += " "
    elif char in MORSE_CODE_DICT:
        morse += MORSE_CODE_DICT[char] + " "
    else:
        morse += char

print (morse)    
"""

#RETO 10 



    
    

       

 
    


