def parse_input(file_path):
    data = None
    with open(file_path, 'r') as f:
        data = f.read()

    return data

def get_marker_indices(data, marker_len=4):
    marker = [0]*len(data)

    i = 0
    while i+marker_len < len(data):
        header = data[i:i+marker_len]
        if len(header) == len(set(header)):
            marker[i] = 1
        i += 1
    
    indices = [i for i in range(len(marker)) if marker[i]==1]

    return indices


if __name__ == '__main__':

    d = parse_input('./day6/input.txt')

    idx = get_marker_indices(d)

    print(idx[0]+4)
