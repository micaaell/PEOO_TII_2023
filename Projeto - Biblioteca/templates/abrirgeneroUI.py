import streamlit as st
from views import View
import time

class AbrirGeneroUI:

  def main():
    st.header("Buscar livros por gênero")
    AbrirGeneroUI.abrir_genero()

  def abrir_genero():
    genero= View.genero_listar()
    genero = st.selectbox("Selecione o genero", genero)
    if st.button("Buscar livro"):
      View.genero_buscar(genero)
      time.sleep(2)
      st.rerun()
