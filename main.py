from PyQt5 import uic,QtWidgets
import pymysql.connections

banco = pymysql.connections.Connection(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "oficina.db"
)


def fazer_login():
    nome=acesso.input_usuario.text()
    senha = acesso.input_senha.text()

    cursor = banco.cursor()
    cursor.execute("SELECT * FROM usuario WHERE login = %s AND senha = %s", (nome, senha))
    resultado = cursor.fetchone ()

    if resultado:
        menu.show()
        acesso.hide()
    else:
        print("Usuário ou senha incorretos!")


def abrir_tela_cliente():
    tela_cliente.show()
    menu.hide()


def cadastrar_cliente():
    nome = tela_cliente.input_nome.text()
    cpf = tela_cliente.input_cpf.text()
    telefone = tela_cliente.input_telefone.text()
    email = tela_cliente.input_email.text()
    endereço = tela_cliente.input_endereco.text()

    
    cursor = banco.cursor()
    sql = "INSERT INTO cliente (nome, cpf, telefone, email, endereco) VALUES (%s, %s, %s, %s, %s)"
    dados = (str(nome), str(cpf), str(telefone), str(email), str(endereço))
    cursor.execute(sql, dados)
    banco.commit()
    tela_cliente.input_nome.setText("")
    tela_cliente.input_cpf.setText("")
    tela_cliente.input_telefone.setText("")
    tela_cliente.input_email.setText("")
    tela_cliente.input_endereco.setText("")


def voltar_de_clientes():
    tela_cliente.hide()
    menu.show()


def listar_clientes():
    tela_listar_clientes.show()

    cursor = banco.cursor()
    sql = "SELECT * FROM cliente"
    cursor.execute(sql)
    dados_lidos = cursor.fetchall()
    
    tela_listar_clientes.tablewidget.setRowCount(len(dados_lidos))
    tela_listar_clientes.tablewidget.setColumnCount(6)
    tela_listar_clientes.tablewidget.setHorizontalHeaderLabels(["ID", "Nome", "CPF", "Telefone", "Email", "Endereço"])
    
    for linha in range(0, len(dados_lidos)):
        for coluna in range(0, 6):
            tela_listar_clientes.tablewidget.setItem(linha, coluna, QtWidgets.QTableWidgetItem(str(dados_lidos[linha][coluna])))


def voltar_de_listar_clientes():
    tela_listar_clientes.hide()
    tela_cliente.show()


def excluircliente():
    linha = tela_listar_clientes.tablewidget.currentRow()
    id = tela_listar_clientes.tablewidget.item(linha,0).text()

    cursor = banco.cursor()
    sql = "DELETE FROM cliente WHERE id = %s"

    cursor.execute(sql, (id,))
    banco.commit()

    print("Cliente excluído com sucesso!")

    listar_clientes()


def editar_cliente():
    linha = tela_listar_clientes.tablewidget.currentRow()
    id = tela_listar_clientes.tablewidget.item(linha,0).text()

    nome = tela_listar_clientes.tablewidget.item(linha,1).text()
    cpf = tela_listar_clientes.tablewidget.item(linha,2).text()
    telefone = tela_listar_clientes.tablewidget.item(linha,3).text()
    email = tela_listar_clientes.tablewidget.item(linha,4).text()
    endereco = tela_listar_clientes.tablewidget.item(linha,5).text()

    cursor = banco.cursor()
    sql = "UPDATE cliente SET nome = %s, cpf = %s, telefone = %s, email = %s, endereco = %s WHERE id = %s"
    dados = (nome, cpf, telefone, email, endereco, id)
    cursor.execute(sql, dados)
    banco.commit()

    print("Cliente atualizado com sucesso!")


def abrir_tela_carros():
    tela_carros.show()
    menu.hide()


