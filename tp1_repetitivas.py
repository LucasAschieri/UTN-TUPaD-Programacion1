# Ejercicio 1
nombre = input("Ingrese su nombre: ")
while not nombre.isalpha():
    nombre = input("Error. Ingrese solo letras: ")

cantidad = input("Ingrese cantidad de productos: ")
while not cantidad.isdigit() or int(cantidad) <= 0:
    cantidad = input("Error. Ingrese un numero mayor a 0: ")

cantidad = int(cantidad)

total_sin = 0
total_con = 0

for i in range(cantidad):
    print(f"\nProducto {i+1}")

    precio = input("Ingrese precio: ")
    while not precio.isdigit():
        precio = input("Error. Ingrese precio valido: ")

    precio = int(precio)
    total_sin += precio 

    desc = input("¿Tiene descuento? (s/n): ").lower()
    while desc != "s" and desc != "n":
        desc = input("Error. Ingrese s o n: ").lower()

    if desc == "s":
        precio_desc = precio * 0.9
    else:
        precio_desc = precio

    total_con += precio_desc

ahorro = total_sin - total_con
promedio = total_con / cantidad

print("\n---RESULTADOS---")
print("Total sin descuento:", total_sin)
print("Total con descuento:", total_con)
print("Ahorro total:", ahorro)
print(f"Promedio por producto: {promedio:.2f}")

#Ejercicio 2
usuario_correcto = "alumno"
clave_correcta = "python123"
intentos = 0

while intentos < 3:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")
    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso correcto")
        break
    else:
        print("Error: credenciales incorrectas")
        intentos += 1
    if intentos == 3:
     print("Cuenta bloquedada")

while True:
    print("1) Estado")
    print("2) Cambiar clave")
    print("3) Mensaje")
    print("4) Salir")
    
    option = input("Elija una opcion: ")

    if not option.isdigit() or int(option) < 1 or int(option) > 4:
        print("Opcion invalida")
        continue

    if option == "1":
        print("Inscripto")

    elif option == "2":
        pass

    elif option == "3":
        print("Segui asi, vas bien")

    elif option == "4":
        break
    
    elif option == "2":
        nueva = input("Ingrese nueva clave: ")
        if len(nueva) < 6:
            print("Clave muy corta")
        while len (nueva) < 6:
            nueva = input("Clave muy corta. Ingrese nueva clave: ")
        
        confirmar = input("Confirme clave: ")

        if nueva != confirmar:
            print("Las claves no coinciden")
        else:
            clave_correcta = nueva
            print("Clave cambiada correctamente")

#Ejercicio 3
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

nombre = input("Ingrese su operador: ")
while not nombre.isalpha():
    nombre = input("Ingrese su operador nuevamente: ")


while True:
    print("\n1) Reservar turno")
    print("2) Cancelar turno")
    print("3) Ver agenda del día")
    print("4) Ver resumen general")
    print("5) Cerrar sistema")

    option = input("Elija una opcion ")

    if not option.isdigit() or int(option) < 1 or int(option) > 5:
        print("Opcion invalida, elija nuevamente")
        continue

    if option == "1":
        dia = input("Elija su dia (1=Lunes, 2=Martes): ")
        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            dia = input("Error. Elija 1 o 2: ")

        paciente = input("Ingrese nombre del paciente: ")
        while not paciente.isalpha():
            paciente = input("Error. Solo letras: ")

        if dia == "1":
            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                print("Paciente ya registrado")
            elif lunes1 == "":
                lunes1 = paciente
            elif lunes2 == "":
                lunes2 = paciente
            elif lunes3 == "":
                lunes3 = paciente
            elif lunes4 == "":
                lunes4 = paciente
            else:
                print("No hay turnos disponibles")

        else:
            if paciente == martes1 or paciente == martes2 or paciente == martes3:
                print("Paciente ya registrado")
            elif martes1 == "":
                martes1 = paciente
            elif martes2 == "":
                martes2 = paciente
            elif martes3 == "":
                martes3 = paciente
            else:
                print("No hay turnos disponibles")

    elif option == "2":
        dia = input("Elija dia (1=Lunes, 2=Martes): ")
        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            dia = input("Error. Elija 1 o 2: ")

        paciente = input("Ingrese nombre a cancelar: ")
        while not paciente.isalpha():
            paciente = input("Error. Solo letras: ")

        if dia == "1":
            if lunes1 == paciente:
                lunes1 = ""
            elif lunes2 == paciente:
                lunes2 = ""
            elif lunes3 == paciente:
                lunes3 = ""
            elif lunes4 == paciente:
                lunes4 = ""
            else:
                print("No encontrado")

        else:
            if martes1 == paciente:
                martes1 = ""
            elif martes2 == paciente:
                martes2 = ""
            elif martes3 == paciente:
                martes3 = ""
            else:
                print("No encontrado")

    elif option == "3":
        dia = input("Elija dia (1=Lunes, 2=Martes): ")

        if dia == "1":
            print("Turno 1:", lunes1 if lunes1 != "" else "(libre)")
            print("Turno 2:", lunes2 if lunes2 != "" else "(libre)")
            print("Turno 3:", lunes3 if lunes3 != "" else "(libre)")
            print("Turno 4:", lunes4 if lunes4 != "" else "(libre)")
        else:
            print("Turno 1:", martes1 if martes1 != "" else "(libre)")
            print("Turno 2:", martes2 if martes2 != "" else "(libre)")
            print("Turno 3:", martes3 if martes3 != "" else "(libre)")
    
    elif option == "4":
        ocupados_lunes = 0
        ocupados_martes = 0

        if lunes1 != "": ocupados_lunes += 1
        if lunes2 != "": ocupados_lunes += 1
        if lunes3 != "": ocupados_lunes += 1
        if lunes4 != "": ocupados_lunes += 1

        if martes1 != "": ocupados_martes += 1
        if martes2 != "": ocupados_martes += 1
        if martes3 != "": ocupados_martes += 1

        print("Lunes ocupados:", ocupados_lunes, "/ 4")
        print("Martes ocupados:", ocupados_martes, "/ 3")

        if ocupados_lunes > ocupados_martes:
            print("Día con más turnos: Lunes")
        elif ocupados_martes > ocupados_lunes:
            print("Día con más turnos: Martes")
        else:
            print("Ambos días tienen igual cantidad")
    elif option == "5":
        print("Sistema cerrado")
        break    

