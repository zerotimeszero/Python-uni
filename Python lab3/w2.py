#1
'''
from statistics import mean
def sum_transitions(company, stat):
    new = list(map(lambda x: int(x.split(',')[2]),list(filter(lambda x: company in x,stat))))
    return [min(new),max(new),mean(new)]
ad_stats = [
    '2023-01-01,vk,43',
    '2023-01-01,fb,775',
    '2023-01-01,ya,64',
    '2023-01-02,vk,1164',
    '2023-01-02,fb,35',
    '2023-01-02,ya,254',
    '2023-01-02,ok,645',
    '2023-01-03,vk,7754',
    '2023-01-03,fb,654',
    '2023-01-03,ya,4625',
    '2023-01-03,ok,245',
]
company = input()
print(sum_transitions(company,ad_stats))
'''
#2
from Currency import Rate


curr = Rate('full')
print(curr.usd(True))
print(curr.get_currency_info('RSD'))