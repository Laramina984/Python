tamanhoOvo = {
  "Pequeno": 7.8,
  "Médio": 12.9,
  "Grande": 23.95
}

saboresDoOvo = {
  "Chocolate Preto": 9.67,
  "Chocolate Branco": 4.50,
  "Chocolate ao leite": 9.32
}

recheioDoOvo = {
  "Chocolate Preto": 4.83,
  "Chocolate Branco": 2.25,
  "Os Dois": 3.54
}

adicionais = {
    "KitKat" : 4.67,
    "MMs" : 5.43,
    "Os Dois" : 5.05
}

formasDeEntrega = {
    "Presente" : 2.50,
    "Entrega" : 5.00,
    "Buscar no Local" : 0
}

preco = 0



def prepararOvo():

    preco = 0

    tamanho = input("\nEscolha um dos tamanhos disponíveis: Grande, Médio e Pequeno: ")
    preco += tamanhoOvo[tamanho]

    sabor = input("\nEscolha um dos sabores disponíveis: Chocolate Preto, Chocolate Branco e Chocolate ao leite: ")
    preco += saboresDoOvo[sabor]

    recheio = input("\nEscolha um dos sabores disponíveis: Chocolate Preto, Chocolate Branco e Os Dois: ")
    preco += recheioDoOvo[recheio] 

    adicional = input("\nEscolha um dos adicionais disponíveis: KiKat, MMs e Os Dois: ")
    preco += adicionais[adicional]

    formaDeEntrega = input("\nEscolha uma das formas de entrega disponíveis: Entrega, Buscar no Local, Presente: ")

    formaPagamento = input("\nEscolha uma das formas de pagamento disponíveis: Cartão de Crédito ou Pix: ")
    if formaPagamento == 'Cartão de Crédito':
        preco += 3.30
    elif formaPagamento == 'Pix':
        percentual = 10 / 100
    preco = preco - (preco * percentual)

    print(f"\nSeu Pedido foi: \nTamanho: {tamanho}\nSabor: {sabor}\nRecheio: {recheio}\nAdicionais: {adicional}\n \nForma de Entrega: {formaDeEntrega}\nForma De Pagamento: {formaPagamento}")
    print("\nValor Total: R$" + "%.2f" % preco)
    confrma = input("Confirma? s/n: ")

    if confrma == "n":
        prepararOvo()

prepararOvo()