import pandas as pd

# Cycle
for idx,row in anime[:2].iterrows():
    print(idx, row)
    
# List of values
anime['genre'].tolist()

# Only current values
anime[anime['type'].isin(['TV', 'Movie'])]
anime[anime['rating'] > 8]

# Sorting
anime.sort_values('rating', ascending=False)

# Creating DataFrame
table = pd.DataFrame({'Bob': [1, 2, 'HOI'], 'Nika': [2, 1, 'LOI'], },
                     index=['Number of projects', 'Number of friends ', 'Logo'])
df = pd.DataFrame([[1,'Bob', 'Builder'],
                  [2,'Sally', 'Baker'],
                  [3,'Scott', 'Candle Stick Maker']], 
                  columns=['id','name', 'occupation'])

data = pd.DataFrame({'num': [i for i in range(1, 11)], 'lit': [j for j in 'abcdefghqr'],
                     'state': ['YES' if k % 2 == 0 else 'FALSE' for k in range(10)]},
                    index=['first', 'seq', 'dtrit', 'a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'b', 'bb'])

# Features with frame
print(data.loc[['a', 'aa', 'b'], ['num']])
print(data.iloc[:5, [0, 1]])
print(data[data.state == 'FALSE'])
print(data.loc[(data.num >= 3) | (data.state == 'YES')])
print(data.loc[(data.num * -1 ).idxmax(), 'lit'])
print(data.lit.map(lambda x: 'a' in x).sum())

frut = reviews.description.map(lambda desc: 'fruity' in desc).sum()
trop = reviews.description.map(lambda desc: 'tropical' in desc).sum()
descriptor_counts = pd.Series([trop, frut], index = ['tropical', 'fruity'])

def f(x):
    if x > 95:
        return 3
    elif 85 <= x <= 95:
        return 2
    else:
        return 1

list = reviews.points.apply(f)
star_ratings = pd.Series(list)
reviews.apply(f, axis='columns')

print(data.groupby('state').num.agg([min]))
price_extremes = reviews.groupby('variety')['price'].agg([min,max])
sorted_varieties = reviews.groupby('variety').price.agg([min, max]).sort_values(by=['min', 'max'], ascending=False)
powerlifting_combined = powerlifting_meets.set_index('MeetID').join(powerlifting_competitors.set_index('MeetID'))
