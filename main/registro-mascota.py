def crear_mascota(id,nombre,edad,peso,tipo_macosta):
        mascota = []
        mascota.append(id)
        mascota.append(nombre)
        mascota.append(edad)
        mascota.append(peso)
        mascota.append(tipo_macosta)
        return tuple(mascota)


if __name__ == '__main__':
    numero_macota = 2

    mascotas=[(0,'benji',2,9,'perro'),(1,'nasu',1,3,'gato')]
    print('Bienvenido')
    while True:
        print('Opciones:\n1.Crear nueva mascota\n2.Ver mascotas\n3.Salir')
        opc = int(input('Ingresar opcion: '))
        if opc == 1:
            id = numero_macota
            nombre = input('nombre: ')
            edad = int(input('edad: '))
            peso = float(input('peso'))
            tipo_macosta = input('tipo mascota')
            mascotas.append(crear_mascota(id,nombre,edad,peso,tipo_macosta))
            numero_macota += 1
        elif opc == 2:
            print('Opciones:\n1.Buscar mascota por nombre\n2.buscar mascota por id\n3.Salir')
            opc = int(input('Ingresar opcion: '))
            while True:
                if opc == 1:
                    nombre_mascota = input('Nombre de la mascota')
                    mascota = [mascotas[mascota] for mascota in range(0,len(mascotas)) if mascotas[mascota][1] == nombre_mascota]
                    print(f'Numero de ingreso: {mascota[0][0]} Nombre: {mascota[0][1]} Edad: {mascota[0][2]} años Peso: {mascota[0][3]} kg Tipo de mascota: {mascota[0][4]}')
                    break
                elif opc == 2:
                    id_mascota = int(input('id de la mascota'))
                    mascota = [mascotas[mascota] for mascota in range(0, len(mascotas)) if mascotas[mascota][0] == id_mascota]
                    print(f'Numero de ingreso: {mascota[0][0]} Nombre: {mascota[0][1]} Edad: {mascota[0][2]} años Peso: {mascota[0][3]} kg Tipo de mascota: {mascota[0][4]}')
                    break
                elif opc == 3:
                    break
        elif opc == 3:
            break
