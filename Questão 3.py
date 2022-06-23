# 3) Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu
# respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

idade = []
altura = []
for i in range (5):
    idade.append(int(input("Idade {}: ".format(i+1))))
    altura.append(float(input("Altura {}: ".format(i+1))))
idade.reverse()
altura.reverse()
print("Idade: ", idade)
print("Altura: ", altura)