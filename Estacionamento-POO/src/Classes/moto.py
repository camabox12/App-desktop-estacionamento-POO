from Classes.veículo import Veiculo

# 2. HERANÇA

class Moto(Veiculo):
    def calcular_tarifa_base(self):
        return 6.00   # Moto é mais barata: R$ 6,00 por hora

    @property
    def tipo(self):
        return "Moto"