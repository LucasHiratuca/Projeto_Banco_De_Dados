class Plano:
    def_init_(self, tipo_plano, id_plano):
        self._id_plano = id_plano
        self._tipo_plano = tipo_plano


    @property
    def id_plano(self):
        return self._id_plano

    @id_plano.setter
    def id_plano(self, value):
        self._id_plano = value

    @property
    def tipo_palno(self):
        return self._tipo_plano

    @tipo_palno.setter
    def tipo_palno(self, value):
        self._tipo_plano = value

   

        pass
