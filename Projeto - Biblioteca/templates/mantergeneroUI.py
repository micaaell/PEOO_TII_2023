import streamlit as st
import pandas as pd
from views import View
import time

class ManterGeneroUI:
  def main():
    st.header("Cadastro de Gêneros")
    tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
    with tab1: ManterGeneroUI.listar()
    with tab2: ManterGeneroUI.inserir()
    with tab3: ManterGeneroUI.atualizar()
    with tab4: ManterGeneroUI.excluir()
  def listar():
    generos = View.genero_listar()
    if len(generos) == 0:
      st.write("Nenhum genero cadastrado")
    else:
      dic = []
      for obj in generos: dic.append(obj.__dict__)
      df = pd.DataFrame(dic)
      st.dataframe(df)

  def inserir():
    genero = st.text_input("Informe o genero")
    if st.button("Inserir"):
      View.genero_inserir(genero)
      st.success("Genero inserido com sucesso")
      time.sleep(2)

  def atualizar():
    generos = View.genero_listar()
    if len(generos) == 0:
      st.write("Nenhum genero cadastrado")
    else:
      op = st.selectbox("Atualização de generos", generos)
      genero = st.text_input("Informe o novo genero", op.get_genero())
      if st.button("Atualizar"):
        id = op.get_id()
        View.genero_atualizar(id,genero)
        st.success("Genero atualizado com sucesso")
        time.sleep(2)

  def excluir():
    generos = View.genero_listar()
    if len(generos) == 0:
      st.write("Nenhum genero cadastrado")
    else:
      op = st.selectbox("Exclusão de generos", generos)
      if st.button("Excluir"):
        id = op.get_id()
        View.genero_excluir(id)
        st.success("Genero excluído com sucesso")
        time.sleep(2)