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
    division.append(eval(row))
highest_value = max(division)
highest_value_index = division.index(highest_value)
best_pair = rows[highest_value_index]
fh.close()
print(best_pair, '=', highest_value)