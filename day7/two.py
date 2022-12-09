from one import parse_input, create_folder_structure, Folder

if __name__ == '__main__':

    total_disk_space = 70000000
    update_space = 30000000

    d = parse_input('./day7/input.txt')

    r = create_folder_structure(d)

    space_needed = update_space - (total_disk_space - r.get_size())

    smallest_folder_size = total_disk_space 
    folders = [r]
    for f in folders:
        # Starting form top dir, iteratively increments list of folders with childs 
        folders.extend(f.childs.values())

        current_size = f.get_size()
        if current_size >= space_needed and current_size < smallest_folder_size:
            smallest_folder_size = current_size

    print(smallest_folder_size)
