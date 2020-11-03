# Juego de adivinanzas
import random
import time
from datetime import datetime

intentos = 0

nombre = input("Hola \U0001f604 ¿Cómo te llamas?  -->   ")


time.sleep(2)

print(f'De acuerdo {nombre}, intentaré no olvidarme tú nombre \U0001f604')
time.sleep(4)

fecha = datetime.now()
hora = datetime.now()
fecha = fecha.strftime("%Y-%m-%d")
hora = hora.strftime("%H:%M:%S")
print(f'Hoy es: {fecha} y son las  {hora} una hora menos en Canarias\n')

time.sleep(2)
num = random.randint(1, 11)
print('Te explico el juego. Tengo en mente un número entre 0 y 10.')
time.sleep(2)
while intentos < 5:
     print('Prueba a ver si eres capaz de adivinarlo.')
     time.sleep(2)
     valor = int(input("Escribelo ya: "))
     intentos = intentos + 1
     if valor > num:
         print('El número es demasiado alto')
     if valor < num:
         print('El número es demasiado bajo')
     if valor == num:
         break

if valor == num:
     intentos = str(intentos)
     print('GENIAL!!!!!!, ' + nombre + '!!!! Has acertado el número en  ' + intentos + ' intentos')

if valor != num:
     num = str(num)
     print('Vaya... '+ nombre + '  No has acertado!!!!  \nEl número era ' + num)
     time.sleep(2)
     print('Pueba de nuevo a ver si tienes más suerte')
