#Disciplina: ALGORITMOS E PROGRAMAÇÃO 1
#Projeto 2: Conta bancária
#Data: 11/2023
#ALUNOS: Camila Carniel
#        Gabriel Mendes
#        Pedro Canto

# código feito com a restrinção de não utilizar dicionarios, bibliotecas ou classes e objetos


'''
 deve incluir as seguintes funcionalidades:
1. Cadastro da conta: é a primeira ação necessária e só deve ser executada uma única vez. Nessa opção, serão fornecidos os dados da conta como nome, saldo inicial, senha, limite de crédito, etc.
2. Depósito: opção utilizada para acrescentar dinheiro na conta, atualizando o saldo e o histórico de operações
3. Saque: mediante fornecimento de senha válida, a opção é utilizada para retirar dinheiro da conta, atualizando o saldo e o histórico de operações. Nessa operação, é necessário validar o saque (saldo suficiente e/ou limite de crédito disponível)
4. Consulta saldo: mediante fornecimento de senha válida, é exibido o saldo da conta
5. Extrato: mediante fornecimento de senha válida, é exibido o histórico das operações
na conta (saques e depósitos)

'''
#-----------------------------------------------------------------------
#01. BÁSICO
#-----------------------------------------------------------------------
#IMPORTS
import random
import os

#VARIÁVEIS INICIAIS
conta = []  #Dados do usuário armazenados em uma lista
clientes_do_banco = []  #Banco de dados com todos os clientes
id = 0
opcao = 0

#-----------------------------------------------------------------------
#02.FUNÇÕES
#-----------------------------------------------------------------------

#Função para iniciar o programa
def inicializacao():
  print('+======================================================+')
  print('|  __  __    _    ____ _  __  ____    _    _   _ _  __ |')
  print('| |  \/  |  / \  / ___| |/ / | __ )  / \  | \ | | |/ / |')
  print('| | |\/| | / _ \| |   |   /  |  _ \ / _ \ |  \| |   /  |')
  print('| | |  | |/ ___ \ |___| . \  | |_) / ___ \| |\  | . \  |')
  print('| |_|  |_/_/   \_\____|_|\_\ |____/_/   \_\_| \_|_|\_\ |')
  print('|                                                      |')
  print('+======================================================+')

  print('''
  (01) Registrar novo usuário
  (02) Login em usuário existente
  (03) Sair do aplicativo
  ''')
  
  entrada = str(input())

  if entrada == "1":
    return cadastro()
  elif entrada == "2":
    
    return login()
  elif entrada == "3":
    fechar()
  else:
    return inicializacao()

#Função para finalizar o programa
def fechar():
  print('\n')
  print('+======================================================+')
  print('|  __  __    _    ____ _  __  ____    _    _   _ _  __ |')
  print('| |  \/  |  / \  / ___| |/ / | __ )  / \  | \ | | |/ / |')
  print('| | |\/| | / _ \| |   |   /  |  _ \ / _ \ |  \| |   /  |')
  print('| | |  | |/ ___ \ |___| . \  | |_) / ___ \| |\  | . \  |')
  print('| |_|  |_/_/   \_\____|_|\_\ |____/_/   \_\_| \_|_|\_\ |')
  print('|                                                      |')
  print('+======================================================+')
  print('''\n
    Este programa foi desenvolvido por:
    Camila Nunes Carniel
    Gabriel Erick Mendes 
    Pedro Moniz Canto 
  ''')
  exit()

#Verificar se o usuário existe (EXTRA)
def verificacao_usuario(usuario):
  #verificar se o usuario existe
  global clientes_do_banco
  
  for i in clientes_do_banco:
    if usuario == i[0]:
      return True
  return False

#Função para realizar o cadastro bancário
def cadastro():
  global id
  print("Para acessar o MACK BANK crie sua conta!")
  
  usuario = str(input("Digite um nome de usuário: "))
  while verificacao_usuario(usuario):
    print("Usuário já existente! Tente novamente")
    usuario = str(input("Digite um nome de usuário: "))
  senha = str(input("Digite uma senha com 6 dígitos: "))

  while not (senha.isdigit() and 100000 <= int(senha) <= 999999 and senha != '123456'):
    if senha == "123456":
      print("Escolha uma senha mais difícil! É um cadastro bancário")
    senha = str(input("Senha inválida. Digite uma senha com 6 dígitos:")).strip()

  historico = []

  conta.insert(0, usuario)  #usuario
  conta.insert(1, senha) #senha
  conta.insert(2, None)  #numero da conta
  conta.insert(3, "")  #nome do cliente
  conta.insert(4, None)  #telefone
  conta.insert(5, "")  #email
  conta.insert(6, 0)  #saldo
  conta.insert(7, 0)  #limite de crédito
  conta.insert(8, historico)  #historico de transações
  conta.insert(9, (len(clientes_do_banco)))  #ID
  id = conta[9]

  if conta[0] and conta[1]:
    print("\n\nCadastro realizado com sucesso!")
    clientes_do_banco.append(conta[:])
  else:
    print("\n\nNão foi possivel cadastro-lo, reescreva os seus dados")
    return cadastro()


