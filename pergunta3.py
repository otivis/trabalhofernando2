import re

while True:
    nome_usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    if senha != nome_usuario and re.search(r'^(?=.[A-Za-z])(?=.\d)(?=.[@$!%#?&])[A-Za-z\d@$!%*#?&]{8,}$', senha):
        print("Nome de usuário e senha registrados com sucesso!")
        break
    else:
        print("Erro: A senha não atende aos critérios. A senha deve conter pelo menos uma letra, um número, um caractere especial e ter um tamanho mínimo de 8 caracteres. Por favor, tente novamente.")