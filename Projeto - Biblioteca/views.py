from models.livro import Livro, NLivros
from models.exemplar import Exemplar, NExemplar
from models.genero import Genero, NGenero
import datetime

class View:
  def livro_inserir(nome,idGenero, datapu, autor,editora):
    livro = Livro(0, nome, idGenero,datapu, autor,editora)
    NLivros.inserir(livro)

  def livro_listar():
    return NLivros.listar()
  
  def livro_listar_nomes():
    return NLivros.listar_nomes()
  
  def livro_listar_id(id):
    return NLivros.listar_id(id)

  def livro_atualizar(id, nome, idGenero,datapu, autor,editora):
    livro = Livro(id, nome,idGenero, datapu, autor,editora)
    NLivros.atualizar(livro)
    
  def livro_excluir(id):
    livro = Livro(id, "", "", "","","")
    NLivros.excluir(livro)    

  def exemplar_listar():
    return NExemplar.listar()

  def exemplar_listar_id(id):
    return NExemplar.listar_id(id)

  def exemplar_inserir(idLivro, unidade, local):
    NExemplar.inserir(Exemplar(0, idLivro, unidade, local))

  def exemplar_atualizar(id, idLivro, unidade, local):
    NExemplar.atualizar(Exemplar(id, idLivro, unidade, local))

  def exemplar_excluir(id):
    NExemplar.excluir(Exemplar(id, "", "", ""))

  def genero_listar():
    return NGenero.listar()

  def genero_inserir(genero):
    NGenero.inserir(Genero(0, genero))

  def genero_atualizar(id,genero):
    NGenero.atualizar(Genero(id, genero))

  def genero_excluir(id):
    NGenero.excluir(Genero(id, ""))

  def genero_buscar(genero,id):
    NLivros.buscar(genero,id)