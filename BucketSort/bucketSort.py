#Bibliotecas importadas
import numpy as np
import matplotlib.pyplot as plt
import random
from random import randint
from typing import List
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

#Gera lista sem repetição com elementos bem grandes
def create_list_big(length):
  lista = []
  while len(lista) < length:
      element = randint(10000*length ,100000*length)
      if element not in lista: lista.append(element)
  return lista

# Método de ordenação

def bucket_sort(input_list):
    # Encontra o valor máximo da lista e usa o tamanho da lista para determinar
    # qual valor na lista vai em cada balde 
    max_value = max(input_list)
    size = max_value /len(input_list)

    # Cria n baldes vazios onde n é igual ao tamanho da lista de entrada.
    buckets_list= []
    for x in range(len(input_list)):
        buckets_list.append([]) 

    # Põe os elementos da lista em diferentes baldes baseados no tamanho.
    for i in range(len(input_list)):
        j = int (input_list[i] / size)
        if j != len (input_list):
            buckets_list[j].append(input_list[i])
        else:
            buckets_list[len(input_list) - 1].append(input_list[i])

    # Ordena os elementos no balde usando o método InsertionSort. 
    for z in range(len(input_list)):
        insertion_sort(buckets_list[z])
            
    # Concatena os baldes com os elementos ordenados em uma única lista. 
    final_output = []
    for x in range(len (input_list)):
        final_output = final_output + buckets_list[x]
    return final_output

    # Método InsertionSort usado para ordenar os baldes.
    # Recebe o balde para executar a ordenação.
def insertion_sort(bucket):
    for i in range (1, len (bucket)):
        var = bucket[i]
        j = i - 1
        while (j >= 0 and var < bucket[j]):
            bucket[j + 1] = bucket[j]
            j = j - 1
        bucket[j + 1] = var


#Medir os tempos do melhor caso
def counter_best():
  best_time = []
  
  list_length = [10000,20000,30000,40000,50000,60000,70000,80000]
  
  for i in list_length:
    best_case = [j for j in range(1, i)]

    start = perf_counter()
    bucket_sort(best_case)
    end = perf_counter()
    duration = end - start
    best_time.append(duration)

  return best_time, list_length

#Medir os tempos do caso médio
def counter_medium():
  medium_time = []
  
  list_length = [10000,20000,30000,40000,50000,60000,70000,80000]
  
  for i in list_length:
    medium_case = create_list(i)

    start = perf_counter()
    bucket_sort(medium_case)
    end = perf_counter()
    duration = end - start
    medium_time.append(duration)

  return medium_time, list_length

#Medir os tempos do pior caso
def counter_worst():
  worst_time = []
  
  list_length = [10000,20000,30000,40000,50000,60000,70000,80000]
  
  for i in list_length:
    worst_case = []

    tamanho_restante = int (0.05 * i)

    w = [j for j in range(1, int (i - 0.05 * i))]
    x = create_list_big(tamanho_restante)
    worst_case = w + x
    worst_case.reverse()

    start = perf_counter()
    bucket_sort(worst_case)
    end = perf_counter()
    duration = end - start
    worst_time.append(duration)

  return worst_time, list_length

b_time, l_len = counter_best()
m_time, l_len = counter_medium()
w_time, l_len = counter_worst()

#Plotando Grafico da Ordenação Rápida (BucketSort) de listas randomicas.
plt.plot(l_len, m_time, label = 'Caso_medio')
plt.plot(l_len, b_time, label = 'Melhor caso')
plt.plot(l_len, w_time, label = 'Pior caso')
plt.legend()
plt.title('BucketSort')
plt.ylabel('Tempo de execução (s)')
plt.xlabel('Tamanho da Lista')
plt.show()