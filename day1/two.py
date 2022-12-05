from one import parse_input

def get_top_n_sum(dict_list, n=3):

    sums = [sum(dict_list[l]) for l in dict_list.keys()]
    sums.sort(reverse=True)
    top = sums[0:n]

    return top

if __name__ == '__main__':

    cal_list = parse_input('./day1/input.txt')

    m = get_top_n_sum(cal_list)
    
    print(sum(m))
