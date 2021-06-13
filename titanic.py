
import pandas as pd


titanic = pd.read_csv('./TitanicSurvival.csv')
pd.set_option('precision', 2)

titanic.columns = ['name', 'survived', 'sex', 'age', 'class']
print(titanic.head(), '\n')
print(titanic.tail(), '\n')

#titanic.describe()

print((titanic.survived == 'yes').describe())

histogram = titanic.hist()

