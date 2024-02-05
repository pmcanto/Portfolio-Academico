#Disciplina: ALGORITMOS E PROGRAMAÇÃO 1
#Projeto 1: Chuva de Meteoros
#Data: 27/09/2023
#ALUNOS: Camila Carniel
#        Gabriel Mendes
#        Pedro Canto

# Projeto feito com a restrinção de não utilizar listas e nem nada mais complexo que isso, como não utilizar funções, bibliotecas além de math, etc

#---------------------------------------------------------------------------------------------------------------------
#1. IMPORTS
import math

#---------------------------------------------------------------------------------------------------------------------
#2. VARIAVEIS 

# variavel para definir perimetro do terreno
terreno_x1 = 0
terreno_x2 = 0
terreno_y1 = 0
terreno_y2 = 0

# variavel para definir perimetro da casa
casa_x1 = 0
casa_x2 = 0
casa_y1 = 0
casa_y2 = 0

# coordenada do instituto de referencia
inst_base_x = 0
inst_base_y = 0


# opção do usuário do menu
op = 1

# valores do meteorito
distancia_met = 0
angulo_met = 0
meteorito = 1
radianos_met = 0
meteoro_x = 0

# quantos meteoritos cairam no total
met_total = 0

# quantos cairam dentro da propriedade
met_qnt_terreno = 0

# acertou a casa?
met_casa = False

# quantos meteoros cairam em cada quadrante
quad_ne = 0
quad_no = 0
quad_se = 0
quad_so = 0

#Centro da Propriedade para calculo posterior do quadrante
centx_terr = 0 #centro do eixo x da propriedade
centy_terr = 0 #centro do eixo y da propriedade
#---------------------------------------------------------------------------------------------------------------------
#3. MENU DE OPÇÕES

while (op!=5):
  # Menu de escolha
  print("\n")
  print(' _.: Sistema para Análise de Chuva de Meteoros :._')
  print('1. Definir perímetro da propriedade e da sede da fazenda')
  print('2. Unificar sistemas de coordenadas de referência')
  print('3. Processar registros de chuva de meteoros')
  print('4. Apresentar estatísticas')
  print('5. Sair')
  op = int(input("Opção: "))
  # se a op não for 1 a 5 pede para colocar um número valido.
  while (op < 1 or op > 5):
    print("\n Opção inválida!")
    op = int(input('digite novamente (1/2/3/4/5) : '))

  # Registra nas variaveis terreno e casa os valores maximo e minimo 

#---------------------------------------------------------------------------------------------------------------------
#4. OPÇÃO 1: Definir perimetro da propriedade e da sede da fazenda

    #perimetro do terreno
  if op == 1:
    print("\n")
    terreno_x1 = float(input('Digite primeira coordenada x do terreno: '))
    terreno_y1 = float(input('Digite primeira coordenada y do terreno: '))
    terreno_x2 = float(input('Digite segunda coordenada x do terreno: '))
    terreno_y2 = float(input('Digite segunda coordenada y do terreno:'))
    
    #achar o centro do terreno
    centx_terr = (terreno_x2+terreno_x1)/2 
    centy_terr = (terreno_y2+terreno_y1)/2

    #perimetro da propriedade
    print("\n")
    casa_x1 = float(input('Digite primeira coordenada x da casa: '))
    casa_y1 = float(input('Digite primeira coordenada y da casa: '))
    casa_x2 = float(input('Digite segunda coordenada x da casa: '))
    casa_y2 = float(input('Digite segunda coordenada y da casa: '))

#---------------------------------------------------------------------------------------------------------------------
#5. OPÇÃO 2: Unificar sistemas de coordenadas de referência

  #ponto de localização do instituto
  elif op == 2:
    print("\n")
    inst_base_x = float(input('Digite a coordernada x do instituto: '))
    inst_base_y = float(input('Digite a coordernada y do instituto: '))

