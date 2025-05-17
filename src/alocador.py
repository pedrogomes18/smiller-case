import pandas as pd
from pandas.tseries.offsets import BDay
from datetime import datetime
from src.utils import contar_placas

CAPACIDADE_DIARIA = 325

def alocar_pedidos(df):
    df["quantidade"] = contar_placas(df["sup"]) + contar_placas(df["inf"])
    df["data_pedido"] = pd.to_datetime(df["data_pedido"])
    df["data_limite"] = pd.to_datetime(df["data_limite"])
    df["cliente_premium"] = df["cliente_premium"].astype(bool)

    df["prioridade"] = (
        (df["data_limite"] - df["data_pedido"]).dt.days +
        (~df["cliente_premium"]).astype(int) * 10000
    )
    df = df.sort_values(by="prioridade").reset_index(drop=True)

    data_inicio = df["data_pedido"].min()
    data_fim = df["data_limite"].max()
    dias_uteis = pd.bdate_range(start=data_inicio, end=data_fim)

    capacidade_por_dia = {}
    alocacoes = []
    alocados = set()
    datas_travadas = set()

    for dia_atual in dias_uteis:
        dias_para_bloquear = pd.bdate_range(dia_atual, dia_atual + BDay(2))
        datas_travadas.update(dias_para_bloquear)

        pedidos_ativos = df[
            (df["data_pedido"] < dia_atual) & (~df["id_pedido"].isin(alocados))
        ]

        for _, row in pedidos_ativos.iterrows():
            pedido_id = row["id_pedido"]
            cliente_id = row["id_cliente"]
            qtd_total = row["quantidade"]
            data_limite = row["data_limite"]
            data_pedido = row["data_pedido"]
            vip = row["cliente_premium"]
            dia_aloc = dia_atual

            while qtd_total > 0:
                if dia_aloc in datas_travadas:
                    dia_aloc += BDay(1)
                    continue

                capacidade_disponivel = capacidade_por_dia.get(dia_aloc, 0)
                if capacidade_disponivel < CAPACIDADE_DIARIA:
                    qtd_lote = min(qtd_total, CAPACIDADE_DIARIA - capacidade_disponivel)

                    alocacoes.append({
                        "id_pedido": pedido_id,
                        "id_cliente": cliente_id,
                        "quantidade_alocada": qtd_lote,
                        "data_alocada": dia_aloc,
                        "cliente_premium": vip,
                        "data_limite": data_limite,
                        "data_pedido": data_pedido
                    })

                    capacidade_por_dia[dia_aloc] = capacidade_disponivel + qtd_lote
                    qtd_total -= qtd_lote

                dia_aloc += BDay(1)

            alocados.add(pedido_id)

    aloc_df = pd.DataFrame(alocacoes)
    return aloc_df.sort_values(by=["data_alocada", "id_cliente"]).reset_index(drop=True)
