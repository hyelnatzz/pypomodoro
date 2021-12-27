words = ['alaba', 'alibi', 'acaba', 'hjjhghg']

find = '**a*a'

pos = {i:find[i] for i in [j for j in range(len(find)) if find[j] != '*']}
print(pos)
found =[]
for i in words:
    num_found = 0
    for j in pos.keys():
        if pos[j] == find[j]:
            num_found += 1
    if num_found == len(pos):
        found.append(i)
    num_found = 0


print(found)