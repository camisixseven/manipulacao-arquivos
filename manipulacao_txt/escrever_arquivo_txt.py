# Modo "r" - Abre o arquivo para leitura
# Modo "w" - Abre para escrita e apaga o conteúdo existente
# Modo "a" - Adiciona novo conteúdo no final do arquivo
# Modo "x" - Cria um arquivo novo e gera erro se ele já existe

def criar_arquivo():
    # O "with" fecha o arquivo automaticamente
    # O "open()" função para leitura ou escrita de arquivos
    with open('alunos.txt', 'w', encoding="utf=8") as arquivo:
        arquivo.write(f"Camila\n")
        arquivo.write(f"Luiza polizeu\n")
        arquivo.write(f"Manu granzotto\n")

#criar_arquivo()

def adicionar_alunos(nome):
    with open('alunos.txt', 'a', encoding="utf=8") as arquivo:
        arquivo.write(nome + "\n")

#adicionar_alunos("terto")
#adicionar_alunos("richard")
#adicionar_alunos("pedro")

def listar_alunos():
    with open('alunos.txt', "r", encoding="utf=8") as arquivo:
        conteudo = arquivo.read()
    print(f"o conteúdo do arquivo alunos é {conteudo}")

#listar_alunos

def listar_alunos_individual():
    with open('alunos.txt', "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            listar_alunos.append(linha.strip())

    print(f"lista de aluno: {listar_alunos}")

#listar_alunos_individual()

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))

    with open('alunos.txt', 'a', encoding="utf-8") as arquivo:
        arquivo.write("f{nome};{idade}\n")

    print("Aluno cadastrado com sucesso!")

#cadastrar_aluno()

def listar_cadastro():
    itens_cadastro = []
    with open('alunos.txt', "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome, idade = linha.strip().split(";")

            obj = {
                "nome": nome,
                "idade": idade
            }

            itens_cadastro.append(obj)
        print(f"lista de cadastro: {itens_cadastro}")

listar_cadastro()




