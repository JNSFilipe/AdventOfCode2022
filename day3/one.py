import string


def parse_input(file_path):
    data = None
    with open(file_path, 'r') as f:
        data = f.read()

    # print(repr(data))
    data = data.split('\n')
    data = [d.strip() for d in data]

    return data

def split_sack(data):
    split_data = []
    for d in data:
        l = int(len(d)/2)
        d1 = d[:l]
        d2 = d[l:]

        split_data.append((d1, d2))

    return split_data

def get_repeated_item(data):
    rep = []
    for d in data:
        for c in d[0]:
            if c in d[1]:
                rep.append(c)
                break

    return rep

def get_priority(data):
    priority_lookup = list(string.ascii_lowercase) + list(string.ascii_uppercase)
    priority_lookup = {priority_lookup[i]: i+1 for i in range(len(priority_lookup))}

    return [priority_lookup[d] for d in data]



if __name__ == '__main__':

    d = parse_input('./day3/input.txt')
    
    d = split_sack(d)

    d = get_repeated_item(d)

    d = get_priority(d)

    print(d)
    print()
    print(sum(d))