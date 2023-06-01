notas = []
nomes = []

while True:
    nome = input("Digite o nome do aluno (ou digite 'sair' para finalizar): ")
    
    if nome.lower() == 'sair':
        break
    
    nota = float(input("Digite a nota do aluno: "))
    
    nomes.append(nome)
    notas.append(nota)

if len(notas) > 0:
    media = sum(notas) / len(notas)
    print("\n--- Resultado ---")
    print("Média da turma:", media)
else:
    print("Nenhum aluno registrado.")