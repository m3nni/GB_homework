"""
Работет из терминала
"""

import sys

import utils


result_value = utils.currency_rates_adv('EUR')[0]
#print(result_value)
result_value = utils.currency_rates_adv('USD')[0]
#print(result_value)
result_value = utils.currency_rates_adv('JPY')[0]
#print(result_value)


if __name__ == '__main__':
    argv = sys.argv[1]
    kurs = list(utils.currency_rates_adv(argv))
    print(kurs[0], kurs[1])

"""
PS C:\...\Bogdanov_Sergey_dz_4> python task_4_5.py USD
74.802 2022-02-09
"""

print('end')