codigo_mais_alto = codigo_mais_baixo = codigo_mais_pesado = codigo_mais_leve = None
altura_mais_alto = altura_mais_baixo = peso_mais_pesado = peso_mais_leve = 0
soma_alturas = soma_pesos = num_clientes = 0

while True:
    codigo = input("Digite o código do cliente (ou '0' para sair): ")
    
    if codigo == '0':
        break
    
    altura = float(input("Digite a altura do cliente (em metros): "))
    peso = float(input("Digite o peso do cliente (em kg): "))
    
    if num_clientes == 0:
        codigo_mais_alto = codigo_mais_baixo = codigo_mais_pesado = codigo_mais_leve = codigo
        altura_mais_alto = altura_mais_baixo = altura
        peso_mais_pesado = peso_mais_leve = peso
    else:
        if altura > altura_mais_alto:
            codigo_mais_alto = codigo
            altura_mais_alto = altura
        elif altura < altura_mais_baixo:
            codigo_mais_baixo = codigo
            altura_mais_baixo = altura
            
        if peso > peso_mais_pesado:
            codigo_mais_pesado = codigo
            peso_mais_pesado = peso
        elif peso < peso_mais_leve:
            codigo_mais_leve = codigo
            peso_mais_leve = peso
    
    soma_alturas += altura
    soma_pesos += peso
    num_clientes += 1

if num_clientes > 0:
    media_alturas = soma_alturas / num_clientes
    media_pesos = soma_pesos / num_clientes
    
    print("\n--- Resultados ---")
    print("Cliente mais alto:")
    print("Código:", codigo_mais_alto)
    print("Altura:", altura_mais_alto, "metros")
    
    print("\nCliente mais baixo:")
    print("Código:", codigo_mais_baixo)
    print("Altura:", altura_mais_baixo, "metros")
    
    print("\nCliente mais pesado:")
    print("Código:", codigo_mais_pesado)
    print("Peso:", peso_mais_pesado, "kg")
    
    print("\nCliente mais leve:")
    print("Código:", codigo_mais_leve)
    print("Peso:", peso_mais_leve, "kg")
    
    print("\nMédia das alturas dos clientes:", media_alturas, "metros")
    print("Média dos pesos dos clientes:", media_pesos, "kg")
else:
    print("Nenhum cliente registrado.")