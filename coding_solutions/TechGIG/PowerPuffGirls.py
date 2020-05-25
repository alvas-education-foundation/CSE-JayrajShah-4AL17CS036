

import numpy as np


def main():

    # Write code here
    N = int(input("Enter n"))
    req = list(map(int, input("enter req").split()))
    avai = list(map(int, input("Enter avai").split()))
    count = 0
    neg_count = len(list(filter(lambda x: (x < 0), avai)))

    while neg_count == 0 or avai.count(0) == 0:
        avai = list(np.array(avai) - np.array(req))
        neg_count = len(list(filter(lambda x: (x < 0), avai)))
        if neg_count == 0:
            count += 1
        else:
            break

    print(count)


main()
