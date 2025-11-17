class Personal:
    def _init_(self, cpf, rg_pers, nome_pers, horario_pers, telefone_pers):
        self._cpf = cpf
        self._rg_pers = rg_pers
        self._nome_pers = nome_pers
        self._horario_pers = horario_pers
        self._telefone_pers = telefone_pers

    def get_cpf(self):
        return self._cpf

    def set_cpf(self, cpf):
        self._cpf = cpf
 
    def get_rg_pers(self):
        return self._rg_pers

    def set_rg_pers(self, rg_pers):
        self._rg_pers = rg_pers

    def get_nome_pers(self):
        return self._nome_pers

    def set_nome_pers(self, nome_pers):
        self._nome_pers = nome_pers
     
    def get_time(self):
        return self._horario_pers

    def set_time(self, horario_pers):
        self._horario_pers = horario_pers
     
    def get_telefone_pers(self):
        return self._telefone_pers

    def set_telefone_pers(self, telefone_pers):
        self._telefone_pers = telefone_pers


        pass
