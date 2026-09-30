def classificar_alunos():
    with open("alunos3.txt", "r") as arquivo:
        for linha in arquivo:
            nome, nota = linha.strip().split(";")

            nota = float(nota)

            if nota >= 6:
                situacao = "Aprovado"
            elif nota >= 4:
                situacao = "Recuperação"
            else:
                situacao = "Reprovado"

            print(nome, "-", nota, "-", situacao)


classificar_alunos()

