def mostrar_menu():
    print("""
    ============================
         CONTROL DE MOTOR
    ============================
    1. Establecer velocidad
    2. Ver estado del motor
    3. Stop
    4. Salir
    """)

def obtener_velocidad():
    while True:
        try:
            vel = int(input("Introduce la velocidad (-255 a 255): "))
            if -255 <= vel <= 255:
                return vel
            else:
                print("⚠ Error: La velocidad debe estar en el rango [-255, 255].")
        except ValueError:
            print("⚠ Error: Entrada inválida. Ingresa un número entero.")

motor_encendido = True
velocidad = 0
sentido = "Detenido"

print("BIENVENIDO AL SISTEMA 'CONTROL DE MOTOR'")

while motor_encendido:
    mostrar_menu()
    opcion = input("Selecciona una opción: ").strip()

    if opcion == "1":
        velocidad = obtener_velocidad()
        if velocidad > 0:
            sentido = "Derecha"
        elif velocidad < 0:
            sentido = "Izquierda"
        else:
            sentido = "Detenido"
        print(f" Velocidad establecida: {velocidad}. Sentido de giro: {sentido}.")

    elif opcion == "2":
        print(f" Estado actual -> Velocidad: {velocidad}, Sentido: {sentido}")

    elif opcion == "3":
        print(" Motor detenido.")
        velocidad = 0
        sentido = "Detenido"

    elif opcion == "4":
        print(" Saliendo del sistema...")
        motor_encendido = False

    else:
        print("⚠ Opción no válida. Intenta nuevamente.")
