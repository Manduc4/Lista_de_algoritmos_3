media = []
acima_media = 0
for i in range(0,3):
    print("Aluno ",i+1,":")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    nota4 = float(input("Nota 4: "))
    print(" ")
    media.append((nota1+nota2+nota3+nota4)/4)
    if media[i] >= 7:
        acima_media = acima_media + 1
print("Número de alunos com nota maior que 7: ", acima_media)
