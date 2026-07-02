from Classes.tarifa import Tarifa
from datetime import datetime
import time

# 3. COMPOSIÇÃO, ASSOCIAÇÃO E ENCAPSULAMENTO

class Ticket:
    def __init__(self, id_ticket, veiculo):
        self.__id_ticket = id_ticket
        self.__veiculo = veiculo  # Associação
        self.__hora_entrada = datetime.now()
        self.__tarifa = None      # Composição (será um objeto Tarifa)

    # Getters necessários
    @property
    def id_ticket(self):
        """Retorna o ID do ticket"""
        return self.__id_ticket

    @property
    def veiculo(self):
        """Retorna o tipo do veiculo"""
        return self.__veiculo

    @property
    def hora_entrada(self):
        """Retorna a hora que o veiculo entra no estacionamento"""
        return self.__hora_entrada

    def calcular_valor_atual(self):
        """Calcula o valor conforme o tempo passa (é simulado)"""
        agora = datetime.now()
        # Na vida real usaria-se tempo_decorrido / 3600. 
        # Para o teste fazer sentido em segundos, 1 segundo real = 1 hora no sistema.
        tempo_decorrido = (agora - self.__hora_entrada).total_seconds()
        if tempo_decorrido < 1:
            tempo_decorrido = 1 # Garante pelo menos 1 hora cobrada
            
        valor = self.__veiculo.calcular_tarifa_base() * int(tempo_decorrido)
        return int(tempo_decorrido), valor

    def fechar_ticket(self):
        """Fecha o ticket guardando o valor final na composição de Tarifa"""
        horas, valor_final = self.calcular_valor_atual()
        self.__tarifa = Tarifa(valor_final)  # Instanciação interna (Composição)
        return horas, valor_final