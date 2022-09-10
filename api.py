import pandas as pd
fd = input('モンスターを入力:')
url = 'https://appmedia.jp/monst/73713'
kfs = pd.read_html(url, match=fd)
print(kfs[0].head())

