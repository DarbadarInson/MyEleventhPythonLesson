import math
'''
#Simple Functions!
def greet():
    print("Hello Johnny")
    print("How do you do Johnny!")
    print("Isn't the weather nice today?")

greet()

print('-------------------------------------------------')
#Function that allows for input
def greet_your_name(name1):
    print(f"Hello {name1}")
    print(f"How do you do {name1}")
greet_your_name("Name")

print('-------------------------------------------------')

def greet_with_name(name):
    name = input("What is your name? ")
    print(f"Hello {name}!")
    print(f"How do you do {name}!")

greet_with_name(__name__)

print('-------------------------------------------------')

def greet_with(lastName,  location):
    print(f"Hello {lastName}")
    print(f"What is it like in {location}")
greet_with("DarbadarInson", "Andijan")
greet_with(location="Tashkent", lastName="DevanaDeaveloper")




def paint_calc(height,  width, cover):
    area = height * width
    cover = 5
    num_of_cans = math.ceil(area / cover)
    print(f"You'll need {num_of_cans} cans of paint.")
paint_calc(15, 5, 3)


def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number")
    else:
        print("It's a not prime number")

n = int(input("Check this is number: "))
prime_checker(number = n)

'''

#Caeser Cipher = TSEZER SHIFRI

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caeser(start_text, shift_amount, cipher_direction):
    end_text = ""       
    if cipher_direction == "decode":
        shift_amount = shift_amount * -1
    for letter in start_text:
        position = alphabet.index(letter)

        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f"Here's the {direction}d result: {end_text}")

caeser(start_text=text, shift_amount=shift, cipher_direction=direction)











