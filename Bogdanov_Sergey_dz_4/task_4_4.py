import utils


result_value = utils.currency_rates_adv('EURII')[0]
print(result_value)
result_value = utils.currency_rates_adv('USD')[0]
print(result_value)
result_value = utils.currency_rates_adv('JPY')[0]
print(result_value)

"""
PS C:\...\Bogdanov_Sergey_dz_4> python task_4_4.py
85.378
74.802
0.648
"""

print('end')