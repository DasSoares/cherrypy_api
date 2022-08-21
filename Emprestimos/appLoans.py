import json
import cherrypy
from db.emprestimos import Loans as LoansDB


class Loans(object):
    exposed = True
    
    def __init__(self):
        """ Nome das rotas
            -----
            exemplo: localhost:8080/emprestimos/get_emprestimos/1
        """
        self.get_emprestimos = GetLoans()
        self.list_empresitmos = LoansList()
        

"""
    atenção, o retorno dos dados deve ser setados com os tipos definidos no modelo
    exemplo> no banco tem o campo chamado 'valor' e o resultado era 300.00000000
    converti para float e funcionou, isso vale para os tipos primitivos de datas também
"""


class GetLoans(object):
    """ Retorna o registro do id selecionado """
    exposed = True
    
    @cherrypy.tools.json_out()
    def GET(self, id):
        try:
            loans = LoansDB().get_loan(id)
            if loans:
                return { 'status': 'found', 'data': loans }
            else:
                return { 'status': 'not found', 'data': None }
        except Exception as e:
            cherrypy.log("ERROR:", e)
            raise cherrypy.HTTPError(message=f"ERROR: {e}")


class LoansList(object):
    exposed = True
    
    @cherrypy.tools.json_out()
    def GET(self, limit=0):
        try:
            loans = LoansDB().list_loans(limit)
            if loans:
                return { 'status': 'found', 'data': loans }
            else:
                return { 'status': 'not found', 'data': None }
        except Exception as e:
            cherrypy.log("ERROR:", e)
            raise cherrypy.HTTPError(message=f"ERROR: {e}")
