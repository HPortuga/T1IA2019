# Matheus Soares / 2016.1904.030-1
# Victor Ezequiel / 2016.1904.047-6
# Gabriel Menezes / 2016.1906.005-1

import copy

coordenadasInexistentes = [
   [0,0],[0,1],[0,5],[0,6],
   [1,0],[1,1],[1,5],[1,6],
   [5,0],[5,1],[5,5],[5,6],
   [6,0],[6,1],[6,5],[6,6]]

meioDoTabuleiro = [
   [2,2],[2,3],[2,4],
   [3,2],[3,3],[3,4],
   [4,2],[4,3],[4,4]]

topoDoTabuleiro = [
   [0,2],[0,3],[0,4],
   [1,2],[1,3],[1,4]]

fundoDoTabuleiro = [
   [5,2],[5,3],[5,4],
   [6,2],[6,3],[6,4]]

esquerdaDoTabuleiro = [
   [2,0],[3,0],[4,0],
   [2,1],[3,1],[4,1]]

direitaDoTabuleiro = [
   [2,5],[3,5],[4,5],
   [2,6],[3,6],[4,6]]

# Verifica se a coordenada nao pertence as coordenadas inexistentes 
# ou se a coordenada nao e maior/menor que o tabuleiro
def verificarMovimentoValido(linha, coluna):
   if ([linha,coluna] in coordenadasInexistentes
   or linha < 0 or linha > 6 or coluna < 0 or coluna > 6):
      return False
   return True

# Tenta mover a peca na coordenada atual para baixo
def moverPecaParaBaixo(linha, coluna, estado):
   if (not verificarMovimentoValido(linha+2, coluna)):
      return

   if (estado[linha+1][coluna] == 1
   and estado[linha+2][coluna] == 0):
      estado[linha][coluna] = 0
      estado[linha+1][coluna] = 0
      estado[linha+2][coluna] = 1
      return estado

# Tenta mover a peca na coordenada atual para cima
def moverPecaParaCima(linha, coluna, estado):
   if (not verificarMovimentoValido(linha-2, coluna)):
      return

   if (estado[linha-1][coluna] == 1
   and estado[linha-2][coluna] == 0):
      estado[linha][coluna] = 0
      estado[linha-1][coluna] = 0
      estado[linha-2][coluna] = 1
      return estado

# Tenta mover a peca na coordenada atual para esquerda
def moverPecaParaEsquerda(linha, coluna, estado):
   if (not verificarMovimentoValido(linha, coluna-2)):
      return

   if (estado[linha][coluna-1] == 1
   and estado[linha][coluna-2] == 0):
      estado[linha][coluna] = 0
      estado[linha][coluna-1] = 0
      estado[linha][coluna-2] = 1
      return estado

# Tenta mover a peca na coordenada atual para direita
def moverPecaParaDireita(linha, coluna, estado):
   if (not verificarMovimentoValido(linha, coluna+2)):
      return
   
   if (estado[linha][coluna+1] == 1
   and estado[linha][coluna+2] == 0):
      estado[linha][coluna] = 0
      estado[linha][coluna+1] = 0
      estado[linha][coluna+2] = 1
      return estado   
   
