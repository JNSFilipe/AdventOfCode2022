def _remove_every_other_row(lines, even=False):
    new_lines = []
    for l in lines:
        nl = ''
        for i in range(len(l)):
            if not even:
                if i%2 != 0:
                    nl += l[i]
            else:
                if i%2 == 0:
                    nl += l[i]

        if not nl[0].isnumeric():
            new_lines.append(nl)

    return new_lines

def parse_input(file_path):
    data = None
    with open(file_path, 'r') as f:
        data = f.read()

    data = data.split('\n\n')

    ########### Parse initial piles
    lines = data[0].split('\n')
    
    # Remove brakets 
    lines = _remove_every_other_row(lines, False)
    # Remove spaces
    lines = _remove_every_other_row(lines, True)

    piles = {i+1:[] for i in range(len(lines[0]))}
    # Store in dictionary
    for l in lines:
        for i in range(len(l)):
            if l[i].isalpha():
                piles[i+1].append(l[i])

    ########### Parse instructions
    lines = data[1].split('\n')

    iset = []
    for l in lines:
        n = l.split(' ')
        iset.append((int(n[1]), int(n[3]), int(n[5])))

    return piles, iset

def update_pile_form_instruction(pile, instruction):
    transport = pile[instruction[1]][:instruction[0]]
    transport.reverse()
    del pile[instruction[1]][:instruction[0]]
    pile[instruction[2]] = transport + pile[instruction[2]]
    return pile

if __name__ == '__main__':

    p, iset = parse_input('./day5/input.txt')

    for i in iset:
        p = update_pile_form_instruction(p, i)

    top_crates = [p[k][0] for k in p.keys()]

    print(''.join(top_crates))
