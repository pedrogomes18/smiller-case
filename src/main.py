import pandas as pd
from datetime import datetime
from src.alocador import alocar_pedidos
from src.metricas import calcular_metricas

def main():
    df = pd.read_csv("data/input/dados.csv")

    aloc_df = alocar_pedidos(df)

    nome_arquivo = f"data/output/alocacao_otimizada_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    aloc_df.to_csv(nome_arquivo, index=False)

    print(f"\n✅ Alocação salva como '{nome_arquivo}'")
    calcular_metricas(aloc_df)

if __name__ == "__main__":
    main()
