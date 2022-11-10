#Bibliotecas importadas
import numpy as np
import matplotlib.pyplot as plt
from random import randint
from time import perf_counter
import sys
sys.setrecursionlimit(1000000)

#Algoritmo para a ordenação - QuickSort
def quickmelhor(lista):
  L=[]
  R=[]
  #Base da recursão
  if len(lista) <= 1:
    return lista

  key = lista[int (len(lista)/2)]

  for i in lista:
    if i < key:
      L.append(i)
    if i > key:
      R.append(i)

  return quickmelhor(L)+[key]+quickmelhor(R)

#Algoritmo para a ordenação - QuickSort pivô no final
def quickpior(lista):
  L=[]
  R=[]
  #Base da recursão
  if len(lista) <= 1:
    return lista

  key = lista[len(lista) - 1]

  for i in lista:
    if i < key:
      L.append(i)
    if i > key:
      R.append(i)

  return quickpior(L)+[key]+quickpior(R)

#Gera lista sem repetição
def create_list(length):
  lista = []
  while len(lista) < length:
      element = randint(1,1*length)
      if element not in lista: lista.append(element)
  return lista

#Medir os tempos
def counter():
  medium_time = []
  best_time = []
  worst_time = []
  
  list_length = [100,500,1000,2000,3000,4000,5000,10000,15000,20000]
  
  for i in list_length:
    medium_case = create_list(i)
    worst_case = [j for j in range(i, 0, -1)]

    start = perf_counter()
    quickmelhor(medium_case)
    end = perf_counter()
    duration = end - start
    medium_time.append(duration)

    start = perf_counter()
    quickpior(worst_case)
    end = perf_counter()
    duration = end - start
    worst_time.append(duration)

  return medium_time, best_time, worst_time, list_length

m_time, w_time, l_len = counter()

#Plotando Grafico da Ordenação Rápida (QuickSort) de listas randomicas.
plt.plot(l_len, m_time, label = 'Melhor caso')
plt.plot(l_len, w_time, label = 'Pior caso')
plt.legend()
plt.title('QuickSort')
plt.ylabel('Tempo de execução (s)')
plt.xlabel('Tamanho da Lista')
plt.show()