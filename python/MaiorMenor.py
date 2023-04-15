n = ''


def TryParseFloat(v):
    try:
        if float(n) == True:
            return True
    except ValueError:
        return False       
    
while n == "": 
    n = input("\nInforme o primeiro numero: ")
    if n != "":
        n = n

if TryParseFloat(n) == True:

    if n >0:
        print("Positivo")
    elif n==0:
        print("Neutro")
    else:
        print("Negativo")
else:
    print("asda")
