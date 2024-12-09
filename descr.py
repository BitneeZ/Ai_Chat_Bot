import pandas as pd
df = pd.read_csv('labeled.csv')
print(df)
for index, row in df.iterrows():
    # print(row)
    # if row['toxic'] == 1.0:
    #     print(row['comment']+'@Toxic')
    # else:
    #     print(row['comment'], '@Neutral')

# df['toxic'] = df['toxic'].replace(1.0, "@Toxic")
# df['toxic'] = df['toxic'].replace(0.0, "@Neutral")
# print(df)
# df['toxic'] = df['toxic'] + "@Toxic"
#
# print(df)

#df.to_csv('toxic4.csv', encoding='utf-8', index=False)










