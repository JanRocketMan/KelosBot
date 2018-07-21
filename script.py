import pandas as pd

df = pd.read_csv('all_posts_with_eda.csv', encoding='utf-8')
df = df[df['category_name'] != 'Бренды']
df = df[df['category_name'] != 'Магазины']
df.to_csv('all_posts_with_eda.csv', encoding='utf-8', index=None)

