import matplotlib.pyplot as plt

def gerar_tabela_vendas(relatorio_cliente):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.axis('off')
    ax.axis('tight')

    tabela = ax.table(cellText=relatorio_cliente.values, colLabels=relatorio_cliente.columns, loc='center', cellLoc='center')
    tabela.auto_set_font_size(False)
    tabela.set_fontsize(12)
    tabela.scale(1.2, 1.2)

    plt.show()
