from Classes.carro import Carro
from Classes.moto import Moto
from Classes.ticket import Ticket


# 4. SISTEMA DO OPERÁRIO

class SistemaEstacionamento:
    def __init__(self):
        self.__vagas_ocupadas = {}  # {placa: objeto_ticket} -> Privado
        self.__faturamento_total = 0.0
        self.__contador_id = 1

    @property
    def vagas_ocupadas(self):
        """Retorna as vagas ocupadas"""
        return self.__vagas_ocupadas

    @property
    def faturamento_total(self):
        """Retorna o faturamento total no dia de expediente"""
        return self.__faturamento_total

    def registrar_entrada(self, placa, tipo_opcao):
        """Emite o ticket de entrada do veículo no estacionamento"""
        if placa in self.__vagas_ocupadas:
            print(f"\nErro: Veículo com placa {placa} já está no estacionamento!")
            return

        if tipo_opcao == "1":
            veiculo = Carro(placa)
        elif tipo_opcao == "2":
            veiculo = Moto(placa)
        else:
            print("\nOpção de veículo inválida!")
            return

        novo_ticket = Ticket(self.__contador_id, veiculo)
        self.__vagas_ocupadas[placa] = novo_ticket
        self.__contador_id += 1
        
        print("\n" + "="*40)
        print(f"TICKET EMITIDO (ID: {novo_ticket.id_ticket})")
        print(f"Placa: {veiculo.placa}")
        print(f"Tipo:  {veiculo.tipo}")
        print(f"Tarifa Base: R$ {veiculo.calcular_tarifa_base():.2f}/h")
        print("="*40)

    def registrar_saida(self, placa):
        """Registra a saída do veículo após o pagamento"""
        if placa not in self.__vagas_ocupadas:
            print(f"\nErro: Veículo com placa {placa} não encontrado!")
            return

        ticket = self.__vagas_ocupadas.pop(placa)
        horas, valor_pago = ticket.fechar_ticket()
        self.__faturamento_total += valor_pago
        
        print("\n" + "$"*40)
        print(f"COMPROVANTE DE PAGAMENTO")
        print(f"Ticket ID: {ticket.id_ticket} | Placa: {placa}")
        print(f"Tempo de permanência: {horas} hora(s) simulada(s)")
        print(f"Valor Total Pago: R$ {valor_pago:.2f}")
        print("$"*40)

    def monitorar_estacionamento(self):
        """Mostra o status atual das vagas e quanto cada um deve até o momento"""
        if not self.__vagas_ocupadas:
            print("\n[ESTACIONAMENTO VAZIO]")
            return

        print("\n--- VEÍCULOS NO ESTACIONAMENTO (O tempo está passando...) ---")
        for placa, ticket in self.__vagas_ocupadas.items():
            horas, valor_atual = ticket.calcular_valor_atual()
            print(f"ID: {ticket.id_ticket} | [{placa}] - {ticket.veiculo.tipo} | Tempo: {horas}h | Valor Atual: R$ {valor_atual:.2f}")
        
        
        