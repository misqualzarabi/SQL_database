import pandas as pd
buddy = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/00476/buddymove_holidayiq.csv')
print(buddy.head())
print(buddy.shape)
print(buddy.isnull().sum())

