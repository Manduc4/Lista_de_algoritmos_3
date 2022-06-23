# 16) Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais:
# taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo
# de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaImposto (taxaImposto,custo):
    custo = (taxaImposto*custo/100) + custo
    print("\nO custo final é {} reais".format(custo))

custo = int(input("Valor do custo: "))
taxaImposto = int(input("Valor da taxa em porcentagem: "))

somaImposto(taxaImposto,custo)