import pandas as pd

df = pd.read_excel('pop2022.xlsx')
df = pd.DataFrame
html = df.to_html()

print(html)