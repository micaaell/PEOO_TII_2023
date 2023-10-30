import streamlit as st
import pandas as pd
from views import View
import time

class Manterlogin:
  def main():
    st.header("Cadrastre-se")
    tab1, tab2,tab3= st.tabs(["Crie sua conta", "Atualizar sua conta","Excluir sua conta"])
    with tab1: Manterlogin.inserir()
    with tab2: Manterlogin.atualizar()
    with tab3: Manterlogin.excluir()

  def inserir():
    nome = st.text_input("Informe o nome")
    email = st.text_input("Informe o e-mail")
    fone = st.text_input("Informe o fone")
    senha = st.text_input("Informe a senha")
    if st.button("Criar Conta"):
      View.cliente_inserir(nome, email, fone,senha)
      st.success("Você se cadrastrou")
      time.sleep(2)

  def atualizar():
    clientes = View.cliente_listar()
    if len(clientes) == 0:
      st.write("Nenhum cliente cadastrado")
    else:
      op = st.selectbox("Atualização de Clientes", clientes)
      nome = st.text_input("Informe o novo nome", op.get_nome())
      email = st.text_input("Informe o novo e-mail", op.get_email())
      fone = st.text_input("Informe o novo fone", op.get_fone())
      senha = st.text_input("Informe a nova senha", op.get_senha())
      if st.button("Atualizar"):
        id = op.get_id()
        View.cliente_atualizar(id, nome, email, fone,senha)
        st.success("Conta Atualizada")
        time.sleep(2) 


  def excluir():
      clientes = View.cliente_listar()
      if len(clientes) == 0:
        st.write("Nenhum cliente cadastrado")
      else:
        op = st.selectbox("Exclusão de conta", clientes)
        if st.button("Excluir conta"):
          id = op.get_id()
          View.cliente_excluir(id)
          st.success("Cliente excluído com sucesso")
          time.sleep(2)
    

  

    

    

    
