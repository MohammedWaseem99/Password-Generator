import random
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', ]
print("Welcome to the password generater")


uletter=int(input(f"how many letters would you like to include in your password ?\n"))
unumber=int(input(f"how many numbers would you like to add to your password ?\n"))
usymbol=int(input(f"how many symbols would you like to add to your password ?\n"))



password_array=[]

for i in  range(0,uletter):
    
   password_array +=random.choice(letters)
    

for i in  range(0,unumber):
    
   password_array +=random.choice(numbers)
    

for i in  range(0,usymbol):
    
   password_array +=random.choice(symbols)


    
print(f"characters of your password : {password_array}\n")
random.shuffle(password_array)
print(f"shuffled characters of your password : {password_array}\n")

final_password=""
for char in password_array:
    final_password+=char
print(f"Your password is :  {final_password}")