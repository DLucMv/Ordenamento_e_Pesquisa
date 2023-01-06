import hashlib


class Conexao:
  def __init__(self, dado):
    self.dado = dado
    self.proximo = None

  def obtemDado(self):
    return self.dado

  def mostraConexao(self):
    print(self.dado, end= " ")


class ListaOrdenada:
  def __init__(self):
    self.primeiro = None

  def inserir(self, conexao):
    chave = conexao.obtemDado()
    anterior = None
    atual = self.primeiro
    while atual != None and chave > atual.obtemDado():
      anterior = atual
      atual = atual.proximo
    if anterior == None:
      self.primeiro = conexao
    else:
      anterior.proximo = conexao
      conexao.proximo = atual

  def apagar(self, chave):
    anterior = None
    atual = self.primeiro
    while atual != None and chave != atual.obtemDado():
      anterior = atual
      atual = atual.proximo
    #Desconecta a conexao
    if anterior == None:
      self.primeiro = self.primeiro.proximo
    else:
      anterior.proximo = atual.proximo

  def procurar(self, chave):
    atual = self.primeiro
    while atual != None and atual.obtemDado() <= chave:
      if atual.obtemDado() == chave:
        return atual
      atual = atual.proximo
    return -1

  def mostraLista(self):
    print("Lista: ", end=" ")
    atual = self.primeiro
    while atual != None:
      atual.mostraConexao()
      atual = atual.proximo


class TabelaHash:
  def __init__(self, tamanho):
    self.matrizHash = []
    self.tamanho = tamanho
    for i in range(tamanho):
      self.matrizHash.append(ListaOrdenada())
      print('\n')

  def mostraTabela(self):
    for i in range(self.tamanho):
      print(i, ":", end=" ")
      self.matrizHash[i].mostraLista()
      print('\n')

  def funcaoHash(self, chave):
    return chave % self.tamanho

  def inserir(self, conexao):
    chave = conexao.obtemDado()
    valorHash = self.funcaoHash(chave)
    self.matrizHash[valorHash].inserir(conexao)

  def apagar(self, chave):
    valorHash = self.funcaoHash(chave)
    self.matrizHash[valorHash].apagar(chave)

  def procurar(self, chave):
    valorHash = self.funcaoHash(chave)
    conexao = self.matrizHash[valorHash].procurar(chave)
    return conexao
  

hash = TabelaHash(3)
hash.mostraTabela()
hash.inserir(Conexao(0))
hash.inserir(Conexao(1))
hash.inserir(Conexao(2))
hash.inserir(Conexao(3))
hash.inserir(Conexao(4))
hash.inserir(Conexao(5))
hash.inserir(Conexao(6))
hash.inserir(Conexao(7))
hash.inserir(Conexao(8))
hash.inserir(Conexao(9))
hash.inserir(Conexao(10))
hash.inserir(Conexao(11))
hash.mostraTabela()
enc = hash.procurar(2)
print('econtrado \n') if enc != -1 else print('Não encontrado \n')
hash.apagar(3)
hash.apagar(9)
hash.mostraTabela()