def cadastrar_carros():
    placa = tela_carros.input_placa.text()
    marca = tela_carros.input_marca.text()
    modelo = tela_carros.input_modelo.text()
    ano = tela_carros.input_ano.text()
    cor = tela_carros.input_cor.text()
    id_cliente = tela_carros.input_id_cliente.text()

    
    cursor = banco.cursor()
    sql = "INSERT INTO carro (placa, marca, modelo, ano, cor, id_cliente) VALUES (%s, %s, %s, %s, %s, %s)"
    dados = (str(placa), str(marca), str(modelo), str(ano), str(cor), str(id_cliente))
    cursor.execute(sql, dados)
    banco.commit()
    tela_carros.input_placa.setText("")
    tela_carros.input_marca.setText("")
    tela_carros.input_modelo.setText("")
    tela_carros.input_ano.setText("")
    tela_carros.input_cor.setText("")
    tela_carros.input_id_cliente.setText("")
    

def voltar_de_carros():
    tela_carros.hide()
    menu.show()


def listar_carros():
    tela_listar_carros.show()

    cursor = banco.cursor()
    sql = "SELECT * FROM carro"
    cursor.execute(sql)
    dados_lidos = cursor.fetchall()
    
    tela_listar_carros.tablewidget.setRowCount(len(dados_lidos))
    tela_listar_carros.tablewidget.setColumnCount(7)
    tela_listar_carros.tablewidget.setHorizontalHeaderLabels(["ID", "Placa", "Modelo", "Marca", "Cor", "Ano", "ID Cliente"])
    
    for linha in range(0, len(dados_lidos)):
        for coluna in range(0, 7):
            tela_listar_carros.tablewidget.setItem(linha, coluna, QtWidgets.QTableWidgetItem(str(dados_lidos[linha][coluna])))


def voltar_de_listar_carros():
    tela_listar_carros.hide()
    tela_carros.show()


def excluircarro():
    linha = tela_listar_carros.tablewidget.currentRow()
    id = tela_listar_carros.tablewidget.item(linha,0).text()

    cursor = banco.cursor()
    sql = "DELETE FROM carro WHERE id = %s"

    cursor.execute(sql, (id,))
    banco.commit()

    print("Carro excluído com sucesso!")

    listar_carros()


def editar_carro():
    linha = tela_listar_carros.tablewidget.currentRow()
    id = tela_listar_carros.tablewidget.item(linha,0).text()

    placa = tela_listar_carros.tablewidget.item(linha,1).text()
    modelo = tela_listar_carros.tablewidget.item(linha,2).text()
    marca = tela_listar_carros.tablewidget.item(linha,3).text()
    cor = tela_listar_carros.tablewidget.item(linha,4).text()
    ano = tela_listar_carros.tablewidget.item(linha,5).text()
    id_cliente = tela_listar_carros.tablewidget.item(linha,6).text()

    cursor = banco.cursor()
    sql = "UPDATE carro SET placa = %s, marca = %s, modelo = %s, ano = %s, cor = %s, id_cliente = %s WHERE id = %s"
    dados = (placa, marca, modelo, ano, cor, id_cliente, id)
    cursor.execute(sql, dados)
    banco.commit()

    print("Carro atualizado com sucesso!")


def abrir_tela_servicos():
    tela_servicos.show()
    menu.hide()


def cadastrar_servico():
    nome = tela_servicos.input_nome.text()
    descricao = tela_servicos.input_descricao.text()
    preco = tela_servicos.input_preco.text()

    
    cursor = banco.cursor()
    sql = "INSERT INTO servico (nome, descricao, preco) VALUES (%s, %s, %s)"
    dados = (str(nome), str(descricao), str(preco))
    cursor.execute(sql, dados)
    banco.commit()
    tela_servicos.input_nome.setText("")
    tela_servicos.input_descricao.setText("")
    tela_servicos.input_preco.setText("")


def voltar_de_servicos():
    tela_servicos.hide()
    menu.show()


