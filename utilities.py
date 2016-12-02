
import os                   # for file- and path-related stuff
import readline, glob       # for autocompletion capabilities
from molecule import *      # import molecule object


def get_parameters():
    molecule = get_xyz()        # parse the molecule from an xyz file
    # TODO: detect symmetry and align molecule
    charge = get_charge()       # get the net charge of the system
    spin = get_spin()           # get get the spin multiplicity
    return (molecule, charge, spin)


# TODO: maybe add counter for mistaken path, after 3 times abort
def get_xyz():
    readline.set_completer_delims(' \t\n;')
    readline.parse_and_bind("tab: complete")
    readline.set_completer(path_completer)
    while True:
        filename = input('\tEnter the geometry file (.xyz): ')
        if not os.path.isfile(filename):
            tprint('The file does not exist!')
            continue
        elif not filename.endswith('.xyz'):
            tprint('The geometry is expected to be in .xyz format!')
            continue
        else:
            break

    file = open(filename, 'r')  # open xyz file
    lines = list(file)			# read file line by line

    # Check that the first line contains only the number of atoms in the molecule
    if len(lines[0].split()) != 1:
        tprint('The xyz file should containt only the number of atoms in the first line!')
        get_xyz()

    n_atoms = int(lines[0])		# saving the number of atoms
    atoms = []					# list of atoms
    xyz = []					# list of cartesian coordaintes
    for i in range(2, n_atoms + 2):   # looping over the atoms
        splitted_line = lines[i].split()
        atoms.append(splitted_line[0])
        xyz.append(list(map(float, splitted_line[1:4])))

    mol_name = input('\tEnter a short descriptive name for the molecule (max 4 characters): ')
    return Molecule(atoms, xyz, n_atoms, mol_name)


def get_charge():
    while True:
        charge = input('\n\tEnter the net charge of the system: ')
        if is_int(charge):
            return int(charge)
        else:
            tprint('The charge must be an integer number!')
            continue


def get_spin():
    while True:
        spin = input('\n\tEnter the spin multiplicity: ')
        if is_int(spin):
            if int(float(spin)) > 0:
                return int(float(spin))
            else:
                tprint('The spin multiplicity must be at least 1!')
                continue

        else:
            tprint('The spin multiplicity must be an integer number!')
            continue


def methods_completer(text, state):
    methods = ['rhf', 'uhf', 'mp2', 'ccsd(t)', 'casscf']
    # fill in the cache by partial completion if text is not empty
    if text:
        cache = [s for s in methods if s and s.startswith(text)]
    else:
        cache = methods

    return (cache + [None])[state]


def path_completer(text, state):
    paths = glob.glob(text + '*')
    # add '/' symbol to directories for better readability
    for i in range(len(paths)):
        if os.path.isdir(paths[i]):
            paths[i] += '/'

    return (paths + [None])[state]


# Add one tab before printing
def tprint(text):
    print('\t' + text)
    return


# Check that input is an integer
def is_int(x):
    try:
        a = float(x)
        b = int(a)
    except ValueError:
        return False
    else:
        return a == b
