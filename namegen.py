import random 
import argparse 

ALPHABET_SIZE = 26
HELLO = "Hi! I'm here to generate a new nickname for you!\nPlease tell me how many syllables you'd like to have in your nickname (2/3/4)\n"
NUMBER = "Ok, now please tell me how many versions you'd like to see, up to 20 (I recommend to choose not less than 7 because I'm not yet really good at generating something... pronouncable at all)\n"
ABOUT_VOWEL = "Cool! Please also tell me if you _would_ like it to end with a vowel (for example, if you want it to sound more feminine) [y/n]\n"
RESPONSE = "Done! Here's what I've generated for you:\n"


alphabet = [chr(i + ord('a')) for i in range(ALPHABET_SIZE)] 
vowels = ['a', 'e', 'o', 'u', 'i']
cons = [i for i in alphabet if i not in vowels]

def gen_syllable(number = 3, is_open = True):
    res = []
    for i in range(number - 1):
        letter = random.choice(cons) 
        res.append(letter)
    vowel = random.choice(vowels)
    if is_open: 
        pos = number - 1
    else:
        if number == 3:
            pos = 1
        else:
            pos = random.randint(1, 2)
    res.insert(pos, vowel)
    return ''.join(res)

def gen_name(number = 3, ends_with_vowel = True):
    name = [gen_syllable(random.randint(1, 4), random.randint(0, 1)) for i in range(number - 1)]
    name.append(gen_syllable(random.randint(1, 4), ends_with_vowel))
    return ''.join(name)


number_of_sylls = int(input(HELLO))
versions = int(input(NUMBER))
ends_with_vowel = True if str(input(ABOUT_VOWEL)) == 'y' else False

res = [gen_name(number_of_sylls, ends_with_vowel) for i in range(versions)]

print(RESPONSE + '\n'.join(res))

