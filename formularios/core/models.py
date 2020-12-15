from django.db import models
import pandas as pd


def xls_to_dict(docfile):
    
    frame = raw_dataset(docfile)    
    acoes = [{
        'acao': row['acao'],
        'objeto': row['objeto'],
        'quantidade': row['quantidade'],
        'valor': f"R$ {row['valor']}"
        } for index, row in frame.iterrows()]

    return {'acoes': acoes}

def raw_dataset(file):
    
    df = pd.read_csv(file)
    #df = df.parse("Planejamento")
    #df = df.iloc[7:]
    #df = df.iloc[:, :9]
    #df.columns = ['acao', 'objeto', 'quantidade', 'valor']
    #df = df.dropna(subset=['acao'])
    #df = df.where(pd.notnull(df), None)
    df = df.reset_index(drop=True)
    return df