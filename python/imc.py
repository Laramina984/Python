peso = float(input("\nInforme seu Peso: ").strip())
altura = float(input("Informe sua altura: ").strip())

imc = peso/(altura * altura)

print("Resultado: " + "%.2f" % imc)

if imc < 18.5:
    print("Magreza")
elif imc >= 18.5 and imc <= 24.9:
    print("Normal")
elif imc >= 25 and imc <= 29.9:
    print("SobrePeso")
elif imc >= 30 and imc <= 34.9:
    print("Obesidade grau 1")
elif imc >= 35 and imc <=39.9:
    print("Obesidade grau 2")
elif imc >= 40:
    print("Obesidade grau 3")

print("\n")



