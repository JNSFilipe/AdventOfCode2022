from one import parse_input

def update_pile_form_instruction(pile, instruction):
    transport = pile[instruction[1]][:instruction[0]]
    del pile[instruction[1]][:instruction[0]]
    pile[instruction[2]] = transport + pile[instruction[2]]
    return pile

if __name__ == '__main__':

    p, iset = parse_input('./day5/input.txt')

    for i in iset:
        p = update_pile_form_instruction(p, i)

    top_crates = [p[k][0] for k in p.keys()]

    print(''.join(top_crates))
