def calcular_metricas(aloc_df):
    print("\n📊 MÉTRICAS DO DESAFIO (alinhadas ao PDF):")

    # 1️⃣ Atraso médio (dias)
    aloc_df["atraso_dias"] = (aloc_df["data_alocada"] - aloc_df["data_limite"]).dt.days
    atrasos = aloc_df[aloc_df["atraso_dias"] > 0]["atraso_dias"]
    atraso_medio = atrasos.mean() if not atrasos.empty else 0
    print(f"\n1️⃣ Atraso médio (dias): {atraso_medio:.2f}")

    # 2️⃣ Média de pedidos agrupados por cliente/dia
    agrupamento = aloc_df.groupby(["data_alocada", "id_cliente"])["id_pedido"].nunique()
    media_agrupamento = agrupamento.mean()
    print(f"2️⃣ Média de pedidos agrupados por cliente/dia: {media_agrupamento:.2f}")

    # 3️⃣ Antecipação média VIPs (dias antes do prazo acordado)
    primeiros_lotes = aloc_df.drop_duplicates(subset=["id_pedido"])
    antecipacao_vip = primeiros_lotes[primeiros_lotes["cliente_premium"]].copy()
    antecipacao_vip["antecipacao_real"] = (
        antecipacao_vip["data_limite"] - antecipacao_vip["data_alocada"]
    ).dt.days
    antecipacao_media = antecipacao_vip["antecipacao_real"].mean() if not antecipacao_vip.empty else 0
    print(f"3️⃣ Antecipação média VIPs (dias antes do prazo acordado): {antecipacao_media:.2f}")
