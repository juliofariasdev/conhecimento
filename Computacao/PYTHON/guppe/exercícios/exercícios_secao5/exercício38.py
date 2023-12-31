print('Data de nascimento:')
dia = int(input('dia '))
mes = int(input('mes '))
ano = int(input('ano '))
res = False
if ano%4 ==0 or ano%400==0 and ano%100!=0:
    if mes in [1,3,5,7,8,10,12] and dia<32:
        res = True
    elif mes in [4,6,9,11] and dia<31:
        res = True
    if mes ==2 and dia<=29:
        res = True
else:
    if mes in [1,3,5,7,8,10,12] and dia<32:
        res = True
    elif mes in [4,6,9,11] and dia<31:
        res = True
    elif mes ==2 and dia<29:
        res =True
if res == True:
    print('Essa data é válida')
    print(f'Você tem {2023-ano} anos')
else:
    print('Essa data é inválida')