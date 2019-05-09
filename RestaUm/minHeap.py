# Matheus Soares / 2016.1904.030-1
# Victor Ezequiel / 2016.1904.047-6
# Gabriel Menezes / 2016.1906.005-1 

# Min Heap implementado considerando o valor do fitness como comparacao
class MinHeap:
   def __init__(self):
      self.heap = [0]
      self.tamanhoAtual = 0
      self.estados = []

   def insere(self, node):
      self.heap.append(node)
      self.tamanhoAtual += 1
      self.sobe(self.tamanhoAtual) 

   def sobe(self, i):
      while (i//2 > 0):
         nodePos = i
         paiPos = i//2
         if (self.heap[nodePos].fitness < self.heap[paiPos].fitness):
            aux = self.heap[paiPos]
            self.heap[paiPos] = self.heap[nodePos]
            self.heap[nodePos] = aux
         i = i//2

   def remove(self):
      if (not self.isVazia()):
         removido = self.heap[1]
         self.heap[1] = self.heap[self.tamanhoAtual]
         self.heap.pop()
         self.tamanhoAtual -= 1
         self.desce(1)
         return removido
      
   def desce(self, pai):
      esquerdo = 2*pai
      posTroca = 2*pai
      direito = 2*pai+1
      if (esquerdo <= self.tamanhoAtual):
         if (esquerdo < self.tamanhoAtual
         and self.heap[esquerdo].fitness > self.heap[direito].fitness):
            posTroca = direito
         if(self.heap[pai].fitness > self.heap[posTroca].fitness):
            aux = self.heap[pai]
            self.heap[pai] = self.heap[posTroca]
            self.heap[posTroca] = aux
            self.desce(posTroca)

   def isVazia(self):
      return self.tamanhoAtual == 0