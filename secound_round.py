classificacao = 0

telefone = input("Telefonou para a Vítima ? (s/n) ")
if telefone == 's' or telefone == 'S':
    classificacao += 1
    print(classificacao)

local = input("Esteve no Local do Crime ? (s/n) ")
if local == 's' or local == 'S':
    classificacao += 1
    print(classificacao)

morada = input("Mora perto da vitima ? (s/n) ")
if morada == 's' or morada == 'S':
    classificacao += 1
    print(classificacao)

money = input("Devia a vitima ? (s/n) ")
if money == 's' or money == 'S':
    classificacao += 1
    print(classificacao)

work = input("Já trabalhou com a vitima ? (s/n) ")
if work == 's' or work == 'S':
    classificacao += 1
    print(classificacao)

if classificacao < 1:
    print('Você é inocente.')
elif classificacao == 2:
    print('Vocé é suspeito.')
elif classificacao > 2 and classificacao < 5:
    print('Você é Cumplice.')
else: 
    print('Você é o ASSASSINO.')

#nao alterar variaveis.


