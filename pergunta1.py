while True:
    nota = float(input("Digite uma nota entre zero e dez: "))
    
    if nota >= 0 and nota <= 10:
        print("Valor válido! Nota:", nota)
        break
    else:
        print("Valor inválido. Por favor, digite uma nota entre zero e dez.")