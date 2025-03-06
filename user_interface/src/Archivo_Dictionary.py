def create_dictionary(first_name, last_name,age,height, weight,birth_place, birthday, blood_type, curp):
    user_info = {
        "first_name" : first_name,
        "last_name" : last_name,
        "age" : age,
        "height" : height,
        "weight" : weight,
        "birth_place" : birth_place,
        "birthday" : birthday,
        "blood_type" : blood_type,
        "curp" : curp
        }
    return user_info
print("Ejecutando script...")

diccionario_Daniel = create_dictionary("Daniel", "Camacho", 20, 175, 62, "Ciudad Victoria", "28 de agosto","O+", "VACD040828HTSZMNA8"
)
print(diccionario_Daniel)
