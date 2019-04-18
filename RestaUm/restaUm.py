import copy
import sys

class Enum(set):
   def __getattr__(self, name):
      if name in self:
         return name

DirecaoDoMovimento = Enum(["CIMA", "BAIXO", "ESQUERDA", "DIREITA"])

# As seguintes posicoes nao sao consideradas no tabuleiro
coordenadasInexistentes = [
   [0,0],[0,1],[0,5],[0,6],
   [1,0],[1,1],[1,5],[1,6],
   [5,0],[5,1],[5,5],[5,6],
   [6,0],[6,1],[6,5],[6,6]
]
estadosDoTabuleiro = [
   [0,0,1,1,1,0,0],
   [0,0,1,1,1,0,0],
   [1,1,1,1,1,1,1],
   [1,1,1,0,1,1,1],
   [1,1,1,1,1,1,1],
   [0,0,1,1,1,0,0],
   [0,0,1,1,1,0,0]
]
estadoInicial = [
   [0,0,1,1,1,0,0],
   [0,0,1,1,1,0,0],
   [1,1,1,1,1,1,1],
   [1,1,1,0,1,1,1],
   [1,1,1,1,1,1,1],
   [0,0,1,1,1,0,0],
   [0,0,1,1,1,0,0]
]

# O estado final possui apenas uma peca no tabuleiro, ou seja, um unico "1".
#  Se a soma de todos os estados for = 1, e estado final
def verificarEstadoFinal():
   soma = 0
   for linhas in estadosDoTabuleiro:
      for coluna in linhas:
         soma += coluna
      if (soma > 1 ):
         break
   return (True if soma == 1 else False)

# Verifica se o movimento partindo da origem para o destino e valido
def movimentoValido(origem, destino):
   if (movimentoCoordenadaInexistente(origem) 
   or movimentoCoordenadaInexistente(destino)):
      return False

   if (movimentoForaDeAlcance(origem, destino)):
      return False

   if (movimentoParaPosicaoOcupada(destino)):
      return False
   return True

# Verifica se o destino ja esta ocupado por um '1'
def movimentoParaPosicaoOcupada(destino):
   if (estadosDoTabuleiro[destino[0]][destino[1]] == 1):
      return True
   return False

# Verifica se o movimento e de apenas 2 posicoes
def movimentoForaDeAlcance(origem, destino):
   ox = origem[0]
   oy = origem[1]
   dx = destino[0]
   dy = destino[1]

   if (abs(ox-dx) == 2 and abs(oy-dy) == 0):
      return False
   if (abs(ox-dx) == 0 and abs(oy-dy) == 2):
      return False

   return True
 
# Verifica se a coordenada esta nas coordenadas inexistentes
def movimentoCoordenadaInexistente(coordenada):
   if (coordenada in coordenadasInexistentes):
      return True
   if (coordenada[0] > 6 or coordenada[0] < 0
      or coordenada[1] > 6 or coordenada[1] < 0):
      return True
   return False

def moverPecaParaBaixo(linha, coluna, estado):
   if (not movimentoValido([linha,coluna], [linha+2,coluna])):
      return

   estado[linha][coluna] = 0
   estado[linha+1][coluna] = 0
   estado[linha+2][coluna] = 1

   return estado

def moverPecaParaEsquerda(linha, coluna, estado):
   if (not movimentoValido([linha,coluna], [linha,coluna-2])):
      return

   estado[linha][coluna] = 0
   estado[linha][coluna-1] = 0
   estado[linha][coluna-2] = 1

   return estado

def moverPecaParaCima(linha, coluna, estado):
   if (not movimentoValido([linha,coluna], [linha-2,coluna])):
      return

   estado[linha][coluna] = 0
   estado[linha-1][coluna] = 0
   estado[linha-2][coluna] = 1

   return estado

def moverPecaParaDireita(linha, coluna, estado):
   if (not movimentoValido([linha,coluna], [linha,coluna+2])):
      return

   estado[linha][coluna] = 0
   estado[linha][coluna+1] = 0
   estado[linha][coluna+2] = 1

   return estado

