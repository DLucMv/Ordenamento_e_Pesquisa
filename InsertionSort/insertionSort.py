#Bibliotecas importadas
import numpy as np
import matplotlib.pyplot as plt
from random import randint
from time import perf_counter

#Gera lista sem repetição
def create_list(length):
  lista = []
  while len(lista) < length:
      element = randint(1,1*length)
      if element not in lista: lista.append(element)
  return lista

#Agoritmo para ordenação - InsertionSort
def insertion(Lista):
    for i in range(1, len(Lista)):
        key_item = Lista[i]
        j = i - 1

        while j >= 0 and Lista[j] > key_item:
            Lista[j + 1] = Lista[j]
            j -= 1

        Lista[j + 1] = key_item

    return Lista

#Medir os tempos
def counter():
  medium_time = []
  best_time = []
  worst_time = []
  
  list_length = [1000,2000,3000,4000,5000,8000,11000,15000]
  
  for i in list_length:
    medium_case = create_list(i)
    best_case = [j for j in range(1, i+1)]
    worst_case = [j for j in range(i, 0, -1)]

    start = perf_counter()
    insertion(medium_case)
    end = perf_counter()
    duration = end - start
    medium_time.append(duration)

    start = perf_counter()
    insertion(best_case)
    end = perf_counter()
    duration = end - start
    best_time.append(duration)

    start = perf_counter()
    insertion(worst_case)
    end = perf_counter()
    duration = end - start
    worst_time.append(duration)

  return medium_time, best_time, worst_time, list_length

m_time, b_time, w_time, l_len = counter()

#Plotando Grafico da Ordenação "InsertionSort".
plt.plot(l_len, m_time, label = 'Caso médio')
plt.plot(l_len, b_time, label = 'Melhor caso')
plt.plot(l_len, w_time, label = 'Pior caso')
plt.legend()
plt.title('InsertionSort')
plt.ylabel('Tempo de execução (s)')
plt.xlabel('Tamanho da Lista')
plt.show()