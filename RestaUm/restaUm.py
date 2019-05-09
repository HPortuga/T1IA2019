# Matheus Soares / 2016.1904.030-1
# Victor Ezequiel / 2016.1904.047-6
# Gabriel Menezes / 2016.1906.005-1

import time
import minHeap as mh
import stNode as stn
import utils
import tabuleiro as tb

def a_star(estadoInicial):
   inicio = time.time()
   raiz = stn.STNode(estadoInicial, -1, 0, "")
   searchTree = mh.MinHeap()
   searchTree.insere(raiz)
   solucoes = []
   explorados = []
   caminhoAteSolucao = []
   nosVisitados = []

   while len(solucoes) < 2:
      nodeAtual = searchTree.remove()
      explorados.append(nodeAtual.estado)
      if (nodeAtual.custo == 31):
         solucoes.append(nodeAtual)
         fim = time.time()
         print("Solucao encontrada em %fs; Estados expandidos = %d - %d" %(fim-inicio, len(explorados), len(nosVisitados)))

      for node in tb.calcularMovimentosPossiveis(nodeAtual.estado):
         nodeNovo = stn.STNode(node[0], nodeAtual.custo, nodeAtual.id, node[1])
         if (nodeNovo.estado not in explorados
         and nodeNovo.estado not in searchTree.estados):
            searchTree.insere(nodeNovo)
            searchTree.estados.append(nodeNovo.estado)
            nosVisitados.append(nodeNovo)

   caminhoAteSolucao = utils.procurarCaminhos(solucoes, nosVisitados)
   utils.escreverSolucao(caminhoAteSolucao)

if __name__ == '__main__':
   estadoInicial = [
   [0,0,1,1,1,0,0],
   [0,0,1,1,1,0,0],
   [1,1,1,1,1,1,1],
   [1,1,1,0,1,1,1],
   [1,1,1,1,1,1,1],
   [0,0,1,1,1,0,0],
   [0,0,1,1,1,0,0]]

   a_star(estadoInicial)