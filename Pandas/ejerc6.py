import pandas as pd

ingredientes = pd.Series(
['4 cups', '1 cup', '2 large', '1 can'],
index=['Flour', 'Milk', 'Eggs', 'Spam'], name='Diner')
print(ingredientes)
