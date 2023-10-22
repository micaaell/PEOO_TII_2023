import streamlit as st
from cliente import Cliente, NCliente
from agenda import Agenda, NAgenda

class Views:

    @classmethod
    def cliente_inserir(cls, nome, email, fone):
        cliente = Cliente(0, nome, email, fone)
        NCliente.inserir(cliente)

    @classmethod
    def cliente_listar(cls):
        return NCliente.listar()

    @classmethod
    def agenda_abrir_agenda_do_dia(cls, data, hinicio, hfim, intervalo):
        # Convert user input to proper data structures (you can add validation)
        date = data.strftime("%d/%m/%Y")
        start_time = f"{hinicio.hour:02d}:{hinicio.minute:02d}"
        end_time = f"{hfim.hour:02d}:{hfim.minute:02d}"
        start_time_parts = start_time.split(":")
        end_time_parts = end_time.split(":")

        # Extract hours and minutes
        start_hour, start_minute = map(int, start_time_parts)
        end_hour, end_minute = map(int, end_time_parts)

        # Calculate the total time difference in minutes
        time_diff_minutes = (end_hour - start_hour) * 60 + (end_minute - start_minute)

        # Calculate the number of slots
        num_slots = time_diff_minutes // intervalo

        # Generate agenda based on the input
        for slot in range(num_slots + 1):
            slot_time = f"{start_hour:02d}:{start_minute:02d}"
            NAgenda.inserir(Agenda(0, f"{date} {slot_time}", False, 0, 0))

# Streamlit code
st.title("Client and Agenda Management")

# Sidebar
st.sidebar.header("Menu")
menu_choice = st.sidebar.radio("Select an option", ["Add Client", "List Clients", "Open Daily Agenda"])

if menu_choice == "Add Client":
    st.header("Add a New Client")
    nome = st.text_input("Name")
    email = st.text_input("Email")
    fone = st.text_input("Phone")
    if st.button("Add Client"):
        if nome and email and fone:
            Views.cliente_inserir(nome, email, fone)
            st.success("Client added successfully!")

elif menu_choice == "List Clients":
    st.header("List of Clients")
    clients = Views.cliente_listar()
    for client in clients:
        st.write(f"ID: {client.get_id()}, Name: {client.get_nome()}, Email: {client.get_email()}, Phone: {client.get_fone()}")

elif menu_choice == "Open Daily Agenda":
    st.header("Open Daily Agenda")
    data = st.date_input("Date")
    hinicio = st.time_input("Start Time")
    hfim = st.time_input("End Time")
    intervalo = st.number_input("Interval (minutes)", min_value=1, value=30)
    if st.button("Open Agenda"):
        Views.agenda_abrir_agenda_do_dia(data, hinicio, hfim, intervalo)
        st.success("Agenda opened successfully!")
