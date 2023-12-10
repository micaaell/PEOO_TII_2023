import json
import datetime

class Genero:
  def __init__(self, id, genero):
    self.__id = id
    self.__genero = genero

  def get_id(self): return self.__id
  def get_genero(self): return self.__genero

  def set_id(self, id): self.__id = id
  def set_genero(self, genero): self.__genero = genero

  def __eq__(self, x):
    if self.__id == x.__id and self.__genero == x.__genero:
      return True
    return False

  def __str__(self):
    return f"{self.__id} - {self.__genero}"

  def to_json(self):
    return {
      'Id': self.__id,
      'Gênero': self.__genero}


class NGenero:
  __generos = []

  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    id = 0
    for aux in cls.__generos:
      if aux.get_id() > id: id = aux.get_id()
    obj.set_id(id + 1)
    cls.__generos.append(obj)
    cls.salvar()

  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.__generos

  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for obj in cls.__generos:
      if obj.get_id() == id: return obj
    return None

  @classmethod
  def atualizar(cls, obj):
    cls.abrir()
    aux = cls.listar_id(obj.get_id())
    if aux is not None:
      aux.set_genero(obj.get_genero())
      cls.salvar()

  @classmethod
  def excluir(cls, obj):
    cls.abrir()
    aux = cls.listar_id(obj.get_id())
    if aux is not None:
      cls.__generos.remove(aux)
      cls.salvar()

  @classmethod
  def abrir(cls):
    cls.__generos = []
    try:
      with open("generos.json", mode="r") as arquivo:
        generos_json = json.load(arquivo)
        for obj in generos_json:
          aux = Genero(obj["id"],(obj["genero"]))
          cls.__generos.append(aux)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("generos.json", mode="w") as arquivo:
      json.dump(cls.__generos, arquivo, default=Genero.to_json)
