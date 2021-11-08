def calculate(num):

    lst = [int(i) for i in str(num)]

    zbroj = sum(lst)

    return zbroj

print(calculate(456))