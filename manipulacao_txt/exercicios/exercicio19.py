def gerar_relatorio():
    vendas = []

    with open("vendas.txt", "r") as arquivo:
        for linha in arquivo:
            vendedor, produto, valor = linha.strip().split(";")

            venda = {
                "vendedor": vendedor,
                "produto": produto,
                "valor": float(valor)
            }

            vendas.append(venda)

    print("VENDAS:")

    valor_total = 0

    for venda in vendas:
        print(venda["vendedor"], "-", venda["produto"], "- R$", format(venda["valor"], ".2f"))
        valor_total = valor_total + venda["valor"]

    print("\nTOTAL DE VENDAS: R$", format(valor_total, ".2f"))

    quantidade_vendas = {}

    for venda in vendas:
        vendedor = venda["vendedor"]

        if vendedor in quantidade_vendas:
            quantidade_vendas[vendedor] = quantidade_vendas[vendedor] + 1
        else:
            quantidade_vendas[vendedor] = 1

    print("\nQuantidade de vendas:")

    for vendedor in quantidade_vendas:
        print(vendedor + ":", quantidade_vendas[vendedor])

    maior_vendedor = ""
    maior_valor = 0

    for venda in vendas:
        vendedor = venda["vendedor"]

        if vendedor not in quantidade_vendas:
            quantidade_vendas[vendedor] = 0

    valores_vendedores = {}

    for venda in vendas:
        vendedor = venda["vendedor"]

        if vendedor in valores_vendedores:
            valores_vendedores[vendedor] = valores_vendedores[vendedor] + venda["valor"]
        else:
            valores_vendedores[vendedor] = venda["valor"]

    for vendedor in valores_vendedores:
        if valores_vendedores[vendedor] > maior_valor:
            maior_valor = valores_vendedores[vendedor]
            maior_vendedor = vendedor

    print("\nMaior valor total em vendas:")

gerar_relatorio()

