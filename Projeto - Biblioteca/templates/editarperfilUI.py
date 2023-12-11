import streamlit as st
import pandas as pd
from views import View
import time

class EditarPerfilUI:
  def main():
    st.header("Editar perfil")
    EditarPerfilUI.editar()
   
  def editar():
      id = st.session_state["cliente_id"]
      if st.session_state["cliente_nome"] == "admin":
        email = st.text_input("Informe o novo e-mail")
        fone = st.text_input("Informe o novo fone")
        senha = st.text_input("Informe a nova senha")
        if st.button("Atualizar"):
          id = st.session_state["cliente_id"]
          View.cliente_atualizar(id, "admin", email, fone, senha)
          st.success("Cliente atualizado com sucesso")
          time.sleep(2)
          st.rerun()
      else:
        nome = st.text_input("Informe o novo nome")
        email = st.text_input("Informe o novo e-mail")
        fone = st.text_input("Informe o novo fone")
        senha = st.text_input("Informe a nova senha")
        if st.button("Atualizar"):
          id = st.session_state["cliente_id"]
          View.cliente_atualizar(id, nome, email, fone, senha)
          st.success("Cliente atualizado com sucesso")
          time.sleep(2)
          st.rerun()