def listar_servicos():
    tela_listar_servicos.show()

    cursor = banco.cursor()
    sql = "SELECT * FROM servico"
    cursor.execute(sql)
    dados_lidos = cursor.fetchall()
    
    tela_listar_servicos.tablewidget.setRowCount(len(dados_lidos))
    tela_listar_servicos.tablewidget.setColumnCount(4)
    tela_listar_servicos.tablewidget.setHorizontalHeaderLabels(["ID", "Nome", "Descrição", "Preço"])    
    for linha in range(0, len(dados_lidos)):
        for coluna in range(0, 4):
            tela_listar_servicos.tablewidget.setItem(linha, coluna, QtWidgets.QTableWidgetItem(str(dados_lidos[linha][coluna])))


def voltar_de_listar_servicos():
    tela_listar_servicos.hide()
    tela_servicos.show()


def excluirservico():
    linha = tela_listar_servicos.tablewidget.currentRow()
    id = tela_listar_servicos.tablewidget.item(linha,0).text()

    cursor = banco.cursor()
    sql = "DELETE FROM servico WHERE id = %s"

    cursor.execute(sql, (id,))
    banco.commit()

    print("Serviço excluído com sucesso!")

    listar_servicos()
    

def editar_servico():
    linha = tela_listar_servicos.tablewidget.currentRow()
    id = tela_listar_servicos.tablewidget.item(linha,0).text()

    nome = tela_listar_servicos.tablewidget.item(linha,1).text()
    descricao = tela_listar_servicos.tablewidget.item(linha,2).text()
    preco = tela_listar_servicos.tablewidget.item(linha,3).text()

    cursor = banco.cursor()
    sql = "UPDATE servico SET nome = %s, descricao = %s, preco = %s WHERE id = %s"
    dados = (nome, descricao, preco, id)
    cursor.execute(sql, dados)
    banco.commit()

    print("Serviço atualizado com sucesso!")


def abrir_tela_os():
    tela_os.show()
    menu.hide()

def cadastrar_os():
    id_cliente = tela_os.input_id_cliente.text()
    id_carro = tela_os.input_id_carro.text()
    data_abertura = tela_os.dateEdit.date().toString("yyyy-MM-dd")
    status = tela_os.comboBox_status.currentText()
    
    
    cursor = banco.cursor()
    sql = "INSERT INTO ordem_servico (id_cliente, id_carro, status, data_abertura) VALUES (%s, %s, %s, %s)"
    dados = (str(id_cliente), str(id_carro), str(status), str(data_abertura))
    cursor.execute(sql, dados)
    banco.commit()
    tela_os.input_id_cliente.setText("")
    tela_os.input_id_carro.setText("")
    tela_os.comboBox_status.setCurrentIndex(0)
   
def voltar_de_cadastrar_os():
    tela_os.hide()
    menu.show()

def listar_os():
    tela_listar_os.show()

    cursor = banco.cursor()
    sql = "SELECT * FROM ordem_servico"
    cursor.execute(sql)
    dados_lidos = cursor.fetchall()
    
    tela_listar_os.tablewidget.setRowCount(len(dados_lidos))
    tela_listar_os.tablewidget.setColumnCount(5)
    tela_listar_os.tablewidget.setHorizontalHeaderLabels(["ID", "ID Cliente", "ID Carro", "Status", "Data Abertura"])    
    for linha in range(0, len(dados_lidos)):
        for coluna in range(0, 5):
            tela_listar_os.tablewidget.setItem(linha, coluna, QtWidgets.QTableWidgetItem(str(dados_lidos[linha][coluna])))

def voltar_de_listar_os():
    tela_listar_os.hide()
    tela_os.show()

def excluir_os():
    linha = tela_listar_os.tablewidget.currentRow()
    id = tela_listar_os.tablewidget.item(linha,0).text()

    cursor = banco.cursor()
    sql = "DELETE FROM ordem_servico WHERE id = %s"

    cursor.execute(sql, (id,))
    banco.commit()

    print("Ordem de serviço excluída com sucesso!")

