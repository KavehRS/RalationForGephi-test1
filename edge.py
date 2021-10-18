# -*- coding: utf-8 -*-
"""

"""

import pandas as pd

df = pd.read_excel(r'C:\Users\Kaveh\Documents\direct-cast\edge.xlsx')

df['ids2'] = df['ids2'].fillna(0)
df['Target'] = df['Target'].fillna(0)
df['ids2'] = df['ids2'].astype(int)
df['ids1'] = df['ids1'].astype(int)
df['source'] = df['source'].astype(int)
df['Target'] = df['Target'].astype(int)
df_new = pd.DataFrame()
for i in range(0, len(df)):   # len(df)
    print(i)
    df_sample = pd.DataFrame()
    k = 0
    df_sample.loc[k, 'source'] = df.loc[i, 'source']
    for j in range(0, len(df)):
        if df.loc[i, 'ids1'] == df.loc[j, 'ids2']:
            df_sample.loc[k, 'Target'] = df.loc[j, 'Target']
            k = k + 1
  #  print(df_sample)
    df_new = df_new.append([df_sample])

df_new['source'].fillna(method='ffill', inplace=True)
            
df_new.to_excel('df_new.xlsx', index=False)

