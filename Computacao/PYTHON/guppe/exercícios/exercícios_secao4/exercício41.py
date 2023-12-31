renda = float(input('Qual o valor da hora de trabalho: R$'))
horas_trabalhadas = int(input('Horas trabalhadas no mês: '))
salario = renda*horas_trabalhadas*1.1
print(f'O valor a ser pago ao funcionário é R${salario:.2f}')