from flask import Blueprint
from app.services.receitas.receitas_manage_csv import listar_receitas, buscar_receita

bp = Blueprint('receitas_route', __name__)

@bp.route('/receitas')
def lista_receitas():
    return {
        'data': listar_receitas()
    }

@bp.route('/receitas/<termo>')
def busca_receita(termo):
    return {
        'data': buscar_receita(termo)
    }