# Verifica se existem movimentos possiveis para todas as pecas em dado estado
def calcularMovimentosPossiveis(estado):
   movimentosPossiveis = []
   for linha in range(0,7):
      for coluna in range(0,7):
         if (estado[linha][coluna] == 0):
            continue

         if ([linha, coluna] in meioDoTabuleiro):
            novoEstado = moverPecaParaBaixo(linha, coluna, copy.deepcopy(estado))
            if (novoEstado):
               movimento = "(%d,%d) - (%d,%d)" % (linha, coluna, linha+2, coluna)
               movimentosPossiveis.append([novoEstado, movimento])
            
            novoEstado = moverPecaParaCima(linha, coluna, copy.deepcopy(estado))
            if (novoEstado): 
               movimento = "(%d,%d) - (%d,%d)" % (linha, coluna, linha-2, coluna)
               movimentosPossiveis.append([novoEstado, movimento])

            novoEstado = moverPecaParaEsquerda(linha, coluna, copy.deepcopy(estado))
            if (novoEstado): 
               movimento = "(%d,%d) - (%d,%d)" % (linha, coluna, linha, coluna-2)
               movimentosPossiveis.append([novoEstado, movimento])

            novoEstado = moverPecaParaDireita(linha, coluna, copy.deepcopy(estado))
            if (novoEstado): 
               movimento = "(%d,%d) - (%d,%d)" % (linha, coluna, linha, coluna+2)
               movimentosPossiveis.append([novoEstado, movimento])
               continue

         if ([linha, coluna] in topoDoTabuleiro):
            novoEstado = moverPecaParaBaixo(linha, coluna, copy.deepcopy(estado))
            if (novoEstado): 
               movimento = "(%d,%d) - (%d,%d)" % (linha, coluna, linha+2, coluna)
               movimentosPossiveis.append([novoEstado, movimento])

            novoEstado = moverPecaParaEsquerda(linha, coluna, copy.deepcopy(estado))
            if (novoEstado): 
               movimento = "(%d,%d) - (%d,%d)" % (linha, coluna, linha, coluna-2)
               movimentosPossiveis.append([novoEstado, movimento])

            novoEstado = moverPecaParaDireita(linha, coluna, copy.deepcopy(estado))
            if (novoEstado): 
               movimento = "(%d,%d) - (%d,%d)" % (linha, coluna, linha, coluna+2)
               movimentosPossiveis.append([novoEstado, movimento])
            continue

         if ([linha, coluna] in fundoDoTabuleiro):
            novoEstado = moverPecaParaCima(linha, coluna, copy.deepcopy(estado))
            if (novoEstado): 
               movimento = "(%d,%d) - (%d,%d)" % (linha, coluna, linha-2, coluna)
               movimentosPossiveis.append([novoEstado, movimento])

            novoEstado = moverPecaParaEsquerda(linha, coluna, copy.deepcopy(estado))
            if (novoEstado): 
               movimento = "(%d,%d) - (%d,%d)" % (linha, coluna, linha, coluna-2)
               movimentosPossiveis.append([novoEstado, movimento])

            novoEstado = moverPecaParaDireita(linha, coluna, copy.deepcopy(estado))
            if (novoEstado): 
               movimento = "(%d,%d) - (%d,%d)" % (linha, coluna, linha, coluna+2)
               movimentosPossiveis.append([novoEstado, movimento])
            continue

         if ([linha, coluna] in esquerdaDoTabuleiro):
            novoEstado = moverPecaParaCima(linha, coluna, copy.deepcopy(estado))
            if (novoEstado): 
               movimento = "(%d,%d) - (%d,%d)" % (linha, coluna, linha-2, coluna)
               movimentosPossiveis.append([novoEstado, movimento])

            novoEstado = moverPecaParaBaixo(linha, coluna, copy.deepcopy(estado))
            if (novoEstado): 
               movimento = "(%d,%d) - (%d,%d)" % (linha, coluna, linha+2, coluna)
               movimentosPossiveis.append([novoEstado, movimento])

            novoEstado = moverPecaParaDireita(linha, coluna, copy.deepcopy(estado))
            if (novoEstado): 
               movimento = "(%d,%d) - (%d,%d)" % (linha, coluna, linha, coluna+2)
               movimentosPossiveis.append([novoEstado, movimento])
            continue

         if ([linha, coluna] in direitaDoTabuleiro):
            novoEstado = moverPecaParaCima(linha, coluna, copy.deepcopy(estado))
            if (novoEstado): 
               movimento = "(%d,%d) - (%d,%d)" % (linha, coluna, linha-2, coluna)
               movimentosPossiveis.append([novoEstado, movimento])

            novoEstado = moverPecaParaBaixo(linha, coluna, copy.deepcopy(estado))
            if (novoEstado): 
               movimento = "(%d,%d) - (%d,%d)" % (linha, coluna, linha+2, coluna)
               movimentosPossiveis.append([novoEstado, movimento])

            novoEstado = moverPecaParaEsquerda(linha, coluna, copy.deepcopy(estado))
            if (novoEstado): 
               movimento = "(%d,%d) - (%d,%d)" % (linha, coluna, linha, coluna-2)
               movimentosPossiveis.append([novoEstado, movimento])
            continue

   return movimentosPossiveis