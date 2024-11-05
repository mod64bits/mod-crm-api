import datetime

class Datas:
    def __init__(self, data_inicial=datetime.date.today(), quantidade_dias=15):
        self.data_inicial = data_inicial
        self.quantidade_dias = quantidade_dias

    def vencimento(self):
        data = self.data_inicial + datetime.timedelta(days=self.quantidade_dias)
        print(f"Data:{data}")
        return self.verificar_fim_de_semana(data)

    def verificar_fim_de_semana(self, data_vencimento):
        dia = data_vencimento.weekday()
        if dia == 5:
            return data_vencimento + datetime.timedelta(days=2)
        if dia == 6:
            return data_vencimento + datetime.timedelta(days=1)
        return data_vencimento
