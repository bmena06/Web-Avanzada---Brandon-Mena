while True:

    dia = input("Ingrese el día de la semana: ")
    dia=dia.lower()
    if dia in ["lunes", "martes", "miercoles"]:
        tarifa = 2.00
    elif dia in ["jueves", "viernes"]:
        tarifa = 2.50
    elif dia in ["sabado", "domingo"]:
        tarifa = 3.00
    else:
        print("Dia de la semana incorrecto")
        tarifa=None

    if tarifa !=None:

        hora = int(input("Ingrese las horas estacionado: "))
        minuto = int(input("Ingrese los minutos estacionado "))
        total=hora * tarifa
        if minuto>= 60 or (minuto and hora) <0:
            print("Tiempo no permitido")
        elif minuto >=5:
            hora +=1
            print("El monto a pagar es: $", total)
        else:
            print("El monto a pagar es: $", total)

    salir = input("¿Desea salir? (si/no): ")
    if salir =="si":
        break
