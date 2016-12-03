
from utilities import *

def input_generator():
    qc_input = {}       # Initialize dictionary
    qc_input['program']   = get_program()
    qc_input['geometry']  = get_geometry()
    qc_input['symmetry']  = get_symmetry()
    qc_input['charge']    = get_charge()
    qc_input['spin']      = get_spin()
    qc_input['basis set'] = get_basis_set(qc_input['program'])
    qc_input['method']    = get_method(qc_input['program'])

    tprint('\n\nSummary of the input:\n')
    for p, v in qc_input.items():
        print('\t' + str(p) + ' : ' + str(v))

    tprint('\n\tInput generated!')
