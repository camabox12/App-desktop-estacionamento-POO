from Classes.sistema import SistemaEstacionamento

# 5. MENU DO OPERÁRIO (TESTE)

if __name__ == "__main__":
    app = SistemaEstacionamento()
    
    print("=" * 55)
    print("      APP DE GERENCIAMENTO DE ESTACIONAMENTO     ")
    print("          PAINEL DE CONTROLE DO OPERÁRIO            ")
    print("=" * 55)

    while True:
        # Toda vez que o menu aparece, ele atualiza o status do estacionamento com os valores subindo
        app.monitorar_estacionamento()
        
        print(f"\nFaturamento do Dia: R$ {app.faturamento_total:.2f}")
        print("\n[1] Registrar Entrada de Veículo")
        print("[2] Registrar Saída (Cobrança)")
        print("[3] Fechar Sistema e Sair")
        
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            placa = input("Digite a placa do veículo (Ex: AAA-0000): ").strip().upper()
            print("Selecione o tipo:")
            print("[1] Carro")
            print("[2] Moto")
            tipo = input("Opção: ").strip()
            app.registrar_entrada(placa, tipo)
            
        elif opcao == "2":
            placa = input("Digite a placa do veículo saindo: ").strip().upper()
            app.registrar_saida(placa)
            
        elif opcao == "3":
            print(f"\nEncerrando o expediente. Faturamento total: R$ {app.faturamento_total:.2f}")
            break
        else:
            print("\n Opção inválida!")
            
        print("\n" + "-"*55)
        