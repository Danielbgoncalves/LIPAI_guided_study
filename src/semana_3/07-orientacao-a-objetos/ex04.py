"""
ex04.py crie o atributo do tipo list participacoesna classe Projeto e implemente o método 
add_participacao que recebe como parâmetro um objeto Participação e adiciona na lista.
"""
from ex01 import Aluno
from ex02 import Projeto
from ex03 import Participacao

class ProjetoComParticipacao(Projeto):
    def __init__(self, codigo, titulo, responsavel):
        super().__init__(codigo, titulo, responsavel)
        self.participantes = []

    def add_participacao(self, participante):
        if isinstance(participante, Participacao):
            self.participantes.append(participante)
        else:
            raise ValueError(f"O valor inserido é do tipo {type(participante)}, mas deveria ser Participacao")

proj = ProjetoComParticipacao("SP1243", "Laboratório de processos químicos", "Aldair Neto")
aluno = Aluno("seila","Agnaldinho Costa","Agnaldinho1001@eumail.com" )
proj.add_participacao(Participacao("a", "12/02/1976", "12/02/2004", aluno, proj))

