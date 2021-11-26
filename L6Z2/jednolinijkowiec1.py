'''
import sys
from collections import Counter

wordsLength = list(map(lambda x: len(x), sys.stdin.read().split()))
wordsCount = Counter(wordsLength)
print(dict(wordsCount))
'''

import sys; from collections import Counter; print(dict(Counter(list(map(lambda x: len(x), sys.stdin.read().split())))))
