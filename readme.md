Pacotes para instalação 
pip install + comandos abaixo
autocommand==2.2.1
cheroot==8.6.0
CherryPy==18.8.0
greenlet==1.1.2
inflect==6.0.0
jaraco.classes==3.2.2
jaraco.collections==3.5.2
jaraco.context==4.1.2
jaraco.functools==3.5.1
jaraco.text==3.9.1
more-itertools==8.14.0
mysql-connector-python==8.0.30
portend==3.1.0
protobuf==3.20.1
pydantic==1.9.2
PyMySQL==1.0.2
pytz==2022.2.1
six==1.16.0
SQLAlchemy==1.4.40
tempora==5.0.2
typing_extensions==4.3.0
zc.lockfile==2.0


# Iniciando a API
python3 Emprestimos/main.py

### Rotas disponíveis

localhost:8080/emprestimos/get_emprestimos/1
localhost:8080/emprestimos/list_emprestimos - /10 -> limite de registros

localhost:8080/devedores/get_devedor/1
localhost:8080/devedores/list_devedores - /10 -> limite de registros