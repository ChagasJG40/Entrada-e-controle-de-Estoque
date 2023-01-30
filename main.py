# Inicializando o estoque como um dicionário vazio
stock = {}

# Define uma função para adicionar ao estoque
def add_to_stock():
    while len(stock) < 10:
        item = input("Insira o nome do item: ")
        amount = int(input("Insira a quantidade a ser adicionada: "))
        if item in stock:
            stock[item] += amount
        else:
            stock[item] = amount
        print(f'{amount} unidades de {item} foram adicionadas ao estoque.')
        report_stock()
    if len(stock) >= 10:
        print("Estoque cheio")
        return

# Define uma função para remover do estoque
def remove_from_stock():
    item = input("Insira o nome do item: ")
    amount = int(input("Insira a quantidade a ser removida: "))
    if item in stock:
        if stock[item] >= amount:
            stock[item] -= amount
            print(f'{amount} unidades de {item} foram removidas do estoque.')
        else:
            print(f'Não há suficiente {item} em estoque.')
    else:
        print(f'{item} não está em estoque.')
    report_stock()

def report_stock():
    print("Relatório de Estoque")
    for item, amount in stock.items():
        print(f'{item}: {amount}')

# Teste as funções
add_to_stock()
remove_from_stock()
