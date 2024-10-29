from flask import Blueprint, request, jsonify
from .service import gerar_relatorio_vendas
from .utils import gerar_tabela_vendas

relatorio_vendas = Blueprint('relatorio_vendas', __name__)


@relatorio_vendas.route('/relatorio-vendas', methods=['POST'])
def relatorio():
    file = request.files['file']
    relatorio_cliente, produtos_por_cliente = gerar_relatorio_vendas(file)

    # Gera a tabela visual
    gerar_tabela_vendas(relatorio_cliente)

    resposta = {
        'relatorio_por_cliente': relatorio_cliente.to_dict(orient='records'),
        'produtos_por_cliente': produtos_por_cliente.to_dict(orient='records')
    }

    return jsonify(resposta)
