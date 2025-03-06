welcome_message = """
     BIENVENIDO AL SISTEMA "CONTROL DE MOTOR"

Escribe "STOP" para detener el motor
Para comenzar, debes introducir una velocidad deseada:
Introduce la velocidad, debe de estar en el intervalo [-255, 255]:
"""
print(welcome_message) #Mostrar el mensaje solo una vez

while True:
    user_input = input(welcome_message).strip().upper()

    if user_input == "STOP":
        print("Motor detenido.")
        break

    if user_input.lstrip('-').isnumeric():  # Permite números negativos
        user_velocity = int(user_input)
        if -255 <= user_velocity <= 255:
            direction = "Derecha" if user_velocity > 0 else "Izquierda" if user_velocity < 0 else "Detenido"
            print(f"Velocidad establecida: {user_velocity}. Sentido de giro: {direction}.")
            
        else:
            print("La velocidad no está en un rango válido.")
    else:
        print("El usuario no ingreso una velocidad valida")
  