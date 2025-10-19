import csv
import unicodedata

def quitar_acentos(s: str) -> str:
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

def normalizar(s: str) -> str:
    # Remueve acentos y convierte a mayúsculas
    return quitar_acentos(s).upper()


def cargar_palabras_desde_csv(nombre_archivo: str):
    palabras = {"facil": [], "medio": [], "dificil": []}

    try:
        # utf-8-sig limpia el BOM \ufeff automáticamente
        with open(nombre_archivo, encoding="utf-8-sig", newline="") as f:
            lector = csv.DictReader(f)

            # Verificación de columnas (tolerante a espacios/acentos/caso)
            def norm(h): return quitar_acentos((h or "").strip().lower())
            headers_norm = {norm(h): h for h in (lector.fieldnames or [])}

            col_dificultad = headers_norm.get("dificultad")
            col_palabra    = headers_norm.get("palabra")
            if not col_dificultad or not col_palabra:
                raise KeyError("Faltan columnas requeridas")

            for fila in lector:
                nivel_raw   = (fila.get(col_dificultad) or "").strip()
                palabra_raw = (fila.get(col_palabra) or "").strip()
                if not nivel_raw or not palabra_raw:
                    continue

                # Normaliza el nivel a claves del diccionario
                nivel_norm = quitar_acentos(nivel_raw).strip().lower()  # “Fácil” -> “facil”
                palabra    = palabra_raw.strip().lower()

                if nivel_norm in palabras:
                    palabras[nivel_norm].append(palabra)
                else:
                    print(f"⚠️ Nivel desconocido '{nivel_raw}' (→ '{nivel_norm}'). Palabra: {palabra_raw}")

        return palabras

    except FileNotFoundError:
        print(f"❌ No se encontró el archivo '{nombre_archivo}'.")
    except KeyError:
        print("❌ El CSV debe tener las columnas: 'Dificultad' y 'Palabra'.")
    except Exception as e:
        print(f"⚠️ Error al leer el archivo: {e}")

    # En caso de error, devuelve estructura vacía
    return {"facil": [], "medio": [], "dificil": []}
