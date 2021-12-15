df[''].dtype

def memory_use(df):
    mem_us = df['passenger_count'].memory_usage(index=False, deep=True)
    max_value = df['passenger_count'].max()
    min_value = df['passenger_count'].min()
    print(f'Memory used: {mem_us}.\n The maximum value for the column is {max_value}.\n The minimum value for the column is {min_value}.)

df['passenger_count'] = df['passenger_count'].astype('int8')
df['passenger_count'].memory_usage(index=False, deep=True)
          
df = pd.read_csv('file.csv', dtype={'column A': 'category'},
                                   {'column B': 'int8'},
                                   {'column C': 'float16'})
