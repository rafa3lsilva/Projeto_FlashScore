import pandas as pd
from tinydb import TinyDB


colecao_partidas1 = TinyDB("db/base_flashscore_temp_atual.json")
df = pd.DataFrame(colecao_partidas1.all())

df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
df = df.sort_values(["Date", "Time"], ascending=True)
flt = df["Season"] == "2020/2021", "2022/2023", "2023/2024","2024/2025"
df = df[flt]

df = df.dropna()
df = df.reset_index(drop=True)
df.index += 1


df.to_csv('base_excel/base_.csv',index=False)