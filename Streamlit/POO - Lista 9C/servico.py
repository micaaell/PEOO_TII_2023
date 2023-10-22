import streamlit as st
import json
import datetime


class Agenda:

    def __init__(self, id, data, confirmado, id_cliente, id_servico):
        self.id = id
        self.data = data
        self.confirmado = confirmado
        self.id_cliente = id_cliente
        self.id_servico = id_servico

    def to_dict(self):
        return {
            'id': self.id,
            'data': self.data,
            'confirmado': self.confirmado,
            'id_cliente': self.id_cliente,
            'id_servico': self.id_servico
        }


class NAgenda:

    agendas = []

    @classmethod
    def inserir(cls, obj):
        NAgenda.abrir()
        id = 0
        for agenda in cls.agendas:
            if agenda.id > id:
                id = agenda.id
        obj.id = id + 1
        cls.agendas.append(obj)
        NAgenda.salvar()

    @classmethod
    def listar(cls):
        NAgenda.abrir()
        return cls.agendas

    @classmethod
    def listar_id(cls, id):
        NAgenda.abrir()
        for agenda in cls.agendas:
            if agenda.id == id:
                return agenda
        return None

    @classmethod
    def atualizar(cls, obj):
        NAgenda.abrir()
        agenda = cls.listar_id(obj.id)
        agenda.data = obj.data
        agenda.confirmado = obj.confirmado
        agenda.id_cliente = obj.id_cliente
        agenda.id_servico = obj.id_servico
        NAgenda.salvar()

    @classmethod
    def excluir(cls, obj):
        NAgenda.abrir()
        agenda = cls.listar_id(obj.id)
        cls.agendas.remove(agenda)
        NAgenda.salvar()

    @classmethod
    def abrir(cls):
        try:
            cls.agendas = []
            with open("agendas.json", mode="r") as f:
                s = json.load(f)
                for agenda in s:
                    c = Agenda(
                        agenda["id"],
                        datetime.datetime.strptime(agenda["data"], "%d/%m/%Y %H:%M"),
                        agenda["confirmado"],
                        agenda["id_cliente"],
                        agenda["id_servico"]
                    )
                    cls.agendas.append(c)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("agendas.json", mode="w") as f:
            json.dump([agenda.to_dict() for agenda in cls.agendas], f)


# Streamlit code
st.title("Appointment Management App")

NAgenda.abrir()  # Load data from JSON file

# Sidebar
st.sidebar.header("Menu")
menu_choice = st.sidebar.radio("Select an option", ["Add Appointment", "List Appointments", "Update Appointment", "Delete Appointment"])

if menu_choice == "Add Appointment":
    st.header("Add a New Appointment")
    new_id = len(NAgenda.agendas) + 1
    new_data = st.datetime_input("Date and Time")
    new_confirmado = st.checkbox("Confirmed")
    new_id_cliente = st.number_input("Client ID")
    new_id_servico = st.number_input("Service ID")
    if st.button("Add"):
        if new_data and new_id_cliente and new_id_servico:
            new_appointment = Agenda(new_id, new_data, new_confirmado, new_id_cliente, new_id_servico)
            NAgenda.inserir(new_appointment)
            NAgenda.salvar()
            st.success("Appointment added successfully!")

elif menu_choice == "List Appointments":
    st.header("List of Appointments")
    appointments = NAgenda.listar()
    for appointment in appointments:
        st.write(f"ID: {appointment.id}, Date: {appointment.data}, Confirmed: {appointment.confirmado}")

elif menu_choice == "Update Appointment":
    st.header("Update Appointment Information")
    appointment_id = st.number_input("Enter the appointment ID you want to update")
    if st.button("Search"):
        appointment_to_update = NAgenda.listar_id(appointment_id)
        if appointment_to_update:
            new_data = st.datetime_input("New Date and Time", appointment_to_update.data)
            new_confirmado = st.checkbox("New Confirmation Status", appointment_to_update.confirmado)
            new_id_cliente = st.number_input("New Client ID", appointment_to_update.id_cliente)
            new_id_servico = st.number_input("New Service ID", appointment_to_update.id_servico)
            if st.button("Update"):
                appointment_to_update.data = new_data
                appointment_to_update.confirmado = new_confirmado
                appointment_to_update.id_cliente = new_id_cliente
                appointment_to_update.id_servico = new_id_servico
                NAgenda.atualizar(appointment_to_update)
                NAgenda.salvar()
                st.success("Appointment information updated successfully!")

        else:
            st.error("Appointment not found")

elif menu_choice == "Delete Appointment":
    st.header("Delete an Appointment")
    appointment_id = st.number_input("Enter the appointment ID you want to delete")
    if st.button("Delete"):
        appointment_to_delete = NAgenda.listar_id(appointment_id)
        if appointment_to_delete:
            NAgenda.excluir(appointment_to_delete)
            NAgenda.salvar()
            st.success("Appointment deleted successfully!")
        else:
            st.error("Appointment not found")
