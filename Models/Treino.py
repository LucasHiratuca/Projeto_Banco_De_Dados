class Treino:
    def __init__(self, id, alongamentos, exercicios_arbcs, exercicios_mqn, carga_mqn, cpf_aluno):
        self._id = id 
        self._alongamentos = alongamentos
        self._exercicios_mqn = exercicios_mqn
        self._exercicios_arbcs = exercicios_arbcs
        self._carga_mqn = carga_mqn
        self._cpf_aluno = cpf_aluno

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def alongamentos(self):
        return self._alongamentos

    @alongamentos.setter
    def alongamentos(self, value):
        self._alongamentos = value

    @property
    def exercicios_mqn(self):
        return self._exercicios_mqn

    @exercicios_mqn.setter
    def exercicios_mqn(self, value):
        self._exercicios_mqn = value

    @property
    def exercicios_arbcs(self):
        return self._exercicios_arbcs

    @exercicios_arbcs.setter
    def exercicios_arbcs(self, value):
        self._exercicios_arbcs = value

    @property
    def carga_mqn(self):
        return self._carga_mqn

    @carga_mqn.setter
    def carga_mqn(self, value):
        self._carga_mqn = value

    @property
    def cpf_aluno(self):
        return self._cpf_aluno

    @cpf_aluno.setter
    def cpf_aluno(self, value):
        self._cpf_aluno = value

        pass

