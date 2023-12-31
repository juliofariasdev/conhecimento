basemaior = float(input("Qual a base maior do trapézio, em metro: "))
basemenor = float(input("Qual a base menor do seu trapézio, em metro: "))
altura = float(input("Qual a altura do seu trapézio: "))
if (basemenor<=0) or (basemaior<=0) or (altura<=0):
    print(f'Isso não é um trapézio!')
else:
    print(f'A área desse trapézio é {(basemenor+basemaior)*altura/2}')