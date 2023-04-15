numero= []

while True:
    num = int(input("Digite um numero(0 para sair):\n"))
    if num == 0:
        break
    numero.append(num)
#lista 1
pares = []
#lista 2
impares = []

for num in numero:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
#sort é a função de ordem crescente
pares.sort()
impares.sort()

print("Numeros pares:\n ",)
for num in pares:
    print(num)
print()

print("Numeros impares:\n ",)
for num in impares:
    print(num)
print()
#sum é função  de seq
soma = sum(numero)
print("Soma dos valores: ", soma)