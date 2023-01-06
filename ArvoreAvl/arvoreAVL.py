#Bibliotecas importadas
import numpy as np
import matplotlib.pyplot as plt
from random import randint
from typing import List
from time import perf_counter
from termcolor import colored


# Defininfo classe Node
class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1
 
# Classe ArvoreAVL
class ArvoreAVL(object):

    # Função recursiva para inserir a chave na sub-arvore
    # enraizada com o nó e retorna nova raiz da sub-arvore
    def insert(self, root, key):
     
        # Árvore de busca binária padrão
        if not root:
            return Node(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
 
        # Atualiza a altura do nó pai
        root.height = 1 + max(self.getHeight(root.left),
                           self.getHeight(root.right))
 
        # Encontrando o fator de balanceamento
        balance = self.getBalance(root)
 
        # Se o nó estiver desbalanceado, um dos 4
        # casos será executado
        
        # Caso 1 - Esquerda Esquerda
        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)
 
        # Caso 2 - Direita Direita
        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)
 
        # Caso 3 - Esquerda Direita
        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
 
        # Caso 4 - Direita Esquerda
        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
 
        return root
 
    def remove(self, root, key):
     
        # Árvore de busca binária padrão
        if not root:
            return False
        elif key < root.val:
            root.left = self.remove(root.left, key)
        else:
            root.right = self.remove(root.right, key)
 
        # Atualiza a altura do nó pai
        root.height = 1 + max(self.getHeight(root.left),
                           self.getHeight(root.right))
 
        # Encontrando o fator de balanceamento
        balance = self.getBalance(root)
 
        # Se o nó estiver desbalanceado, um dos 4
        # casos será executado
        
        # Caso 1 - Esquerda Esquerda
        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)
 
        # Caso 2 - Direita Direita
        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)
 
        # Caso 3 - Esquerda Direita
        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
 
        # Caso 4 - Direita Esquerda
        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
 
        return root

    def leftRotate(self, z):
 
        y = z.right
        T2 = y.left
 
        # Executa a rotação
        y.left = z
        z.right = T2
 
        # Atualiza a altura
        z.height = 1 + max(self.getHeight(z.left),
                         self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                         self.getHeight(y.right))
 
        # Retorna a nova raiz
        return y
 
    def rightRotate(self, z):
 
        y = z.left
        T3 = y.right
 
        # Executa a rotação
        y.right = z
        z.left = T3
 
        # Atualiza a altura
        z.height = 1 + max(self.getHeight(z.left),
                        self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                        self.getHeight(y.right))
 
        # Retorna a nova raiz
        return y
 
    def getHeight(self, root):
        if not root:
            return 0
 
        return root.height
 
    def getBalance(self, root):
        if not root:
            return 0
 
        return self.getHeight(root.left) - self.getHeight(root.right)
 
    # Exibe os nós da arvore em Pré-Ordem
    def preOrder(self, root):
 
        if not root:
            return
 
        print("{0} ".format(root.val), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)


# Execução do balanceamento de uma árvore com
# alto fator de desbalanceamento
arvore = ArvoreAVL()
root = None
 
root = arvore.insert(root, 1)
root = arvore.insert(root, 3)
root = arvore.insert(root, 4)
root = arvore.insert(root, 5)
root = arvore.insert(root, 7)
root = arvore.insert(root, 9)
 
"""
O modelo abstrato da árvore AVL deverá ser :
           5
          / \
         3   7
        / \   \
       1   4   9
"""
 
# Exibindo em Pré-Ordem
print(colored("Exibição da arvore AVL em Pré-Ordem : ", "blue"))
print()
arvore.preOrder(root)