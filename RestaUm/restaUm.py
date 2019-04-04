class Enum(set):
   def __getattr__(self, name):
      if name in self:
         return name
      raise AttributeError

DirecaoDoMovimento = Enum(["CIMA", "BAIXO", "ESQUERDA", "DIREITA"])

# as seguintes posicoes nao sao consideradas no tabuleiro
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

# Recebe conjuntos de coordenadas de origem e tenta mover a peca
# para as coordenadas de destino.
def moverPecaPara(origem, destino):
   if (not movimentoValido(origem, destino)):
      return

   direcaoDoMovimento = identificarDirecaoDoMovimento(origem, destino)

   ox = origem[0]
   oy = origem[1]
   dx = destino[0]
   dy = destino[1]
   
   if (direcaoDoMovimento == DirecaoDoMovimento.BAIXO):
      estadosDoTabuleiro[dx-1][dy] = 0
   elif (direcaoDoMovimento == DirecaoDoMovimento.ESQUERDA):
      estadosDoTabuleiro[dx][dy+1] = 0
   elif (direcaoDoMovimento == DirecaoDoMovimento.CIMA):
      estadosDoTabuleiro[dx+1][dy] = 0
   elif (direcaoDoMovimento == DirecaoDoMovimento.DIREITA):
      estadosDoTabuleiro[dx][dy-1] = 0

   estadosDoTabuleiro[ox][oy] = 0
   estadosDoTabuleiro[dx][dy] = 1
   
   imprimirTabuleiro()

# Identifica para qual direcao o movimento e feito
def identificarDirecaoDoMovimento(origem, destino):
   ox = origem[0]
   oy = origem[1]
   dx = destino[0]
   dy = destino[1]

   if (ox < dx and oy == dy): return DirecaoDoMovimento.BAIXO
   if (ox == dx and oy > dy): return DirecaoDoMovimento.ESQUERDA
   if (ox > dx and oy == dy): return DirecaoDoMovimento.CIMA
   if (ox == dx and oy < dy): return DirecaoDoMovimento.DIREITA

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
      print "Posicao Ocupada"
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

   print "Movimento fora de alcance"
   return True
 
# Verifica se a coordenada esta nas coordenadas inexistentes
def movimentoCoordenadaInexistente(coordenada):
   if (coordenada in coordenadasInexistentes):
      print "Coordenada inexistente"
      return True
   if (coordenada[0] > 6 or coordenada[0] < 0
   or coordenada[1] > 6 or coordenada[1 < 0])
      print "Coordenada inexistente"
      return True
   return False

def imprimirTabuleiro():
   print "------------------------------"
   for estado in estadosDoTabuleiro:
      print estado

# Funcao Main
if __name__ == '__main__':
   imprimirTabuleiro()
   moverPecaPara([3,1], [3,3])