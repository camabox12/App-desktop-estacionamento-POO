from Classes.veículo import Veiculo

# 2. HERANÇA

class Carro(Veiculo):
    def calcular_tarifa_base(self):
        return 12.00  # Carro é mais caro: R$ 12,00 por hora

    @property
    def tipo(self):
        return "Carro"
    