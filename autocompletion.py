
import os, glob

def path_completer(text, state):
    paths = glob.glob(text + '*')
    # add '/' symbol to directories for better readability
    for i in range(len(paths)):
        if os.path.isdir(paths[i]):
            paths[i] += '/'

    return (paths + [None])[state]


class ListCompleter:
    def __init__(self, completions):
        self.completions = completions

    def complete(self, text, state):
        if text:
            self.matches = [s for s in self.completions if s and s.startswith(text)]
        else:
            self.matches = self.completions[:]

        # return match indexed by state
        try:
            return self.matches[state]
        except IndexError:
            return None


### OLD ###
# def methods_completer(text, state):
#     methods = ['rhf', 'uhf', 'mp2', 'ccsd(t)', 'casscf']
#     # fill in the cache by partial completion if text is not empty
#     if text:
#         cache = [s for s in methods if s and s.startswith(text)]
#     else:
#         cache = methods
#
#     return (cache + [None])[state]
###
