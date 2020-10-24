import pandas as pd
import numpy as np
from pandas.io.sql import table_exists

url=r'https://thermo.pressbooks.com/chapter/saturation-properties-temperature-table/'

t_table = pd.read_html(url, header=1)
t_table = t_table[0]

cols = t_table.columns
t_table = t_table.rename({'°C': 'degC'}, axis=1)
t_table = t_table.drop(columns=['vg', 'MPa', 'ug', 'hfg', 'hg', 'sfg', 'sg'])
temp = float(input('Enter a temperature from 0.01 to 373.95: '))

continue_yn ='y'

while continue_yn=='y':

    temp = float(input('Enter a temperature from 0.01 to 373.95: '))

    if temp < 0.01 or temp > 373.95:
        print(f'The temperature is not valid {temp}.')
        print(f'Enter a valid value 0.01 to 373.95')

    else:
        if temp in t_table.degC.values:
            t_table = t_table[t_table['degC']==temp]
            print(t_table)
            continue_yn = input('Do you wish to continue? Y or N ').lower()
        else:
            t_table = t_table.append({'degC': temp}, ignore_index=True)
            t_table = t_table.sort_values('degC')
            t_table = t_table.reset_index(drop=True)
            t_table = t_table.interpolate(method='pchip')

            t_table = t_table[t_table['degC']==temp]

            print(t_table)
            continue_yn = input('Do you wish to continue? Y or N ').lower()