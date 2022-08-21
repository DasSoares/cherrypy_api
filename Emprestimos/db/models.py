# coding: utf-8
from operator import index
from sqlalchemy import CHAR, Column, DECIMAL, Date, DateTime, Float, ForeignKey, Index, MetaData, String, TIMESTAMP, Table, Text, Time, text
from sqlalchemy.dialects.mysql import BIGINT, BIT, CHAR, DATETIME, DECIMAL, INTEGER, LONGTEXT, TINYINT, VARCHAR, BINARY
metadata = MetaData()

""" Tabelas do banco de dados """

t_loans = Table(
    'loans', metadata,
    Column('id', INTEGER(11), primary_key=True, comment='Chave primaria da tabela'),
    Column('data', Date, nullable=False, comment='Data do emprestimo feito para a pessoa'),
    Column('nome', String(255), nullable=False, comment='Nome da pessoa que pediu dinheiro, cartão emprestado e etc'),
    Column('descricao', String(255), nullable=True, comment='Descreva o ocorrido do emprestimo'),
    Column('tipo', INTEGER(11), nullable=False, comment='Tipo do emprestimo'),
    Column('dinpar', TINYINT(1), nullable=False, comment='Parcelado Sim(1) ou Não(0)'),
    Column('valor', Float(asdecimal=True), nullable=False, comment='Valor total do emprestimo'),
    Column('parcelas', INTEGER(11), nullable=False, comment='Quantidade de parcelas'),
    Column('created_at', DateTime, nullable=True, comment='Data de criação'),
    Column('updated_at', DateTime, nullable=True, comment='Data de alteração'),
    comment='Tabela de emprestimos'
)

t_debtors = Table(
    'debtors', metadata,
    Column('id', INTEGER(11), primary_key=True, comment='Chave primaria da tabela'),
    Column('nome', String(255), nullable=False, comment='Nome da pessoa'),
    Column('telefone', String(255), nullable=True, comment='Telefone para contato'),
    Column('created_at', DateTime, nullable=True, comment='Data de criação'),
    Column('updated_at', DateTime, nullable=True, comment='Data de alteração'),
    comment='Tabela de devedores'
)

t_receipts = Table(
    'receipts', metadata,
    Column('id', INTEGER(11), primary_key=True, comment='Chave primaria da tabela'),
    Column('idemp', INTEGER(11), ForeignKey('loans.id'), nullable=False, index=True, comment='Chave estrangeira de loans.id'),
    Column('data', Date, nullable=False, comment='Data da parcela'),
    Column('datapag', Date, nullable=False, comment='Data que a parcela foi paga'),
    Column('numparcela', INTEGER(11), nullable=True, comment='Número da parcela 1, 2 ou 3...'),
    Column('valorparcela', Float(asdecimal=True), nullable=False, comment='Valor total do emprestimo'),
    Column('pago', TINYINT(1), nullable=False, comment='Parcelado Sim(1) ou Não(0)'),
    Column('valorpago', Float(asdecimal=True), nullable=False, comment='Valor que o  devedor lhe pagou'),
    Column('pagador', String(255), nullable=True, comment='Descrição, coloque o que quiser'),
    Column('created_at', DateTime, nullable=True, comment='Data de criação'),
    Column('updated_at', DateTime, nullable=True, comment='Data de alteração'),
    comment='Tabela das parcelas do emprestimos'
)

t_users = Table(
    'users', metadata,
    Column('id', INTEGER(11), primary_key=True, comment='Chave primaria da tabela'),
    Column('nome', String(255), nullable=False, comment='Nome do usuário'),
    Column('email', String(255), nullable=True, comment='e-mail do usuário'),
    Column('email_verified_at', DateTime, nullable=True, comment='Data de verificação de e-mail'),
    Column('password', String(255), nullable=False, comment='Senha do usuário'),
    Column('remember_token', String(255), nullable=True, comment='Relembrar token'),
    Column('created_at', DateTime, nullable=True, comment='Data de criação'),
    Column('updated_at', DateTime, nullable=True, comment='Data de alteração'),
    comment='Tabela de autenticação de usuários do sistema'
)