#Função para Login e trocar de senha (EXTRA)
def login():
  global id
  global conta
  #ler_txt()
  nome_do_usuario = str(input("Digite seu nome de usuário: "))
  senha = input("Digite sua senha: ")

  for usuario in clientes_do_banco:
    if usuario[0] == nome_do_usuario and usuario[1] == senha:
      print("Bem vindo ao MACK BANK!")
      conta = usuario
      id = conta[9]
      return conta
  else:
    print("\nLogin Incorreto. Tente novamente!")
    return inicializacao()

#Função para Logoff e trocar de senha (EXTRA)
def logoff():
  #Reseta as variáveis
  salvar()
  conta.clear()
  id = 0
  return inicializacao()

#Função para salvar as alterações no id do usuário (EXTRA)
def salvar():
  global clientes_do_banco
  global conta

  if clientes_do_banco[id][0] == conta[0] and clientes_do_banco[id][
      1] == conta[1]:
    clientes_do_banco[id] = conta[:]
    #escrever_txt()
    print("\n\nAlterações realizadas com sucesso!\n\n")

  return

#Função para cadastrar a conta corrente
def cadastro_conta_corrente():

  print("CADASTRO DE CONTA CORRENTE")
  num_conta = random.randint(1000, 9999)  #número aleatório de 4 digitos

  nome_do_cliente = str(input("\nNome do cliente:"))
  while nome_do_cliente.isalpha() == False:
    print("\nO nome pode conter apenas letras! Por favor, tente novamente")
    nome_do_cliente = str(input("\nNome do cliente:"))

  telefone = str(input("\nTelefone:"))
  while telefone.isnumeric() == False:
    print("\nO telefone pode conter apenas números!")
    telefone = str(input("\nTelefone: "))

  email = str(input("\nEmail:"))
  while "@" not in email:
    print("\nEmail inválido. Digite novamente!")
    email = str(input("\nEmail:"))

  saldo = 0
  valor = int(input("\nQual é o valor inicial a ser depositado? "))
  while valor <= 1000:
    print("\nVocê precisa de um saldo inicial maior que 1000! Tente novamente")
    valor = int(input("\nQual é o valor inicial a ser depositado? "))
  saldo += valor

  historico = []   #HISTÓRICO - Lista para armazenar o histórico de transações
  conta.insert(7, historico)
  
  limite_de_credito = saldo+1000
  print(f"\nLimite de crédito calculado a partir do saldo inicial: R$ {limite_de_credito}")


  verificar_senha()
 

  conta[2] = num_conta  #numero da conta
  conta[3] = nome_do_cliente  #nome do cliente
  conta[4] = telefone  #telefone
  conta[5] = email  #email
  conta[6] = saldo  #saldo
  conta[8] = limite_de_credito  #limite de crédito
  salvar()

  return


#Função para depositar
def depositar():

  if conta[2] == None:
    print("\nCadastre sua conta corrente ates de consultar seu saldo!")
    return
  
  deposito = int(input("Quanto deseja depositar? "))
  if deposito <= 0:
    print("Valor Inválido")
  conta[6] += deposito  #valor mais att no zero
  conta[7].append(deposito)  #valor depositado no extrato
  print(f"Valor depositado: {deposito}")
  print("Depósito realizado com sucesso!")
  return conta[6]

#Função para Sacar
def sacar():

  
  if conta[2] == None:
    print("\nCadastre sua conta corrente ates de consultar seu saldo!")
    return

  sacar_din = (int(input("\nQuanto deseja sacar? ")))
  if sacar_din > conta[6]:
    print("Saldo insuficiente")
    return conta[6]

  elif sacar_din <= 0:
    print("Valor Inválido")
    return conta[6]
  
  else:
    print(f"\nValor sacado: {sacar_din}")
    print("Saque realizado com sucesso")
    conta[6] -= sacar_din
    conta[7].append(-sacar_din)  #Registro da transação
  
    return conta[6]
 
#Função para verificar senha
def verificar_senha():
  global id

  senha_confirmacao = str(
    input("\n\nConfirme sua senha:  "))

  cont = 1 #Contador para estabelecer um numero máximo de tentativas de senha incorretas
  while cont != 3:
    if senha_confirmacao != clientes_do_banco[id][1]:
      senha_confirmacao = str(
        input(f"\n\nTentativa numero {cont}: Senha incorreta! Tente novamente: "))
    if senha_confirmacao == clientes_do_banco[id][1]:
      break
    else:
      cont += 1

  if cont == 3:
    print("Número máximo de tentativos. Por segurança, o aplicativo será fechado")
    fechar()
  else:
    return True

