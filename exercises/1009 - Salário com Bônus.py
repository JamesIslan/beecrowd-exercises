nome = str(input()).capitalize()
salario_inicial = float(input())
vendas = float(input())
salario_final = salario_inicial + (0.15 * vendas)
print(f'TOTAL = R$ {salario_final:.2f}')