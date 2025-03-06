welcome_message ="""
     BIENVENIDO AL SISTEMA "CONTROL DE MOTOR"

Para comenzar, debes introducir una velocidad deseada:
Introduce la velocidad: debe estar en el intervalo [0 255]: """
user_velocity = ""

while True:
  
    user_velocity = input(welcome_message)

    if user_velocity.isnumeric():
        user_velocity = int(user_velocity)
        if user_velocity<=255:
            break
        else:
            print("La velocidad no esta en un rango valido")
    else:
        print("El usuario no ingreso una velocidad valida")

print(user_velocity)