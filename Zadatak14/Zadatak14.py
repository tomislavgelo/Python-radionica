import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

df = pd.DataFrame([33, 33, 33, 1], index=['Sugar', 'Spice', 'Everything Nice', 'Chemical X'], columns=['x'])
df.plot(kind='pie', subplots=True, figsize=(10, 10))

plt.savefig('plot.png')