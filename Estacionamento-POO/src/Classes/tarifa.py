class Tarifa:
    def __init__(self, valor_total):
        self.__valor_total = valor_total

    @property
    def valor_total(self):
        """Retorna o valor total da tarifa a ser paga"""
        return self.__valor_total