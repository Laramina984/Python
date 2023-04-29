produtos = ['tomate', 'batata', 'limão','goiaba']
estoque = [100, 200, 50,80]
min_estoque= [10, 20 , 5,8]

for num in range (len(produtos)):
    print(f'O produto {produtos[num]} tem estoque de {estoque[num]} unidades, e o minímo é de {min_estoque[num]}')

prod = input('Digite o nome do produto:\n ')
qnt = int(input('Digite a quantidade do produto:\n '))
min = int(input('Digite o minímo do estoque:\n '))
produtos.append(prod)
estoque.append(qnt)
min_estoque.append(min)

for num in range(len(produtos)):
  if estoque[num] <= min_estoque[num]:
    print(f'Produto {produtos[num]} com a quantidade minima')

lista = []
for num in range(len(produtos)):
 lista.append([produtos[num],estoque[num], min_estoque[num]])
print(lista)

while True:
  busca = input('Digite o nome do produto para apagar:\n')
  if busca in produtos:
    break
  else:
    print('produto não encontrado!!!') 
ind = produtos.index(busca)
produtos.remove(busca)
estoque.remove(estoque[ind])
min_estoque.remove(min_estoque[ind])
print(produtos, estoque, min_estoque)

pedidos = []
while True:
 ped_prod = input('Digite o produto que deseja comprar: ')
 ped_qtn = int(input('Digite a quantidade de produtos:'))
 pedidos.append([ped_prod, ped_qtn])
 repete = input('Deseja continuar s\n:')
 if repete.upper() == 'n':
   break
print(pedidos)

for itens in pedidos:
  if itens[0] not in produtos:
    print(f'produtos {itens[0]} não tem')
  elif itens[1] > estoque[produtos.index(itens[0])]:
    print('Saldo insuficiente!')

