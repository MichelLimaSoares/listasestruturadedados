print("")
print("-----Vamos trabalhar STRINGS-----")
print("")
print("-----Definindo uma string-----")
print("")

# Definindo uma string
frase = "Eu vou viajar para o EUA"
frase1 = input(f"Digite uma frase: ")

print("")
print("-----Transformando em maiúsculas-----")
print("")

# Transformando em maiúsculas
frase_maiuscula = frase1.upper()
print(frase_maiuscula) # Saída: "Eu vou viajar para o EUA"

print("")
print("-----Transformando em minúsculas-----")
print("")

# Transformando em minúsculas
frase_minuscula = frase1.lower()
print(frase_minuscula) # Saída: "Eu vou viajar para o EUA"

print("")
print("-----Contando o número de ocorrências de um caractere ou substring-----")
print("")

# Contando o número de ocorrências de um caractere ou substring
numero_ocorrencias = frase1.count("o")
print("O caractere 'o' aparece", numero_ocorrencias, "vezes na frase:", frase1)


print("")
print("-----Verificando se uma substring está presente na string-----")
print("")

# Verificando se uma substring está presente na string
substring = "EUA"
print("Verifique se a palavra", substring, "esta presente na frase\n")
if substring in frase1:
    print(f"a palavra {substring} foi Encontrado!")
else:
    print(f"a palavra {substring} Não foi encontrado.")

print("")
print("-----Substituindo uma substring por outra-----")
print("")

# Substituindo uma substring por outra
subAlter = "o EUA"
nova_frase = frase1.replace(subAlter, "Lisboa\n")
print(f"substitua a substring {subAlter} por Lisboa")
print(nova_frase)

print("\n----- Fim -----")