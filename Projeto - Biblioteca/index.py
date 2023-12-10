from templates.manterlivroUI import ManterLivroUI
from templates.manterexemplarUI import ManterExemplarUI
from templates.mantergeneroUI import ManterGeneroUI
from templates.abrirgeneroUI import AbrirGeneroUI

import streamlit as st

class IndexUI:
      
    def sidebar():
      op = st.sidebar.selectbox("Menu", ["Livros", "Exemplares", "Gêneros", "Buscar livros por gênero"])
      if op == "Livros": ManterLivroUI.main()
      if op == "Exemplares": ManterExemplarUI.main()
      if op == "Gêneros": ManterGeneroUI.main()
      if op == "Buscar livros por gênero": AbrirGeneroUI.main()

      #if op == "Manter Clientes": st.session_state["page"] = "manter_clienteUI"

    def main():
      IndexUI.sidebar()

      #if "page" not in st.session_state: st.session_state["page"] = "equacaoUI"
      #if st.session_state["page"] == "manter_clienteUI": ManterClienteUI.main()

IndexUI.main()



