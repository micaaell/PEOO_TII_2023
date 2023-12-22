import streamlit as st
import pandas as pd
from views import View
import time

class ManterExemplarUI:
  def main():
    st.header("Cadastro de Exemplares")
    tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
    with tab1: ManterExemplarUI.listar()
    with tab2: ManterExemplarUI.inserir()
    with tab3: ManterExemplarUI.atualizar()
    with tab4: ManterExemplarUI.excluir()

  def listar():
    exemplares = View.exemplar_listar()
    if len(exemplares) == 0:
      st.write("Nenhum serviço exemplar")
    else:  
      dic = []
      for obj in exemplares: dic.append(obj.__dict__)
      df = pd.DataFrame(dic)
      st.dataframe(df)

  def inserir():
    livros= View.livro_listar()
    idLivro = st.selectbox("Selecione o livro",livros)
    unidade = st.text_input("Informe a Unidade")
    local = st.text_input("Informe o Local")
    if st.button("Inserir"):
      View.exemplar_inserir(idLivro.get_nome(), unidade, local)
      st.success("Exemplar inserido com sucesso")
      time.sleep(2)
      st.rerun()

  def atualizar():
    exemplares = View.exemplar_listar()
    if len(exemplares) == 0:
      st.write("Nenhum exemplar cadastrado")
    else:  
      livros= View.livro_listar()
      idLivro = st.selectbox("Selecione o livro", livros, key="unique_key_for_selectbox")
      unidade = st.text_input("Informe a nova unidade")
      local = st.text_input("Informe o novo local")
      if st.button("Atualizar"):
        id = idLivro.get_id()
        View.exemplar_atualizar(id, idLivro.get_nome(), unidade, local)
        st.success("exemplar atualizado com sucesso")
        time.sleep(2)
        st.rerun()

  def excluir():
    exemplares = View.exemplar_listar()
    if len(exemplares) == 0:
      st.write("Nenhum exemplar cadastrado")
    else:  
      op = st.selectbox("Exclusão de exemplares", exemplares)
      if st.button("Excluir"):
        id = op.get_id()
        View.exemplar_excluir(id)
        st.success("exemplar excluído com sucesso")
        time.sleep(2)
        st.rerun()