'''Write some code to use the mio.py module in listing 13.1 to capture all the print output
of a script to a file named myfile.txt, reset the standard output to the screen, and print
that file to screen.
'''


import mio



mio.capture_output("myfile.txt")
print("hello")
print("how are you? do you know the answer of the mathematic expresion '3+4'?")
print(3+4)
mio.restore_output()

mio.print_file("myfile.txt")

