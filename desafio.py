# 1. Solicita o nome ao usuario
user = input('Digite seu nome\n')

# 2. Solicita salario
salario = float(input('Digite seu salario\n'))

# 3. Solicita bonus
bonus = float(input('Digite seu bonus\n'))

# 4. Calculo do bonus finalr
bonus_final = 1000 + bonus * salario

print(f' O usuario {user} considerando seu salario de {salario}, seu bonus final e: {bonus_final}')
