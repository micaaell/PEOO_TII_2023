import streamlit as st
import json

class Cliente:
    def __init__(self, id, nome, email, fone):
        self.id = id
        self.nome = nome
        self.email = email
        self.fone = fone

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
        NCliente.salvar()

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
        cliente = cls.listar_id(obj.id)
        cliente.nome = obj.nome
        cliente.email = obj.email
        cliente.fone = obj.fone
        NCliente.salvar()

    @classmethod
    def excluir(cls, obj):
        cliente = cls.listar_id(obj.id)
        cls.clientes.remove(cliente)
        NCliente.salvar()

    @classmethod
    def abrir(cls):
        try:
            with open("clientes.json", mode="r") as f:
                cls.clientes = json.load(f)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("clientes.json", mode="w") as f:
            json.dump(cls.clientes, f, default=lambda o: o.__dict__)

def main():
    st.title("POO lista 9B")

    menu_option = st.selectbox("Menu", ["Inserir Cliente", "Listar Clientes", "Atualizar Cliente", "Excluir Cliente"])

    if menu_option == "Inserir Cliente":
        st.header("Inserir Cliente")
        nome = st.text_input("Nome:")
        email = st.text_input("Email:")
        fone = st.text_input("Telefone:")
        if st.button("Cadastrar Cliente"):
            if nome and email and fone:
                new_client = Cliente(0, nome, email, fone)
                NCliente.inserir(new_client)
                st.success("Cliente cadastrado com sucesso!")
            else:
                st.warning("Por favor, preencha todos os campos.")

    elif menu_option == "Listar Clientes":
        st.header("Listar Clientes")
        NCliente.abrir()
        for cliente in NCliente.listar():
            st.write(f"ID: {cliente.id}, Nome: {cliente.nome}, Email: {cliente.email}, Fone: {cliente.fone}")

    elif menu_option == "Atualizar Cliente":
        st.header("Atualizar Cliente")
        id_to_update = st.number_input("Informe o ID do cliente a ser atualizado")
        if st.button("Buscar Cliente"):
            cliente_to_update = NCliente.listar_id(id_to_update)
            if cliente_to_update:
                new_nome = st.text_input("Novo Nome", value=cliente_to_update.nome)
                new_email = st.text_input("Novo Email", value=cliente_to_update.email)
                new_fone = st.text_input("Novo Telefone", value=cliente_to_update.fone)
                if st.button("Atualizar"):
                    cliente_to_update.nome = new_nome
                    cliente_to_update.email = new_email
                    cliente_to_update.fone = new_fone
                    NCliente.atualizar(cliente_to_update)
                    st.success("Cliente atualizado com sucesso!")

    elif menu_option == "Excluir Cliente":
        st.header("Excluir Cliente")
        id_to_delete = st.number_input("Informe o ID do cliente a ser excluído")
        if st.button("Excluir Cliente"):
            cliente_to_delete = NCliente.listar_id(id_to_delete)
            if cliente_to_delete:
                NCliente.excluir(cliente_to_delete)
                st.success("Cliente excluído com sucesso!")
            else:
                st.warning("Cliente não encontrado")

if __name__ == '__main__':
    main()
