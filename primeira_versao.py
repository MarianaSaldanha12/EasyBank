import sys

saldo = 0.0
extrato_file = "extrato.txt" # Nome do arquivo para armazenar o extrato

def salvar_extrato(transacoes):
    with open(extrato_file, "w") as file:
        for transacao in transacoes:
            file.write(transacao + "\n")

def carregar_extrato():
    try:
        with open(extrato_file, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []
    
def apagar_extrato():
    with open(extrato_file, 'w') as file:
        file.write("") #Escreve um astring vazia para apagar os dados
    
while True:
    
    extrato = carregar_extrato()

    opcao = int(input("Informe uma opção: \n[1] Sacar \n[2] Depositar \n[3] Extrato \n[4] Excluir Conta \n[5] Sair: \n "))

    if opcao == 1:
        valor = float(input("Informe a quantia para o saque: "))
        saldo -= valor # Atualizando o saldo após o saque
        transacao = f"Saque: - R$ {valor:.2f}"
        extrato.append(transacao)# Adiciona a transação ao extrato
        salvar_extrato(extrato)# Salva o extrato no arquivo
        print(f"Saque de R$ {valor:.2f} efetuado com sucesso.")
        print(f"Saldo restante: R$ {saldo:.2f}")
    elif opcao == 2:
        valor = float(input("Informe a quantia para o depósito: "))
        saldo += valor # Atualizando o saldo após o depósito
        transacao = f"Saque: + R$ {valor:.2f}"
        extrato.append(transacao)# Adiciona a transação ao extrato
        salvar_extrato(extrato)# Salva o extrato no arquivo
        print(f"Depósito de R$ {valor:.2f} efetuado com sucesso.")
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("Exibindo o extrato...")
    elif opcao == 3:
        print("Exibindo o extrato...")
        if len(extrato) == 0:
            print("Nenhuma transação no extrato")
        else:
            for transacao in extrato:
                print(transacao.strip())# Remove quebras de linha ao imprimir
    elif opcao == 4:
        apagar_extrato() # Chama a função para apagar o extrato
        saldo = 0.0 #Reinicia o saldo para zero
        print("Conta excluída com sucesso!")
    elif opcao == 5:
        sys.exit("Saindo da conta.")
    else:
        print("Opção inválida")

    continuar = input("Deseja continuar? (S/N): ").upper()
    if continuar != 'S':
        break