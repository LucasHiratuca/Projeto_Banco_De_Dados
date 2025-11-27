# Models/Aula.py
class Aula: # CORREÇÃO: Renomeado de Alula para Aula
    def __init__(self, id_aula, tipo_aula, cpf_professor):
        self._id_aula = id_aula
        self._tipo_aula = tipo_aula
        self._cpf_professor = cpf_professor

    @property
    def id_aula(self):
        return self._id_aula

    @id_aula.setter
    def id_aula(self, value):
        self._id_aula = value

    @property
    def tipo_aula(self):
        return self._tipo_aula

    @tipo_aula.setter
    def tipo_aula(self, value):
        self._tipo_aula = value

    @property
    def cpf_professor(self):
        return self._cpf_professor

    @cpf_professor.setter
    def cpf_professor(self, value):
        self._cpf_professor = value