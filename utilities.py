
import readline
from autocompletion import *

def get_program():
    programs_completer = ListCompleter(QC_programs)
    readline.set_completer(programs_completer.complete)
    readline.parse_and_bind('tab: complete')

    while True:
        program = input('\n\tEnter the QC program you want to use: ')
        if program in QC_programs:
            return program
        else:
            tprint('You need to enter one of the following (supported) programs:')
            for prog in QC_programs:
                tprint(prog)
            continue


def get_geometry():
    readline.set_completer_delims(' \t\n;')
    readline.parse_and_bind("tab: complete")
    readline.set_completer(path_completer)
    while True:
        filename = input('\n\tEnter the geometry file (.xyz): ')
        if not os.path.isfile(filename):
            tprint('The file does not exist!')
            continue
        elif not filename.endswith('.xyz'):
            tprint('The geometry is expected to be in .xyz format!')
            continue
        else:
            break

    file = open(filename, 'r')  # open xyz file
    lines = list(file)          # read file line by line

    # Check that the first line contains only the number of atoms in the molecule
    if len(lines[0].split()) != 1:
        tprint('The xyz file should containt only the number of atoms in the first line!')
        get_geometry()

    return filename


def get_symmetry():
    while True:
        symmetry = input('\n\tDo you want to use symmetry [Yes]? ')
        if symmetry == 'Yes' or 'yes' or 'YES' or 'y' or 'Y':
            return True
        elif symmetry == 'No' or 'no' or 'NO' or 'n' or 'N':
            return False
        else:
            tprint('Not a valid answer!')
            continue


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


def get_basis_set(QC_program):
    basis_set_completer = ListCompleter(basis_sets_list[QC_program])
    readline.set_completer(basis_set_completer.complete)
    readline.parse_and_bind('tab: complete')

    while True:
        basis_set = input('\n\tEnter the basis set: ')
        if basis_set in basis_sets_list[QC_program]:
            return basis_set
        else:
            tprint('You need to enter one of the available basis sets:')
            for _basis_set in basis_sets_list[QC_program]:
                tprint(_basis_set)
            continue


def get_method(QC_program):
    method_completer = ListCompleter(methods_list[QC_program])
    readline.set_completer(method_completer.complete)
    readline.parse_and_bind('tab: complete')

    while True:
        method = input('\n\tEnter the method: ')
        if method in methods_list[QC_program]:
            return method
        else:
            tprint('You need to enter one of the available methods:')
            for _method in methods_list[QC_program]:
                tprint(_method)
            continue


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


# Temporary database TODO: to move
QC_programs = ['MOLPRO 2015.1', 'Gaussian09', 'MOLCAS 8.1', 'Psi4', 'ORCA']
basis_sets_list = {'MOLPRO 2015.1':['STO-3G','3-21G','6-31G'],
                   'Gaussian09':['STO-3G','3-21G','6-31G'],
                   'MOLCAS 8.1':['STO-3G','3-21G','6-31G'],
                   'Psi4':['STO-3G','3-21G','6-31G'],
                   'ORCA':['STO-3G','3-21G','6-31G']
                   }
methods_list = {'MOLPRO 2015.1':['RHF','ROHF','CASSCF'],
                'Gaussian09':['RHF','ROHF','RDFT'],
                'MOLCAS 8.1':['DMRG-CI','DMRG-SCF','CASPT2'],
                'Psi4':['RHF','ROHF','RDFT'],
                'ORCA':['RHF','ROHF','RDFT']
                }


# def get_xyz():
#     readline.set_completer_delims(' \t\n;')
#     readline.parse_and_bind("tab: complete")
#     readline.set_completer(path_completer)
#     while True:
#         filename = input('\tEnter the geometry file (.xyz): ')
#         if not os.path.isfile(filename):
#             tprint('The file does not exist!')
#             continue
#         elif not filename.endswith('.xyz'):
#             tprint('The geometry is expected to be in .xyz format!')
#             continue
#         else:
#             break
#
#     file = open(filename, 'r')  # open xyz file
#     lines = list(file)          # read file line by line
#
#     # Check that the first line contains only the number of atoms in the molecule
#     if len(lines[0].split()) != 1:
#         tprint('The xyz file should containt only the number of atoms in the first line!')
#         get_xyz()
#
#     n_atoms = int(lines[0])     # saving the number of atoms
#     atoms = []                  # list of atoms
#     xyz = []                    # list of cartesian coordaintes
#     for i in range(2, n_atoms + 2):   # looping over the atoms
#         splitted_line = lines[i].split()
#         atoms.append(splitted_line[0])
#         xyz.append(list(map(float, splitted_line[1:4])))
#
#     mol_name = input('\tEnter a short descriptive name for the molecule (max 4 characters): ')
#     return Molecule(atoms, xyz, n_atoms, mol_name)
