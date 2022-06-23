# 14) Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses
# três argumentos.

def soma (a,b,c):
    soma = (a+b+c)
    print("Soma = ",soma)

a = int(input("Valor de A: "))
b = int(input("Valor de B: "))
c = int(input("Valor de C: "))
soma(a,b,c)