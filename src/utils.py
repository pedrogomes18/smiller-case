import pandas as pd

def contar_placas(col):
    return col.astype(str).apply(
        lambda x: len(x.split(';')) if pd.notna(x) and x.lower() != 'nan' else 0
    )
