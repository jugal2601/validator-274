####################################################
# Acknowledgements: none
# Description: This program validates a password and later generates a secure one.
#####################################################################

import random
import string


def validate(password):
    # initializing everything
	upperletterchk= False
	lowerletterchk= False
	specialchar= False
	forbidchar= False
	numchk= False
	list01= [" ", "@", "#"]
	list02= ["!", "-", "$", "%", "&", "'", "(", ")", "*", ",", "+", ".", "/", ":", ";", "<", "=", ">", "?", "_", "[", "]", "^", "`", "{", "|", "}", "~"]
	list03= ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

	# this loop checks if the password contains any upper,lower
	# forbidden character, special character and decimal digit 
	for i in password:
		if i.isupper()==True:
			upperletterchk=True
		elif i.islower()==True:
			lowerletterchk=True
		elif i in list01:
			forbidchar=True
		elif i in list02:
			specialchar=True
		elif i in list03:
			numchk=True

	# if cases to return the appropriate result
	if forbidchar==True or len(password)<8:
		return ("Invalid")
	elif (forbidchar==False and len(password)>=8) and (specialchar==True) and (numchk==True) and upperletterchk==True and lowerletterchk==True:
		return ("Secure")
	else:
		return ("Insecure")
    
# generates a random code of length >= 8
# with uppercase, lowercase, decimal digit and special characters
def generate(n):
	list02= ["!", "-", "$", "%", "&", "'", "(", ")", "*", ",", "+", ".", "/", ":", ";", "<", "=", ">", "?", "_", "[", "]", "^", "`", "{", "|", "}", "~"]
	pass01= ""
	lowcase= string.ascii_lowercase
	upcase= string.ascii_uppercase
	pass01+= random.choice(list02)
	pass01+= str(random.randint(0,9))
	pass01+= random.choice(lowcase)
	pass01+= random.choice(upcase)
	for i in range(4,6): 
		pass01+=random.choice(upcase)
	for i in range(6,n):
		pass01+=random.choice(lowcase)

	pass02=list(pass01)
	random.shuffle(pass02)
	pass03="".join(pass02)
	return(pass03)


if __name__ == "__main__":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 validator.py". This can be useful for
    # testing your implementations.
    print(validate("BFjb0v,lY"))
    print(generate(9))
    pass