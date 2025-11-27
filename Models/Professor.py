class Professor:
    def __init__(self, cpf, rg_prof, nome_prof, horario_prof, telefone_prof):
        self._cpf = cpf
        self._rg_prof = rg_prof
        self._nome_prof = nome_prof
        self._horario_prof = horario_prof
        self._telefone_prof = telefone_prof

    def get_cpf(self):
        return self._cpf

    def set_cpf(self, cpf):
        self._cpf = cpf
 
    def get_rg_prof(self):
        return self._rg_prof

    def set_rg_prof(self, rg_prof):
        self._rg_prof = rg_prof 

    def get_nome_prof(self):
        return self._nome_prof

    def set_nome_prof(self, nome_prof):
        self._nome_prof = nome_prof
     
    def get_horario_prof(self):
        return self._horario_prof

    def set_horario_prof(self, horario_prof):
        self._horario_prof = horario_prof
     
    def get_telefone_prof(self):
        return self._telefone_prof

    def set_telefone_prof(self, telefone_prof):
        self._telefone_prof = telefone_prof
        
    pass
