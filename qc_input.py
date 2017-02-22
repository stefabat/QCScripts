#!/usr/bin/python

from input_generator import *
from utilities import tprint

print('\n\t\tHello! Welcome to the Quantum Chemistry input generation program!\n')

# this is executed only if running it directly from the terminal, not if imported
if __name__ == "__main__":
    input_generator()
    tprint('Ciao ciao')
