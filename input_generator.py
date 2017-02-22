
from utilities import *

def input_generator():
    qc_input = {}       # Initialize dictionary
    qc_input['program']  = get_program()
    qc_input['geometry'] = get_geometry()
    qc_input['symmetry'] = get_symmetry()
    qc_input['charge']   = get_charge()
    qc_input['spin']     = get_spin()
    qc_input['basis']    = get_basis_set(qc_input['program'])
    qc_input['method']   = get_method(qc_input['program'])
    qc_input['title']    = get_title()

    # Autogeneration of title
    # $mol_$method_$basis_S$spin
    qc_input['filename'] = qc_input['title']  + '_' + ...
                           qc_input['method'] + '_' + ...
                           qc_input['basis']  + '_' + ...
                           'S' str(qc_input['spin'])

    tprint('\n\nSummary of the input:\n')
    for p, v in qc_input.items():
        tprint(str(p) + ' : ' + str(v))

    # Based on the method, call the correct generator
    if qc_input['program'] == 'MOLPRO':
        molpro_generator(qc_input)
    elif qc_input['program'] == 'Gaussian':
        gaussian_generator(qc_input)
    else:
        tprint('The generator for this program has not been implemented yet!')


    tprint('\n\tInput generated!')
