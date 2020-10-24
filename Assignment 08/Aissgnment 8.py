import pandas as pd
import numpy as np
from pandas.io.sql import table_exists

url=r'https://thermo.pressbooks.com/chapter/saturation-properties-temperature-table/'

t_table = pd.read_html(url, header=1)
t_table = t_table[0]

cols = t_table.columns
t_table = t_table.rename({'°C': 'degC'}, axis=1)
t_table = t_table.drop(columns=['vg', 'ug', 'hfg', 'hg', 'sfg', 'sg'])

continue_yn ='y'

while continue_yn=='y':
    temp = float(input('Enter a temperature from 0.01 to 373.95: '))
    t_table = t_table
    if temp < 0.01 or temp > 373.95:
        print(f'The temperature is not valid {temp}.')
        print(f'Enter a valid value 0.01 to 373.95')

    else:
        if temp in t_table.degC.values:
            t_table_temp = t_table[t_table['degC']==temp]
            print(t_table_temp)
            continue_yn = input('Do you wish to continue? Y or N ').lower()
        else:
            t_table_ap = t_table

            # t_table_ap = t_table_ap.sort_values('degC')
            # t_table_ap = t_table_ap.reset_index(drop=True)

            table_columns = list(t_table_ap.columns)
            degC_list = t_table_ap['degC'].to_list()
            inter_values = []
            for value in table_columns:
                column_list = t_table_ap[value].to_list()
                inter = np.interp(temp,degC_list,column_list)
                inter_values.append(inter)
            t_table_ap = t_table_ap[t_table_ap['degC']==temp]

            print(inter_values)
            # print(t_table_ap)
            continue_yn = input('Do you wish to continue? Y or N ').lower()