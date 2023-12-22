import json
import datetime
from models.models import Modelo


class Genero:
  def __init__(self, id, genero):
    self.__id = id
    self.__genero = genero

  def get_id(self): return self.__id
  def get_genero(self): return self.__genero

  def set_id(self, id): self.__id = id
  def set_genero(self, genero): self.__genero = genero

  def __eq__(self, x):
    if self.__id == x.__id and self.__genero == x.__genero: return True
    return False

  def __str__(self):
    return f"{self.__id} - {self.__genero}"

  def to_json(self):
    return {
      'id': self.__id,
      'genero': self.__genero}


class NGenero(Modelo):

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("generos.json", mode="r") as arquivo:
        generos_json = json.load(arquivo)
        for obj in generos_json:
          aux = Genero(obj["id"],(obj["genero"]))
          cls.objetos.append(aux)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("generos.json", mode="w") as arquivo:
      json.dump(cls.objetos, arquivo, default=Genero.to_json)
