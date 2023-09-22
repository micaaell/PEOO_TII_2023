import json
class Cliente:
  def __init__(self, id, nome, email, fone):
    self.__id = id
    self.__nome = nome
    self.__email = email
    self.__fone = fone
  def get_id(self): return self.__id
  def get_nome(self): return self.__nome
  def get_email(self): return self.__email
  def get_fone(self): return self.__fone
  def set_id(self, id): self.__id = id
  def set_nome(self, nome): self.__nome = nome
  def set_email(self, email): self.__email = email
  def set_fone(self, fone): self.__fone = fone
  def __str__(self):
    return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"

class NCliente:
  __clientes = []         # lista de clientes inicia vazia
  @classmethod
  def inserir(cls, obj):
    NCliente.abrir()
    id = 0 # encontrar o maior id já usado
    for cliente in cls.__clientes:
      if cliente.get_id() > id: id = cliente.get_id()
    obj.set_id(id + 1)
    cls.__clientes.append(obj)  # insere um cliente (obj) na lista
    NCliente.salvar()
  @classmethod
  def listar(cls):
    NCliente.abrir()    
    return cls.__clientes       # retorna a lista de clientes
  @classmethod
  def listar_id(cls, id):
    NCliente.abrir()
    for cliente in cls.__clientes:
      if cliente.get_id() == id: return cliente
    return None
  @classmethod
  def atualizar(cls, obj):
    NCliente.abrir()
    cliente = cls.listar_id(obj.get_id())
    cliente.set_nome(obj.get_nome())
    cliente.set_email(obj.get_email())
    cliente.set_fone(obj.get_fone())
    NCliente.salvar()
  @classmethod
  def excluir(cls, obj):
    NCliente.abrir()
    cliente = cls.listar_id(obj.get_id())
    cls.__clientes.remove(cliente)    
    NCliente.salvar()
  @classmethod
  def abrir(cls):
    try:
      cls.__clientes = []
      with open("clientes.json", mode="r") as f:
        s = json.load(f)
        for cliente in s:
          c = Cliente(cliente["_Cliente__id"], cliente["_Cliente__nome"],
                     cliente["_Cliente__email"], cliente["_Cliente__fone"])
          cls.__clientes.append(c)
    except FileNotFoundError:
      pass
  @classmethod
  def salvar(cls):
    with open("clientes.json", mode="w") as f:
      json.dump(cls.__clientes, f, default=vars)

class UI:
  @classmethod
  def Main(cls):
    op = 0
    while(op != 99):
      op = UI.Menu()
      if op == 1: UI.ClienteInserir()
      if op == 2: UI.ClienteListar()
      if op == 3: UI.ClienteAtualizar()
      if op == 4: UI.ClienteExcluir()
  @classmethod
  def Menu(cls):
    print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 99-Sair")
    return int(input())
  @classmethod
  def ClienteInserir(cls):
    # id = int(input("Id: "))
    nome = input("Nome: ")
    email = input("E-mail: ")
    fone = input("fone: ")
    cliente = Cliente(0, nome, email, fone)
    NCliente.inserir(cliente)
  @classmethod
  def ClienteListar(cls):
    for cliente in NCliente.listar():
      print(cliente)
  @classmethod
  def ClienteAtualizar(cls):
    UI.ClienteListar()
    id = int(input("Id do cliente a ser atualizado: "))
    nome = input("Novo nome: ")
    email = input("Novo e-mail: ")
    fone = input("Novo fone: ")
    cliente = Cliente(id, nome, email, fone)
    NCliente.atualizar(cliente)    
  @classmethod
  def ClienteExcluir(cls):
    UI.ClienteListar()
    id = int(input("Id do cliente a ser excluído: "))
    cliente = Cliente(id, "", "", "")
    NCliente.excluir(cliente)

UI.Main()
