from crypt import methods

import pandas as pd
from flask import Flask, request, jsonify
import pandas
import matplotlib.pyplot as plt

app = Flask(__name__)


@app.route('/relatorio-vendas', methods=['POST'])
def relatorio_vendas():
    file = request.files['file']

    df = pd.read_csv(file)

    relatorio_cliente = df.groupby(['cliente', 'empresa']).agg(
        total_gasto = ('valor', lambda x: (x * df['quantidade']).sum()),
        total_produtos=('produto', 'count')
    ).reset_index()

    produtos_por_cliente = df[['cliente', 'produto', 'quantidade', 'valor']]

    resposta = {
        'relatorio_por_cliente' : relatorio_cliente.dict(orient='records'),
        'produtos_por_cliente' : produtos_por_cliente.dict(orient='records')
    }

    return jsonify(resposta)