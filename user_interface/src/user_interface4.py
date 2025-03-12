welcome_message = """ 
    Bienvenido al sistema "Control de motor"
    Introduce una velocidad dentro de intervalo (0 - 255) y dirección (I ó D), o STOP para detener el motor: 
"""

print(welcome_message)
      
while True:
    user_velocity = input("-> ").strip().upper()
    
    if user_velocity == "STOP":
        motor_info = {"velocidad": 0, "dirección": "STOP"}
        print(motor_info, "\nEl motor se ha detenido.")
        break

    parts = user_velocity.split()
    if len(parts) != 2 or not parts[0].isdigit() or parts[1] not in "ID":
        print("Error: Formato incorrecto. Usa '100 I' o 'STOP'.")
        continue

    velocity = int(parts[0])
    direction = parts[1]

    if 0 <= velocity <= 225:

        motor_info = {"velocidad": velocity,
                       "dirección": direction}
        
        print(motor_info, f"\nEl motor gira {'CWW' if direction == 'I' else 'CW'} a {velocity} RPM.")
    else:
        print("Error: Velocidad fuera de rango.")