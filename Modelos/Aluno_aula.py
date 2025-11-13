class Aluno_Aula:
    def_init_(self, id_aula, cpf_aluno):
        self._id_aula = id_aula
        self._cpf_aluno = cpf_aluno

    @property
    def id_aula(self):
        return self._id_aula

    @id_aula.setter
    def id_aula(self, value):
        self._id_aula = value

    @property
    def cpf_aluno(self):
        return self._cpf_aluno

    @cpf_aluno.setter
    def cpf_aluno(self, value):
        self._cpf_aluno = value

        pass
