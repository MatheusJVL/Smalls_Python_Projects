from sys import exit
origin_cpf = input('Digite seu cpf: ')

#calculation of the first digit of the CPF:

if '.' in origin_cpf or '-' in origin_cpf: 
    cpf_only_number = origin_cpf\
        .replace('-','')\
        .replace('.','')\
        .replace(' ','')
else:
    cpf_only_number = origin_cpf

if len(cpf_only_number) < 9 or len(cpf_only_number) > 11:
    print('CPF inválido')
    exit()

cpf_only_number_9digits = cpf_only_number[:9]

acumulador = 0

try:
    for p,c in enumerate(cpf_only_number_9digits):
        acumulador += int(c) * (10-p)
except ValueError:
    print('CPF inválido')
    exit()

acumulador = (acumulador*10) % 11

if acumulador > 9:
    resultado_1_digit = '0'
else:
    resultado_1_digit = str(acumulador)

#calculation of the second digit of the CPF

cpf_only_number_9digits_plus_1 = cpf_only_number_9digits + resultado_1_digit

acumulador2 = 0

for p,c in enumerate(cpf_only_number_9digits_plus_1):
    acumulador2 += int(c) * (11-p)

acumulador2 = (acumulador2 * 10) % 11 

if acumulador2 > 9:
    resultado_2_digit = '0'
else:
    resultado_2_digit = str(acumulador2)

if cpf_only_number == len(cpf_only_number) * cpf_only_number[0]:
    print('CPF inválido')
    exit()

new_cpf = cpf_only_number_9digits + resultado_1_digit + resultado_2_digit

if new_cpf == cpf_only_number:
    print('CPF válido')
else:
    print('CPF inválido')