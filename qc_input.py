#!/usr/bin/python

import os		# For file- and path-related stuff
import utilities
import readline

print('\n\t\tHello! Welcome to the Quantum Chemistry input generation program!\n')


def get_parameters():
    molecule = get_xyz()  # parse the molecule from an xyz file
    # TODO: detect symmetry and align molecule
    charge = get_charge()  # get the net charge of the system
    spin = get_spin()		# get get the spin multiplicity
    return (molecule, charge, spin)


# TODO: maybe add counter for mistaken path, after 3 times abort
def get_xyz():
    readline.set_completer_delims(' \t\n;')
    readline.parse_and_bind("tab: complete")
    readline.set_completer(utilities.path_completer)
    #filename = input('\tEnter the geometry file (.xyz): ')
    while True:
        # TODO: add autocompletion with TAB
        filename = input('\tEnter the geometry file (.xyz): ')
        # TODO: maybe need a check of relative/absolute paths
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

    # Check that the first line contains only the number of atoms in the
    # molecule
    if len(lines[0].split()) != 1:
        tprint('The xyz file should containt only the number of atoms in the first line!')
        get_geometry()

    atoms_num = int(lines[0])		# saving the number of atoms
    molecule = []						# Initialize molecule datastructure
    for i in range(2, atoms_num + 2):  # looping over the atoms
        splitted_line = lines[i].split()
        molecule.append([splitted_line[0], list(
            map(float, splitted_line[1:4]))])

    return molecule


def get_charge():
    while True:
        charge = input('\n\tEnter the net charge of the system: ')
        if is_int(charge):
            return int(charge)
        else:
            continue


def get_spin():
    while True:
        spin = input('\n\tEnter the spin multiplicity: ')
        if is_int(spin):
            if int(float(spin)) > 0:
                return int(float(spin))
            else:
                continue

        else:
            continue


# Add one tab before printing #
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
