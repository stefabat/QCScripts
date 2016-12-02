#!/usr/bin/python

import utilities as util

print('\n\t\tHello! Welcome to the Quantum Chemistry input generation program!\n')

def main():
    util.tprint('For which program do you want to create the input?\n')

    while True:
        util.tprint('1] MOLPRO 2015.1')
        util.tprint('2] Gaussian09')
        program = input('\n\tEnter your choice (number): ')
        if program == '1':
            molpro_generator()
            break
        elif program == '2':
            gaussian_generator()
            break
        else:
            util.tprint('Enter a valid number!\n')
            continue

    util.tprint('Bye bye!')

# this is executed only if running it directly from the terminal, not if imported
if __name__ == "__main__":
    main()