#Função para alterar senha (EXTRA)
def alterar_senha():
  senha = input('\nDigite sua nova senha de 6 dígitos: ')

  while not (senha.isdigit() and 100000 <= int(senha) <= 999999 and senha != '123456'):
    if senha == "123456":
      print("Escolha uma senha mais difícil! É um cadastro bancário")
    senha = str(input("Senha inválida. Digite uma senha com 6 dígitos: "))

  clientes_do_banco[id][1] = senha
  
#Função para consultar
def consultar():

  if conta[2] == None:
    print("\nCadastre sua conta corrente ates de consultar seu saldo!")
    return
  
  print(f"Valor atual em conta: {conta[6]}")

#Função para Extrato
def extrato():
  global id

  if conta[2] == None:
    print("\nCadastre sua conta corrente ates de consultar seu saldo!\n")
    return
  indice = 0
  
  print("\n")
  for transacao in conta[7]:
    indice += 1
    print(f"Histórico: {indice}, valor: {transacao}")
  consultar()

#Função para PIX (EXTRA)
def pix():
  valor = float(input("Digite o valor a ser transferido via PIX: "))
  destinatario = str(input("Digite o usuário de destino: "))

  
  usuario_localizado = None
  #ver se o destinatario existe
  for i in range(len(clientes_do_banco)):
    if clientes_do_banco[i][1] == destinatario:
      usuario_localizado = i
      print("\nUsuário encontrado")
      break
    
      
      
  if usuario_localizado == None:
    print("\nUsuário não encontrado. Transferência cancelada.")
    return
  #Verificar a senha
  print("\nConfirme sua senha para realizar o PIX: ")
  verificar_senha()

  #Verificar se tem saldo
  if valor > float(conta[6]):
    print("\nSaldo insuficiente para realizar o PIX.\n")
    return
    
  conta[6] -= valor  
  clientes_do_banco[usuario_localizado][6] += valor  
  conta[7].append(f"-{valor} para {destinatario[0]}")
  clientes_do_banco[usuario_localizado][7].append(f"{valor} de {conta[0]}")
  print("\nPIX realizado com sucesso!\n")
    

#-----------------------------------------------------------------------
#03. PROGRAMA
#-----------------------------------------------------------------------
inicializacao()

#Enquanto a opçãp escolhida for diferente de sair, o programa continua
while opcao != 9:
  opcao = input('''
    MACK BANK - ESCOLHA UMA OPÇÃO:
    (01) CADASTRAR CONTA CORRENTE
    (02) DEPOSITAR
    (O3) SACAR
    (04) CONSULTAR SALDO
    (05) CONSULTAR EXTRATO
    (06) ALTERAR A SENHA DE CADASTRO
    (07) VER O HISTÓRICO DE TRANSAÇÕES
    (08) PIX
    (09) LOG OFF
    (10) FECHAR BANCO
    Digite: 
  ''')

  #----------------------------------------------------------------------
  #OPÇÃO: CONTA CORRENTE
  if opcao == "1":
    opcao = '0'

    cadastro_conta_corrente()

  #-----------------------------------------------------------------------
  #OPÇÃO:DEPOSITAR
  elif opcao == "2":
    opcao = '0'

    verificar_senha()
    depositar()

  #-----------------------------------------------------------------------
  #OPÇÃO: SACAR
  elif opcao == "3":
    opcao = '0'

    verificar_senha()
    sacar()

  #-----------------------------------------------------------------------
  #OPÇÃO: CONSULTAR SALDO
  elif opcao == "4":
    opcao = '0'

    verificar_senha()
    consultar()

  #-----------------------------------------------------------------------
  #OPÇÃO: CONSULTAR EXTRATO
  elif opcao == "5":
    opcao = '0'

    verificar_senha()
    extrato()

  #-----------------------------------------------------------------------
  #OPÇÃO: ALTERAR A SENHA DE CADASTRO
  elif opcao == "6":
    opcao = '0'

    verificar_senha()
    alterar_senha()

  #-----------------------------------------------------------------------
  #OPÇÃO: VER O HISTÓRICO DE TRANSAÇÕES
  elif opcao == "7":
    opcao = '0'

    verificar_senha()
    extrato()

  #-----------------------------------------------------------------------
  #OPÇÃO: PIX
  elif opcao == "8":
    opcao = '0'

    pix()
    
  #-----------------------------------------------------------------------
  #OPÇÃO: Log Off
  elif opcao == "9":
    opcao = '0'

    logoff()

#-------------------------------------------------------------------------
#OPÇÃO: FINALIZAR
  elif opcao == "10":
    fechar()
    
#Caso a opção seja inválida
  else:
    print("\nOpção inválida! Digite novamente")
    opcao = input('''
    MACK BANK - ESCOLHA UMA OPÇÃO:
    (01) CADASTRAR CONTA CORRENTE
    (02) DEPOSITAR
    (O3) SACAR
    (04) CONSULTAR SALDO
    (05) CONSULTAR EXTRATO
    (06) ALTERAR A SENHA DE CADASTRO
    (07) VER O HISTÓRICO DE TRANSAÇÕES
    (08) PIX
    (09) LOG OFF
    (10) FECHAR BANCO
    Digite: 
    ''')
