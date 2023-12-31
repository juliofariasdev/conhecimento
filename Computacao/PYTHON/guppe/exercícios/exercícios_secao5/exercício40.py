custo_base = float(input("Qual o custo de fábrica do carro novo: R$"))
custo_final =0
if custo_base<=12000:
    custo_final = custo_base*1.05
elif custo_base>12000 and custo_base<=25000:
    custo_final = custo_base*1.25
elif custo_base>25000:
    custo_final = custo_base*1.35
print(f'o custo ao comsumidor será de R${custo_final:.2f}')