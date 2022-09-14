import random
import time

iniciar_trivia = True  # Iniciamos la variable en True
intentos = 0  # variable que almacenará el número de veces que el usuario intenta nuestra trivia.

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

puntaje = random.randint(0, 10)

# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia
print (BLUE+"Bienvenido a mi trivia sobre one piece"+RESET)
time.sleep(2)

print ("Pondre a prueba tus conocimientos")
time.sleep(2)

print(RED+"Tienes", puntaje, "puntos"+RESET)
time.sleep(2)

nombre = input("Ingresa tu nombre nakama: ")

print(BLUE+"\n Hola nakama", nombre, "responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n"+RESET)
time.sleep(2)

while iniciar_trivia == True: #  Mientras iniciar_trivia sea True, repite:
  intentos += 1
  puntaje = 0

  print("\nIntento número:", intentos)
  input("Presiona Enter para continuar")

  # Pregunta 1
  print ("1) ¿Como se llama el protagonista de one piece?")
  time.sleep(1)
  print ("a) Chopper")
  time.sleep(1)
  print ("b) Naruto")
  time.sleep(1)
  print ("c) Monkey D. luffy")
  time.sleep(1)
  print ("d) Zoro Roronoa")
  time.sleep(1)
  
  # Almacenamos la respuesta del usuario en la variable "respuesta_1"
  respuesta_1 = input("\nTu respuesta: ")
  
  while respuesta_1 not in ("a", "b", "c", "d", "x"):
    respuesta_1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  
  if respuesta_1 == "c":
    puntaje += random.randint(0, 10)
    print(GREEN+"Muy bien", nombre, "llevas", puntaje, "puntos!\n"+RESET)
  
  elif respuesta_1 == "x":
    puntaje += random.randint(20, 30)
    print(YELLOW+"esta es un mensaje secreto", nombre, "llevas", puntaje, "puntos!\n"+RESET)
    
  else :
    puntaje -= random.randint(0, 10)
    print(RED+"Incorrecto", nombre, "llevas", puntaje, "puntos!\n"+ RESET)
  
  time.sleep(3)
    
  print ("1) ¿Cual es la fruta preferida de Nami?")
  time.sleep(1)
  print ("a) Durazno")
  time.sleep(1)
  print ("b) Mandarina")
  time.sleep(1)
  print ("c) Naranja")
  time.sleep(1)
  print ("d) Platano")
  time.sleep(1)
  
  respuesta_2 = input("\nTu respuesta: ")
  
  while respuesta_2 not in ("a", "b", "c", "d", "j"):
    respuesta_2 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  
  if respuesta_2 == "b":
    puntaje *= random.randint(0, 10)
    print(GREEN+"Muy bien", nombre, "llevas", puntaje, "puntos!\n"+RESET)
  
  elif respuesta_1 == "j":
    puntaje += random.randint(20, 30)
    print(YELLOW+"esta es un mensaje secreto", nombre, "llevas", puntaje, "puntos!\n"+RESET)
    
  else :
    puntaje /= random.randint(0, 10)
    print(RED+"Incorrecto", nombre, "llevas", puntaje, "puntos!\n"+ RESET)
  
  time.sleep(3)
    
  print ("1) ¿Cual fue la primera katana de Zoro Roronoa?")
  time.sleep(1)
  print ("a) Shusui")
  time.sleep(1)
  print ("b) Ichimonji")
  time.sleep(1)
  print ("c) Kiketsu")
  time.sleep(1)
  print ("d) Enma")
  time.sleep(1)
  
  respuesta_3 = input("\nTu respuesta: ")
  
  while respuesta_3 not in ("a", "b", "c", "d", "o"):
    respuesta_3 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  
  if respuesta_3 == "b":
    puntaje += random.randint(0, 10)
    print(GREEN+"Muy bien", nombre, "llevas", puntaje, "puntos!\n"+RESET)
  
  elif respuesta_1 == "o":
    puntaje += random.randint(20, 30)
    print(YELLOW+"esta es un mensaje secreto", nombre, "llevas", puntaje, "puntos!\n"+RESET)
    
  else :
    puntaje -= random.randint(0, 10)
    print(RED+"Incorrecto", nombre, "llevas", puntaje, "puntos!\n"+ RESET)
  
  time.sleep(3)
  
  print ("1) ¿En que arco se un el doctor de la tripulación?")
  time.sleep(1)
  print ("a) Arabasta")
  time.sleep(1)
  print ("b) La isla del cielo")
  time.sleep(1)
  print ("c) Isla Drum")
  time.sleep(1)
  print ("d) Wano")
  time.sleep(1)
  
  respuesta_4 = input("\nTu respuesta: ")
  
  while respuesta_4 not in ("a", "b", "c", "d", "j"):
    respuesta_4 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
    
  if respuesta_4 == "a":
    puntaje -= random.randint(0, 10)
    print(RED+"Incorrecto!", nombre, "mmmmmm"+RESET)
    
  elif respuesta_4 == "b":
    puntaje -= random.randint(0, 10)
    print(RED+"Incorrecto!", nombre, "Nooooo"+RESET)
    
  elif respuesta_4 == "d":
    puntaje -= random.randint(0, 10)
    print(RED+"Incorrecto!", nombre, "No has visto one piece"+RESET)
    
  else:
    puntaje += random.randint(0, 10)
    print (GREEN+"Muy bien", nombre, "!"+RESET)
  
  time.sleep(4) 
  
  print (BLUE+"Gracias", nombre, "por jugar mi trivia, alcanzaste", puntaje, "puntos"+RESET)

  print("\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()
  if repetir_trivia != "si":  # != significa "distinto"
   print("\nEspero {nombre} que lo hayas pasado bien, hasta pronto!")
   iniciar_trivia = False  # Cambiamos el valor de iniciar_trivia a False para evitar que se repita.

