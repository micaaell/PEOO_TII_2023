from templates.manterlivroUI import ManterLivroUI
from templates.manterexemplarUI import ManterExemplarUI
from templates.mantergeneroUI import ManterGeneroUI
from templates.loginUI import LoginUI
from templates.listarlivrosUI import ListarLivroUI
from templates.editarperfilUI import EditarPerfilUI
from views import View

import streamlit as st



class IndexUI:
    def menu_visitante():
      op = st.sidebar.selectbox("Menu", ["Login","Todos os livros"])
      if op == "Login": LoginUI.main()
      if op == "Todos os livros": ListarLivroUI.main()
      
    def menu_admin():
      op = st.sidebar.selectbox("Menu", ["Livros", "Exemplares", "Gêneros", "Editar Perfil"])
      if op == "Livros": ManterLivroUI.main()
      if op == "Exemplares": ManterExemplarUI.main()
      if op == "Gêneros": ManterGeneroUI.main()
      if op == "Editar Perfil": EditarPerfilUI.main()
      
    def menu_cliente():
      op = st.sidebar.selectbox("Menu", ["Todos os livros"])
      if op == "Todos os livros": ListarLivroUI.main()

    def btn_logout():
      if st.sidebar.button("Logout"):
        del st.session_state["cliente_id"]
        del st.session_state["cliente_nome"]
      st.rerun()
      
    def sidebar():
      if "cliente_id" not in st.session_state:
        IndexUI.menu_visitante()   
      else:
        st.sidebar.write("Bem-vindo(a), " + st.session_state["cliente_nome"])
        if st.session_state["cliente_nome"] == "admin": IndexUI.menu_admin()
        else:
          IndexUI.menu_cliente()
          IndexUI.btn_logout() 
          

    def main():
      View.cliente_admin()
      IndexUI.sidebar()

      #if "page" not in st.session_state: st.session_state["page"] = "equacaoUI"
      #if st.session_state["page"] == "manter_clienteUI": ManterClienteUI.main()

IndexUI.main()



