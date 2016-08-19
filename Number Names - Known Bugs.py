""" NUMBER NAMES (KNOWN BUGS) by Ravi Teja Gannavarapu """

def welcome():
	for i in range (22):
		print ("*"),
	print ("\n*  NUMBER NAMES by Ravi Teja Gannavarapu  *")
	for i in range (22):
		print ("*"),

def bugs():
    print ("\n\nKNOWN BUGS:\n\n1. Numbers greater than 9999999999 are not supported.\n\
2. Numbers with all zeroes except the first number are not supported. For example: 100, 200, 1000, 7000, etc. are not supported.")

welcome()
bugs()
x = raw_input()
