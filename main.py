from clientes import Clientes
from extrato import Extrato

def menu():
    print("\n=== EasyBank ===")
    print("1. Criar Conta")
    print("2. Autenticar")
    print("3. Sacar")
    print("4. Depositar")
    print("5. Exibir Extrato")
    print("6. Excluir Conta")
    print("0. Sair")

clientes = Clientes()  # Criando uma instância da classe Clientes
extrato = Extrato()    # Criando uma instância da classe Extrato
usuario_autenticado = False

while True:
    menu()
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        if not clientes.conta_criada:
            clientes.criar_conta()
        else:
            print("Conta já foi criada!")
    elif escolha == "2":
        if not clientes.conta_criada:
            print("Crie uma conta antes de fazer login.")
        else:
            usuario_autenticado = clientes.autenticar()
    elif escolha == "3":
        if usuario_autenticado:
            clientes.sacar()
        else:
            print("Faça login primeiro.")
    elif escolha == "4":
        if usuario_autenticado:
            clientes.depositar()
        else:
            print("Faça login primeiro.")
    elif escolha == "5":
        if usuario_autenticado:
            extrato.exibir_extrato()
        else:
            print("Faça login primeiro.")
    elif escolha == "6":
        if usuario_autenticado:
            clientes.excluir_conta()
            usuario_autenticado = False
        else:
            print("Faça login primeiro.")
    elif escolha == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")



