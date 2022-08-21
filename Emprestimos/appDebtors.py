import json
import cherrypy
from db.emprestimos import Debtors as DebtorsDB


class Debtors(object):
    exposed = True
    
    def __init__(self):
        """ Nome das rotas
            -----
            exemplo: localhost:8080/devedores/get_devedor/1
        """
        self.get_devedor = GetDebtors()
        self.list_devedores = DebtorList()


class GetDebtors(object):
    """ Retorna o registro do id selecionado """
    exposed = True
    
    @cherrypy.tools.json_out()
    def GET(self, id):
        try:
            debtors = DebtorsDB().get_debtor(id)
            if debtors:
                return { 'status': 'found', 'data': debtors }
            else:
                return { 'status': 'not found', 'data': None }
        except Exception as e:
            cherrypy.log("ERROR:", e)
            raise cherrypy.HTTPError(message=f"ERROR: {e}")


class DebtorList(object):
    """ Retorna um json dos registros """
    exposed = True
    
    @cherrypy.tools.json_out()
    def GET(self, limit=0):
        try:
            debtors = DebtorsDB().list_debtors(limit)
            if debtors:
                return { 'status': 'found', 'data': debtors }
            else:
                return { 'status': 'not found', 'data': None }
        except Exception as e:
            cherrypy.log("ERROR:", e)
            raise cherrypy.HTTPError(message=f"ERROR: {e}")
