

while True:
    input1 = input('Inserire un numero intero:')
    valore_OK=True
    try:
        x=int(input1)
    except ValueError:
        print(input1 + ' non è un intero')
        valore_OK=False
            if valore_OK:
                break
            




i =0
if x > 0:
    while i < x:
        print('*', end='')
        i= i + 1
else:
    print('numero inserito minore di 0')