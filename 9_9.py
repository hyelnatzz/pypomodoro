import random
import time
from pprint import pprint
row = []

col = {}

main_lst = []

while len(main_lst) < 5:
    while len(row) < 5:
        num = random.randint(1, 5)
        step = len(row) + 1
        if step not in col.keys():
            col[step] = []
        if num not in col[step] and num not in row:
            row.append(num)
            col[step].append(num)
    main_lst.append(row)
    row = []
    pprint(main_lst)

    pprint(col)
    time.sleep(3)

pprint(main_lst)

pprint(col)
