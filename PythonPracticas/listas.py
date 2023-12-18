"""
import calendar
yy = 2023 
mm = 12

print (calendar.month(yy,mm))
"""
import random
palabras_posibles = ["python", "programacion", "tecnologia", "ciencia", "computadora", "inteligencia", "artificial", "desarrollo", "aprendizaje", "datos", "algoritmo", "web", "internet", "seguridad", "criptografia", "software", "hardware", "ingenieria", "proyecto", "innovacion", "robotica"]


while True:
    secret = random.choice(palabras_posibles)
    secreto = [' _ ']*len(secret)
    letras = []
    count = 6
    for i in secret:
        letras.append(i)
    print ("\nADIVINA LA PALABRA")

    while count!= 0:
        print (f"\nPista: {' '.join(secreto).upper()}")
        respuesta = input("\nEscribe una letra o la palabra si es que la descubriste: ")
        
        if respuesta == secret:
            print (f"Ganaste, la palabra era ''{' '.join(secret).upper()}''")
            break
        
        elif respuesta in letras:
            print ("\nSi está")
            
            for e in range(len(secret)):
                if secret[e] == respuesta:
                    secreto [e] = respuesta
        
        else:
            count -= 1
            
            print (f"\nNo está. Intenta con otra letra, te quedan {count} intentos")
    else:
        print ("\nTe quedaste sin intentos")
        print (f"La palabra era {' '.join(secret.upper())}")
    
    otra = input("Desea jugar otra vez? (y/n)")
    if otra == "n":
        break
        
 

    