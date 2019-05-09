# Matheus Soares / 2016.1904.030-1
# Victor Ezequiel / 2016.1904.047-6
# Gabriel Menezes / 2016.1906.005-1

import heuristica as h

# Search Tree Node. Representa um no da arvore de busca.
# Movimento e o movimento feito para se chegar do estado anterior ao atual
idCount = 0
class STNode:
   def __init__(self, estado, custo, paiId, movimento):
      global idCount
      self.id = idCount
      idCount += 1
      self.estado = estado
      self.custo = custo + 1
      self.paiId = paiId
      self.movimento = movimento
      self.avaliacao = self.avaliar()
      self.fitness = self.custo + self.avaliacao

   def avaliar(self):
      return h.calcularHeuristica(self)

   def __str__(self):
      string = "======================"
      string += "\ncusto=%d" % self.custo
      string += "\navaliacao=%d" % self.avaliacao
      string += "\nfitness=%s" % self.fitness
      string += "\n"
      for linha in self.estado:
         string += str(linha)
         string += "\n"
      string += "======================"

      return string