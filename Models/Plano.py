class Plano:
    def __init__(self, tipo_plano, id_plano):
        self._id_plano = id_plano
        self._tipo_plano = tipo_plano

    def get_id_plano(self):
        return self._id_plano

    def set_id_plano(self, value):
        self._id_plano = value

    def get_tipo_plano(self):
        return self._tipo_plano

    def set_tipo_plano(self, value):
        self._tipo_plano = value
        
    pass
