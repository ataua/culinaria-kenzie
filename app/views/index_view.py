from flask import Blueprint
 
bp = Blueprint('index_route', '__name__')
 

@bp.route('/')
def home():
    return {'status': 'OK'}