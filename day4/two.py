from one import parse_input, convert_to_range

def count_overlaps(data):
    pair_overlap = []
    for d1, d2 in data:
        c = 0
        for i in d1:
            if i in d2:
                c+=1
        pair_overlap.append(c)
    
    return pair_overlap

if __name__ == '__main__':

    d = parse_input('./day4/input.txt')

    d = convert_to_range(d)

    c = count_overlaps(d)

    print(c)
    print()
    c = [i for i in c if i>0]
    print(len(c))
 