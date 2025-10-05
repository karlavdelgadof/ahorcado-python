import random

# Lista de palabras por nivel de dificultad
palabras = {
  "facil": ["gato", "perro", "casa", "árbol", "libro", "mesa", "silla", "coche", "flor", "sol", "luna", "agua", "fuego", "tierra", "aire"],
  "medio": ["elefante", "computadora", "avión", "montaña", "teléfono", "ventana", "reloj", "camión", "bicicleta", "ciudad", "jardín", "escuela", "hospital", "restaurante", "biblioteca"],
  "dificil": ["hipopótamo", "paralelepípedo", "otorrinolaringólogo", "anticonstitucionalmente", "electroencefalografista", "desoxirribonucleico", "inconstitucionalidad", "esternocleidomastoideo", "antropomorfización", "psiconeuroinmunología"]
}
intentos = 0
letras_utilizadas = []
palabra_oculta = []
palabra_seleccionada = ""

# Inicio del juego y selección de nivel
nivel_seleccionado = input("Juguemos al ahorcado! Elige un nivel de dificultad (F - Fácil, M - Medio, D - Difícil): ").lower()

# Selección de la palabra según el nivel
if nivel_seleccionado == 'f':
  # Selección de una palabra fácil
  palabra_seleccionada = random.choice(palabras["facil"])
  intentos = len(palabra_seleccionada) + 1
elif nivel_seleccionado == 'm':
    # Selección de una palabra media
    palabra_seleccionada = random.choice(palabras["medio"])
    intentos = len(palabra_seleccionada) + 2
elif nivel_seleccionado == 'd':
    # Selección de una palabra difícil
    palabra_seleccionada = random.choice(palabras["dificil"])
    intentos = len(palabra_seleccionada) + 3
else:
    print("Nivel no válido. Por favor, elige F, M o D.")
    exit()

# Inicialización de la palabra oculta con guiones
palabra_oculta = ['_' for _ in palabra_seleccionada]

# Mostrar estado inicial del juego
print("Palabra a adivinar: " + ' '.join(palabra_oculta))
print("Tienes " + str(intentos) + " intentos para adivinar la palabra.")
print("Letras utilizadas: " + ', '.join(letras_utilizadas))

# Bucle principal del juego
while intentos > 0 and '_' in palabra_oculta:
    letra = input("Adivina una letra: ").lower()

    # Validación de entrada
    if len(letra) != 1 or not letra.isalpha():
        print("Por favor, ingresa una sola letra válida.")
        continue
    elif letra in letras_utilizadas:
        print("Ya has utilizado esa letra. Intenta nuevamente con otra.")
        continue

    # Añadir la letra a las letras utilizadas
    letras_utilizadas.append(letra)

    # Comprobar si la letra está en la palabra seleccionada
    if letra in palabra_seleccionada:
      print("¡Bien hecho! Encontraste una letra.")
      for idx, char in enumerate(palabra_seleccionada):
        if char == letra:
          palabra_oculta[idx] = letra
    else:
        intentos -= 1
        print("La letra '" + letra + "' no está en la palabra. Te quedan " + str(intentos) + " intentos.")

    # Mostrar el estado actual del juego
    print("Palabra a adivinar: " + ' '.join(palabra_oculta))
    print("Letras utilizadas: " + ', '.join(letras_utilizadas))

# Resultado final del juego
if '_' not in palabra_oculta:
    print("¡Felicidades! Has adivinado la palabra: " + palabra_seleccionada)
else:
    print("Lo siento, te has quedado sin intentos. Tu palabra era: " + palabra_seleccionada)

juego = input("Gracias por jugar al ahorcado! Quieres intentarlo de nuevo? (S/N): ").lower()

if juego == 's':
  exec(open("main.py").read())
else:
  print("¡Hasta la próxima!")
