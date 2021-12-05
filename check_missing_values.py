def check_missing_values_and_duplicates(dataframe):
    if dataframe.isnull().sum().sum() > 0 or dataframe.isnull().sum().sum() > 0:
        m_total = dataframe.isnull().sum().sort_values(ascending=False)
        total = m_total[m_total > 0]

        m_percent = dataframe.isnull().mean().sort_values(ascending=False)
        percent = m_percent[m_percent > 0]

        m_duplicates = dataframe.duplicated().sort_values(ascending=False)
        duplicates = m_duplicates[m_duplicates > 0]

        missing_data = pd.concat([total, percent, duplicates], axis=1, keys=['Total', 'Percent', 'Duplicates'])

        print(f'Total and Percentage of NaN & Duplicates:\n {missing_data}')
    else:
        print('No NaN or Duplicate found.')
