# Matheus Soares / 2016.1904.030-1
# Victor Ezequiel / 2016.1904.047-6
# Gabriel Menezes / 2016.1906.005-1

def calcularHeuristica(node):
   numPecas, coordenadasDasPecas = contarPecas(node.estado)
   unsPresosNosCantos = contarUnsPresos(node.estado)
   distanciaMediaManhattan = calcularDistanciaManhattan(node.estado, coordenadasDasPecas) / numPecas
   # fatorDeProfundidade = 1024 - (node.custo * node.custo)

   return  distanciaMediaManhattan + (pow(unsPresosNosCantos,pow(2,unsPresosNosCantos)))

# Calcula a soma da distancia de cada peca ate todas as outras pecas no tabuleiro
def calcularDistanciaManhattan(estado, coordenadasDasPecas):
   dMan = 0
   for linha in coordenadasDasPecas:
      for coluna in coordenadasDasPecas:
         if (linha == coluna): continue
         x = abs(linha[0]-coluna[0])
         y = abs(linha[1]-coluna[1])
         dMan += (x+y)

   return dMan

# Conta numero de 1's no tabuleiro
def contarPecas(estado):
   numPecas = 0
   coordenadasDasPecas = []
   for linha in range(0,7):
      for coluna in range(0,7):
         if (estado[linha][coluna] == 1):
            numPecas += estado[linha][coluna]
            coordenadasDasPecas.append([linha,coluna])

   return (numPecas, coordenadasDasPecas)

# Serao contados 1's nas extremidades dos tabuleiros cujas pecas adjacentes sao 0's
def contarUnsPresos(estado):
   unsNosCantos = 0
   if (estado[0][2] == 1
   and estado[0][3] == 0
   and estado[1][2] == 0):      
      unsNosCantos += 1

   if (estado[0][4] == 1
   and estado[0][3] == 0
   and estado[1][4] == 0):
      unsNosCantos += 1

   if (estado[2][0] == 1
   and estado[3][0] == 0
   and estado[2][1] == 0):
      unsNosCantos += 1

   if (estado[4][0] == 1
   and estado[3][0] == 0
   and estado[4][1] == 0):
      unsNosCantos += 1
      
   if (estado[6][2] == 1
   and estado[5][2] == 0
   and estado[6][3] == 0):
      unsNosCantos += 1

   if (estado[6][4] == 1
   and estado[6][3] == 0
   and estado[5][4] == 0):
      unsNosCantos += 1

   if (estado[2][6] == 1
   and estado[2][5] == 0
   and estado[3][6] == 0):
      unsNosCantos += 1

   if (estado[4][6] == 1
   and estado[4][5] == 0
   and estado[3][6] == 0):
      unsNosCantos += 1

   return unsNosCantos