#Ejercicio 4
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
racha_forzar = 0

nombre = input("Ingrese nombre del agente: ")
while not nombre.isalpha():
    nombre = input("Error. Solo letras: ")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:

    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print("SISTEMA BLOQUEADO POR ALARMA")
        break

    print("\n--- ESTADO ---")
    print("Energia:", energia)
    print("Tiempo:", tiempo)
    print("Cerraduras abiertas:", cerraduras_abiertas)
    print("Alarma:", alarma)

    print("\n1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")

    opcion = input("Elija una opcion: ")

    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        opcion = input("Error. Elija 1, 2 o 3: ")

    if opcion == "1":
        energia -= 20
        tiempo -= 2
        racha_forzar += 1

        
        if racha_forzar == 3:
            alarma = True
            print("La cerradura se trabó. Alarma activada.")
            continue

        
        if energia < 40:
            eleccion = input("Riesgo de alarma. Elija un numero (1-3): ")
            while not eleccion.isdigit() or int(eleccion) < 1 or int(eleccion) > 3:
                eleccion = input("Error. Elija 1, 2 o 3: ")

            if eleccion == "3":
                alarma = True
                print("Se activó la alarma.")

        if not alarma:
            cerraduras_abiertas += 1
            print("Cerradura abierta.")

    elif opcion == "2":
        energia -= 10
        tiempo -= 3
        racha_forzar = 0

        for i in range(4):
            print("Hackeando paso", i + 1)
            codigo_parcial += "A"

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("Hackeo exitoso. Cerradura abierta.")

    elif opcion == "3":
        energia += 15
        if energia > 100:
            energia = 100

        tiempo -= 1
        racha_forzar = 0

        if alarma:
            energia -= 10

        print("Descansando...")

if cerraduras_abiertas == 3:
    print("\nVICTORIA. Boveda abierta.")
elif energia <= 0 or tiempo <= 0:
    print("\nDERROTA. Te quedaste sin recursos.")
elif alarma and tiempo <= 3:
    print("\nDERROTA. Sistema bloqueado por alarma.")

#Ejercicio 5
nombre = input("Ingrese nombre del gladiador: ")
while not nombre.isalpha():
    nombre = input("Error: Solo se permiten letras. Ingrese nuevamente: ")

hp_jugador = 100
hp_enemigo = 100

pociones = 3

juego_activo = True

while juego_activo:

    print("\n--- ESTADO ---")
    print(nombre, "HP:", hp_jugador)
    print("Enemigo HP:", hp_enemigo)
    print("Pociones:", pociones)

    print("\n1. Atacar")
    print("2. Usar pocion")
    print("3. Salir")

    opcion = input("Elija una opcion: ")

    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        opcion = input("Error. Elija 1, 2 o 3: ")

    if opcion == "1":
        daño = 10

        critico = input("¿Golpe critico? (s/n): ").lower()
        while critico != "s" and critico != "n":
            critico = input("Error. Ingrese s o n: ").lower()

        if critico == "s":
            daño = int(daño * 1.5)

        hp_enemigo -= daño
        print("Hiciste", daño, "de daño.")

    elif opcion == "2":
        if pociones > 0:
            hp_jugador += 20
            if hp_jugador > 100:
                hp_jugador = 100
            pociones -= 1
            print("Usaste una pocion.")
        else:
            print("No tenes pociones.")

    elif opcion == "3":
        print("Saliste del juego.")
        break

    if hp_enemigo <= 0:
        print("\nVICTORIA. Derrotaste al enemigo.")
        break

    daño_enemigo = 8

    hp_jugador -= daño_enemigo
    print("El enemigo te hizo", daño_enemigo, "de daño.")

    if hp_jugador <= 0:
        print("\nDERROTA. Fuiste derrotado.")
        break