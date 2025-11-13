class Personal():
    def _init_(self, cpf, rg, nome, horario_pers, telefone):
        self._cpf = cpf
        self._rg = rg
        self._nome = nome
        self._horario_pers = horario_pers
        self._telefone = telefone

    def get_cpf(self):
        return self._cpf

    def set_cpf(self, cpf):
        self._cpf = cpf
 
    def get_rg(self):
        return self._rg

    def set_rg(self, rg):
        self._rg = rg

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome
     
    def get_time(self):
        return self._horario_pers

    def set_time(self, horario_pers):
        self._horario_pers = horario_pers
     
    def get_telefone(self):
        return self._telefone

    def set_telefone(self, telefone):
        self._telefone = telefone


        pass