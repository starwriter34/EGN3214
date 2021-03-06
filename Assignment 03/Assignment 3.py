'''
Chris Oakley
Present Value
08/31/2020
EGN3214 - Assignment 3

Variables:

cash - What you have
rate - Intreset Rate per period
nper - Number of compounding periods
pmt - Payment(Revenue Generated)
fv - Future value


np.pv() - Present Value
np.fv() - Future Value
'''

import numpy_financial as np

cash = [10000, 9000, 5000, 3000, 0]
pmt = [500, 600, 1000, 1200, 1500]
rate = 0.05
nper = 10
continue_yn='y'
question = 'ask'

def investmentGB(pv, fv):

    rv = fv+pv
       
    if (rv >= 0):
        investment = 'Good Investment'
    else:
        investment = 'Bad Investment'
        
    print()
    print(f'The Future Value:$ {fv:.2f}')
    print(f'The Present Value:$ {pv:.2f}')
    print(f'Return Value:$ {rv:.2f}')
    print()
    print(investment)
    print()
    print('*'*50)

while continue_yn=='y':

    if question == 'ask':
        question = input('Do you wish to (M)anually Calculate your PV & FV, or run the (A)ssignment Numbers (M or A)?').upper()

    if question == 'M':
        print()
        cash = float(input('Enter in the Original Price: '))
        rate = float(input("Enter in the Intreset Rate (i.e. 5% is 0.05): "))
        nper = float(input("Enter in the Number of Years: "))
        pmt = float(input("Enter in the Yearly Revenue: "))

        pv = np.pv(rate, nper, pmt, cash)
        fv = np.fv(rate, nper, pmt, pv)

        print('*'*50)
        print(f'Intial Investment:$ {cash}')
        print(f'Intrest Rate: {rate*100}%')
        print(f'Revenue:$ {pmt}')
        print(f'Number of Periods: {nper}')

        investmentGB(pv, fv)
        
        print()
        continue_yn = input('Do you wish to continue? (Y or N)').lower()
        print()

    elif question == 'A':
        
        for (i, j) in zip(cash, pmt):
            
            pv = np.pv(rate, nper, j, i)
            fv = np.fv(rate, nper, j , pv)

            print('*'*50)
            print(f'Intial Investment:$ {i}')
            print(f'Intrest Rate: {rate*100}%')
            print(f'Revenue:$ {j}')
            print(f'Number of Periods: {nper}')

            investmentGB(pv, fv)
        break

