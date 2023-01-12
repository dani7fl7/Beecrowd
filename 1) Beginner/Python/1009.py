nome = input()
salario = float(input())
totalvendas = float(input())

totalrecebido = (salario + (totalvendas * 0.15))

print("TOTAL = R$ %.2f" %totalrecebido)
