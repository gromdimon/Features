# That's a feature from Vlad Yashin

def check_missing_values(dataframe):
    if dataframe.isnull().sum().sum() > 0:
        m_total = dataframe.isnull().sum().sort_values(ascending=False)
        total = m_total[m_total > 0]

        m_percent = dataframe.isnull().mean().sort_values(ascending=False)
        percent = m_percent[m_percent > 0]

        missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])

        print(f'Total and Percentage of NaN:\n {missing_data}')
    else:
        print('No NaN found.')