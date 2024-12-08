Mikel = int(input('Vvedite summu investicii Mikela: '))
Ivan = int(input('vvedite summu investicii Ivana: '))
min_summ = 1000
if (Mikel >= min_summ) and (Ivan >= min_summ ):
    print('2')
elif (Mikel >= min_summ) and (Ivan < min_summ):
    print('Mike')
elif (Mikel < min_summ) and (Ivan >= min_summ):
    print('Ivan')
elif ((Mikel + Ivan) >= min_summ):
    print('1')
else: 
    print('0')