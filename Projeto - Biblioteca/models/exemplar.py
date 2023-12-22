import json
from models.models import Modelo


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


class NExemplar(Modelo):

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("exemplares.json", mode="r") as arquivo:
        exemplares_json = json.load(arquivo)
        for obj in exemplares_json:
          aux = Exemplar(obj["_Exemplar__id"], obj["_Exemplar__idLivro"], obj["_Exemplar__unidade"], obj["_Exemplar__local"])
          cls.objetos.append(aux)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("exemplares.json", mode="w") as arquivo:
      json.dump(cls.objetos, arquivo, default=vars)
