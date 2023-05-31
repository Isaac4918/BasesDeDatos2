# =============================================================================
# UNO

def UNO(num1,num2,num3):
    if type(num1) == int and type(num2) == int and type(num3) == int:
        num1 = abs(num1)
        num2 = abs(num2)
        num3 = abs(num3)
        if esImpar(abs(num1)):
            if lenDeNum(num1) == lenDeNum(num2) and lenDeNum(num2) == lenDeNum(num3):
                return UNOaux(num1,num2,num3)
            else:
                return "Numeros tienen distinta cantidad de digitos"
        else:
            return "Numeros no tienen cantidad impar de digitos"
    else:
        return "Los parametros no son numeros enteros"

def UNOaux(num1,num2,num3):
    lista = []
    largo = lenDeNum(num1)
    izquierda = largo - 1
    derecha = 0
    centro = (largo-1)//2
    for i in range(0,largo,1):
        lista += [obtenerDigitoNumero(num1,izquierda)]
        lista += [obtenerDigitoNumero(num2,derecha)]
        lista += [obtenerDigitoNumero(num3,izquierda)]
        lista += [obtenerDigitoNumero(num3,derecha)]
        lista += [obtenerDigitoNumero(num2,izquierda)]
        lista += [obtenerDigitoNumero(num1,derecha)]

        if abs(izquierda-centro) > 1 and abs(derecha-centro) > 1:
            izquierda -= 1
            derecha += 1
        
        else:
            lista += [obtenerDigitoNumero(num1,centro)]
            lista += [obtenerDigitoNumero(num2,centro)]
            lista += [obtenerDigitoNumero(num3,centro)]
            break

    for i in range(0,len(lista),1):
        if i%2 == 0:
            lista[i] = lista[i]**3
        else:
            lista[i] = lista[i]**2

    return lista

# Funciones auxiliares
# Funcion que devuelve si es impar o no
def esImpar(num):
    if type(num) == int:
        if num%2==0:
            return False
        else:
            return True
    else:
        print("Parametro incorrecto")

# Funcion que devuelve la cantidad de digitos de un numero
def lenDeNum(num):
    if type(num) == int:
        if num < 10:
            return 1
        else:
            return 1 + lenDeNum(num//10)
    else:
        print("Parametro incorrecto")

# Funcion que devuelve un digito especifico de un numero
def obtenerDigitoNumero(num, dig):
    if type(num) == int and type(dig) == int:
        if dig == 0:
            return num%10
        else:
            return obtenerDigitoNumero(num//10, dig-1)
    else:
        print("Parametro incorrecto")

# =============================================================================
# DOS1 Cola
def DOS1(num):
    if type(num) == int:
        if num > 0:
            return DOS1aux(num, 1, 0)
        else:
            return "El numero debe ser mayor a 0"
    else:
        return "Parametro incorrecto"

def DOS1aux(num,i, resultado):
    if i == num + 1:
        return resultado
    else:
        temp = (factorial(i)*((num-2)**num)*(num-1))/(2*((num*4)**i)+num)
        return DOS1aux(num, i+1, resultado+temp)

# Funcion factorial
def factorial(num):
    if type(num) == int:
        if num >= 0:
            if num == 0:
                return 1
            else:
                return num * factorial(num-1)
        else:
            return "El numero debe ser mayor o igual a 0"
    else:
        return "Parametro incorrecto"

# =============================================================================
# DOS2 Pila
def DOS2(num):
    if type(num) == int:
        if num > 0:
            return (DOS2aux(num, 1))**2
        else:
            return "El numero debe ser mayor a 0"
    else:
        return "Parametro incorrecto"

def DOS2aux(num, i):
    if i == num + 1:
        return 0
    else:
        temp = (((i**2)*(num+1)*num)*(num-1))/((2*((num*3)**(i-1)))+num)
        return temp + DOS2aux(num, i+1)
