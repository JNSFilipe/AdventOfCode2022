import numpy as np
from one import parse_input, get_priority

def aggregate_list_n_by_n(data, n=3):
    d = np.array(data)
    d = np.reshape(d, (-1, n)).tolist()
    return d 

def get_badges(data):
    badges = []
    for d in data:
        unique_chars = list(set(''.join(d)))
        for c in unique_chars:
            if (c in d[0]) and (c in d[1]) and (c in d[2]):
                badges.append(c)
                break
    return badges

if __name__ == '__main__':

    d = parse_input('./day3/input.txt')
    
    d = aggregate_list_n_by_n(d)

    d = get_badges(d)

    d = get_priority(d)

    print(d)
    print()
    print(sum(d))