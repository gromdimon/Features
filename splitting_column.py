split1 = employment.series_code.str.split(".", expand=True)
employment = pd.concat([employment, split1], axis=1)
