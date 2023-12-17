import streamlit as st
import pandas as pd
from views import View
import time

class ManterLivroUI:
  def main():
    st.header("Cadastro de Livros")
    tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
    with tab1: ManterLivroUI.listar()
    with tab2: ManterLivroUI.inserir()
    with tab3: ManterLivroUI.atualizar()
    with tab4: ManterLivroUI.excluir()

  def listar():
    livros = View.livro_listar()
    if len(livros) == 0:
      st.write("Nenhum livro cadastrado")
    else:
      dic = []
      for obj in livros: dic.append(obj.__dict__)
      df = pd.DataFrame(dic)
      st.dataframe(df)


  def inserir():
    generos= View.genero_listar()
    idGenero = st.selectbox("Selecione o genero", generos)
    nome = st.text_input("Informe o nome")
    datapu = st.text_input("Informe o data da publicação")
    autor = st.text_input("Informe o autor")
    editora = st.text_input("Informe a editora")
    if st.button("Inserir"):
      View.livro_inserir(idGenero,nome ,datapu, autor,editora)
      st.success("Livro inserido com sucesso")
      time.sleep(2)
      st.rerun()
     

  def atualizar():
    livros = View.livro_listar()
    generos = View.genero_listar() 
    if len(livros) == 0:
      st.write("Nenhum livro cadastrado")
    else:
      op = st.selectbox("Escolha o livro para a atualização", livros)
      idGenero = st.selectbox("Qual o genero?", generos)
      nome = st.text_input("Informe o novo nome", op.get_nome())
      datapu = st.text_input("Informe a nova data de publicação", op.get_datapu())
      autor = st.text_input("Informe o novo autor", op.get_autor())
      editora = st.text_input("Informe a nova editora", op.get_editora())
    if st.button("Atualizar"):
      id = op.get_id()
      View.livro_atualizar(id,idGenero,nome,datapu, autor,editora)
      st.success("Livro atualizado com sucesso")
      time.sleep(2)

  def excluir():
    livros = View.livro_listar()
    if len(livros) == 0:
      st.write("Nenhum livro cadastrado")
    else:
      op = st.selectbox("Exclusão de Livros", livros)
      if st.button("Excluir"):
        id = op.get_id()
        View.livro_excluir(id)
        st.success("Livro excluído com sucesso")
        time.sleep(2)
