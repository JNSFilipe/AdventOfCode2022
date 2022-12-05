def parse_input(file_path):
    data = None
    with open(file_path, 'r') as f:
        data = f.read()

    # print(repr(data))
    data = data.split('\n\n')
    data = [d.strip() for d in data]

    i = 0
    parsed_data = {}
    for chunk in data:
        parsed_data[i] = list(map(int, chunk.split('\n')))
        i+=1

    return parsed_data


def get_max_sum(dict_list):
    return max([sum(dict_list[l]) for l in dict_list.keys()])

if __name__ == '__main__':

    cal_list = parse_input('./day1/input.txt')

    m = get_max_sum(cal_list)
    
    print(m)