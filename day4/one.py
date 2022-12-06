def parse_input(file_path):
    data = None
    with open(file_path, 'r') as f:
        data = f.read()

    # print(repr(data))
    data = data.split('\n')
    data = [d.strip() for d in data]

    return data

def convert_to_range(data):
    ranges = []
    for d in data:
        r1, r2 = d.split(',')

        r1 = list(map(int, r1.split('-')))
        r2 = list(map(int, r2.split('-')))

        r1 = list(range(r1[0], r1[1]+1))
        r2 = list(range(r2[0], r2[1]+1))

        ranges.append((r1, r2))

    return ranges

def count_fully_contained(data):
    c = 0
    for d1, d2 in data:
        l1 = d1[0]
        r1 = d1[-1]
        l2 = d2[0]
        r2 = d2[-1]
        
        if (l1 >= l2 and r1 <= r2) or (l2 >= l1 and r2 <= r1):
            c+=1
    
    return c

if __name__ == '__main__':

    d = parse_input('./day4/input.txt')

    d = convert_to_range(d)

    c = count_fully_contained(d)

    print(c)
 