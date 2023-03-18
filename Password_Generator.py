#SergioCharruadas      
#04/08/2022      
#PasswordGenerator 

#import libraries

import random
import string
import secrets

#define all needed variables
maximumlen = 12
 
rand_digit = list(string.digits)
rand_upper = list(string.ascii_uppercase)
rand_lower = list(string.ascii_lowercase)
rand_symbol = list(string.punctuation)
 
alphabets_count = 3
digits_count = 3
special_characters_count = 3

def passwordgenerator():
	
  password = []
  ## picking random alphabets
  for i in range(alphabets_count):
	  password.append(random.choice(rand_upper))

  for i in range(alphabets_count):
	  password.append(random.choice(rand_lower)) 
  
	## picking random digits
  for i in range(digits_count):
	  password.append(random.choice(rand_digit))

	## picking random symbols
  for i in range(special_characters_count):
	  password.append(random.choice(rand_symbol))


  new_pass = random.shuffle(password)
  new_pass = ("".join(password))
#check if maximum len is bigger than lenght of new_pass variable and then add more characters if needed
  if maximumlen > len(new_pass):
    for x in range(maximumlen-len(new_pass)):
     new_pass = new_pass + secrets.choice(rand_digit + rand_upper + rand_lower + rand_symbol)
   
# print out password
  print(new_pass)

#run function
passwordgenerator()

#ask if user would like to generate a new password otherwise quit program
answer = input("Would you like to generate a new password?\n").casefold()
if answer == "y".casefold() or answer == "yes".casefold():
  maximumlen = int(input("Enter another password lenght? (Bigger than 12 characters)"))
  passwordgenerator()
else:
  quit()