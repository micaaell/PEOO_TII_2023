import json
from time import strftime
from models.models import Modelo
import datetime


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
  def set_autor(self, autor): self.__autor = autor
  def set_editora(self, editora): self.__editora = editora
  def set_datapu(self, datapu): self.__datapu = datapu

  def __eq__(self, x):
    if self.__id == x.__id and self.__idGenero==x.__idGenero and self.__nome == x.__nome and self.__datapu == x.__datapu and self.__autor == x.__autor and self.__editora == x.__editora:
      return True
    return False

  def __str__(self):
    return f"{self.__id} - {self.__idGenero} - {self.__nome} - {self.__datapu} - {self.__autor} - {self.__editora}"

  def to_json(self):
    return {
      'id': self.__id,
      'idGenero': self.__idGenero,
      'datapu': self.__datapu,
      'nome': self.__nome,
      'editora': self.__editora,
      'autor': self.__autor}


class NLivros(Modelo):

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("livros.json", mode="r") as arquivo:
        livros_json = json.load(arquivo)
        for obj in livros_json:
          aux = Livro(obj["_Livro__id"],obj["_Livro__idGenero"],obj["_Livro__nome"], obj["_Livro__datapu"], obj["_Livro__autor"], obj["_Livro__editora"])
          cls.objetos.append(aux)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("livros.json", mode="w") as arquivo:
      json.dump(cls.objetos, arquivo, default=vars)
