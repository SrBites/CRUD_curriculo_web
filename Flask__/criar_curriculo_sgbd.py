from base import sql

# criar_curso.py

mysql = sql.SQL("root", '', "test")

comando = "DROP TABLE IF EXISTS tb_curriculo;"

if mysql.executar(comando, ()):
    print("Tabela de currículos excluída com sucesso!")

comando = "CREATE TABLE tb_curriculo (idt INT AUTO_INCREMENT PRIMARY KEY, " + \
         "nome VARCHAR(55) NOT NULL, " + \
          "data DATE NOT NULL, " + \
          "telefone VARCHAR(20) NOT NULL, " + \
         "descricao VARCHAR(150) NOT NULL, " + \
         "locadouro VARCHAR(100) NOT NULL, " + \
         "salario INT(55) NOT NULL); "

if mysql.executar(comando, []):
    print("Tabela de currículo criada com sucesso!")