#---------------------------------------------------------------------------------------------------------------------
#6. OPÇÃO 3: Processar registros de chuva de meteoros
  elif op == 3:
    
    # "Os dados são recalculados a cada chuva de meteoro" -> reseta as variáveis sempre que a op.3 for chamada 
    distancia_met = 0
    angulo_met = 0
    meteorito = 1
    radianos_met = 0
    meteoro_x = 0
    met_total = 0
    met_qnt_terreno = 0
    met_casa = False
    quad_ne = 0
    quad_no = 0
    quad_se = 0
    quad_so = 0
  
    
    #mensagem de erro caso o usuário não informe o terreno:
    if terreno_x1 == 0 and terreno_x2 == 0 and terreno_y1 == 0 and terreno_y1 == 0: 
      print("\n")
      print("Impossível processar qualquer registro de queda no momento: terreno ainda não informado")
      continue
    
    #mensagem de erro caso o usuário não informe a localização da casa:
    if casa_x1 == 0 and casa_x2 == 0 and casa_y1 == 0 and casa_y2 == 0:
      print("\n")
      print("Impossível processar qualquer registro de queda no momento: localização da propriedade ainda não informada")
      continue

    #mensagem de erro caso o usuário não informe o ponto do instituto:
    if inst_base_x == 0 and inst_base_y == 0:
      print("\n")
      print("Impossível processar qualquer registro de queda no momento: não foi feita a unificação dos sistemas referenciais nos cálculos")
      continue
    
    # Enquanto a distancia não for negativa
    while distancia_met >= 0:
      # pergunta a distancia e angulo do meteorito
      print(f'\n\nRegistro de meteorito número {meteorito} : \n')
      distancia_met = float(input('Digite a distância do meteorito: '))
      if distancia_met < 0:
        print("\n")
        print(f"Fim da coleta de registros: {met_total} queda(s) informada(s)")
        break
      angulo_met = float(input('Digite o ângulo do meteorito: '))

      # atualiza meteoritos no total e qual está sendo registrado agora
      met_total += 1
      meteorito += 1

      # converter angulo em radianos
      radianos_met = math.radians(angulo_met)

      #ponto a partir do instituto
      meteoro_x = distancia_met * math.cos(radianos_met)
      meteoro_y = distancia_met * math.sin(radianos_met)
      #ponto do instituto para o ponto cardesiano
      meteoro_x = (meteoro_x + inst_base_x)
      meteoro_y = (meteoro_y + inst_base_y)
    
      # caiu dentro do terreno
      if (terreno_x1<= meteoro_x) and (meteoro_x<=terreno_x2) and (terreno_y2<=meteoro_y) and (meteoro_y<=terreno_y1):
        met_qnt_terreno += 1

        #Caso o meteoro caia em cima da linha limite da propriedade ele registrará no sentido horário (meteorito 2 da lista de exercícios)
        
        # se o meteoro caiu no quadrante norte
        if meteoro_y >= centy_terr:
          # se caiu no quadrante nordeste
          if meteoro_x >= centx_terr:
            quad_ne += 1
          # se caiu no quadrante noroeste
          else:
            quad_no += 1
            
        # se caiu no quadrante sul
        elif meteoro_y <= centy_terr:
          # se caiu no quadrante sudeste
          if meteoro_x >= centx_terr:
            
            quad_se += 1
          # se caiu no sudoeste
          
          else:
            quad_so += 1

        
      # identificar se houve dano a propriedade 
      if (casa_x1<=meteoro_x>=casa_x2) and (casa_y1<=meteoro_y>=casa_y2):
        met_casa = True
        
    

#---------------------------------------------------------------------------------------------------------------------
#7. OPÇÃO 4: Apresentar estatísticas
  elif op == 4:
    print("\n")
    print(f"Total de quedas registradas: {met_total} (100%)" )
    print(f"Quedas dentro da propriedade: {met_qnt_terreno} ({met_qnt_terreno*100/met_total}%)" )
    
    if met_qnt_terreno == 0: #evitar erro ZeroDivisionError caso nenhum meteoro caia no terreno
      print("\n")
      print("Nenhum meteorito caiu no terreno")
      continue 
      #percentual de meteoritos que cairam em cada quadrante
    print(f"-> Quadrante NE:{quad_ne} ({quad_ne*100/met_qnt_terreno}%)" )
    print(f"-> Quadrante NO:{quad_no} ({quad_no*100/met_qnt_terreno}%)" )
    print(f"-> Quadrante SO:{quad_so} ({quad_so*100/met_qnt_terreno}%)" )
    print(f"-> Quadrante SE:{quad_se} ({quad_se*100/met_qnt_terreno}%)" )
    if met_casa == True:
        print("A edificação principal foi atingida? SIM")
    else: 
        print("A edificação principal foi atingida? NÃO")
      
#---------------------------------------------------------------------------------------------------------------------
#8. OPÇÃO 5: Sair
  elif op==5:
    exit
    
    