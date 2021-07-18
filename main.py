preco = float(input('Digite o valor do produto:'))
p = float(input('Digite percentual de desconto (0-100)%:'))

desconto = preco * (p / 100)
final = preco - desconto

print('o preco do produto será {}. Desconto  de {}%.'.format(preco, p))
print(' valor calculado de desconto: {}. Valor final do produto:{}'.format(desconto,final))
