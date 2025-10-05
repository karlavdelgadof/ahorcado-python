import random

# ==================================
#   DIBUJOS DEL AHORCADO (ART ASCII)
# ==================================

# 6 intentos → 6 etapas
dibujo_ahorcado_6 = [
  r'''
  ========
  ''',
  r'''
     +---+
     |   |
         |
         |
         |
         |
  =========
  ''',
  r'''
     +---+
     |   |
     O   |
         |
         |
         |
  =========
  ''',
  r'''
     +---+
     |   |
     O   |
     |   |
         |
         |
  =========
  ''',
  r'''
     +---+
     |   |
     O   |
    /|   |
         |
         |
  =========
  ''',
  r'''
     +---+
     |   |
     O   |
    /|\  |
         |
         |
  =========
  ''',
  r'''
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
  =========
  '''
]

# 9 intentos → 9 etapas
dibujo_ahorcado_9 = [
  r'''
  =========
  ''',
  r'''
     +---+
         |
         |
         |
         |
         |
  =========
  ''',
  r'''
     +---+
     |   |
         |
         |
         |
         |
  =========
  ''',
  r'''
     +---+
     |   |
     O   |
         |
         |
         |
  =========
  ''',
  r'''
     +---+
     |   |
     O   |
     |   |
         |
         |
  =========
  ''',
  r'''
     +---+
     |   |
     O   |
    /|   |
         |
         |
  =========
  ''',
  r'''
     +---+
     |   |
     O   |
    /|\  |
         |
         |
  =========
  ''',
  r'''
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
  =========
  ''',
  r'''
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
  =========
  ''',
  r'''
     +---+
     |   |
     X   |
    /|\  |
    / \  |
         |
  =========
  '''
]

# 12 intentos → 12 etapas
dibujo_ahorcado_12 = [
  r'''
  =========
  ''',
  r'''
         +
         |
         |
         |
         |
  =========
  ''',
  r'''
     +---+
         |
         |
         |
         |
  =========
  ''',
  r'''
     +---+
     |   |
         |
         |
         |
  =========
  ''',
  r'''
     +---+
     |   |
     O   |
         |
         |
  =========
  ''',
  r'''
     +---+
     |   |
     O   |
     |   |
         |
  =========
  ''',
  r'''
     +---+
     |   |
     O   |
    /|   |
         |
  =========
  ''',
  r'''
     +---+
     |   |
     O   |
    /|\  |
         |
  =========
  ''',
  r'''
     +---+
     |   |
     O   |
    /|\  |
     |   |
  =========
  ''',
  r'''
     +---+
     |   |
     O   |
    /|\  |
    /    |
  =========
  ''',
  r'''
     +---+
     |   |
     O   |
    /|\  |
    / \  |
  =========
  ''',
  r'''
     +---+
     |   |
     o   |
    /|\  |
    / \  |
  =========
  ''',
  r'''
     +---+
     |   |
     X   |
    /|\  |
    / \  |
  =========
  '''
]

# =================================
#   MAPEO DE DIBUJOS SEGÚN INTENTOS
# =================================
dibujos_por_intentos = {
  6: dibujo_ahorcado_6,
  9: dibujo_ahorcado_9,
  12: dibujo_ahorcado_12,
}

# =======================
#   LISTA DE PALABRAS
# =======================

palabras = {
  "facil": ["gato", "perro", "casa", "árbol", "libro", "mesa", "silla", "coche", "flor", "sol", "luna", "agua", "fuego", "tierra", "aire"],
  "medio": ["elefante", "computadora", "avión", "montaña", "teléfono", "ventana", "reloj", "camión", "bicicleta", "ciudad", "jardín", "escuela", "hospital", "restaurante", "biblioteca"],
  "dificil": ["hipopótamo", "paralelepípedo", "otorrinolaringólogo", "anticonstitucionalmente", "electroencefalografista", "desoxirribonucleico", "inconstitucionalidad", "esternocleidomastoideo", "antropomorfización", "psiconeuroinmunología"]
}

# =======================
#   INICIO DEL JUEGO
# =======================
print("\n🎯 ¡Bienvenido al Juego del Ahorcado! 🎯")
nivel_seleccionado = input("\nElige un nivel de dificultad (F - Fácil, M - Medio, D - Difícil): ").lower()

if nivel_seleccionado == 'f':
    palabra_seleccionada = random.choice(palabras["facil"])
    intentos = 6
elif nivel_seleccionado == 'm':
    palabra_seleccionada = random.choice(palabras["medio"])
    intentos = 9
elif nivel_seleccionado == 'd':
    palabra_seleccionada = random.choice(palabras["dificil"])
    intentos = 12
else:
    print("⚠️ Nivel no válido. Por favor, elige F, M o D.")
    exit()

dibujo_ahorcado = dibujos_por_intentos[intentos]

# Convertir palabra a mayúsculas
palabra_seleccionada = palabra_seleccionada.upper()
palabra_oculta = ['_' for _ in palabra_seleccionada]
letras_utilizadas = []
fallos = 0

print("\n" + dibujo_ahorcado[0])
print("\n🔤 Palabra a adivinar: " + ' '.join(palabra_oculta))
print(f"💪 Tienes {intentos} intentos totales.\n")

# =======================
#   BUCLE PRINCIPAL
# =======================
while fallos < intentos and '_' in palabra_oculta:
    letra = input("👉 Adivina una letra: ").upper()

    if len(letra) != 1 or not letra.isalpha():
        print("\n⚠️ Por favor, ingresa una sola letra válida.\n")
        continue
    if letra in letras_utilizadas:
        print("\nℹ️ Ya has utilizado esa letra. Intenta con otra.\n")
        continue

    letras_utilizadas.append(letra)

    if letra in palabra_seleccionada:
        print("\n✅ ¡Bien hecho! Encontraste una letra.")
        for idx, char in enumerate(palabra_seleccionada):
            if char == letra:
                palabra_oculta[idx] = letra
    else:
        fallos += 1
        restantes = intentos - fallos
        print(f"\n❌ La letra '{letra}' no está en la palabra. Te quedan {restantes} intentos.")
        print(dibujo_ahorcado[min(fallos, len(dibujo_ahorcado) - 1)])

    print("\n🔤 Palabra: " + ' '.join(palabra_oculta))
    print("📚 Letras utilizadas: " + ', '.join(letras_utilizadas))
    print("─────────────────────────────\n")

# =======================
#   RESULTADOS FINALES
# =======================
if '_' not in palabra_oculta:
    print(f"🎉 ¡Felicidades! Has adivinado la palabra: {palabra_seleccionada} 🎉\n")
else:
    print(f"💀 Lo siento, te has quedado sin intentos. La palabra era: {palabra_seleccionada}\n")
    print(dibujo_ahorcado[-1])

# =======================
#   REINICIO DEL JUEGO
# =======================
juego = input("¿Quieres jugar otra vez? (S/N): ").lower()
if juego == 's':
    exec(open("main.py").read())
else:
    print("\n👋 ¡Gracias por jugar al ahorcado! ¡Hasta la próxima!\n")
