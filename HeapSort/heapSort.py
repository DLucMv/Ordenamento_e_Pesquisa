#Bibliotecas importadas
import numpy as np
import matplotlib.pyplot as plt
import random
from random import randint
from typing import List
from time import perf_counter
from termcolor import colored


#Gera lista sem repetição
def create_list(length):
  lista = []
  while len(lista) < length:
      element = randint(1,1*length)
      if element not in lista: lista.append(element)
  return lista


# Classe nó
class Noh:
  def __init__(self, chave):
    self.dado = chave

  def obtemChave(self):
    return self.dado
    
  def atribuiChave(self, chave):
    self.dado = chave

    
# Classe Heap
class Heap:
  def __init__(self, max):
    self.tamanhoMaximo = max
    self.tamanhoAtual = 0
    self.matrizHeap = []
    for i in range(max): self.matrizHeap.append(None)

# Método isEmpty (auto-explicativo).
  def estaVazio(self):
    return self.tamanhoAtual == 0

# Insere um novo elemento no Heap.
  def inserir (self, chave):
    if self.tamanhoAtual == self.tamanhoMaximo : return False
    novoNoh = Noh(chave)
    self.matrizHeap[self.tamanhoAtual] = novoNoh
    self.borbulhaAcima(self.tamanhoAtual)
    self.tamanhoAtual +=1
    return True

# Faz o elemento "subir" enquanto seu valor for maior que
# o valor de seu nó pai.
  def borbulhaAcima(self, indice):
    pai = (indice - 1) // 2
    base = self.matrizHeap[indice]
    while indice > 0 and self.matrizHeap[pai].obtemChave() < base.obtemChave():
      self.matrizHeap[indice] = self.matrizHeap[pai]
      indice = pai
      pai = (pai - 1) // 2
    self.matrizHeap[indice] = base

# Remove o maior valor. Ou seja, remove o elemento
# do topo do Heap.
  def removeMaior(self):
    raiz = self.matrizHeap[0]
    self.tamanhoAtual -=1
    self.matrizHeap[0] = self.matrizHeap[self.tamanhoAtual]
    self.borbulhaAbaixo(0)
    return raiz

# Faz o elemento "descer" enquanto seu valor for menor que
# o valor de seu nó filho.
  def borbulhaAbaixo(self, indice):
    topo = self.matrizHeap[indice]
    while indice < self.tamanhoAtual // 2:
      filhoEsquerdo = 2 * indice + 1
      filhoDireito = filhoEsquerdo + 1
      if filhoDireito < self.tamanhoAtual and self.matrizHeap[filhoEsquerdo].obtemChave() \
                  < self.matrizHeap[filhoDireito].obtemChave():
        filhoMaior = filhoDireito
      else:
        filhoMaior = filhoEsquerdo
      if topo.obtemChave() >= self.matrizHeap[filhoMaior].obtemChave(): break 
      self.matrizHeap[indice] = self.matrizHeap[filhoMaior]
      indice = filhoMaior
    self.matrizHeap[indice] = topo

# Troca o valor de um nó dependendo do valor de
# seus nós pai e filhos
  def troca(self, indice, novoValor):
    if indice < 0 or indice >= self.tamanhoAtual: return False
    valorAntigo = self.matrizHeap[indice].obtemChave()
    self.matrizHeap[indice].atribuiChave(novoValor)
    if valorAntigo < novoValor:
      self.borbulhaAcima(indice)
    else:
      self.borbulhaAbaixo(indice)
    return True

# Mostra o Heap de acordo com seu conceito abstrato.
  def mostraHeap(self):
    print("Conteudo do Heap")
    for i in range (self.tamanhoAtual):
      if self.matrizHeap[i] != None:
        print(self.matrizHeap[i].obtemChave(), end=" ")
      else:
        print(" -- ")
    print()
    numBrancos = 32
    intensPorLinha = 1
    coluna = 0
    j = 0
    pontos = ".................................."
    print(2 * pontos)
    while self.tamanhoAtual > 0:
      if coluna == 0:
        for i in range (numBrancos):
          print(end=" ")
      print(self.matrizHeap[j].obtemChave(), end= " ")
      j += 1
      if j == self.tamanhoAtual: break
      coluna += 1
      if coluna == intensPorLinha:
        numBrancos = numBrancos // 2
        intensPorLinha = intensPorLinha * 2
        coluna = 0
        print("\n")
      else:
        for i in range(numBrancos * 2 - 2):
          print(end=" ")
    print("\n" + 2 * pontos)

# A partir deste ponto são implementados os métodos
# para o ordenamento propriamente dito.
  def inserirEm(self, indice, noh):
    self.matrizHeap[indice] = noh

  def mostraMatriz(self):
    for i in range(self.tamanhoMaximo):
      print(self.matrizHeap[i].obtemChave(), end= " ")
    print("\n")

  def incrementarTamanho(self):
    self.tamanhoAtual += 1



# Apenas para mostrar a estrutura abstrata da classe Heap
# (Uma espécie de prova de conceito???)
heap = Heap(31)
heap.inserir(70)
heap.inserir(40)
heap.inserir(50)
heap.inserir(20)
heap.inserir(60)
heap.inserir(100)
heap.inserir(80)
heap.inserir(30)
heap.inserir(10)
heap.inserir(90)
heap.mostraHeap()


list_length = [10]
for i in list_length:
  heapParaOrdenacao = Heap(i)
  for j in range(i):
    element = randint(1,1*i)
    novoNoh = Noh(element)
    heapParaOrdenacao.inserirEm(j, novoNoh)
    heapParaOrdenacao.incrementarTamanho()
  print (colored("Matriz aleatória : ", "blue"))
  heapParaOrdenacao.mostraHeap()
  print("\n")

  # Executa o borbulhamento para "criar" 
  # a "lista de prioridades".
  k = i // 2 - 1
  while k >= 0:
    heapParaOrdenacao.borbulhaAbaixo(k)
    k -= 1
  print(colored("Após borbulhamento : ", "blue"))
  heapParaOrdenacao.mostraHeap()
  print("\n")

  # Transforma o heap em uma matriz ordenada
  k = i - 1
  while k >=0:
    maiorNoh = heapParaOrdenacao.removeMaior()
    heapParaOrdenacao.inserirEm(k, maiorNoh)
    k -= 1
  print(colored("Matriz Ordenada :", "blue"))
  heapParaOrdenacao.mostraMatriz()
  print("\n\n\n")


#Medir os tempos
def counter():
  medium_time = []
  best_time = []
  worst_time = []
  
  list_length = [10000,20000,40000,70000,100000,500000]

  for i in list_length:
    heapParaOrdenacao = Heap(i)
    for j in range(i):
      element = randint(1,1*i)
      novoNoh = Noh(element)
      heapParaOrdenacao.inserirEm(j, novoNoh)
      heapParaOrdenacao.incrementarTamanho()

    start = perf_counter()

    k = i // 2 - 1
    while k >= 0:
      heapParaOrdenacao.borbulhaAbaixo(k)
      k -= 1

    k = i - 1
    while k >=0:
      maiorNoh = heapParaOrdenacao.removeMaior()
      heapParaOrdenacao.inserirEm(k, maiorNoh)
      k -= 1

    end = perf_counter()
    duration = end - start
    medium_time.append(duration)

  return medium_time, list_length


m_time, l_len = counter()
#Plotando Grafico da Ordenação Heap de listas randomicas.
plt.plot(l_len, m_time, label = 'Caso médio')
plt.legend()
plt.title('HeapSort')
plt.ylabel('Tempo de execução (s)')
plt.xlabel('Tamanho da Lista')
plt.show()