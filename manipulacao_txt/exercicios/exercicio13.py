def menu_arquivo():
    while True:
        print("\n1 - Ler arquivo")
        print("2 - Adicionar texto")
        print("3 - Sobrescrever arquivo")
        print("4 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            with open("notas.txt", "r") as arquivo:
                texto = arquivo.read()

            print(texto)

        elif opcao == "2":
            texto = input("Digite o texto que deseja adicionar: ")

            with open("notas.txt", "a") as arquivo:
                arquivo.write(texto + "\n")

            print("Texto adicionado com sucesso!")

        elif opcao == "3":
            texto = input("Digite o novo texto: ")

            with open("notas.txt", "w") as arquivo:
                arquivo.write(texto + "\n")

            print("Arquivo sobrescrito com sucesso!")

        elif opcao == "4":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida!")


menu_arquivo()
