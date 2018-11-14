import itertools

characters = input("Enter the characters the passwords will contain. alphabet, numbers, special characters all ok. : ")
length = input("Enter the character length each password will be. : ")
file = open ('passlist.txt','a')
letters = itertools.product(characters, repeat=int(length))
print ('Generating the passwords based on the specific requirements you entered and creating a file called passlist.txt. This may take while but once it is done this will exit.')
for i in letters:
    file.write("".join(i) + '\n')
file.close()
