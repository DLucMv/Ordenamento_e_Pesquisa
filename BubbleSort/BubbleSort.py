#Bibliotecas importadas
import numpy as np
import matplotlib.pyplot as plt
from random import randint
from time import perf_counter

#Algoritmo para a ordenação - Ordenação Bolha
def bubble(lista):
  inv = True
  while inv:
    inv = False
    for i in range(len(lista)-1):
      if lista[i] > lista[i+1]:
        lista[i],lista[i+1] = lista[i+1],lista[i]
        inv = True
  return lista

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
  
  list_length = [1000,2000,3000,4000,5000,8000,11000,15000]
  
  for i in list_length:
    medium_case = create_list(i)
    best_case = sorted(medium_case)
    worst_case = sorted(best_case, reverse = True)

    start = perf_counter()
    bubble(medium_case)
    end = perf_counter()
    duration = end - start
    medium_time.append(duration)

    start = perf_counter()
    bubble(best_case)
    end = perf_counter()
    duration = end - start
    best_time.append(duration)

    start = perf_counter()
    bubble(worst_case)
    end = perf_counter()
    duration = end - start
    worst_time.append(duration)

  return medium_time, best_time, worst_time, list_length

m_time, b_time, w_time, l_len = counter()

#Plotando Grafico da Ordenação bolha de listas randomicas.
plt.plot(l_len, m_time, label = 'Caso médio')
plt.plot(l_len, b_time, label = 'Melhor caso')
plt.plot(l_len, w_time, label = 'Pior caso')
plt.legend()
plt.title('Ordenação bolha')
plt.ylabel('Tempo de execução (s)')
plt.xlabel('Tamanho da Lista')
plt.show()