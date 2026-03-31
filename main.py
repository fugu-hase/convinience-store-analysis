import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from src.analysis import analy_sum, clean_data, save_csv, save_plot

INPUT_FILE = "data/smartdata.csv"
OUTPUT_CSV = "output/smartdata_out.csv"
OUTPUT_IMG = "output/sales_by_category.png"

def main():
    # フォント設定
    matplotlib.rcParams["font.family"] = "MS Gothic"

    # データ読み込み
    df = pd.read_csv(INPUT_FILE, encoding="cp932")

    # 前処理
    df = clean_data(df)

    # 分析
    result = analy_sum(df)

    # 出力
    save_csv(result, OUTPUT_CSV)
    save_plot(result, OUTPUT_IMG)

if __name__ == "__main__":
    main()