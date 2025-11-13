class Produto:
    def _init_(self,tipo_pr ,nome_pr ,cpf_aluno):
        self._tipo_pr = tipo_pr
        self._nome_pr_ = nome_pr
        self._cpf_aluno = cpf_aluno

    def get_tipo_pr(self):
        return self._tipo_pr

    def set_tipo_pr(self, tipo_pr):
        self._tipo_pr = tipo_pr   

    def get_nome_pr(self):
        return self._nome_pr

    def set_nome_pr(self, nome_pr):
        self._nome_pr = nome_pr

    def get_cpf_aluno(self):
        return self._cpf_aluno

    def set_cpf_aluno(self, cpf_aluno):
        self._cpf_aluno = cpf_aluno

        pass
