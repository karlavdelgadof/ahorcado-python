# 🎯 Juego del Ahorcado en Python

Un juego clásico del ahorcado implementado en Python con arte ASCII y múltiples niveles de dificultad.

## 📖 Descripción

El Juego del Ahorcado es un juego de adivinanzas donde el jugador debe descubrir una palabra oculta letra por letra. Con cada letra incorrecta, se dibuja una parte del ahorcado. El objetivo es adivinar la palabra completa antes de que se complete el dibujo.

## 🎮 Características

- **3 Niveles de Dificultad:**

  - 🟢 **Fácil:** Palabras cortas y comunes (6 intentos)
  - 🟡 **Medio:** Palabras de dificultad moderada (9 intentos)
  - 🔴 **Difícil:** Palabras largas y complejas (12 intentos)

- **Arte ASCII Progresivo:** Dibujos detallados del ahorcado que se van completando con cada error
- **Interfaz Amigable:** Emojis y mensajes claros para una mejor experiencia
- **Validación de Entrada:** Control de letras duplicadas y entradas inválidas
- **Opción de Reinicio:** Posibilidad de jugar múltiples partidas

## 🚀 Cómo Empezar a Jugar

### Requisitos

- Python 3.6 o superior

### Instalación y Ejecución

1. **Clona el repositorio:**

   ```bash
   # Si tienes git instalado
   git clone <url-del-repositorio>

2. **Navega al directorio del juego:**

   ```bash
   cd ahorcado-python
   ```

3. **Ejecuta el juego:**

   ```bash
   python main.py
   ```

   O en algunos sistemas:

   ```bash
   python3 main.py
   ```

### 🎯 Instrucciones de Juego

1. **Selecciona la Dificultad:**

   - Escribe `F` para Fácil
   - Escribe `M` para Medio
   - Escribe `D` para Difícil

2. **Adivina las Letras:**

   - Escribe una letra y presiona Enter
   - Las letras correctas aparecerán en la palabra
   - Las incorrectas agregarán una parte al dibujo del ahorcado

3. **Gana o Pierde:**

   - **Victoria:** Completa la palabra antes de agotar los intentos
   - **Derrota:** Se completa el dibujo del ahorcado

4. **Jugar de Nuevo:**
   - Al final, elige `S` para otra partida o `N` para salir

## 📝 Ejemplo de Juego

```
🎯 ¡Bienvenido al Juego del Ahorcado! 🎯

Elige un nivel de dificultad (F - Fácil, M - Medio, D - Difícil): f

🔤 Palabra a adivinar: _ _ _ _
💪 Tienes 6 intentos totales.

👉 Adivina una letra: a

✅ ¡Bien hecho! Encontraste una letra.

🔤 Palabra: _ A _ A
📚 Letras utilizadas: A
─────────────────────────────
```

## 🎨 Niveles de Dificultad

### 🟢 Fácil (6 intentos)

Palabras como: gato, perro, casa, árbol, libro, mesa, silla, coche, flor, sol...

### 🟡 Medio (9 intentos)

Palabras como: elefante, computadora, avión, montaña, teléfono, ventana, reloj...

### 🔴 Difícil (12 intentos)

Palabras como: hipopótamo, paralelepípedo, otorrinolaringólogo, anticonstitucionalmente...

## 🛠️ Estructura del Código

- **Arte ASCII:** Dibujos progresivos del ahorcado
- **Diccionario de Palabras:** Organizadas por nivel de dificultad
- **Lógica del Juego:** Bucle principal con validaciones
- **Sistema de Reinicio:** Opción para jugar múltiples partidas

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Puedes:

- Añadir más palabras a cualquier nivel
- Mejorar el arte ASCII
- Optimizar el código
- Añadir nuevas características

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

---

¡Disfruta jugando al ahorcado! 🎮✨
