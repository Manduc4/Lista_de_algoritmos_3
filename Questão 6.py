# 6) Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe
# também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.
# Exemplo:
# String 1: Brasil Hexa 2006
# String 2: Brasil! Hexa 2006!
# Tamanho de "Brasil Hexa 2006": 16 caracteres
# Tamanho de "Brasil! Hexa 2006!": 18 caracteres
# As duas strings são de tamanhos diferentes.
# As duas strings possuem conteúdos diferente.

palavra1 = str(input("Digite uma palavra ou uma frase: "))
palavra2 = str(input("Digite mais uma palavra ou frase: "))

print("Tamanho de {}: {}".format(palavra1, len(palavra1)))
print("Tamanho de {}: {}".format(palavra2, len(palavra2)))

if len(palavra1) != len(palavra2):
    print("As duas strings são de tamanhos diferentes")
else:
    print("As duas strings são de tamanhos iguais")
if palavra1 != palavra2:
    print("As duas strings possuem conteúdos diferentes")
else:
    print("As duas palavras possuem conteúdos iguais")