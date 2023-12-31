valor = int(input('Qual o valor do saque: R$'))
nt100 = valor//100
nt50 = (valor%100)//50
nt20 = (valor%50)//20
nt10 = ((valor%50)%20)//10
nt5 = (valor%10)//5
nt2 = (valor%5)//2
nt1 = ((valor%5)%2)//1
print(f'''Serão utilizadas um total de {nt1+nt2+nt5+nt10+nt20+nt50+nt100} notas
{nt100} de 100
{nt50} de 50
{nt20} de 20
{nt10} de 10
{nt5} de 5
{nt2} de 2 
{nt1} moeda de 1 real''')
