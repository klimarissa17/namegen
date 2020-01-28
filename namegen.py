import random 
import argparse 

ALPHABET_SIZE = 26
HELLO = "Hi! I'm here to generate a new nickname for you!\n Please tell me how many syllables you'd like to have in your nickname (2/3/4)"
NUMBER = "Ok, now please tell me how many versions you'd like to see, up to 20 (I recommend to choose not less than 7 because I'm not yet really good at generating ssomething... pronouncable at all)" 
ABOUT_VOWEL = "Cool! Please also tell me if you _would_ like it to end with a vowel (for example, if you want it to sound more feminine) [y/n]"
RESPONSE = "Done! Here's what I've generated for you:\n"


alphabet = [chr(i + ord('a')) for i in range(ALPHABET_SIZE)] 
vowels = ['a', 'e', 'o', 'u', 'i']
cons = [i for i in alphabet if i not in vowels]

def gen_syllable(number = 3, is_open = True):
    res = []
    for i in range(number - 1):
        letter = cons[random.randint(0, len(cons) - 1)] 
        res.append(letter)
    vowel = vowels[random.randint(0, len(vowels) - 1)]
    if is_open: 
        pos = number - 1
    else:
        if number == 3:
            pos = 1
        else:
            pos = random.randint(1, 2)
    res.insert(pos, vowel)
    return ''.join(res)

def gen_name(number = 3, is_female = True):
    name = [gen_syllable(random.randint(1, 4), random.randint(0, 1)) for i in range(number - 1)]
    name.append(gen_syllable(random.randint(1, 4), True))
    return ''.join(name)


print(HELLO)
number_of_sylls = int(input())
print(NUMBER)
versions = int(input())
print(ABOUT_VOWEL)
vowel = True if str(input()) == 'y' else False

res = [gen_name(number_of_sylls, vowel) for i in range(versions)]

print(RESPONSE + '\n'.join(res))

