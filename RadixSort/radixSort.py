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

#Gera lista com números de dígitos constantes
def create_list_const(length):
  digits = len(str(length))
  lista = []
  while len(lista) < (length - 10**(digits - 1)):
      element = randint(10**(digits - 1), 1*length)
      if element not in lista: lista.append(element)
  return lista

# Método de ordenação

def countingSort(lista, exp1):
 
    n = len(lista)
 
    # A lista de saida cujo os elementos serão ordenados. 
    output = [0] * (n)
 
    # Inicializa o contador como 0. 
    count = [0] * (10)
 
    # Armazena no contador as ocorrencias. 
    for i in range(0, n):
        index = lista[i] // exp1
        count[index % 10] += 1
 
    # Muda o contador 'count[i] para que o mesmo contenha o valor atual. 
    # Posição do dígito na lista de saida. 
    for i in range(1, 10):
        count[i] += count[i - 1]
 
    # Constrói a lista de saida. 
    i = n - 1
    while i >= 0:
        index = lista[i] // exp1
        output[count[index % 10] - 1] = lista[i]
        count[index % 10] -= 1
        i -= 1
 
    # Copiando a lista de saida para a lista. 
    # Agora a lista contém os numeros ordenados. 
    i = 0
    for i in range(0, len(lista)):
        lista[i] = output[i]
 
# Método para RadixSort
def radixSort(lista):
 
    # Procurando o valor máximo pra conhecer o numero de dígitos. 
    max1 = max(lista)
 
    # Executa o countingSort para cada dígito.
    # Note que ao invés de passar o número do dígito, é passado o exp.
    # exp é 10^i onde i é o digito atual.
    exp = 1
    while max1 / exp >= 1:
        countingSort(lista, exp)
        exp *= 10

#Medir os tempos do caso médio
def counter_medium():
  medium_time = []
  
  list_length = [j for j in range(200, 1000, 100)]
  
  for i in list_length:
    medium_case = create_list_const(i)

    start = perf_counter()
    radixSort(medium_case)
    end = perf_counter()
    duration = end - start
    medium_time.append(duration)

  return medium_time, list_length

def counter_medium_2():
  medium_time2 = []
  
  list_length2 = [j for j in range(2000, 10000, 1000)]
  
  for i in list_length2:
    medium_case = create_list_const(i)

    start = perf_counter()
    radixSort(medium_case)
    end = perf_counter()
    duration = end - start
    medium_time2.append(duration)

  return medium_time2, list_length2

def counter_medium_3():
  medium_time3 = []
  
  list_length = [j for j in range(10, 100, 10)]
  
  for i in list_length:
    medium_case3 = create_list_const(i)

    start = perf_counter()
    radixSort(medium_case3)
    end = perf_counter()
    duration = end - start
    medium_time3.append(duration)

  return medium_time3, list_length

#Medir os tempos do pior caso
def counter_worst():
  worst_time = []
  
  list_length = [10000,20000,30000,40000,50000,80000,100000]
  
  for i in list_length:
    worst_case = create_list(i)

    start = perf_counter()
    radixSort(worst_case)
    end = perf_counter()
    duration = end - start
    worst_time.append(duration)

  return worst_time, list_length

m_time, l_len1 = counter_medium()
m_time2, l_len2 = counter_medium_2()
m_time3, l_len3 = counter_medium_3()
w_time, l_len = counter_worst()

#Plotando Grafico da Ordenação (RadixtSort) de listas randomicas.
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
plt.subplots_adjust(right = 2, top = 2)

ax1.plot(l_len3, m_time3, 'tab:blue')
ax2.plot(l_len1, m_time, 'tab:orange')
ax3.plot(l_len2, m_time2, 'tab:green')
ax4.plot(l_len, w_time, 'tab:red')

ax1.set_title('Caso médio - 2 digitos')
ax2.set_title('Caso médio - 3 digitos')
ax3.set_title('Caso médio - 4 digitos')
ax4.set_title('Pior caso')

ax1.set(xlabel = 'Tamanho da lista', ylabel = 'Tempo de execução(s)')
ax2.set(xlabel = 'Tamanho da lista', ylabel = 'Tempo de execução(s)')
ax3.set(xlabel = 'Tamanho da lista', ylabel = 'Tempo de execução(s)')
ax4.set(xlabel = 'Tamanho da lista', ylabel = 'Tempo de execução(s)')