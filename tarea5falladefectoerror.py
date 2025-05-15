# -*- coding: utf-8 -*-

# login_module.py
# Este código implementa un módulo de inicio de sesión con dos fallas intencionales
# para ejemplificar los conceptos de error, defecto y falla en testing de software.

import getpass

# Diccionario de usuarios simulados
usuarios = {
    "tefo": "1234",
    "sebas": "abcd",
    "jeff": "admin"
}

def iniciar_sesion():
    intentos = 3

    while intentos > 0:
        usuario = input("Usuario: ")
        clave = getpass.getpass("Contraseña: ")

        # Falla 1: Aunque el usuario ingrese bien su usuario y contraseña,
        # el sistema no permite iniciar sesión.
        # Error: El programador cree que 'is' compara valores de texto.
        # Defecto: Se usa 'is' en lugar de '=='.
        # Falla: Acceso denegado aunque las credenciales sean correctas.
        if usuario in usuarios and usuarios[usuario] is clave:
            print("Inicio de sesión exitoso")
            return True
        else:
            print("Credenciales incorrectas")
            intentos -= 1
            print(f"Intentos restantes: {intentos}")

    # Falla 2: El sistema no bloquea realmente el acceso después de 3 intentos.
    # Error: El programador cree que el mensaje final es suficiente.
    # Defecto: El ciclo no se detiene, el sistema permite seguir intentando.
    # Falla: Aunque se muestre el mensaje de bloqueo, no hay ningún control real
    #        que impida continuar usando el sistema.

    print("Demasiados intentos fallidos. Acceso bloqueado.")
    # El return False no es efectivo porque el programa ya ejecutó todo, pero podría repetirse el proceso.

# No hay control de cierre, por lo tanto el sistema sigue activo y vulnerable.

if __name__ == "__main__":
    while True:
        iniciar_sesion()
