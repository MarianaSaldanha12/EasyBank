import sys

saldo = 2000.0
extrato_file = "extrato.txt"

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
    
extrato = carregar_extrato()

opcao = int(input("Informe uma opção: \n[1] Sacar \n[2] Extrato: \n "))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))
    if valor > saldo:
        print("Saldo insuficiente para saque.")
    else:
        saldo -= valor
        transacao = f"Saque: - R$ {valor:.2f}"
        extrato.append(transacao)# Adiciona a transação ao extrato
        salvar_extrato(extrato)# Salva o extrato no arquivo
        print(f"Saque de R$ {valor:.2f} efetuado com sucesso.")
        print(f"Saldo restante: R$ {saldo:.2f}")
elif opcao == 2:
    print("Exibindo o extrato...")
    if len(extrato) == 0:
        print("Nenhuma transação no extrato")
    else:
        for transacao in extrato:
            print(transacao.strip())# Remove quebras de linha ao imprimir
else:
    sys.exit("Opção inválida")