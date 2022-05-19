input1=input('inserire un numero tra 1 e 12:')
x=int(input1)

if x<1 or x > 12:
    print('numero inserito non valido:')
    
else:
    if x>=1 and x<=3:
        print('Inverno')
    elif x>=4 and x<=6:
        print('Primavera')
    elif x>=7 and x<=9:
        print('Estate')
    elif x>=10 and x<=12:
        print('Autunno')