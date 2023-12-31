import datetime
ano_atual = datetime.date.today().year
salario = 2000*(1+0.015*2**(ano_atual-1996))
print(f'O salário atual do funcionário é R${salario:.2f}')