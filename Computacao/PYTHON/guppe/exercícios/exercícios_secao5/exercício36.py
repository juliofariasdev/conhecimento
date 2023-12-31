venda_mensal = float(input('Venda mensal: R$'))
comissão = 0
if venda_mensal<20000:
    comissão = 400+ 0.14*venda_mensal
elif venda_mensal<40000 and venda_mensal>20000:
    comissão = 500 + 0.14*venda_mensal
elif venda_mensal<60000 and venda_mensal>40000:
    comissão = 550 + 0.14*venda_mensal
elif venda_mensal<80000 and venda_mensal<60000:
    comissão = 600 + 0.14*venda_mensal
elif venda_mensal<100000 and venda_mensal<80000:
    comissão = 600 + 0.14*venda_mensal
elif venda_mensal>100000:
    comissão = 700+ 0.16*venda_mensal
print(f'A sua comissão será de R${comissão:.2f}')