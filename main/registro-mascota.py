Silicon Vallei
#0821

\eliam — 05/15/2022
Semana 1 Ciclo 2 Open 🏁
Andres — Yesterday at 10:00 AM
def crear_mascota(id,nombre,edad,peso,tipo_macosta):
        mascota = []
        mascota.append(id)
        mascota.append(nombre)
        mascota.append(edad)
        mascota.append(peso)
Expand
ejer_5162022.txt
3 KB
\eliam
 pinned 
a message
 to this channel. See all 
pinned messages
.
 — Yesterday at 10:01 AM
Marlonubeimar — Yesterday at 11:41 AM
Cuando se empieza el ciclo 2 que no me di cuenta
\eliam — Yesterday at 11:47 AM
Hoy inicio compañero
Image
\eliam
 pinned 
a message
 to this channel. See all 
pinned messages
.
 — Yesterday at 11:47 AM
Marlonubeimar — Yesterday at 11:47 AM
Pues si estuve en clase
Pero no escuché
Jajaja
Cómo que me perdí
\eliam — Yesterday at 11:49 AM
El ciclo uno concluyo con el reto #4
OARG — Yesterday at 11:58 AM
No se supone que cada ciclo dura aproximadamente 2 meses?
\eliam — Yesterday at 11:58 AM
ahora estoy confundido yo jaja 
Marlonubeimar — Yesterday at 11:59 AM
Pues te gon entendido que dura soda meses cada ciclo
OARG — Yesterday at 11:59 AM
Yo diría que el ciclo 1 finaliza cuando se finalice FUNDAMENTOS DE PROGRMACION
Marlonubeimar — Yesterday at 11:59 AM
Y en cada ciclo toca escoger los horarios
OARG — Yesterday at 12:00 PM
Exacto
Marlonubeimar — Yesterday at 12:00 PM
Lo que piensi es que lo dividen en dos cortes
Y ahora terminó el primer corte
\eliam — Yesterday at 12:00 PM
oh gracias por esa aclaracion compañeros, eso es importante para la estructura del servidor
lo ajustare entonces
OARG — Yesterday at 12:01 PM
En total son 7 retos por el ciclo 1
\eliam — Yesterday at 12:03 PM
quitando el 1ro que fue la semana 1
OARG — Yesterday at 12:05 PM
Incluyendo la semana 1
Es un módulo por semana
\eliam — Yesterday at 12:06 PM
oh vale entonces son solo 7 semanas(modulos) este priemr ciclo 
OARG — Yesterday at 12:06 PM
Y en moodle llega hasta el modulo 7
OARG — Yesterday at 12:06 PM
Creería yo son 7 semanas para todos los ciclos
Sacando cuentas que finalizamos en diciembre
\eliam — Yesterday at 12:07 PM
maravilloso
Alento — Yesterday at 12:07 PM
Nuestro profesor dijo que eran 7 semanas por ciclo y que entre ciclos nos dan como una semana para terminar de entregar todo y de saldar notas antes de proseguir y revisar quienes salen por asistencia o por no entregar trabajos.
Algo así le entendí
Alento — Yesterday at 12:08 PM
Si, a finales de noviembre principios de diciembre. Creo que hasta el 10 hay como plazo de tener notas o entregar lo que falte de ese ciclo
germangb — Yesterday at 12:24 PM
Buenas tardes compañeros, ya vi el reto y la verdad no entendí nada, vi el desarrollo del ejercicio enviado por Andres (de paso muchassss gracias), y entendí mas o menos, es posible que se hagan sesiones para poder entender cada paso?
steranc — Yesterday at 12:27 PM
Ese reto se ve duro, yo también lo revise. Se recomienda que todos vean los vídeos de esta semana que es el módulo 5
Andres — Yesterday at 12:27 PM
me tienen confundidos con esos retos
entren al canal charlando
steranc — Yesterday at 12:27 PM
Es lo que vamos a trabajar porque vi que lo de tuplas y eso es del módulo 5
Fabio Andrés Bonilla — Yesterday at 12:28 PM
hola
Andres — Yesterday at 12:29 PM
por eso hay compañeros con retos difrentes si es asi entren al canal charlando
steranc — Yesterday at 12:29 PM
Ah
iseaad — Today at 10:43 AM
Hola, les comparto el reto que le corresponde a mi grupo, veo que es algo diferente pero va enlazado al anterior
Attachment file type: acrobat
Reto_05_Estudiantes.pdf
3.23 MB
﻿
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
ejer_5162022.txt
3 KB
