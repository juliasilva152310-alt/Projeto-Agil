# Login e solicitação de serviço

serviços_disponiveis = {
    1 : "E-mail",
    2 : "Faxinação de rua",
    3 : "Solicitação de recipientes de lixo"
}

def tela_login():
    print("\n--- Tela de Login ---")
    email = input("Email: ")
    senha = input("Senha: ")

    # Validação do Email
    if "@" in email and ".com" in email:
        print("E-mail formatado corretamente.")
    else:
        print("Erro: E-mail inválido (faltando @ ou .com)")
        return False # Indica que o login falhou

    # Validação da Senha
    if len(senha) == 8:
        print("Senha válida.")
    else:
        print("Erro: A senha deve ter exatamente 8 caracteres.")
        return False

    print("Acesso permitido!\n")
    return True # Sucesso!

def solicitação():
    print("---- Atendimentos ----")
    for num, servico in serviços_disponiveis.items():
        print(f"{num}: {servico}")
    print("0: Sair/Voltar ao Login")

    while True: # Ela mantem o programa rodando até o usuário escolher sair
        try:
            escolha = int(input("\nDigite o número do serviço: "))

            if escolha == 0:
                print("...Voltando ao login...")
                iniciar_sistema() # Reinicia o fluxo
                break # Comando para sair


            elif escolha == 1:
              usuario = str(input("Digite o seu nome: "))
              mensagem = input("Digite sua mensagem: ")

              print(mensagem)

              print("A mensagem do usuário", usuario, "foi enviada com sucesso")



            elif escolha == 2:
              endereço = input("Digite o endereço para solicicitar a faxineiro de rua: ")
              print("O faxineiro foi solicitado para o endereço ",endereço)



            elif escolha == 3:
              print("___Tipos de recipiente___")
              print("1 - Caçambas")
              print("2 - Lata reciclavel")
              print("3 - Container grande")
              print("4 - Lixeira comum")

              tipo = int(input("Digite o número do recipitente desejado: "))
              endereço = input("Digite o endereço da entrega: ")

              tipos = {
                  1: "Caçambas",
                  2: "Lata reciclavel",
                  3: "Container grande",
                  4: "Lixeira comum"
              }

              if tipo in tipos:
                  print(f"Solicitação do Recipiente de lixo ",{tipos[tipo]},"para o endereço",endereço)
              else:
                    print("Solicitação de recipiente inválida")
              break

            else:
                print("Opção inválida, tente novamente.")

        except ValueError:
            print("Por favor, digite apenas números.")

def iniciar_sistema():
    if tela_login():
        solicitação()

# Iniciar o programa
iniciar_sistema()
