import mysql.connector
import locale
from base import sql
from flask import Flask, render_template, request

# crud.py
app = Flask(__name__)

#rota main
@app.route('/')
def menu():
    return render_template('menu.html')

#rota formulario para inclusão do SGBD
@app.route('/formincluir')
def formIncluir_curso():
    return render_template('formIncluir.html')

# função incluir
@app.route('/incluir', methods=['POST'])
def incluir():
    nome = request.form['nome']
    data = request.form['data']
    telefone = request.form['telefone']
    descricao = request.form['descricao']
    locadouro = request.form['locadouro']
    salario = request.form['salario']

    mysql = sql.SQL("root", "", "test")
    comando = "INSERT INTO tb_curriculo(nome, data, telefone, descricao, locadouro, salario) VALUES (%s, %s, %s, %s, %s, %s);"

    if mysql.executar(comando, [nome, data, telefone, descricao, locadouro, salario]):
        msg = f"{nome},seu currículo foi adicionado com sucesso"
    else:
        msg = "Falha ao adicionar currículo, por favor tente novamente."
    return render_template('incluir.html', msg=msg)


# formulario para consulta de dados
@app.route('/parconsultar')
def parConsultar():
   # Recuperando modelos existentes na base de dados
   mysql = sql.SQL("root", "", "test")
   comando = "SELECT DISTINCT nome FROM tb_curriculo ORDER BY nome;"

   cs = mysql.consultar(comando, ())
   sel = "<SELECT NAME='nome'>"
   sel += "<OPTION>Todos</OPTION>"
   for [nome] in cs:
       sel += "<OPTION>" + nome + "</OPTION>"
   sel += "</SELECT>"
   cs.close()

   return render_template('parConsultar.html', nome=sel)

# função consultar banco de dados e verificação
@app.route('/consultar', methods=['POST'])
def consultar():
    # Pegando os dados de parâmetro vindos do formulário parConsultar()
    nome = request.form['nome']

    # Testando se é para considerar todos os modelos
    nome = "" if nome == "Todos" else nome

    # Recuperando dados que satisfazem aos parâmetros de filtragem
    mysql = sql.SQL("root", "", "test")
    comando = "SELECT * FROM tb_curriculo WHERE nome LIKE CONCAT('%', %s, '%')"
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF8')

    cs = mysql.consultar(comando, [nome])
    nomes = ""
    for [idt, nome, data, telefone, descricao, locadouro, salario] in cs:
        nomes += "<TR>"
        nomes += "<TD>" + str(nome) + "</TD>"
        nomes += "<TD>" + str(data) + "</TD>"
        nomes += "<TD>" + str(telefone) + "</TD>"
        nomes += "<TD>" + str(descricao) + "</TD>"
        nomes += "<TD>" + str(locadouro) + "</TD>"
        nomes += "<TD>" + str(salario) + "</TD>"
        nomes += "</TR>"
    cs.close()

    return render_template('consultar.html', nomes=nomes)

# rota busca para alteração
@app.route('/paralterar')
def parAlterar_curso():
    return render_template('parAlterar.html')

# formulario para alteração de dados
@app.route('/formalterar', methods=['POST'])
def formAlterar_curso():

    nome = request.form['nome']

    mysql = sql.SQL("root", "", "test")
    comando = "SELECT * FROM tb_curriculo WHERE nome=%s;"

    cs = mysql.consultar(comando, [nome])
    dados = cs.fetchone()
    cs.close()

    if dados == None:
        return render_template('naoEncontrado.html')
    else:
        return render_template('formAlterar.html', idt=dados[0], nome=dados[1], data=dados[2], telefone=dados[3],
                               descricao=dados[4], locadouro=dados[5], salario=dados[6])

# rota para alterar dados
@app.route('/alterar', methods=['POST'])
def alterar():
    print("1 stop")
    idt = request.form['idt']
    nome = request.form['nome']
    data = request.form['data']
    telefone = request.form['telefone']
    descricao = request.form['descricao']
    locadouro = request.form['locadouro']
    salario = request.form['salario']
    print(idt, nome, data, telefone, descricao, locadouro, salario)
    print('2 stop')

    mysql = sql.SQL("root", "", "test")
    comando = "UPDATE tb_curriculo SET nome=%s, data=%s, telefone=%s, descricao=%s, locadouro=%s, salario=%s WHERE idt=%s;"

    if mysql.executar(comando, [nome, data, telefone, descricao, locadouro, salario, idt]):
        msg = "curso: " + nome + " alterado com sucesso!"
    else:
        msg = "Falha na alteração de curso"

    return render_template('alterar.html', msg=msg)

# rota para exclusão(não há necessidade de formulario)
@app.route('/parexcluir')
def parExcluir_curso():
    # Recuperando todos os modelos da base de dados
    mysql = sql.SQL("root", "", "test")
    comando = "SELECT idt, nome, telefone, data FROM tb_curriculo ORDER BY nome;"

    cs = mysql.consultar(comando, ())
    nomes = ""
    for [idt, nome, telefone, data] in cs:
        nomes += "<TR>"
        nomes += "<TD>" + nome + "</TD>"
        nomes += "<TD>" "nascimento: " + str(data) + "</TD>"
        nomes += "<TD><BUTTON ONCLICK=\"jsExcluir('" + nome + " telefone:(" + telefone + ")" + "', " + str(idt) + ")\">Excluir" + "</BUTTON></TD>"
        nomes += "</TR>"
    cs.close()

    return render_template('parExcluir.html', nomes=nomes)

# rota para exclusão no banco de dados
@app.route('/excluir', methods=['POST'])
def excluir_curso():

    # Recuperando dados do formulário de parExcluir() utilizando idt
    idt = int(request.form['idt'])

    # Excluindo dados no SGBD
    mysql = sql.SQL("root", "", "test")
    comando = "DELETE FROM tb_curriculo WHERE idt=%s;"

    if mysql.executar(comando, [idt]):
        msg = "Curriculo excluído com sucesso!"
    else:
        msg = "Falha na exclusão do currículo..."

    return render_template('excluir.html', msg=msg)

app.run()