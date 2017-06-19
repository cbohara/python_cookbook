#!/usr/local/bin/python3
from collections import Counter

# determine the most frequent occuring item in a sequence
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

# super easy!
word_count = Counter(words)
top_three = word_count.most_common(3)
print(top_three)

# can also combine and subtract counts 
more_words = ['why','are','you','not','looking','in','my','eyes']
more_words_count = Counter(more_words)

print(word_count)
print(more_words_count)

# combine counts
combo = word_count + more_words_count
print(combo)
difference = word_count - more_words_count
print(difference)
