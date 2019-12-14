codigo_peca_1 = input()
numero_peca_1 = int(input())
valor_peca_1 = float(input())

codigo_peca_2 = input()
numero_peca_2 = int(input())
valor_peca_2 = float(input())

total_pagar = round((numero_peca_1 * valor_peca_1)+(numero_peca_2 * valor_peca_2), 2)

print('VALOR A PAGAR: R$', total_pagar)
