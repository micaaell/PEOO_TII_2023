import json

class Livro:
  def __init__(self, id,idGenero, nome, datapu,autor, editora):
    self.__id = id
    self.__idGenero = idGenero
    self.__nome = nome
    self.__datapu = datapu
    self.__autor = autor
    self.__editora = editora

  def get_id(self): return self.__id
  def get_idGenero(self): return self.__idGenero
  def get_nome(self): return self.__nome
  def get_autor(self): return self.__autor
  def get_editora(self): return self.__editora
  def get_datapu(self): return self.__datapu

  def set_id(self, id): self.__id = id
  def set_idGenero(self, idGenero): self.__id = idGenero
  def set_nome(self, nome): self.__nome = nome
  def set_autor(self, autor): self.__email = autor
  def set_editora(self, editora): self.__fone = editora
  def set_datapu(self, datapu): self.__datapu = datapu

  def __eq__(self, x):
    if self.__id == x.__id and self.__idGenero==x.__idGenero and self.__nome == x.__nome and self.__datapu == x.__datapu and self.__autor == x.__autor and self.__editora == x.__editora:
      return True
    return False

  def __str__(self):
    return f"{self.__id} - {self.__idGenero} - {self.__nome} - {self.__datapu} - {self.__autor} - {self.__editora}"


class NLivros:
  __livros = [] # lista de clientes inicia vazia

  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    id = 0  # encontrar o maior id já usado
    for aux in cls.__livros:
      if aux.get_id() > id: id = aux.get_id()
    obj.set_id(id + 1)
    cls.__livros.append(obj)# insere um cliente (obj) na lista
    cls.salvar()
    return True

  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.__livros  # retorna a lista de clientes

  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for obj in cls.__livros:
      if obj.get_id() == id: return obj
    return None

  @classmethod
  def atualizar(cls, obj):
    cls.abrir()
    aux = cls.listar_id(obj.get_id())
    if aux is not None:
      aux.set_idGenero(obj.get_idGenero())
      aux.set_nome(obj.get_nome())
      aux.set_datapu(obj.get_datapu())
      aux.set_autor(obj.get_autor())
      aux.set_editora(obj.get_editora())
      cls.salvar()

  @classmethod
  def excluir(cls, obj):
    cls.abrir()
    aux = cls.listar_id(obj.get_id())
    if aux is not None:
      cls.__livros.remove(aux)
      cls.salvar()
      
  

  @classmethod
  def abrir(cls):
    cls.__livros = []
    try:
      with open("livros.json", mode="r") as arquivo:
        livros_json = json.load(arquivo)
        for obj in livros_json:
          aux = Livro(obj["_Livro__id"],obj["_Livro__idGenero"],obj["_Livro__nome"], obj["_Livro__datapu"], obj["_Livro__autor"], obj["_Livro__editora"])
          cls.__livros.append(aux)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("livros.json", mode="w") as arquivo:
      json.dump(cls.__livros, arquivo, default=vars)
