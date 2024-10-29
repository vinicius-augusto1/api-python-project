import pandas as pd

def gerar_relatorio_vendas(file):
    df = pd.read_csv(file)

    # Agrupa os dados por cliente e empresa
    relatorio_cliente = df.groupby(['cliente', 'empresa']).agg(
        total_gasto=('valor', lambda x: (x * df['quantidade']).sum()),
        total_produtos=('produto', 'count')
    ).reset_index()

    # Detalhes dos produtos comprados por cliente
    produtos_por_cliente = df[['cliente', 'produto', 'quantidade', 'valor']]

    return relatorio_cliente, produtos_por_cliente
