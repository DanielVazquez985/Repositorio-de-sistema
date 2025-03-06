descripcion= {"Nombre":"Daniel Alberto",
        'Apellido':"Vazquez Camacho",
        'Edad':"20",
        'sexo':"Masculino",
        'curp':"VACD040828HTSZMNA8",
        'Fecha_de_nacimiento':"28 agosto de 2004",
        'Lugar_de_nacimiento':"Ciudad Victoria",
        'Tipo_de_sangre':"O+",
        'Telefono':"834 115 2295",
        'Correo_electrónico':"vazquezcamachodaniel7@gmail.com",
         } 

for clave, valor in descripcion.items():
    print(f"{clave.replace("_"," ").title()}: {valor if valor else "No especificado"}")