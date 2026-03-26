from datetime import datetime


class Veiculo:
    def __init__(self, tag: str, morador: str, apartamento: str, placa: str, modelo: str, data_inscricao: str):
        self.tag = tag
        self.morador = morador
        self.apartamento = apartamento
        self.placa = placa
        self.modelo = modelo
        self.data_inscricao = data_inscricao

    def to_dict(self):
        return {
            "morador": self.morador,
            "apartamento": self.apartamento,
            "placa": self.placa,
            "modelo": self.modelo,
            "data-inscricao": self.data_inscricao,
            "entrada": None,
            "saida": None
        }

    