class Alula:
    def __init__(self, id_aula, tipo_aula, id_professor):
        self._id_aula = id_aula
        self._tipo_aula = tipo_aula
        self._id_professor = id_professor

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
    def id_professor(self):
        return self._id_professor

    @id_professor.setter
    def id_professor(self, value):
        self._id_professor = value