idCount = 0
searchTree = []
explorados = []
# Search Tree Node
class STNode:
   def __init__(self, paiId, estado, movimento):
      global idCount
      self.id = idCount
      idCount += 1
      self.paiId = paiId
      self.estado = estado
      self.movimento = movimento
      self.listaDeFilhos = []
      self.funcaoCusto = 0
      self.funcaoAvaliacao = 0
      self.fitness = sys.maxsize
      self.procurarFilhosPossiveis()
      self.avaliarNode()

   def __str__(self):
      string = "======================"
      string += "\nid=%d" % self.id
      string += "\npaiId=%d" % self.paiId
      string += "\nmovimento=%s" % self.movimento
      string += "\nfitness=%s" % self.fitness
      string += "\n"
      for linha in self.estado:
         string += str(linha)
         string += "\n"
      string += "======================"

      return string

   # Heuristicas
   def calcularFuncaoAvaliacao(self):
      posOcupadas = 0
      for linha in self.estado:
         for coluna in linha:
            posOcupadas += coluna

      return self.funcaoCusto + posOcupadas

   def avaliarNode(self):
      pai = None
      for node in explorados:
         if (node.id == self.paiId): 
            pai = node
      if (pai != None):
         self.funcaoCusto = pai.funcaoCusto + 1
         self.funcaoAvaliacao = self.calcularFuncaoAvaliacao()
         self.fitness = self.funcaoCusto + self.funcaoAvaliacao
      

   def procurarFilhosPossiveis(self):
      for linha in range(0,7):
         for coluna in range(0,7):
            estado = moverPecaParaBaixo(linha, coluna, copy.deepcopy(self.estado))
            movimento = "(%d,%d) - (%d,%d)" % (linha, coluna, linha+2, coluna)
            if (estado): self.listaDeFilhos.append([estado,movimento])

            estado = moverPecaParaEsquerda(linha, coluna, copy.deepcopy(self.estado))
            movimento = "(%d,%d) - (%d,%d)" % (linha, coluna, linha, coluna-2)
            if (estado): self.listaDeFilhos.append([estado, movimento])

            estado = moverPecaParaCima(linha, coluna, copy.deepcopy(self.estado))
            movimento = "(%d,%d) - (%d,%d)" % (linha, coluna, linha-2, coluna)
            if (estado): self.listaDeFilhos.append([estado, movimento])

            estado = moverPecaParaDireita(linha, coluna, copy.deepcopy(self.estado))
            movimento = "(%d,%d) - (%d,%d)" % (linha, coluna, linha, coluna+2)
            if (estado): self.listaDeFilhos.append([estado, movimento])
      

# with open("saida-resta-um.txt", "a+") as arquivo:
#    arquivo.write()   


menorFitnessGlobal = sys.maxsize
def encontrarMelhorFitness():
   global menorFitnessGlobal
   for node in searchTree:
      if (node.fitness < menorFitnessGlobal): menorFitnessGlobal = node.fitness

   for node in searchTree:
      if (node.fitness == menorFitnessGlobal): return node

def explorarNode(node):
   explorados.append(node)
   for filho in node.listaDeFilhos:
      novoNo = STNode(node.id, filho[0], filho[1])
      searchTree.append(novoNo)

# Algoritmo A*
def a_star():
   raiz = STNode(0, estadoInicial, "")
   searchTree.append(raiz)
   a = 10
   while(len(searchTree) > 0):
      nextBestNode = encontrarMelhorFitness()
      searchTree.remove(nextBestNode)
      explorarNode(nextBestNode)

      

   # Explorar raiz
   for filho in raiz.listaDeFilhos:
      novoNo = STNode(raiz.id, filho[0], filho[1])

   for estado in searchTree:
      print(estado)

   

# Funcao Main
if __name__ == '__main__':
   a_star()