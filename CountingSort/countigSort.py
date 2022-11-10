#Bibliotecas importadas
import numpy as np
import matplotlib.pyplot as plt
from random import randint
from time import perf_counter
import sys
sys.setrecursionlimit(1000000)

#Gera lista sem repetição
def create_list(length):
  lista = []
  while len(lista) < length:
      element = randint(1,1*length)
      if element not in lista: lista.append(element)
  return lista

def countingSort(Lista):
    # Encontrando o elemento de maior valor na lista
    maxElement= max(Lista)

    countArrayLength = maxElement + 1

    # Iniciando o array de contadores com zeros
    countArray = [0] * countArrayLength

    # Percorre o array contador e inicia o valor 
    # de cada elemento da lista com 1.
    for el in Lista: 
        countArray[el] += 1

    # Soma o valor atual com o valor anterior 
    # e armazena como o valor atual para o elemento
    for i in range(1, countArrayLength):
        countArray[i] += countArray[i-1] 

    # Calculando a posicao do elemento baseado 
    # nos valores do array de contagem
    outputArray = [0] * len(Lista)
    i = len(Lista) - 1
    while i >= 0:
        currentEl = Lista[i]
        countArray[currentEl] -= 1
        newPosition = countArray[currentEl]
        outputArray[newPosition] = currentEl
        i -= 1

    return outputArray

#Medir os tempos
def counter():
  medium_time = []
  best_time = []
  worst_time = []
  
  list_length = [10000,20000,30000,40000,50000,80000,100000]
  
  for i in list_length:
    medium_case = create_list(i)
    best_case = [j for j in range(1, i)]
    worst_case = [j for j in range(i, 0, -1)]

    start = perf_counter()
    countingSort(medium_case)
    end = perf_counter()
    duration = end - start
    medium_time.append(duration)

    start = perf_counter()
    countingSort(best_case)
    end = perf_counter()
    duration = end - start
    best_time.append(duration)

    start = perf_counter()
    countingSort(worst_case)
    end = perf_counter()
    duration = end - start
    worst_time.append(duration)

  return medium_time, best_time, worst_time, list_length

m_time, b_time, w_time, l_len = counter()

#Plotando Grafico da Ordenação Rápida (CountingSort) de listas randomicas.
plt.plot(l_len, m_time, label = 'Caso_medio')
plt.plot(l_len, b_time, label = 'Melhor caso')
plt.plot(l_len, w_time, label = 'Pior caso')
plt.legend()
plt.title('CountingSort')
plt.ylabel('Tempo de execução (s)')
plt.xlabel('Tamanho da Lista')
plt.show()