"""
ex02.py crie uma classe Projeto que deve ter como atributos o  codigo (número inteiro que 
representa o código do projeto), titulo e responsável (nome do professor responsável pelo projeto). 
Deve ser possível construir um objeto projeto a partir da string codigo, titulo,responsavel 
ex: 1,Laboratório de Desenvolvimento de Software,Pedro Gomes . Nenhum dos atributos pode ser vazio ou 
nulos (utilizar propriedades). Dois projetos podem ser considerados iguais caso tenham o mesmo codigo.
"""

class Projeto:
    def __init__(self, codigo, titulo, responsavel):
        self.codigo = codigo
        self.titulo = titulo
        self.responsavel = responsavel

    @classmethod
    def from_string(cls, string):
        dados = [dado.strip() for dado in string.split(sep=",")]

        if not len(dados) == 3:
            raise ValueError("String inválida: não possui os valores codigo, titulo e resposnavel")
        
        return cls(dados[0], dados[1], dados[2])
    
    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return self.codigo == value.codigo
        
        return False

    @property
    def codigo(self):
        return self._codigo
    
    @codigo.setter
    def codigo(self, value):
        if not value and value != 0:
            raise ValueError(f"valor inválido, codigo inserido foi: {value}")
        self._codigo = value

    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, value):
        if not value:
            raise ValueError(f"valor inválido, titulo inserido foi: {value}")
        self._titulo = value

    @property
    def responsavel(self):
        return self._responsavel
    
    @responsavel.setter
    def responsavel(self, value):
        if not value:
            raise ValueError(f"valor inválido, responsavel inserido foi: {value}")
        self._responsavel = value

