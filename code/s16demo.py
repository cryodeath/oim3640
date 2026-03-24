import timeit
words = open('data/words.txt').read().split()
word_set = set(words)     # 113K+ words

def search_list():
    return 'python' in words
def search_set():
    return 'python' in word_set

print('List:', timeit.timeit(search_list, number=1000))
print('Set: ', timeit.timeit(search_set, number=1000))