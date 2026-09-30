def contar_linhas():
    contador = 0

    with open("nomes.txt", "r") as arquivo:
        for linha in arquivo:
            contador += 1

    print("O arquivo possui", contador, "linhas.")


contar_linhas()