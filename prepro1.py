import pandas as pd
import numpy as np

# col_names = [ 'c{0:02d}'.format(i) for i in range(11) ]
# print("hello")

# gls_raw = pd.read_csv("data/gls.csv", sep="\t", names=col_names)

# print(gls_raw.head())

# print(gls_raw.isna().sum().T)

# new_df = pd.DataFrame()
# for i in range(len(gls_raw)):
#     #print("i:", len(gls_raw))
#     new_series = pd.Series()
#     gls_raw.iloc[i]
#     for j in range(len(gls_raw.iloc[i])):
#         target = gls_raw.iloc[i].iloc[j]
#         if (type(target) is not str) and (np.isnan(target)):
#             pass
#         else:
#             new_series = pd.Series([target])
#             # print(new_series)
#             new_df = new_df.append(new_series, ignore_index=True)
#         #print("j:", len(gls_raw.iloc[i]))
#         #pd.Series(gls_raw[i]


# print("------------------------info")
# print(new_df.info())
# print("------------------------desc")
# print(new_df.describe())
# print("------------------------size")
# print(new_df.size)
# print("------------------------head")
# print(new_df.head(200))
# print("------------------------unique")
# print(new_df.nunique())
# print("------------------------duplicated sum")
# print(new_df.duplicated().sum())

# new_df = new_df.drop_duplicates()
# new_df.to_csv("data/gls_flatten.csv")


