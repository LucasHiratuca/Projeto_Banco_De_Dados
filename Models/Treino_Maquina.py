class Treino_Maquina:
    def __init__(self, id_tr, nome_mqn):
        self._id_tr = id_tr
        self._nome_mqn = nome_mqn


    @property
    def id_tr(self):
        return self._id_tr

    @id_tr.setter
    def id_tr(self, value):
        self._id_tr = value

    @property
    def nome_mqn(self):
        return self._nome_mqn

    @nome_mqn.setter
    def nome_mqn(self, value):
        self._nome_mqn = value

        pass

