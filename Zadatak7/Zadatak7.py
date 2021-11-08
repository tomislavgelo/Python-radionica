fh = open('zadatak_7.csv')
data = fh.read()
rows = data.split('\n')
i = len(rows)
j = 0
lst = []
while j < i:
    lst += [rows[j].split(',')]
    j += 1
calc = 0
k = 1
while k < i:
    calc += float(lst[k][1])
    k += 1
a_mid = calc / (i - 1)
a_mid_format = "{:.2f}".format(a_mid)
fh.close()
print(a_mid_format)