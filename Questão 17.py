# 17) Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve
# receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e
#
# o valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para
# valores dentro da faixa de forma elegante.

def retangulo (linhas, colunas):
    print("+", "---" * colunas, "+")
    for i in range(linhas):
        print("|"," "*colunas*3,"|")
    print("+", "---" * colunas, "+")

linhas = int(input("Numero de linhas: "))
colunas = int(input("Número de colunas: "))

if linhas>20:
    linhas = 20
if colunas>20:
    colunas = 20
retangulo(linhas, colunas)
