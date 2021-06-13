
import pandas as pd

states = pd.read_csv('./States.csv')

pd.set_option('precision', 3)

states.columns = ['State', 'Region', 'Population', 'SATV', 'SATM', 'Percent', 'Dollars', 'Pay']


# reflect the actual population by multiplying 1000
states.Population = states['Population'] * 1000
# reflect actual thousands spent on each student
states.Dollars = states['Dollars'] * 1000
print(states[ ['State', 'Population', 'Dollars'] ], '\n') 

print(states.describe(), '\n')

histogram = states.hist()
