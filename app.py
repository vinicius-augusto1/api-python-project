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

    return jsonify(relatorio_cliente.to_dict(orient='records'))