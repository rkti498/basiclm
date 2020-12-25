import pandas as pd

# gls = pd.read_csv("data/gls_flatten.csv", names=["wrong_index", "word"])
# print(gls.head(30))
# print(gls["word"].str.contains(",").sum())

# 手で直して、gls_flatten1.csvを作成。

# gls_flatten1.csvを読み込み、誤って付与されたインデクスを除去
# gls1 = pd.read_csv("data/gls_flatten1.csv", names=["wrong_index", "word"])
# print(gls1.shape)
# gls1 = gls1.drop("wrong_index", axis=1)
# print(gls1.head(50))
# gls1.to_csv("data/gls_flatten2.csv", index=False)

# flatten2.csvはword、0というレコードから始まっていたのでその２行は手で削除した

# gls = pd.read_csv("data/gls_flatten2.csv", header=None)
# print("-----------------desc")
# print(gls.describe())
# ef = pd.read_csv("data/ef.csv", header=None)
# print("-----------------desc")
# print(ef.describe())

# con_df = pd.concat([gls, ef])

# print("-----------------shape")
# print(con_df.shape)
# print("-----------------head")
# print(con_df.head(20))
# print("-----------------desc")
# print(con_df.describe())

# con_df = con_df.drop_duplicates()
# print("-----------------shape")
# print(con_df.shape)
# print("-----------------desc")
# print(con_df.describe())

# con_df.to_csv("data/concat_data.csv", index=False)
# 最初のレコードの0と、最後の空白レコードを消した。


# memo
# 数字単語one, two, three,...はあるけど、数字がない1, 2, 3...
# plusがあるのにminusがない
