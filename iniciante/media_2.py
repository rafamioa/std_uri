A = -1
B = -1
C = -1
peso_A = 2
peso_B = 3
peso_C = 5

while A < 0 or A > 10:
    A = round(float(input()))
while B < 0 or B > 10:
    B = round(float(input()))
while C < 0 or C > 10:
    C = round(float(input()))

media = ((A * peso_A) + (B * peso_B) +(C * peso_C))/(peso_A + peso_B + peso_C)

print('MEDIA =', media)
     
