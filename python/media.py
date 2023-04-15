nota1 = float(input("Informe a primeira nota: "))   
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))

media =  (nota1 + nota2 + nota3)/3

print("\nMedia Final: " +  "%.2f" % media)

if media >= 7:
    print("\n\033[1;32m Aprovado \033[m")
elif (media >= 3):
    print("\n\033[1;33m Exame \033[m")
else:
    print("\n\033[1;31m Reprovado \033[m")