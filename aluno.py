class Aluno:  
    def __init__(self,matricula,nome,curso):
        self.matricula=matricula
        self.nome=nome
        self.curso=curso
        self.notas=[]
        self.media=0
    def cadastrarnotas(self,nota):
        self.notas.append(nota)
    def calcmedia(self):
        media=sum(self.notas)/len(self.notas)
        self.media=media


