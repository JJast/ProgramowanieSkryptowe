'''
import sys
from collections import Counter

wordsLength = list(map(lambda x: len(x), sys.stdin.read().split()))
#wordsCount = map(lambda x: (x, wordsLength.count(x)), wordsLength)
wordsCount = Counter(wordsLength)
print(dict(wordsCount))
'''

import sys; from collections import Counter; print(dict(Counter(list(map(lambda x: len(x), sys.stdin.read().split())))))