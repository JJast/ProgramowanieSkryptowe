'''
#!/usr/bin/python3

import itertools

listOfNumbers = list(itertools.chain.from_iterable(list(map(lambda x: open(x).read().split(), input().split()))))
test = list(filter(lambda num: int(num) % 2 == 0, listOfNumbers))
print(test)


print(list(filter(lambda num: int(num) % 2 == 0, itertools.chain.from_iterable(list(map(lambda x: open(x).read().split(), input().split())))))) # WYSWIETLA LISTE PARZYSTYCH
'''

import sys;import itertools;print(len(list(filter(lambda num: int(num) % 2 == 0, itertools.chain.from_iterable(list(map(lambda x: open(x).read().split(), sys.argv[1:])))))))