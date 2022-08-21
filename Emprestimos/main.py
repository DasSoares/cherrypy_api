import cherrypy

import main_config
import appLoans
import appDebtors


def validate_password(realm, username, password):
    if realm:
        pass
    elif username in main_config.users and main_config.users[username] == password:
        return True
    return False


if __name__ == '__main__':
    
    daemon = False
    
    conf = { '/': {
        'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
        # 'tools.auth_basic.on': True,
        # 'tools.auth_basic.realm': 'api-empresitmos',
        # 'tools.auth_basic.checkpassword': validate_password
    }}
    
    """_summary_
        Adicione seus apps aqui
    """
    cherrypy.tree.mount(appLoans.Loans(), '/emprestimos', conf)
    cherrypy.tree.mount(appDebtors.Debtors(), '/devedores', conf)

    
    cherrypy.engine.start()
    cherrypy.engine.block()
    