from aluno import Aluno
listacurso=['mat','port','red','his']
alunos={}
while True:
    x=0
    curso=input("digite seu curso: ")
    matricula=input("digite sua matricula: ")
    nome=input("digite seu nome: ")
    alunoc1=Aluno(matricula,nome,curso)
    for i in listacurso:
        if i==curso:
            while x<3:
                x+=1
                if x==1:
                    notas1=float(input('digite uma nota:'))
                    alunoc1.cadastrarnotas(notas1)
                else:
                    notas1=float(input('digite outra nota:'))
                    alunoc1.cadastrarnotas(notas1)

    mediageral=alunoc1.calcmedia()
    alunos[alunoc1.nome]=alunoc1.media
    print(alunos)
    menu=input("voce deseja adicionar outro aluno(S/N): ")
    if menu.upper()=="N":
        break
#menu
while True:
    print("digite a opcao que deseja")
    print("(1)-consulta de aluno")
    print("(2)-sair do codigo")
    opcao=input()
    if opcao=="1":
        x=input("digite seu nome: ")
        print('aluno:',x,'media: ',alunos[x])
    elif opcao=="2":
        break
    else:
        print("aluno nao existente")
