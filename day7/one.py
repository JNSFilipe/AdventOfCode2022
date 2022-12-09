class Folder:
    def __init__(self, name='', size=0, parent=None):
        self.name = name
        self.size = size
        self.parent = parent
        self.childs = {}

    def get_size(self):
        size = self.size
        for c in self.childs.values():
            size += c.get_size()
        return size


def parse_input(file_path):
    data = None
    with open(file_path, 'r') as f:
        data = f.read()

    # print(repr(data))
    data = data.split('\n')
    data = [d.strip() for d in data]

    return data

def create_folder_structure(data):
    root = Folder('/')
    cwd = root
    for line in data:
        d = line.split(' ')

        match (d[0], d[1]):
            case ('$', 'ls'):
                pass
            case ('$', 'cd'):
                match d[2]:
                    case '/':
                        cwd = root
                    case '..':
                        cwd = cwd.parent
                    case child:
                        cwd = cwd.childs[child]
            case ('dir', subdir):
                cwd.childs[subdir] = (Folder(name=subdir, size=0, parent=cwd))
            case (size, _):
                cwd.size += int(size)
    return root

if __name__ == '__main__':

    d = parse_input('./day7/input.txt')

    r = create_folder_structure(d)

    total = 0
    folders = [r]
    for f in folders:
        # Starting form top dir, iteratively increments list of folders with childs 
        folders.extend(f.childs.values())

        current_size = f.get_size()
        if current_size <= 100000:
            total += current_size

    print(total)
