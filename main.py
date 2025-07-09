import string
import random

print("🔐 Generador de Contraseñas Seguras 🔐")

# 1. Pedir longitud de la contraseña
longitud = int(input("¿Cuántos caracteres debe tener tu contraseña?: "))

# 2. Preguntar por tipos de caracteres
usar_mayusculas = input("¿Deseas incluir letras mayúsculas? (s/n): ").lower() == 's'
usar_minusculas = input("¿Deseas incluir letras minúsculas? (s/n): ").lower() == 's'
usar_numeros = input("¿Deseas incluir números? (s/n): ").lower() == 's'
usar_simbolos = input("¿Deseas incluir símbolos? (s/n): ").lower() == 's'

# 3. Validar que eligió al menos un tipo de carácter
if not (usar_mayusculas or usar_minusculas or usar_numeros or usar_simbolos):
    print("❌ Debes elegir al menos un tipo de carácter para generar la contraseña.")
    exit()

# 4. Crear la lista de caracteres posibles
caracteres = ""

if usar_mayusculas:
    caracteres += string.ascii_uppercase  #ABC...Z

if usar_minusculas:
    caracteres += string.ascii_lowercase #abc...z

if usar_numeros:
    caracteres += string.digits #0123456789

if usar_simbolos:
    caracteres += string.punctuation #!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~

# 5. Generar contrase;a y mostrarla
contraseña = ""

for _ in range(longitud):
    caracter_aleatorio = random.choice(caracteres)
    contraseña += caracter_aleatorio

print("\n🔑 Tu contraseña generada es:")
print(contraseña)