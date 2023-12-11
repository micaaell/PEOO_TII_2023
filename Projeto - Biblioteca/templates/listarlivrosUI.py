import streamlit as st
import pandas as pd
from views import View
import time

class ListarLivroUI:
  def main():
    st.header("Livros Cadastrados")
    tab_names = ["Listar"]
    selected_tab = st.radio("Livros", tab_names)
    if selected_tab == "Listar":
        ListarLivroUI.listar()

  def listar():
    livros = View.livro_listar()
    if len(livros) == 0:
      st.write("Nenhum livro cadastrado")
    else:
      dic = []
      for obj in livros: dic.append(obj.__dict__)
      df = pd.DataFrame(dic)
      st.dataframe(df)
