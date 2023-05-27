print('GERADOR DE P.A')
print('-='*12)
t = int(input('Primeiro termo: '))
r = int(input('Razão da P.A: '))
termo = t
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print('{} - '.format(termo), end='')
        termo += r
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar á mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))