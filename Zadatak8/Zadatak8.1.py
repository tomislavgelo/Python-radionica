fh = open('zadatak_8.txt')
data = fh.read()
rows = data.split('\n')
i = 0
for row in rows:
    if '/' not in str(row):
        rows.pop(i)
    i += 1
division = []
for row in rows:
    division.append(row.split('/'))
results = []
j = 0
k = 1
for d in division:
    d1 = float(d[j])
    d2 = float(d[k])
    d3 = d1/d2
    results.append(d3)
max_result = max(results)
max_result_index = results.index(max_result)
print(max_result, '=', rows[max_result_index])