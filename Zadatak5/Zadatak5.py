def preokret(string):

    li = list(string.split(' '))

    for i in range(1, len(li), 2):

        li[i] = li[i][::-1]

    obrnuti_string = ' '.join(li)

    return obrnuti_string

print(preokret('the quick brown fox jumps over the lazy dog'))