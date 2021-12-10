# Applying lower_case_style
df_1.columns = [i.replace(' ', '_').lower() for i in df_1.columns] 
df_1.head(3)
