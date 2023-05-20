def celsius_para_fahrenheit(tem_celsius):
    return (tem_celsius * 1.8) + 32

def fahrenheit_para_celsius(tem_fahrenheit):
    return (tem_fahrenheit - 32)/1,8

def celsius_para_kelvin(tem_celsius):
    return (tem_celsius + 273,15)

def kelvin_para_celsius(tem_kelvin):
    return (tem_kelvin - 273,15)

def fahrenheit_para_kelvin(tem_fahrenheit):
    return (tem_fahrenheit + 459,67)/1,8

def kelvin_para_fahrenheit(tem_kelvin):
    return (tem_kelvin*1,8 - 459,67)



def menu():
    print("1 - Celsius para Fahrenheit")
    print("2 - Fahrenheit para Celsius")
    print("3 - Celsius para Kelvin")
    print("4 - Kelvin para Celsius")
    print("5 - Fahrenheit para kelvin")
    print("6 - Kelvin para Fahrenheit")
    escolha = int(input("Escolha uma opção:\nR: "))
    return escolha

def main():
    escolha = menu()
    if escolha == 1:
            tem_celsius = float(input("Digite a temperatura em Celsius: "))
            tem_fahrenheit = celsius_para_fahrenheit(tem_celsius)
            print("A temperatura em Fahrenheit é:\n", tem_fahrenheit)
    elif escolha == 2:
            tem_fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
            tem_celsius = fahrenheit_para_celsius(tem_fahrenheit)
            print("A temperatura em Celsius é:\n", tem_celsius)
    elif escolha == 3:
            tem_celsius = float(input("Digite a temperatura em Celsius: "))
            tem_kelvin = celsius_para_kelvin(tem_celsius)
            print("A temperatura em Kelvin é:\n", tem_kelvin)
    elif escolha == 4:
            tem_kelvin = float(input("Digite a temperatura em kelvin: "))
            tem_celsius = kelvin_para_celsius(tem_kelvin)
            print("A temperatura em Celsius é:\n", tem_celsius)
    elif escolha == 5:
            tem_fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
            tem_kelvin = fahrenheit_para_kelvin(tem_fahrenheit)
            print("A temperatura em kelvin é:\n", tem_kelvin)
    elif escolha == 6:
            tem_kelvin = float(input("Digite a temperatura em kelvin: "))
            tem_fahrenheit = kelvin_para_fahrenheit(tem_kelvin)
            print("A temperatura em Fahrenhaeit é:\n", tem_fahrenheit)
    else:
        print("Opção inválida!")

main()
