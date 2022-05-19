import math

input1=input('inserire primo numero:\t')
input2=input('inserire secondo numero:')
input3=input('inserire terzo numero:\t')

x=int(input1)
y=int(input2)
z=int(input3)

magg=int(x)
min=int(x)

if int(y)>magg:
    magg=int(y)
else:
    min = int(y)

if int(z)>magg:
    magg=int(z)
else:
    min = int(z)

print (magg)
print (min)

somma=int(x+y+z)
media =int(somma)/3

print(media)

if somma > 0:
    rad=math.sqrt(somma)
    print(rad)