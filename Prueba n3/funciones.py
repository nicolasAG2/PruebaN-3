def validanum(tipo,texto,min=None,max=None):
    while True:
        try:
            num=tipo(input(texto))
            if min!=None and max!=None:
                if min<=num<=max:
                    break
                else:
                    print("Número fuera de rango!")
            elif min!=None:
                if num>=min:
                    break
                else:
                    print(f"El número deber ser MAYOR a {min}")
            elif max!=None:
                if num<=max:
                    break
                else:
                    print(f"El número debe ser MENOR a {max}")
        except:
            print("Error de tipo!!")
    return num

def validaMail(texto,leng):
    while True:
        try:
            correo=input(texto)
            if len(correo)>=leng:
                if '@' in correo:
                    break
                else:
                    print("Falta el (@) dentro de correo")
            else:
                print(f"El largo de correo no puede ser menor a {leng} dígitos")
        except:
            print("Error de tipo!!")
    return correo

def validaEdad(annio):#1943
    while True:
        try:
            fecNac=validanum(int,"Año de nacimiento: ",1943,annio)
            calculoEdad=annio-fecNac
            if 10<calculoEdad<=80:
                print("Puede participar!!")
                break
            else:
                print(f"Lo sentimos debe ser menor de {annio-1943} años y mayor a 10 años")
        except:
            print("Error de tipo!!")
    return calculoEdad

def validarletras(texto):
    while True:
            letras=(input(texto))
            if letras.isalpha():
                break
            else:
                print("El nombre no debe contener números.")
    return letras

def validalargo(texto,leng,estricto):
    while True:
        try:
            estricto
            var=str(input(texto))
            if estricto:
                if len(var)==leng:
                    break
                else:
                    print(f"El largo de {var} debe tener {leng} carácteres!!")
            else:
                if len(var)>=leng:
                    break
                else:
                    print(f"El largo de {var} debe ser mayor o igual a {leng}!!")
        except:
            print("Error de tipo")
    return var

def grabar(jugadores):
    jugador=[]
    jugador.append(validarletras("Ingrese su nombre: "))#Nombre
    jugador.append(validanum(int,"Ingrese su rut\nSin digito verificador, guiones ni puntos\n-> ",5000000,25000000))#Rut
    jugador.append(validaEdad(2023))#Fecha nacimiento
    jugador.append(validarletras("Ingrese categoria\nOro-Plata-Bronce : ").upper())#categoria
    jugador.append(validalargo("Ingrese su numero de telefono: ",9,True))#Telefono
    jugador.append(validalargo("Ingresar el nombre de la pareja: ",2,False).upper())#NombrePareja
    jugador.append(validaMail("Ingrese su mail: ",6))#Correo
    jugadores.append(jugador)
    print("Registro completado")
    return jugadores

def buscar(jugadores):
    rut=validanum(int,"Ingrese su rut: ",5000000,25000000)
    for i in range(len(jugadores)):
        if jugadores[i][1]==rut:
            print(f"rut: {jugadores[i][1]} Nombre: {jugadores[i][0]} Categoría: {jugadores[i][3]} Fono: {jugadores[i][4]} Correo: {jugadores[i][6]}")


def imprimir(jugadores):
    identificador=(validalargo("Ingrese el nombre de la pareja: ",2,False))
    print("Integrantes del equipo:")
    for i in range(len(jugadores)):
        if jugadores[i][5]==identificador.upper():
            print(f"{jugadores[i][0]}")


def despedida():
    nombre="Nicolas Gonzále González"
    seccion="PGY1121_015D"
    print("Hasta luego, vuelva pronto!!")
    print(f"{nombre}")
    print(f"{seccion}")

def menu():
    print("\tRegistro campeonato")
    print("1.-Grabar jugadores")
    print("2.-Buscar jugador")
    print("3.-Imprimir parejas")
    print("4.-Salir")
    return validanum(int,"Ingrese opción -> ",1,4)