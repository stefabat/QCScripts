
import readline, glob, os
def complete(text, state):
	if os.path.isdir(text):
		text += '/'

	return (glob.glob(text+'*')+[None])[state]

readline.set_completer_delims(' \t\n;')
readline.parse_and_bind("tab: complete")
readline.set_completer(complete)
input('file? ')
