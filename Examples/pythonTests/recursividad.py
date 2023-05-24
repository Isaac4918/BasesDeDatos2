# Funcion 1
def funcion1(n):
    if type(n)==int:
        if n>=0:
            return funcion1Aux(0,n)
        else:
            print("Paramentro incorrecto")    
    
def funcion1Aux(i,n):
    if i==n:
        return ((n**2)**2) + (i**n)
    else:
        return ((n**2)**2) + (i**n) + funcion1Aux(i+1,n)
    

# Funcion 2
def funcion2(num):
    if type(num)==int:
        if num>=0:
            return funcion2Aux(num,1)
        else:
            print("Paramentro incorrecto")

def funcion2Aux(num, result):
    if num==0:
        return result
    if esImpar(num%10):
        return funcion2Aux(num//10, result * (num%10)**3)
    else:
        return funcion2Aux(num//10, result)
    
def esImpar(num):
    if type(num) == int:
        if num%2==0:
            return False
        else:
            return True
    else:
        print("Paramentro incorrecto")
