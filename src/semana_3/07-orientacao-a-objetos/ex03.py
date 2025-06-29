"""
ex03.py crie uma classe Participacao que deve ter como atributos codigo, data inicio, data fim, 
aluno e o projeto associado. 
"""

class Participacao:
    def __init__(self, codigo, data_inicio, data_fim, aluno, projeto_associado):
        self.codigo = codigo
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.aluno = aluno
        self.projeto_associado = projeto_associado

    def __eq__(self, value):
        if isinstance(self.__class__, value):
            return self.codigo == value.codigo
    
        return False

    @property
    def codigo(self):
        return self._codigo
    
    @codigo.setter
    def codigo(self, value):
        if not value:
            raise ValueError(f"valor inválido, codigo inserido foi: {value}")
        self._codigo = value

    @property
    def data_inicio(self):
        return self._data_inicio
    
    @data_inicio.setter
    def data_inicio(self, value):
        if not value:
            raise ValueError(f"valor inválido, data_inicio inserido foi: {value}")
        self._data_inicio = value
    
    @property
    def data_fim(self):
        return self._data_fim
    
    @data_fim.setter
    def data_fim(self, value):
        if not value:
            raise ValueError(f"valor inválido, data_fim inserido foi: {value}")
        self._data_fim = value
    
    @property
    def aluno(self):
        return self._aluno
    
    @aluno.setter
    def aluno(self, value):
        if not value:
            raise ValueError(f"valor inválido, aluno inserido foi: {value}")
        self._aluno = value

    @property
    def projeto_associado(self):
        return self._projeto_associado
    
    @projeto_associado.setter
    def projeto_associado(self, value):
        if not value:
            raise ValueError(f"valor inválido, projeto_associado inserido foi: {value}")
        self._projeto_associado = value