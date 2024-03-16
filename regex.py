import re

def main():
    # Exemplo 1: Verificar se uma string contém um padrão específico
    texto = "O gato está no telhado"
    padrao = r"gato"  # String crua
    if re.search(padrao, texto):
        print("Padrão encontrado!")
    else:
        print("Padrão não encontrado.")

    # Exemplo 2: Encontrar todas as ocorrências de um padrão em uma string
    texto = "O rato roeu a roupa do rei de Roma"
    padrao = r"r\w+"  # String crua
    matches = re.findall(padrao, texto)
    print("Palavras que começam com 'r':", matches)

    # Exemplo 3: Substituir todas as ocorrências de um padrão em uma string
    texto = "Python é uma linguagem de programação maravilhosa"
    padrao = r"maravilhosa"  # String crua
    novo_texto = re.sub(padrao, "poderosa", texto)
    print("Texto modificado:", novo_texto)

    # Exemplo 4: Separar uma string em partes usando um padrão como delimitador
    texto = "banana, maçã, uva, morango, abacaxi"
    padrao = r",\s*"  # String crua
    frutas = re.split(padrao, texto)
    print("Frutas separadas:", frutas)

    # Exemplo 5: Validar um formato de e-mail usando regex
    email = "usuario@example.com"
    padrao = r"^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$"  # String crua
    if re.match(padrao, email):
        print("Formato de e-mail válido!")
    else:
        print("Formato de e-mail inválido.")

if __name__ == "__main__":
    main()
