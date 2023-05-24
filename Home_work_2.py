'''
n=int(input('Введите общее количество монеток -->'))
sum_orel=0
sum_resh=0
i=0
while i < n :
    a=int(input ('Введите 1, если орел или 0, если решка -->'))
    if a==1 :
        sum_orel=sum_orel+1
    else:
         sum_resh=sum_resh+1
    i+=1
if sum_resh>=sum_orel:
    print (f'{sum_orel} монеток нужно перевернуть')
else:
    print (f'{sum_resh} монеток нужно перевернуть')
    '''
'''
S=int(input('Введите cумму чисел -->'))
P=int(input('Введите  произведение чисел -->'))
for x in range (1000): 
    y=S-x
    if x*y==P and x<y and y<1000:
        print (f'это числа {x} и {y}')
'''
n=int(input (' Введите число  N-->'))
i=0
while 2**i<n:
    print (2**i)
    i+=1