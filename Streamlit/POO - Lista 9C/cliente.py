import json
import streamlit as st

class Cliente:
    def __init__(self, id, nome, email, fone):
        self.id = id
        self.nome = nome
        self.email = email
        self.fone = fone
    def get_id(self):
        return self.id
    def get_nome(self):
        return self.nome
    def get_email(self):
        return self.email
    def get_fone(self):
        return self.fone

class NCliente:
    clientes = []

    @classmethod
    def inserir(cls, obj):
        id = 0
        for cliente in cls.clientes:
            if cliente.id > id:
                id = cliente.id
        obj.id = id + 1
        cls.clientes.append(obj)
    
    @classmethod
    def listar(cls):
        return cls.clientes
    
    @classmethod
    def listar_id(cls, id):
        for cliente in cls.clientes:
            if cliente.id == id:
                return cliente
        return None

    @classmethod
    def atualizar(cls, obj):
        cliente = NCliente.listar_id(obj.id)
        cliente.nome = obj.nome
        cliente.email = obj.email
        cliente.fone = obj.fone

    @classmethod
    def excluir(cls, obj):
        cliente = NCliente.listar_id(obj.id)
        cls.clientes.remove(cliente)

    @classmethod
    def abrir(cls):
        try:
            with open("clientes.json", "r") as f2:
                clientes_json = json.load(f2)  # lista de dicts
                for obj in clientes_json:
                    c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"])
                    cls.clientes.append(c)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("clientes.json", "w") as f1:
            clientes_json = [{"id": c.id, "nome": c.nome, "email": c.email, "fone": c.fone} for c in cls.clientes]
            json.dump(clientes_json, f1)

# Streamlit code
st.title("Client Management App")

NCliente.abrir()  # Load data from JSON file

# Sidebar
st.sidebar.header("Menu")
menu_choice = st.sidebar.radio("Select an option", ["Add Client", "List Clients", "Update Client", "Delete Client"])

if menu_choice == "Add Client":
    st.header("Add a New Client")
    new_id = len(NCliente.clientes) + 1
    new_nome = st.text_input("Name")
    new_email = st.text_input("Email")
    new_fone = st.text_input("Phone")
    if st.button("Add"):
        if new_nome and new_email and new_fone:
            new_client = Cliente(new_id, new_nome, new_email, new_fone)
            NCliente.inserir(new_client)
            NCliente.salvar()
            st.success("Client added successfully!")

elif menu_choice == "List Clients":
    st.header("List of Clients")
    clients = NCliente.listar()
    for client in clients:
        st.write(f"ID: {client.id}, Name: {client.nome}, Email: {client.email}, Phone: {client.fone}")

elif menu_choice == "Update Client":
    st.header("Update Client Information")
    client_id = st.number_input("Enter the client ID you want to update")
    if st.button("Search"):
        client_to_update = NCliente.listar_id(client_id)
        if client_to_update:
            new_nome = st.text_input("New Name", client_to_update.nome)
            new_email = st.text_input("New Email", client_to_update.email)
            new_fone = st.text_input("New Phone", client_to_update.fone)
            if st.button("Update"):
                client_to_update.nome = new_nome
                client_to_update.email = new_email
                client_to_update.fone = new_fone
                NCliente.atualizar(client_to_update)
                NCliente.salvar()
                st.success("Client information updated successfully!")
        else:
            st.error("Client not found")

elif menu_choice == "Delete Client":
    st.header("Delete a Client")
    client_id = st.number_input("Enter the client ID you want to delete")
    if st.button("Delete"):
        client_to_delete = NCliente.listar_id(client_id)
        if client_to_delete:
            NCliente.excluir(client_to_delete)
            NCliente.salvar()
            st.success("Client deleted successfully!")
        else:
            st.error("Client not found")
