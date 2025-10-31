def lernotas():
    n = float(input("Digite uma nota para o aluno(a):"))
    return n

def resultado(n1, n2):
    media = (n1 + n2)/2
    print("Nota 1:", n1)
    print("Nota 2:", n2)
    print(f"Média: {media:.2f} - Reultado: ", end="")

    if media >= 7:
          print("Aprovado")
    else:
          print("Reprovado")

while True:
        print("\n=== Cadastro de Notas ===")
        a = lernotas()
        b = lernotas()
        resultado(a, b)


        repetir = input("\nDeseja calcular outro aluno? (s/n): ").lower()
        if repetir  != 's':
            print("Encerrando o Programa...")
            break