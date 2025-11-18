class Maquina:
    def _init_(self, nome, id_mqn, parte_trabalhada):
        self._nome = nome
        self._id_mqn = id_mqn
        self._parte_trabalhada = parte_trabalhada
        

    @property
    def nome(self):
        return self._nome_mqn

    @nome.setter
    def nome(self, value):
        self._nome_mqn = value

    @property
    def id_mqn(self):
        return self._id_mqn

    @id_mqn.setter
    def id_mqn(self, value):
        self._id_mqn = value

    @property
    def parte_trabalhada(self):
        return self._parte_trabalhada

    @parte_trabalhada.setter
    def parte_trabalhada(self, value):
        self._parte_trabalhada = value

        pass

    



