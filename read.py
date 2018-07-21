word2index = {}

with open('word_indices.txt', 'r', encoding='utf-8') as fout:
    for line in fout:
        word2index[line.split()[0]] = line.split()[1]

WORD2VEC = np.load('word2vec100.npy')
