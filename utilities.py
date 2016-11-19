
import glob
import os


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
