alunos = []
testes = []
medias = []
provas = []
trabalhos = []
i = 0

while len(alunos) != 3:
    a = input("Digite o nome do aluno: ")
    alunos.append(a)
    test = float(input("Digite nota do teste: "))
    testes.append(test)
    prov = float(input("Digite nota da prova: "))
    provas.append(prov)
    trab = float(input("Digite nota do trabalho: "))
    trabalhos.append(trab)
    medias.append(((testes[i] + provas[i] + trabalhos[i])/ 3))
    i = i + 1
    print("------------------------------------------")

for a in alunos:
        print("------------------------------------------")
        print(f"Nome do(a) aluno: {a}")
        print(f"Nota do Teste: {test}")
        print(f"Nota da Prova: {prov}")
        print(f"Nota do Trabalho: {trab}")
        for media in medias:
            print("------------------------------------------")
            print(f"Media do(a) aluno(a): {media}")
            print("------------------------------------------")