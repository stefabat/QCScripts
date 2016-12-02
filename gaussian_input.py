#!/usr/bin/python

# TODO: add everywhere defaults and exceptions checks

# TODO: automatic creation of title based on input
title = input('\n\tEnter the title of your calculation: ')

# TODO: add TAB autocompletion for files
geo_filename = input('\n\tEnter the geometry file (.xyz): ')
geo_file = open(geo_filename, 'r')
geo_lines = list(geo_file)

# TODO: check that there are no white spaces
system_name = input('\n\tEnter a short acronym for the system name: ')

# TODO: make it less implicit: r -> restricted, ro -> restricted open-shell, ...
calc_type = input('\n\tWhich type of calculations do you want to run (r,ro,u)? ')

# print('\n\tWhich functional do you want to use?\n\tAvailable functionals:\n\tb3lyp\n\tpbe\n\tpw91\n\tm06l\n\twb97xd\n\tbhandh\n\tlc-wpbe\n\tcam-b3lyp\n')
functional = input('\n\tFunctional: ')

method = calc_type + functional
route = '#P ' + method + '/'

# print('\n\tWhich basis set do you want to use?\n\tAvailable basis set:\n\tsto-3g\n\t3-21g\n\t6-31g\n\t6-311g')
basis_set = input('\n\tBasis set: ')
route += basis_set + ' integral=ultrafine cachesize=131072 gfinput '

charge = input('\n\tWhat is the net charge of the system? ')
spin = input('\n\tWhat is the spin multiplicity of the system? ')

# systemName_method_basis_spin.com
input_filename = '%s_%s_%s_mult%s' % (system_name, method, basis_set, spin)

_optg = input('\n\tDo you want to optimize the geometry?[No] ')
_freq = input('\n\tDo you want to run a frequency calculation?[No] ')
_pop = input('\n\tDo you want to print out all orbitals?[No] ')

if _pop == 'y' or _pop == 'Y' or _pop == 'yes' or _pop == 'Yes':
    route += 'pop=full '
else:
    route += 'pop=regular '

if _optg == 'y' or _optg == 'Y' or _optg == 'yes' or _optg == 'Yes':
    route += 'opt '
    input_filename += '_optg'

if _freq == 'y' or _freq == 'Y' or _freq == 'yes' or _freq == 'Yes':
    route += 'freq '
    input_filename += '_freq'

input_filename += '.com'

_mem = input('\n\tHow much memory do you want to use (in Gb)? ')
_cpus = input('\n\tHow many processors do you want to use? ')

mem = '%%NProcShared=%s' % _cpus
cpus = '%%Mem=%sGb' % _mem

input_file = open(input_filename, 'w')
input_file.writelines([mem, '\n', cpus, '\n', route, '\n\n', title, '\n\n', ' ' + charge + ' ' + spin, '\n'])

# TODO: strip blank lines at the end of xyz
for i in range(2, len(geo_lines)):
    input_file.write(geo_lines[i])

input_file.write('\n\n\n')
input_file.close()

print('\n\tInput generated!\n')
