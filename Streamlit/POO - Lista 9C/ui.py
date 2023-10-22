import streamlit as st
from cliente import Cliente, NCliente
from servico import Servico, NServico
from agenda import Agenda, NAgenda
from views import Views
import datetime

st.title("Client and Agenda Management")

menu_choice = st.sidebar.selectbox(
    "Select an option",
    ["Client Operations", "Service Operations", "Agenda Operations"]
)

if menu_choice == "Client Operations":
    st.header("Client Operations")
    client_op = st.selectbox(
        "Select an operation",
        ["Add Client", "List Clients", "Update Client", "Delete Client"]
    )

    if client_op == "Add Client":
        st.subheader("Add a New Client")
        nome = st.text_input("Name")
        email = st.text_input("Email")
        fone = st.text_input("Phone")
        if st.button("Add Client"):
            if nome and email and fone:
                Views.cliente_inserir(nome, email, fone)
                st.success("Client added successfully!")

    elif client_op == "List Clients":
        st.subheader("List of Clients")
        clients = Views.cliente_listar()
        for client in clients:
            st.write(f"ID: {client.get_id()}, Name: {client.get_nome()}, Email: {client.get_email()}, Phone: {client.get_fone()}")

    # Add code for Update Client and Delete Client operations

elif menu_choice == "Service Operations":
    st.header("Service Operations")
    service_op = st.selectbox(
        "Select an operation",
        ["Add Service", "List Services", "Update Service", "Delete Service"]
    )

    if service_op == "Add Service":
        st.subheader("Add a New Service")
        desc = st.text_input("Description")
        valor = st.number_input("Value")
        duracao = st.number_input("Duration")
        if st.button("Add Service"):
            if desc and valor and duracao:
                Views.servico_inserir(desc, valor, duracao)
                st.success("Service added successfully!")

    elif service_op == "List Services":
        st.subheader("List of Services")
        services = Views.servico_listar()
        for service in services:
            st.write(f"ID: {service.get_id()}, Description: {service.get_descricao()}, Value: {service.get_valor()}, Duration: {service.get_duracao()}")

    # Add code for Update Service and Delete Service operations

elif menu_choice == "Agenda Operations":
    st.header("Agenda Operations")
    agenda_op = st.selectbox(
        "Select an operation",
        ["Add Agenda", "List Agendas", "Update Agenda", "Delete Agenda"]
    )

    if agenda_op == "Add Agenda":
        st.subheader("Add a New Agenda")
        data = st.date_input("Date")
        confirmado = st.checkbox("Confirmed")
        id_cliente = st.selectbox("Select a Client", [client.get_nome() for client in Views.cliente_listar()])
        id_servico = st.selectbox("Select a Service", [service.get_descricao() for service in Views.servico_listar()])
        if st.button("Add Agenda"):
            if data and id_cliente and id_servico:
                Views.agenda_inserir(data, confirmado, id_cliente, id_servico)
                st.success("Agenda added successfully!")

    elif agenda_op == "List Agendas":
        st.subheader("List of Agendas")
        agendas = Views.agenda_listar()
        for agenda in agendas:
            st.write(f"ID: {agenda.get_id()}, Date: {agenda.get_data()}, Confirmed: {agenda.get_confirmado()}")

    # Add code for Update Agenda and Delete Agenda operations
