df_labels = list(df_visual.columns)
plt.figure(figsize=(15,15))
k=1
for var in df_labels:
   #plotting boxplot for each variable
   plt.subplot(round(len(df_labels),0)/3+3,4,k)
   plt.boxplot(df_visual[var],whis=5)
   plt.title(var)
   k+=1
   plt.tight_layout()
plt.show()
