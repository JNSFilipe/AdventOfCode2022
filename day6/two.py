from one import parse_input, get_marker_indices

if __name__ == '__main__':

    d = parse_input('./day6/input.txt')

    idx = get_marker_indices(d, marker_len=14)

    print(idx[0]+14)
