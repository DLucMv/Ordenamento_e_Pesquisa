import numpy as np
import matplotlib.pyplot as plt
import random
from random import randint
from typing import List
from time import perf_counter
import graphviz
from graphviz import nohtml


#Classe nó
class NoArvore:
    def __init__(self, payLoad=None):
        self.payLoad = payLoad
        self.esquerda = None
        self.direita = None
        
    def __str__(self):
        return "{"+str(self.payLoad)+"}"
    

# Definição da classe árvore
class ArvoreBinaria:    

    #inicializa a raiz da arvore como vazia         
    def __init__(self):
        self.raiz = None     
    
    #cria um novo nó e o retorna           
    def criarNovoNo(self, payLoad): 
          
        return NoArvore(payLoad)

    #insere um novo dado(payLoad)
    def insere(self, raiz, payLoad):    
        if raiz == None:                #Caso arvore vazia
            return self.criarNovoNo(payLoad)
        else:
            if payLoad <= raiz.payLoad:
                raiz.esquerda = self.insere(raiz.esquerda, payLoad)
            else:
                raiz.direita = self.insere(raiz.direita, payLoad)
        return raiz
       
    #Pesquisa um valor na árvore
    def pesquisar(self, raiz, valor): 
        if raiz == None:
            return 0
        else:
            if valor == raiz.payLoad:
                return 1
            else:
                if valor < raiz.payLoad:
                    return self.pesquisar(raiz.esquerda, valor)
                else:
                    return self.pesquisar(raiz.direita, valor)

    #imprime a árvore (em ordem)
    def imprimirArvoreEmOrdem(self, raiz): 
        if raiz == None:
            pass
        else:
            self.imprimirArvoreEmOrdem(raiz.esquerda)
            print("{",raiz.payLoad,"}", end=' ')
            self.imprimirArvoreEmOrdem(raiz.direita)

    #imprime a árvore (em ordem) usando a 
    #biblioteca GraphViz
    def imprimirArvoreGraphViz(self, raiz):
      if raiz == None:
          pass
      else:
        if raiz.esquerda != None:
          g.edge(str(raiz.payLoad), str(raiz.esquerda.payLoad))
        self.imprimirArvoreGraphViz(raiz.esquerda)
        if raiz.direita != None:
          g.edge(str(raiz.payLoad), str(raiz.direita.payLoad))
        self.imprimirArvoreGraphViz(raiz.direita)
        
    #imprime a árvore invertida (EmOrdemInvertida)
    def imprimeArvoreInvertida(self, raiz): 
        if raiz == None:
            pass
        else:
            self.imprimeArvoreInvertida(raiz.direita)
            print("{",raiz.payLoad,"}", end=' ')
            self.imprimeArvoreInvertida(raiz.esquerda)

    #imprime os nós da arvore
    def imprimeNos(self,raiz):
        if raiz == None: return
        a = raiz.payLoad
        if raiz.esquerda != None:
            b = raiz.esquerda.payLoad
        else:
            b = None
        if raiz.direita != None:
            c = raiz.direita.payLoad
        else:
            c = None
        print("{",a,"[",b,",",c,"]","}", end=' ')
        self.imprimeNos(raiz.esquerda)
        self.imprimeNos(raiz.direita)


minhaArvore = ArvoreBinaria();

minhaArvore.raiz = minhaArvore.criarNovoNo(80)

esquerdo = minhaArvore.insere(minhaArvore.raiz, 61)
minhaArvore.insere(esquerdo, 44)
minhaArvore.insere(esquerdo, 73)

direito = minhaArvore.insere(minhaArvore.raiz, 96)
direitoDaEsquerda = minhaArvore.insere(direito, 95)
direitoDaDireita = minhaArvore.insere(direito, 101)

minhaArvore.insere(direitoDaEsquerda, 109)

g = graphviz.Digraph('g', filename='btree.gv',
                     node_attr={'shape': 'record', 'height': '.2'}, 
                     engine = 'sfdp')
g.attr(bgcolor='white', label='ArvoreBinaria', fontcolor='Black')

minhaArvore.imprimirArvoreGraphViz(minhaArvore.raiz)
g