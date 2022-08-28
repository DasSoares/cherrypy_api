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
        self.inserir = InsertDebtor()
        self.update = UpdateDebetor()
        self.deletar = DeleteDebtor()


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


class InsertDebtor(object):
    """ Insere registro no banco de dados """
    exposed = True
    
    @cherrypy.tools.json_out()
    def POST(self):
        try:
            data = json.loads(cherrypy.request.body.read())
            response = DebtorsDB().insert(data.get('nome'), data.get('telefone'))

            if response:
                return { 'status': 'success', 'response': 'Dados inseridos com sucesso!' }
            else:
                return { 'status': 'error', 'response': 'Não foi possível inserir no banco!' }
        except  Exception as e:
            cherrypy.log("ERROR exception:", e)
            raise cherrypy.HTTPError(message=f"ERROR: {e}")


class UpdateDebetor(object):
    """ Altera os dados do registro """
    exposed = True
    
    @cherrypy.tools.json_out()
    def PUT(self):
        try:
            data = json.loads(cherrypy.request.body.read())
            response = DebtorsDB().update(data.get('id'), data.get('nome'), data.get('telefone'))
            if response:
                return { 'status': 'success', 'response': 'Dados alterados com sucesso!' }
            else:
                return {
                    'status': 'error', 
                    'response': 'Registro não encontrado ou não foi possível alterar os dados do registro. ' \
                        'Tente novamente mais tarde' 
                }
        except Exception as e:
            cherrypy.log("ERROR:", e)
            raise cherrypy.HTTPError(message=f"ERROR: {e}")


class DeleteDebtor(object):
    """ Remove registro do banco de dados """
    exposed = True
    
    @cherrypy.tools.json_out()
    def DELETE(self, id):
        try:
            response = DebtorsDB().delete(id)
            if response:
                return { 'status': 'success', 'response': 'Registro removido com sucesso!' }
            else:
                return { 'status': 'error', 'reponse': 'Erro ao excluir ou registro não encontrado' }
        except Exception as e:
            cherrypy.log("ERROR:", e)
            raise cherrypy.HTTPError(message=f"ERROR: {e}")
