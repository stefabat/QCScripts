
class Molecule:
    """A class defining a molecule"""

    def __init__(self, atoms, xyz, n_atoms, name):
        self.atoms = atoms
        self.xyz = xyz
        self.n_atoms = n_atoms
        self.name = name
