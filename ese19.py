input1=input('inserire un numero tra 1 e 12:')
x=int(input1)

input2=input('inserire giorno:')
y=int(input2)
if x<1 or x > 12:
    print('numero inserito non valido:')
    
else:
    if x>=1 and x<=3:
        if x ==3 and y>20:
            print('Primavera')
        else:
            print('Inverno')
    elif x>=4 and x<=6:
        if x == 6 and y>21:
            print('Estate')
        else:
            print('Primavera')
    elif x>=7 and x<=9:
        if x==9 and y>23:
            print('Autunno')
        else:
            print('Estate')
    elif x>=10 and x<=12:
        if x==12 and y>20:
            print('Inverno')
        else:
            print('Autunno')
            
