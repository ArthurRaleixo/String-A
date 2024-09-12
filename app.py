def verificar_letra_a(s):
    contagem = s.lower().count('a')
    
    if contagem > 0:
        print(f"A letra 'a' aparece {contagem} vezes na string.")
    else:
        print("A letra 'a' não foi encontrada na string.")

string = input("Informe uma string: ")

verificar_letra_a(string)