from abc import ABC, abstractmethod

# 1. CLASSE ABSTRATA E ENCAPSULAMENTO

class Veiculo(ABC):
    def __init__(self, placa):
        self.__placa = placa  # Atributo privado

    # Getter para acessar a placa com segurança
    @property
    def placa(self):
        return self.__placa

    @abstractmethod
    def calcular_tarifa_base(self) -> float:
        """Cálculo da tarifa do veículo"""
        pass

    @property
    @abstractmethod
    def tipo(self) -> str:
        """Retorna o tipo do veículo"""
        pass
        
        
            
    
