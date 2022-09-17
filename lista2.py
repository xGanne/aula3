carrinho = []
produto = 't'
while produto!= 'sair':
    print("Adicione um produto ou digite sair para encerrar: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)
