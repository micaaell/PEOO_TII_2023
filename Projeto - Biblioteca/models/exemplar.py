import json

class Exemplar:
  def __init__(self, id, idLivro, unidade, local):
    self.__id = id
    self.__idLivro = idLivro
    self.__unidade = unidade
    self.__local = local

  def get_id(self): return self.__id
  def get_idLivro(self): return self.__idLivro
  def get_unidade(self): return self.__unidade
  def get_local(self): return self.__local

  def set_id(self, id): self.__id = id
  def set_idLivro(self, idLivro): self.__idLivro = idLivro
  def set_unidade(self, unidade): self.__valor = unidade
  def set_local(self, local): self.__local = local

  def __eq__(self, x):
    if self.__id == x.__id and self.__idLivro == x.__idLivro and self.__unidade == x.__unidade and self.__local == x.__local:
      return True
    return False

  def __str__(self):
    return f"{self.__id} - {self.__idLivro} - {self.__unidade} - {self.__local} "


class NExemplar:
  __exemplares = []

  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    id = 0
    for aux in cls.__exemplares:
      if aux.get_id() > id: id = aux.get_id()
    obj.set_id(id + 1)
    cls.__exemplares.append(obj)
    cls.salvar()

  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.__exemplares

  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for obj in cls.__exemplares:
      if obj.get_id() == id: return obj
    return None

  @classmethod
  def atualizar(cls, obj):
    cls.abrir()
    aux = cls.listar_id(obj.get_id())
    if aux is not None:
      aux.set_idLivro(obj.get_idLivro())
      aux.set_unidade(obj.get_unidade())
      aux.set_local(obj.get_local())
      cls.salvar()

  @classmethod
  def excluir(cls, obj):
    cls.abrir()
    aux = cls.listar_id(obj.get_id())
    if aux is not None:
      cls.__exemplares.remove(aux)
      cls.salvar()

  @classmethod
  def abrir(cls):
    cls.__exemplares = []
    try:
      with open("exemplares.json", mode="r") as arquivo:
        exemplares_json = json.load(arquivo)
        for obj in exemplares_json:
          aux = Exemplar(obj["_Exemplar__id"], obj["_Exemplar__idLivro"], obj["_Exemplar__unidade"], obj["_Exemplar__local"])
          cls.__exemplares.append(aux)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("exemplares.json", mode="w") as arquivo:
      json.dump(cls.__exemplares, arquivo, default=vars)
