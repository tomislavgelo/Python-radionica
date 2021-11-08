fh = open('zadatak_7.csv')

data = fh.read()

rows = data.split('\n')

i = len(rows)

j = 0

lst = []

while j < i:

    lst += [rows[j].split(',')]

    j += 1

lst.pop(0)

calc = 0

for items in lst:

    calc += float(items[1])

k = len(lst)

a_mid = calc / k

a_mid_format = "{:.2f}".format(a_mid)

fh.close()

print(a_mid_format)