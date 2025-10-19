import random
from dibujo_ahorcado import dibujos_por_intentos
from helpers import (
    cargar_palabras_desde_csv,
    normalizar,
)

try:
    pass
except Exception as e:
    # Fallback en caso de error al importar dibujos
    print(f"⚠️ No se pudieron cargar los dibujos: {e}")
    dibujos_por_intentos = {
        6: ["(dibujo no disponible)"],
        9: ["(dibujo no disponible)"],
        12: ["(dibujo no disponible)"],
    }

# ====================================
#   LISTA DE PALABRAS EXTRAÍDAS DE CSV
# ====================================

palabras = cargar_palabras_desde_csv("palabras_juego.csv")

# =======================
#   INICIO DEL JUEGO
# =======================
def inicializar_juego():
    print("\n🎯 ¡Bienvenido al Juego del Ahorcado! 🎯")
    nivel = input("Elige un nivel de dificultad (F - Fácil, M - Medio, D - Difícil): ").lower()

    if nivel == 'f':
        palabra_seleccionada = random.choice(palabras["facil"])
        intentos = 6
    elif nivel == 'm':
        palabra_seleccionada = random.choice(palabras["medio"])
        intentos = 9
    elif nivel == 'd':
        palabra_seleccionada = random.choice(palabras["dificil"])
        intentos = 12
    else:
        print("⚠️ Nivel no válido. Por favor, elige F, M o D.")
        exit()

    return palabra_seleccionada.upper(), intentos, dibujos_por_intentos[intentos]


def mostrar_estado_inicial(palabra, intentos, dibujo):
    palabra_oculta = ['_' for _ in palabra]
    print("\n" + dibujo[0])
    print(f"\n🔤 Palabra a adivinar: {' '.join(palabra_oculta)}")
    print(f"💪 Tienes {intentos} intentos totales.\n")
    return palabra_oculta


def pedir_letra(letras_utilizadas):
    while True:
        letra = input("👉 Adivina una letra: ").upper()
        if len(letra) != 1 or not letra.isalpha():
            print("⚠️ Por favor ingresa una sola letra válida.\n")
            continue
        letra_base = normalizar(letra)
        if letra_base in letras_utilizadas:
            print("\nℹ️ Ya has utilizado esa letra. Intenta con otra.\n")
            continue
        return letra_base


def actualizar_palabra_oculta(palabra_original, palabra_base, palabra_oculta, letra_base):
    for idx, char_base in enumerate(palabra_base):
        if char_base == letra_base:
            palabra_oculta[idx] = palabra_original[idx]
    return palabra_oculta


def mostrar_estado_actual(palabra_oculta, letras_utilizadas, dibujo, fallos):
    print(dibujo[min(fallos, len(dibujo) - 1)])
    print("\n🔤 Palabra:", ' '.join(palabra_oculta))
    print("📚 Letras utilizadas:", ', '.join(letras_utilizadas))
    print("─────────────────────────────\n")


def jugar():
    palabra_seleccionada, intentos, dibujo = inicializar_juego()
    # Normaliza la palabra seleccionada para comparaciones
    palabra_base = normalizar(palabra_seleccionada)
    palabra_oculta = mostrar_estado_inicial(palabra_seleccionada, intentos, dibujo)
    letras_utilizadas = []
    fallos = 0

    while fallos < intentos and '_' in palabra_oculta:
        letra_base = pedir_letra(letras_utilizadas)
        letras_utilizadas.append(letra_base)

        if letra_base in palabra_base:
            print("✅ ¡Bien hecho! Has adivinado una letra.")
            palabra_oculta = actualizar_palabra_oculta(palabra_seleccionada, palabra_base, palabra_oculta, letra_base)
        else:
            fallos += 1
            print(f"❌ La letra '{letra_base}' no existe en la palabra. Te quedan {intentos - fallos} intentos.")

        mostrar_estado_actual(palabra_oculta, letras_utilizadas, dibujo, fallos)

    if '_' not in palabra_oculta:
        print(f"🎉 ¡Felicidades! Has adivinado la palabra: {palabra_seleccionada} 🎉\n")
    else:
        print(f"💀 Lo siento, te has quedado sin intentos. La palabra era: {palabra_seleccionada}\n")
        print(dibujo[-1])


def reiniciar_juego():
    while True:
        opcion = input("¿Quieres jugar otra vez? (S/N): ").lower()
        if opcion == 's':
            jugar()
        elif opcion == 'n':
            print("\n👋 ¡Gracias por jugar al ahorcado!")
            break
        else:
            print("⚠️ Responde con S o N.")


# ========================
#   EJECUCIÓN PRINCIPAL
# ========================
if __name__ == "__main__":
    jugar()
    reiniciar_juego()
