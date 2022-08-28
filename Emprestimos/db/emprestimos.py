from datetime import datetime

from .connection import ConnectDB
from sqlalchemy import select, insert, update, delete
from .models import t_loans, t_debtors


class Loans(ConnectDB):
    
    def get_loan(self, id):
        query = select(t_loans).where(t_loans.c.id == id)
        response = self.execute(query).one_or_none()
        if response:
            result = {
                'id' : response[0],
                'data' : str(response[1]),
                'nome' : response[2],
                'descricao' : response[3],
                'tipo' : response[4],
                'dinpar' : response[5],
                'valor' : float(response[6]),
                'parcelas' : response[7],
                'created_at' : str(response[8]),
                'updated_at' : str(response[9])
            }
            return dict(result) if result else None
        return {}
    
    def list_loans(self, limit=None):
        query = select(t_loans)
        if limit:
            query = query.limit(limit)
        response = self.execute(query).all() # fetchall() - tanto faz
        
        result = list()
        for item in response:
            result.append({
                'id' : item[0],
                'data' : str(item[1]),
                'nome' : item[2],
                'descricao' : item[3],
                'tipo' : item[4],
                'dinpar' : item[5],
                'valor' : float(item[6]),
                'parcelas' : item[7],
                'created_at' : str(item[8]),
                'updated_at' : str(item[9])
            })        
        return result
    
    
    def insert(self, data=None, nome=None, descricao=None, tipo=None, dinpar=None, valor=None,
            parcelas=None):
        
        query = t_loans.insert().values(data = data, nome = nome, descricao = descricao, tipo = tipo, dinpar = dinpar, valor = valor,
            parcelas = parcelas, created_at = datetime.now())
        
        response = self.execute(query)
        if response.rowcount > 0:
            self.commit()
            return True
        return False
    
    
    def update(self, id, data=None, nome=None, descricao=None, 
               tipo=None, dinpar=None, valor=None, parcelas=None):
        
        query = t_loans.update()
        
        if data:
            query = query.values(data = data)
        if nome:
            query = query.values(nome = nome)
        if descricao:
            query = query.values(descricao = descricao)
        if tipo:
            query = query.values(tipo = tipo)
        if dinpar:
            query = query.values(dinpar = dinpar)
        if valor:
            query = query.values(valor = valor)
        if parcelas:
            query = query.values(parcelas = parcelas)
        
        query = query.values(updated_at = datetime.now())
        query = query.where(t_loans.c.id == id)
        response = self.execute(query)
        
        if response.rowcount > 0:
            self.commit()
            return True
        return False
    
    
    def delete(self, id):
        query = t_loans.delete().where(t_loans.c.id == id)
        response = self.execute(query)
        
        if response.rowcount > 0:
            self.commit()
            return True
        return False


class Debtors(ConnectDB):

    def get_debtor(self, id):
        query = select(t_debtors).where(t_debtors.c.id == id)
        response = self.execute(query).one_or_none()
        if response:
            result = {
                'id' : response[0],
                'nome' : response[1],
                'telefone' : response[2],
                'created_at' : str(response[3]),
                'updated_at' : str(response[4])
            }
            return dict(result) if result else None
        return {}

    def list_debtors(self, limit=None):
        query = select(t_debtors)
        if limit:
            query = query.limit(limit)
        response = self.execute(query).all()

        result = list()
        for item in response:
            result.append({
                'id' : item[0],
                'nome' : item[1],
                'telefone' : item[2],
                'created_at' : str(item[3]),
                'updated_at' : str(item[4])
            })
        return result
    
    def insert(self, nome=None, telefone=None):

        query = t_debtors.insert().values(
            nome = nome, telefone = telefone, created_at = datetime.now())

        response = self.execute(query)
        if response.rowcount > 0:
            self.commit()
            return True
        return False


    def update(self, id, nome=None, telefone=None):

        query = t_debtors.update()

        if nome:
            query = query.values(nome = nome)
        if telefone:
            query = query.values(telefone = telefone)

        query = query.values(updated_at = datetime.now())

        query = query.where(t_debtors.c.id == id)
        response = self.execute(query)

        if response.rowcount > 0:
            self.commit()
            return True
        return False

    def delete(self, id):
        query = t_debtors.delete().where(t_debtors.c.id == id)
        response = self.execute(query)

        if response.rowcount > 0:
            self.commit()
            return True
        return False
