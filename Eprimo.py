n = int(input("Verificar numeros primos ate: "))
mult=0
while True:
    for count in range(2,n):
        if (n % count == 0):
            print(f"Múltiplo de {count}")
            mult += 1

    if(mult==0):
        print("É primo")
    else:
        print(f"Tem {mult} múltiplos acima de 2 e abaixo de {n}")
    mult=0

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar ? [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
    n = int(input("Verificar numeros primos ate: "))
