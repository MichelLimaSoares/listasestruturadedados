
print("")
print("-----Vamos trabalhar com um vetor de 5 posições-----")
print("")
print("-----Digite um numero para cada posição do vetor-----")
print("")

# criação de um vetor com 5 posições
vetor = [0] * 5

# preenchimento do vetor com valores informados pelo usuário
for i in range(len(vetor)):
    vetor[i] = int(input(f"Digite um número para a posição {i}: "))

print("")
print("-----Como exibir um vetor-----")

# exibição do vetor
print("\nO vetor informado é:\n")
for i in range(len(vetor)):
    print(f"Posição {i}: {vetor[i]}")

print("")
print("-----Acessando elementos de um vetor-----\n")

# saída: Acessando o elemento do vetor no índice 0: 1
print("Acessando o elemento do vetor no índice 0: ", vetor[0])
# saída: Acessando o elemento do vetor no índice 3: 4
print("Acessando o elemento do vetor no índice 3: ", vetor[3])

print("")
print("-----Alterando um elemento do vetor pelo índice-----")

# Alterando um elemento do vetor pelo índice
print("\nAlterando o elemento do indice 2, e colocando o elemento 10\n")
print("Elemento anterior = ", vetor[2], "\n")
vetor[2] = 10
print("Novo vetor: ", vetor)

print("")
print("-----Percorrendo o vetor com um loop for-----\n")

# Percorrendo o vetor com um loop for
for elemento in vetor:
    print(f"Elemento: {elemento}")

print("")
print("-----Percorrendo o vetor com um loop while-----\n")

# Percorrendo o vetor com um loop while
i = 0
while i < len(vetor):
    print("Elemento na posição", i, ":", vetor[i])
    i += 1

print("\n----- Fim -----")
