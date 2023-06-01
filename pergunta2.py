while True:
    nome_usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    if senha != nome_usuario:
        print("Nome de usuário e senha registrados com sucesso!")
        break
    else:
        print("Erro: A senha não pode ser igual ao nome de usuário. Por favor, tente novamente.")