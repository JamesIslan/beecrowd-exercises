produto1 = list(map(lambda x: float(x), input().split()))
produto2 = list(map(lambda x: float(x), input().split()) )
valor_total = (produto1[1] * produto1[2]) + (produto2[1] * produto2[2])
print(f'VALOR A PAGAR: R$ {valor_total:.2f}')