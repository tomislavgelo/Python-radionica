import pandas as pd
from datetime import datetime

url = 'https://www.hnb.hr/statistika/glavni-makroekonomski-indikatori'
df = pd.read_html(url)[0]
today = datetime.now()
ddmmyy = today.strftime("%d-%m-%Y")
df.to_csv('HNB_[{0}].csv'.format(ddmmyy))