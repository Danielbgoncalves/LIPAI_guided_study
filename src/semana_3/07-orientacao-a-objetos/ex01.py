"""
ex01.py crie uma classe Aluno que deve ter como atributos o prontuario, nome e email. 
Deve ser possível construir um objeto aluno a partir da string prontuario,nome,email ex: 
SP0101,João da Silva,joao@email.com . Nenhum dos atributos pode ser vazio ou nulos 
(utilizar propriedades). Dois alunos podem ser considerados iguais caso tenham o mesmo prontuário.
"""

class Aluno:
    def __init__(self, prontuario, nome, email):
        self.prontuario = prontuario
        self.nome = nome
        self.email = email
    
    @classmethod
    def from_string(cls, listagem):
        valores = [ valor.strip() for valor in listagem.split(",") ]

        if not len(valores) == 3:
            raise ValueError("Quantidade de valores inválida. Esperado: prontuario,nome,email")
        
        return cls(valores[0], valores[1], valores[2])

    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return self.prontuario == value.prontuario 
        return False

    @property
    def prontuario(self):
        return self._prontuario
    @property
    def nome(self):
        return self._nome
    
    @property
    def email(self):
        return self._email

    @prontuario.setter
    def prontuario(self, value):
        if not value:
            raise ValueError(f"Valor inválido: 'prontuario' é inválido, o valor passado é: {value}")
        self._prontuario = value

    @nome.setter
    def nome(self, value):
        if not value:
            raise ValueError(f"Valor inválido: 'nome' é inválido, o valor passado é: {value}")
        self._nome = value

    @email.setter
    def email(self, value):
        if not value:
            raise ValueError(f"Valor inválido: 'email' é inválido, o valor passado é: {value}")
        self._email = value
    
    
aluno1 = Aluno("SP0101", "André", "andre@eumail.com")
aluno2 = Aluno.from_string("SP0101, André, andre@eumail.com")
aluno3 = Aluno("SP0102", "Maria", "maria@email.com")

print(f"aluno1 == aluno2: {aluno1 == aluno2}")  
print(f"aluno1 == aluno3: {aluno1 == aluno3}") 
print(f"aluno2 details: {aluno2.prontuario}, {aluno2.nome}, {aluno2.email}")

