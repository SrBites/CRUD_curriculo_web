# READ ME
Trabalho de programação web quarta menção.\
opção(currículo)\
Diogo Bites Faria de Paula RA:22007351

# interpretador: python3.7

(pacote/versão:)

Flask	                  1.1.2\
Jinja2	                2.11.3\
MarkupSafe	            1.1.1\
Werkzeug	              1.0.1\
click	                  7.1.2\
et-xmlfile	            1.0.1\
graphics.py	            5.0.1.post1\
graphics.py-extra	      0.2.0\
itsdangerous	          1.1.0\
jdcal	                  1.4.1\
mysql-connector	        2.2.9\
mysql-connector-python	8.0.25\
pip	                    10.0.1\
protobuf	              3.17.0\
setuptools	            39.1.0\
six	                    1.16.0\
tp-python-docx	        0.8.5\
trianglesolver	        1.2\


observações:

-recomendado: utilização do pycharm e seus pacotes\
-Flask_/crud_curso.py é o MAIN\
-Flask_/criarcurriculo_sgbd.py cria uma tabel no SQL necessaria ao funcionamento além do schema em SQL\
-Caso seja necessario mudança de parametros relacionados a maquina local ou servidor como "login","password","host", eles podem ser modificados em "Flask_/base/sql.py" em suas -primeiras 3 linhas úteis.\
-static/bootstrap são pastas extras para modificações futuras, assim como certos pacotes importados\
-as tabelas e schemas necessarios são criadas automaticamente ao executar o codigo "criar_curriculo_sgbd.py"


