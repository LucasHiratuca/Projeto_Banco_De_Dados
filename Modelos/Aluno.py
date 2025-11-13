class Aluno:
    def_init_(self, cpf_aluno, rg_aluno, telfone_aluno, nome_aluno, objetivo_treino, tipo_plano, cpf_pers):
        self._cpf_aluno = cpf_aluno
        self._rg_aluno = rg_aluno
        self._telefone_aluno = telfone_aluno
        self._nome_aluno = nome_aluno
        self._objetivo_treino = objetivo_treino
        self._tipo_plano = tipo_plano
        self._cpf_pers = cpf_pers

    @property
    def cpf_aluno(self):
        return self._cpf_aluno

    @cpf_aluno.setter
    def cpf_aluno(self, value):
        self._cpf_aluno = value

    @property
    def rg_aluno(self):
        return self._rg_aluno

    @rg_aluno.setter
    def rg_aluno(self, value):
        self._rg_aluno = value

    @property
    def telefone_aluno(self):
        return self._telefone_aluno

    @telefone_aluno.setter
    def telefone_aluno(self, value):
        self._telefone_aluno = value

    @property
    def nome_aluno(self):
        return self._nome_aluno

    @nome_aluno.setter
    def nome_aluno(self, value):
        self._nome_aluno = value

    @property
    def objetivo_treino(self):
        return self._objetivo_treino

    @objetivo_treino.setter
    def objetivo_treino(self, value):
        self._objetivo_treino = value

    @property
    def tipo_plano(self):
        return self._tipo_plano

    @tipo_plano.setter
    def tipo_plano(self, value):
        self._tipo_plano = value

    @property
    def cpf_pers(self):
        return self._cpf_pers

    @cpf_pers.setter
    def cpf_pers(self, value):
        self._cpf_pers = value
    pass
