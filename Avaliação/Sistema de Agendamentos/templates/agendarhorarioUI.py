import streamlit as st
import pandas as pd
from views import View
import time
import datetime

class AgendarHorarioUI:
  def main():
    st.header("CAgendar Horario")
    tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
    with tab1: AgendarHorarioUI.listar()
    with tab2: AgendarHorarioUI.inserir()
    with tab3: AgendarHorarioUI.atualizar()
    with tab4: AgendarHorarioUI.excluir()    

  def listar():
    agendas = View.agenda_listar()
    if len(agendas) == 0:
      st.write("Nenhum horário cadastrado")
    else:
      dic = []
      for obj in agendas: dic.append(obj.to_json())
      df = pd.DataFrame(dic)
      st.dataframe(df)

  def inserir():
    available_slots = View.get_available_time_slots_week()
    if len(available_slots) == 0:
      st.write("Nenhum horário disponível na próxima semana.")
    else:
      selected_slot = st.selectbox("Selecione um horário disponível:", available_slots)

      clientes = View.cliente_listar()
      cliente = st.selectbox("Selecione o cliente", clientes)
      servicos = View.servico_listar()
      servico = st.selectbox("Selecione o serviço", servicos)
      servicos = View.servico_listar()

    if st.button("Agendar Atendimento"):
      data = datetime.datetime.strptime(selected_slot,"%d/%m/%Y %H:%M")
      View.agenda_inserir(data, False, cliente.get_id(), servico.get_id())
      st.success("Horário inserido com sucesso")
      time.sleep(2)
      

  def atualizar():
    agendas = View.agenda_listar()
    if len(agendas) == 0:
      st.write("Nenhum horário disponível")
    else:  
      op = st.selectbox("Atualização de horários", agendas)
      datastr = st.text_input("Informe a nova data no formato *dd/mm/aaaa HH\:MM*", op.get_data().strftime('%d/%m/%Y %H:%M'))
      clientes = View.cliente_listar()
      cliente_atual = View.cliente_listar_id(op.get_id_cliente())
      if cliente_atual is not None:
        cliente = st.selectbox("Selecione o novo cliente", clientes, clientes.index(cliente_atual))
      else:  
        cliente = st.selectbox("Selecione o novo cliente", clientes)
      servicos = View.servico_listar()
      servico_atual = View.servico_listar_id(op.get_id_servico())
      if servico_atual is not None:
        servico = st.selectbox("Selecione o novo serviço", servicos, servicos.index(servico_atual))
      else:
        servico = st.selectbox("Selecione o novo serviço", servicos)
      if st.button("Atualizar"):
        data = datetime.datetime.strptime(datastr, "%d/%m/%Y %H:%M")
        View.agenda_atualizar(op.get_id(), data, op.get_confirmado(), cliente.get_id(), servico.get_id())
        st.success("Horário atualizado com sucesso")
        time.sleep(2)
        st.rerun()

  def excluir():
    agendas = View.agenda_listar()
    if len(agendas) == 0:
      st.write("Nenhum horário disponível")
    else:  
      op = st.selectbox("Exclusão de horários", agendas)
      if st.button("Excluir"):
        View.agenda_excluir(op.get_id())
        st.success("Horário excluído com sucesso")
        time.sleep(2)
 
        


