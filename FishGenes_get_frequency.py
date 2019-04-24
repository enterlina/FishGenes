import pandas as pd

dataframe = pd.read_csv('/Users/alena_paliakova/Google Drive/!Bioinf_drive/00_FishPr/02_Fishgenes_work/Fishgenes.csv')
replace_array = []

for i in range(dataframe.shape[0]):
    for j in range(2, dataframe.shape[1]):
        if (dataframe.iloc[i][j] != '-') and (dataframe.iloc[i][j] != 'nan') and (dataframe.iloc[i][j] != ' ') and (
                dataframe.iloc[i][j] != '}\\') and (dataframe.iloc[i][j] != '\\}') and (
                dataframe.iloc[i][j]) not in replace_array:
            replace_array.append(dataframe.iloc[i][j])

df_replace_array = pd.DataFrame()

df_replace_array = pd.DataFrame(data=None, columns=dataframe.columns)

df_replace_array = df_replace_array.drop(columns=['deepwater', 'shallowater'], axis=1)

df_replace_array.insert(0, 'replace', replace_array)

dataframe = dataframe.drop(['shallowater'], axis=1)
# print(df_replace_array.iloc[1][0])
# print(dataframe.shape[1])
# print(df_replace_array)
# print(df_replace_array.shape[0])
counter = 0

for j in range(1, dataframe.shape[1]):
    for k in range(df_replace_array.shape[0]):
        for i in range(dataframe.shape[0]):
            # print('df_replace_array.iloc[k][0]',df_replace_array.iloc[k][0],'k',k)
            # print('dataframe.iloc[i][j]',dataframe.iloc[i][j],'i',i,'j',j)
            if dataframe.iloc[i][j] != '-' and df_replace_array.iloc[k][0] == dataframe.iloc[i][j]:
                counter += 1
                # print('df_replace_array.iloc[k][0]',df_replace_array.iloc[k][0])
                # print('dataframe.iloc[i][j]',dataframe.iloc[i][j])
                # print('counter ', counter)
        df_replace_array.loc[k][j] = counter
        counter = 0
print(df_replace_array)

df_replace_array.to_csv(
    '/Users/alena_paliakova/Google Drive/!Bioinf_drive/00_FishPr/02_Fishgenes_work/Fishgenes_replace.csv', index=False)
