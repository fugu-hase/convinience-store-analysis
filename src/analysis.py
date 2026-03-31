import pandas as pd
import matplotlib.pyplot as plt

def clean_data(df):
    df["売上"] = pd.to_numeric(df["売上"], errors="coerce")
    df = df.dropna(subset=["売上"])
    df = df[df["売上"] < 10000]
    return df

def analy_sum(df):
    result = df.groupby("商品カテゴリ")["売上"].sum()
    return result

def save_csv(result, path):
    result.to_frame().to_csv(path, index=False, encoding="cp932")

def save_plot(result, path):
    result.plot(kind="bar")
    plt.title("カテゴリ別売上")
    plt.xlabel("商品カテゴリ")
    plt.ylabel("売上")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()