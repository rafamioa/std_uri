A = -1
B = -1
peso_A = 3.5
peso_B = 7.5

while A < 0 or A > 10:
    A = round(float(input()), 1)

while B < 0 or B > 10:
    B = round(float(input()), 1)

media = round(((A * peso_A) + (B * peso_B))/ (peso_A + peso_B), 5)

print('MEDIA =', media)
    
