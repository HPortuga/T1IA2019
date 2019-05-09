# Matheus Soares / 2016.1904.030-1
# Victor Ezequiel / 2016.1904.047-6
# Gabriel Menezes / 2016.1906.005-1

# Procura o caminho da folha ate a raiz consultando o pai do node atual
def procurarCaminhos(solucoes, nosVisitados):
   caminhoAteSolucao = []
   for solucao in solucoes:
      caminhoAteSolucao.append(solucao)
      noPai = buscarPai(solucao, nosVisitados)
      while noPai != None:
         caminhoAteSolucao.append(noPai)
         noPai = buscarPai(noPai, nosVisitados)
   return caminhoAteSolucao

# Busca node na lista
def buscarPai(node, lista):
   noPai = None
   for item in lista:
      if (item.id == node.paiId):
         noPai = item
         break
   return noPai

# Escreve a solucao no arquivo saida-resta-um.txt
def escreverSolucao(caminhoAteSolucao):
   with open("saida-resta-um.txt", "w") as arquivo:
      while len(caminhoAteSolucao) > 0:
         lastNode = caminhoAteSolucao.pop()
         if (lastNode.custo == 1):
            arquivo.write("==SOLUCAO\n")
         if (lastNode.custo == 31):
            arquivo.write("FINAL %s\n\n" % (lastNode.movimento))
         else: arquivo.write("%s\n" % (lastNode.movimento))