def editar_os():
    linha = tela_listar_os.tablewidget.currentRow()
    id = tela_listar_os.tablewidget.item(linha,0).text()

    id_cliente = tela_listar_os.tablewidget.item(linha,1).text()
    id_carro = tela_listar_os.tablewidget.item(linha,2).text()
    status = tela_listar_os.tablewidget.item(linha,3).text()
    data_abertura = tela_listar_os.tablewidget.item(linha,4).text()

    cursor = banco.cursor()
    sql = "UPDATE ordem_servico SET id_cliente = %s, id_carro = %s, status = %s, data_abertura = %s WHERE id = %s"
    dados = (id_cliente, id_carro, status, data_abertura, id)
    cursor.execute(sql, dados)
    banco.commit()

    print("Ordem de serviço atualizada com sucesso!")


app = QtWidgets.QApplication([])
acesso = uic.loadUi("login.ui")
menu = uic.loadUi("Sistema_Oficina.ui")
tela_cliente = uic.loadUi("clientes.ui")
tela_listar_clientes = uic.loadUi("listar_clientes.ui")
tela_carros = uic.loadUi("carros.ui")
tela_listar_carros = uic.loadUi("listar_carros.ui")
tela_servicos = uic.loadUi("servicos.ui")
tela_listar_servicos = uic.loadUi("listar_servicos.ui")
tela_os = uic.loadUi("ordem_servico.ui")
tela_listar_os = uic.loadUi("listar_ordem_servico.ui")


acesso.button_entrar.clicked.connect(fazer_login)

menu.button_clientes.clicked.connect(abrir_tela_cliente)
menu.button_carros.clicked.connect(abrir_tela_carros)
menu.button_servicos.clicked.connect(abrir_tela_servicos)
menu.button_os.clicked.connect(abrir_tela_os)

tela_cliente.button_cadastrar.clicked.connect(cadastrar_cliente)
tela_cliente.button_editar.clicked.connect(listar_clientes)
tela_cliente.button_voltar.clicked.connect(voltar_de_clientes)

tela_listar_clientes.button_listar.clicked.connect(listar_clientes)
tela_listar_clientes.button_excluir.clicked.connect(excluircliente)
tela_listar_clientes.button_editar.clicked.connect(editar_cliente)
tela_listar_clientes.button_voltar.clicked.connect(voltar_de_listar_clientes)


tela_carros.button_cadastrar.clicked.connect(cadastrar_carros)
tela_carros.button_editar.clicked.connect(listar_carros)
tela_carros.button_voltar.clicked.connect(voltar_de_carros)

tela_listar_carros.button_listar.clicked.connect(listar_carros)
tela_listar_carros.button_excluir.clicked.connect(excluircarro)
tela_listar_carros.button_editar.clicked.connect(editar_carro)
tela_listar_carros.button_voltar.clicked.connect(voltar_de_listar_carros)

tela_servicos.button_cadastrar.clicked.connect(cadastrar_servico)
tela_servicos.button_editar.clicked.connect(listar_servicos)
tela_servicos.button_voltar.clicked.connect(voltar_de_servicos)

tela_listar_servicos.button_listar.clicked.connect(listar_servicos)
tela_listar_servicos.button_excluir.clicked.connect(excluirservico)
tela_listar_servicos.button_editar.clicked.connect(editar_servico)
tela_listar_servicos.button_voltar.clicked.connect(voltar_de_listar_servicos)

tela_os.button_cadastrar.clicked.connect(cadastrar_os)
tela_os.button_editar.clicked.connect(listar_os)
tela_os.button_voltar.clicked.connect(voltar_de_cadastrar_os)

tela_listar_os.button_listar.clicked.connect(listar_os)
tela_listar_os.button_excluir.clicked.connect(excluir_os)
tela_listar_os.button_editar.clicked.connect(editar_os)
tela_listar_os.button_voltar.clicked.connect(voltar_de_listar_os)


acesso.show()
app.exec()