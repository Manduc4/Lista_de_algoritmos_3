# 8) Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical. Exemplo:
# F
# U
# L
# A
# N
# O

nome = []
nome = str(input("Digite seu nome: "))
nome = nome.upper()
for i in range (len(nome)):
    print(nome[i])
