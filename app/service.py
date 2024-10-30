import pandas as pd

def gerar_relatorio_vendas(file):
    df = pd.read_csv(file)

    relatorio_cliente = df.groupby(['cliente', 'empresa']).agg(
        total_gasto=('valor', lambda x: (x * df['quantidade']).sum()),
        total_produtos=('produto', 'count')
    ).reset_index()

    produtos_por_cliente = df[['cliente', 'produto', 'quantidade', 'valor']]

    return relatorio_cliente, produtos_por_cliente
