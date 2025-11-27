# Models/Produto.py
class Produto:
    def __init__(self,tipo_pr ,nome_pr ,cpf_aluno, id_pr):
        self._id_pr = id_pr
        self._tipo_pr = tipo_pr
        self._nome_pr = nome_pr # CORREÇÃO: Nome do atributo corrigido
        self._cpf_aluno = cpf_aluno
     
    def get_id_pr(self):
        return self._id_pr

    def set_id_pr(self, id_pr):
        self._id_pr = id_pr   
    
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