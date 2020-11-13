import pandas as pd
import numpy as np

url=r'https://thermo.pressbooks.com/chapter/saturation-properties-temperature-table/'
t_table = pd.read_html(url, header=1)
t_table = t_table[0]

cols = t_table.columns
t_table = t_table.rename({'°C': 'degC'}, axis=1)
t_table = t_table.drop(columns=['vg', 'ug', 'hfg', 'hg', 'sfg', 'sg'])

temp = float(input('Enter a temperature from 0.01 to 373.95: '))
continue_yn = 'y'

while continue_yn=='y':
    t_table = t_table

    temp = float(input('Enter a temperature from 0.01 to 373.95: '))
    if temp < 0.01 or temp > 373.95:
        print(f'The temperature is not valid {temp}.')
        print(f'Enter a valid value 0.01 to 373.95')

else:
    if temp in t_table.degC.values:
        t_table_temp = t_table[t_table['degC']==temp]
        print(t_table_temp)
    else:
        t_table_ap = t_table
        table_columns = list(t_table_ap.columns)
        degC_list = t_table_ap['degC'].to_list()

        inter_values = []
        t_tablenew = t_table

        for value in table_columns:

            column_list = t_table_ap[value].to_list()
            inter = np.interp(temp,degC_list,column_list)
            inter_values.append(inter)
        
        t_tablenew.loc[99] = inter_values
        t_tablenew = t_tablenew.sort_values('degC')
        t_tablenew = t_tablenew.reset_index(drop=True)
        t_tablenew = t_tablenew[t_tablenew['degC']==temp]

        print(t_tablenew)