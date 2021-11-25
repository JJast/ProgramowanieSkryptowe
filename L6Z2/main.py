from random import randint
from itertools import product   # petla for w petli for:     ((x,y) for x in A for y in B)

od = randint(53, 63)
dlugosc = randint(2, 4)
do = randint(od+1, od + dlugosc + 1) #od+dlugosc
# od=56
# do=58
# dlugosc=2
print("od={}, do={}, dlugość={}".format(od, do, dlugosc))

listaZnakow = list(map(lambda x: chr(x), list(range(od, od+dlugosc+1))))
print("Lista znaków: " + str(listaZnakow))

listaKombinacji = [''.join(kombinacja) for kombinacja in product(listaZnakow, repeat=dlugosc)] # produkt zwraca tablice tablic opjedynczych charow
print("Lista kombinacji: " + str(list(listaKombinacji)))


def checkHowManyDigits(arg):
    if arg[0].isdigit():
        digitSum = sum(list(map(lambda x: 1 if x[0].isdigit() else 0, list(arg))))
        if digitSum < dlugosc:
            return True
    return False


przefiltrowane = filter(checkHowManyDigits, listaKombinacji)

print("Przefiltrowane: " + str(list(przefiltrowane)))